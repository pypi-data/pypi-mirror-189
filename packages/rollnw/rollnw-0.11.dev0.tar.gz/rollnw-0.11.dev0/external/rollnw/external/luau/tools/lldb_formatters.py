# This file is part of the Luau programming language and is licensed under MIT License; see LICENSE.txt for details

# HACK: LLDB's python API doesn't afford anything helpful for getting at variadic template parameters.
# We're forced to resort to parsing names as strings.
def templateParams(s):
    depth = 0
    start = s.find("<") + 1
    result = []
    for i, c in enumerate(s[start:], start):
        if c == "<":
            depth += 1
        elif c == ">":
            if depth == 0:
                result.append(s[start:i].strip())
                break
            depth -= 1
        elif c == "," and depth == 0:
            result.append(s[start:i].strip())
            start = i + 1
    return result


def getType(target, typeName):
    stars = 0

    typeName = typeName.strip()
    while typeName.endswith("*"):
        stars += 1
        typeName = typeName[:-1]

    if typeName.startswith("const "):
        typeName = typeName[6:]

    ty = target.FindFirstType(typeName.strip())
    for _ in range(stars):
        ty = ty.GetPointerType()

    return ty


def luau_variant_summary(valobj, internal_dict, options):
    return valobj.GetChildMemberWithName("type").GetSummary()[1:-1]


class LuauVariantSyntheticChildrenProvider:
    node_names = ["type", "value"]

    def __init__(self, valobj, internal_dict):
        self.valobj = valobj
        self.type_index = None
        self.current_type = None
        self.type_params = []
        self.stored_value = None

    def num_children(self):
        return len(self.node_names)

    def has_children(self):
        return True

    def get_child_index(self, name):
        try:
            return self.node_names.index(name)
        except ValueError:
            return -1

    def get_child_at_index(self, index):
        try:
            node = self.node_names[index]
        except IndexError:
            return None

        if node == "type":
            if self.current_type:
                return self.valobj.CreateValueFromExpression(
                    node, f'(const char*)"{self.current_type.GetDisplayTypeName()}"'
                )
            else:
                return self.valobj.CreateValueFromExpression(
                    node, '(const char*)"<unknown type>"'
                )
        elif node == "value":
            if self.stored_value is not None:
                if self.current_type is not None:
                    return self.valobj.CreateValueFromData(
                        node, self.stored_value.GetData(), self.current_type
                    )
                else:
                    return self.valobj.CreateValueExpression(
                        node, '(const char*)"<unknown type>"'
                    )
            else:
                return self.valobj.CreateValueFromExpression(
                    node, '(const char*)"<no stored value>"'
                )
        else:
            return None

    def update(self):
        self.type_index = self.valobj.GetChildMemberWithName(
            "typeId"
        ).GetValueAsSigned()
        self.type_params = templateParams(
            self.valobj.GetType().GetCanonicalType().GetName()
        )

        if len(self.type_params) > self.type_index:
            self.current_type = getType(
                self.valobj.GetTarget(), self.type_params[self.type_index]
            )

            if self.current_type:
                storage = self.valobj.GetChildMemberWithName("storage")
                self.stored_value = storage.Cast(self.current_type)
            else:
                self.stored_value = None
        else:
            self.current_type = None
            self.stored_value = None

        return False


class DenseHashTableSyntheticChildrenProvider:
    def __init__(self, valobj, internal_dict):
        """this call should initialize the Python object using valobj as the variable to provide synthetic children for"""
        self.valobj = valobj
        self.update()

    def num_children(self):
        """this call should return the number of children that you want your object to have"""
        return self.capacity

    def get_child_index(self, name):
        """this call should return the index of the synthetic child whose name is given as argument"""
        try:
            if name.startswith("[") and name.endswith("]"):
                return int(name[1:-1])
            else:
                return -1
        except Exception as e:
            print("get_child_index exception", e)
            return -1

    def get_child_at_index(self, index):
        """this call should return a new LLDB SBValue object representing the child at the index given as argument"""
        try:
            dataMember = self.valobj.GetChildMemberWithName("data")

            data = dataMember.GetPointeeData(index)

            return self.valobj.CreateValueFromData(
                f"[{index}]",
                data,
                dataMember.Dereference().GetType(),
            )

        except Exception as e:
            print("get_child_at_index error", e)

    def update(self):
        """this call should be used to update the internal state of this Python object whenever the state of the variables in LLDB changes.[1]
        Also, this method is invoked before any other method in the interface."""
        self.capacity = self.valobj.GetChildMemberWithName(
            "capacity"
        ).GetValueAsUnsigned()

    def has_children(self):
        """this call should return True if this object might have children, and False if this object can be guaranteed not to have children.[2]"""
        return True


def luau_symbol_summary(valobj, internal_dict, options):
    local = valobj.GetChildMemberWithName("local")
    global_ = valobj.GetChildMemberWithName("global").GetChildMemberWithName("value")

    if local.GetValueAsUnsigned() != 0:
        return f'local {local.GetChildMemberWithName("name").GetChildMemberWithName("value").GetSummary()}'
    elif global_.GetValueAsUnsigned() != 0:
        return f"global {global_.GetSummary()}"
    else:
        return "???"


class AstArraySyntheticChildrenProvider:
    def __init__(self, valobj, internal_dict):
        self.valobj = valobj

    def num_children(self):
        return self.size

    def get_child_index(self, name):
        try:
            if name.startswith("[") and name.endswith("]"):
                return int(name[1:-1])
            else:
                return -1
        except Exception as e:
            print("get_child_index error:", e)

    def get_child_at_index(self, index):
        try:
            dataMember = self.valobj.GetChildMemberWithName("data")
            data = dataMember.GetPointeeData(index)
            return self.valobj.CreateValueFromData(
                f"[{index}]", data, dataMember.Dereference().GetType()
            )
        except Exception as e:
            print("get_child_index error:", e)

    def update(self):
        self.size = self.valobj.GetChildMemberWithName("size").GetValueAsUnsigned()

    def has_children(self):
        return True
