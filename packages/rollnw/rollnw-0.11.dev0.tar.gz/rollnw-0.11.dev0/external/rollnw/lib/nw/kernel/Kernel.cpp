#include "Kernel.hpp"

#include "../log.hpp"
#include "../objects/Module.hpp"
#include "EffectSystem.hpp"
#include "EventSystem.hpp"
#include "Objects.hpp"
#include "ParsedScriptCache.hpp"
#include "Resources.hpp"
#include "Rules.hpp"
#include "ScriptSystem.hpp"
#include "Strings.hpp"
#include "TwoDACache.hpp"

namespace nw::kernel {

namespace detail {
Config s_config;
Services s_services;
} // namespace detail

Services::Services()
    : strings{new Strings}
    , resources{new Resources}
    , twoda_cache{new TwoDACache}
    , rules{new Rules}
    , effects{new EffectSystem}
    , objects{new ObjectSystem}
    , events{new EventSystem}
#ifdef ROLLNW_BUILD_RUNTIME_SCRIPTING
    , scripts{new ScriptSystem}
#endif
{
    LOG_F(INFO, "kernel: initializing default services");
}

void Services::start()
{
    strings->initialize();
    resources->initialize();
    twoda_cache->initialize();
    rules->initialize();
    effects->initialize();
    objects->initialize();
    events->initialize();
#ifdef ROLLNW_BUILD_RUNTIME_SCRIPTING
    scripts->initialize();
#endif

    for (auto& s : services_) {
        s.service->initialize();
    }
}

void Services::shutdown()
{
#ifdef ROLLNW_BUILD_RUNTIME_SCRIPTING
    scripts->clear();
#endif
    events->clear();
    objects->clear();
    effects->clear();
    rules->clear();
    twoda_cache->clear();

    for (auto& s : reverse(services_)) {
        s.service->clear();
    }
}

Config& config() { return detail::s_config; }
Services& services() { return detail::s_services; }

void load_profile(const GameProfile* profile)
{
    detail::s_services.set_profile(profile);
}

Module* load_module(const std::filesystem::path& path, std::string_view manifest)
{
    resman().load_module(path, manifest);

    Module* mod = objects().make_module();
    if (mod) {
        mod->instantiate();
    }

    return mod;
}

void unload_module()
{
    resman().unload_module();
    strings().unload_custom_tlk();
}

} // namespace nw::kernel
