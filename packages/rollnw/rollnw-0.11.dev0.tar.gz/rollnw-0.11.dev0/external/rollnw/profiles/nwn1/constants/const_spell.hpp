#pragma once

#include <nw/rules/Spell.hpp>

namespace nwn1 {

constexpr nw::Spell spell_all_spells = nw::Spell::invalid(); // used for spell immunity.

constexpr nw::Spell spell_acid_fog = nw::Spell::make(0);
constexpr nw::Spell spell_aid = nw::Spell::make(1);
constexpr nw::Spell spell_animate_dead = nw::Spell::make(2);
constexpr nw::Spell spell_barkskin = nw::Spell::make(3);
constexpr nw::Spell spell_bestow_curse = nw::Spell::make(4);
constexpr nw::Spell spell_blade_barrier = nw::Spell::make(5);
constexpr nw::Spell spell_bless = nw::Spell::make(6);
constexpr nw::Spell spell_bless_weapon = nw::Spell::make(537);
constexpr nw::Spell spell_blindness_and_deafness = nw::Spell::make(8);
constexpr nw::Spell spell_bulls_strength = nw::Spell::make(9);
constexpr nw::Spell spell_burning_hands = nw::Spell::make(10);
constexpr nw::Spell spell_call_lightning = nw::Spell::make(11);
// constexpr nw::Spell spell_calm_emotions =nw::Spell::make( 12);
constexpr nw::Spell spell_cats_grace = nw::Spell::make(13);
constexpr nw::Spell spell_chain_lightning = nw::Spell::make(14);
constexpr nw::Spell spell_charm_monster = nw::Spell::make(15);
constexpr nw::Spell spell_charm_person = nw::Spell::make(16);
constexpr nw::Spell spell_charm_person_or_animal = nw::Spell::make(17);
constexpr nw::Spell spell_circle_of_death = nw::Spell::make(18);
constexpr nw::Spell spell_circle_of_doom = nw::Spell::make(19);
constexpr nw::Spell spell_clairaudience_and_clairvoyance = nw::Spell::make(20);
constexpr nw::Spell spell_clarity = nw::Spell::make(21);
constexpr nw::Spell spell_cloak_of_chaos = nw::Spell::make(22);
constexpr nw::Spell spell_cloudkill = nw::Spell::make(23);
constexpr nw::Spell spell_color_spray = nw::Spell::make(24);
constexpr nw::Spell spell_cone_of_cold = nw::Spell::make(25);
constexpr nw::Spell spell_confusion = nw::Spell::make(26);
constexpr nw::Spell spell_contagion = nw::Spell::make(27);
constexpr nw::Spell spell_control_undead = nw::Spell::make(28);
constexpr nw::Spell spell_create_greater_undead = nw::Spell::make(29);
constexpr nw::Spell spell_create_undead = nw::Spell::make(30);
constexpr nw::Spell spell_cure_critical_wounds = nw::Spell::make(31);
constexpr nw::Spell spell_cure_light_wounds = nw::Spell::make(32);
constexpr nw::Spell spell_cure_minor_wounds = nw::Spell::make(33);
constexpr nw::Spell spell_cure_moderate_wounds = nw::Spell::make(34);
constexpr nw::Spell spell_cure_serious_wounds = nw::Spell::make(35);
constexpr nw::Spell spell_darkness = nw::Spell::make(36);
constexpr nw::Spell spell_daze = nw::Spell::make(37);
constexpr nw::Spell spell_death_ward = nw::Spell::make(38);
constexpr nw::Spell spell_delayed_blast_fireball = nw::Spell::make(39);
constexpr nw::Spell spell_dismissal = nw::Spell::make(40);
constexpr nw::Spell spell_dispel_magic = nw::Spell::make(41);
constexpr nw::Spell spell_divine_power = nw::Spell::make(42);
constexpr nw::Spell spell_dominate_animal = nw::Spell::make(43);
constexpr nw::Spell spell_dominate_monster = nw::Spell::make(44);
constexpr nw::Spell spell_dominate_person = nw::Spell::make(45);
constexpr nw::Spell spell_doom = nw::Spell::make(46);
constexpr nw::Spell spell_elemental_shield = nw::Spell::make(47);
constexpr nw::Spell spell_elemental_swarm = nw::Spell::make(48);
constexpr nw::Spell spell_endurance = nw::Spell::make(49);
constexpr nw::Spell spell_endure_elements = nw::Spell::make(50);
constexpr nw::Spell spell_energy_drain = nw::Spell::make(51);
constexpr nw::Spell spell_enervation = nw::Spell::make(52);
constexpr nw::Spell spell_entangle = nw::Spell::make(53);
constexpr nw::Spell spell_fear = nw::Spell::make(54);
constexpr nw::Spell spell_feeblemind = nw::Spell::make(55);
constexpr nw::Spell spell_finger_of_death = nw::Spell::make(56);
constexpr nw::Spell spell_fire_storm = nw::Spell::make(57);
constexpr nw::Spell spell_fireball = nw::Spell::make(58);
constexpr nw::Spell spell_flame_arrow = nw::Spell::make(59);
constexpr nw::Spell spell_flame_lash = nw::Spell::make(60);
constexpr nw::Spell spell_flame_strike = nw::Spell::make(61);
constexpr nw::Spell spell_freedom_of_movement = nw::Spell::make(62);
constexpr nw::Spell spell_gate = nw::Spell::make(63);
constexpr nw::Spell spell_ghoul_touch = nw::Spell::make(64);
constexpr nw::Spell spell_globe_of_invulnerability = nw::Spell::make(65);
constexpr nw::Spell spell_grease = nw::Spell::make(66);
constexpr nw::Spell spell_greater_dispelling = nw::Spell::make(67);
// constexpr nw::Spell spell_greater_magic_weapon              =nw::Spell::make( 68);
constexpr nw::Spell spell_greater_planar_binding = nw::Spell::make(69);
constexpr nw::Spell spell_greater_restoration = nw::Spell::make(70);
// constexpr nw::Spell spell_greater_shadow_conjuration =nw::Spell::make( 71);
constexpr nw::Spell spell_greater_spell_breach = nw::Spell::make(72);
constexpr nw::Spell spell_greater_spell_mantle = nw::Spell::make(73);
constexpr nw::Spell spell_greater_stoneskin = nw::Spell::make(74);
constexpr nw::Spell spell_gust_of_wind = nw::Spell::make(75);
constexpr nw::Spell spell_hammer_of_the_gods = nw::Spell::make(76);
constexpr nw::Spell spell_harm = nw::Spell::make(77);
constexpr nw::Spell spell_haste = nw::Spell::make(78);
constexpr nw::Spell spell_heal = nw::Spell::make(79);
constexpr nw::Spell spell_healing_circle = nw::Spell::make(80);
constexpr nw::Spell spell_hold_animal = nw::Spell::make(81);
constexpr nw::Spell spell_hold_monster = nw::Spell::make(82);
constexpr nw::Spell spell_hold_person = nw::Spell::make(83);
constexpr nw::Spell spell_holy_aura = nw::Spell::make(84);
constexpr nw::Spell spell_holy_sword = nw::Spell::make(538);
constexpr nw::Spell spell_identify = nw::Spell::make(86);
constexpr nw::Spell spell_implosion = nw::Spell::make(87);
constexpr nw::Spell spell_improved_invisibility = nw::Spell::make(88);
constexpr nw::Spell spell_incendiary_cloud = nw::Spell::make(89);
constexpr nw::Spell spell_invisibility = nw::Spell::make(90);
constexpr nw::Spell spell_invisibility_purge = nw::Spell::make(91);
constexpr nw::Spell spell_invisibility_sphere = nw::Spell::make(92);
constexpr nw::Spell spell_knock = nw::Spell::make(93);
constexpr nw::Spell spell_lesser_dispel = nw::Spell::make(94);
constexpr nw::Spell spell_lesser_mind_blank = nw::Spell::make(95);
constexpr nw::Spell spell_lesser_planar_binding = nw::Spell::make(96);
constexpr nw::Spell spell_lesser_restoration = nw::Spell::make(97);
constexpr nw::Spell spell_lesser_spell_breach = nw::Spell::make(98);
constexpr nw::Spell spell_lesser_spell_mantle = nw::Spell::make(99);
constexpr nw::Spell spell_light = nw::Spell::make(100);
constexpr nw::Spell spell_lightning_bolt = nw::Spell::make(101);
constexpr nw::Spell spell_mage_armor = nw::Spell::make(102);
constexpr nw::Spell spell_magic_circle_against_chaos = nw::Spell::make(103);
constexpr nw::Spell spell_magic_circle_against_evil = nw::Spell::make(104);
constexpr nw::Spell spell_magic_circle_against_good = nw::Spell::make(105);
constexpr nw::Spell spell_magic_circle_against_law = nw::Spell::make(106);
constexpr nw::Spell spell_magic_missile = nw::Spell::make(107);
constexpr nw::Spell spell_magic_vestment = nw::Spell::make(546);
// constexpr nw::Spell spell_magic_weapon                      =nw::Spell::make( 109);
constexpr nw::Spell spell_mass_blindness_and_deafness = nw::Spell::make(110);
constexpr nw::Spell spell_mass_charm = nw::Spell::make(111);
// constexpr nw::Spell spell_mass_domination =nw::Spell::make( 112);
constexpr nw::Spell spell_mass_haste = nw::Spell::make(113);
constexpr nw::Spell spell_mass_heal = nw::Spell::make(114);
constexpr nw::Spell spell_melfs_acid_arrow = nw::Spell::make(115);
constexpr nw::Spell spell_meteor_swarm = nw::Spell::make(116);
constexpr nw::Spell spell_mind_blank = nw::Spell::make(117);
constexpr nw::Spell spell_mind_fog = nw::Spell::make(118);
constexpr nw::Spell spell_minor_globe_of_invulnerability = nw::Spell::make(119);
constexpr nw::Spell spell_ghostly_visage = nw::Spell::make(120);
constexpr nw::Spell spell_ethereal_visage = nw::Spell::make(121);
constexpr nw::Spell spell_mordenkainens_disjunction = nw::Spell::make(122);
constexpr nw::Spell spell_mordenkainens_sword = nw::Spell::make(123);
constexpr nw::Spell spell_natures_balance = nw::Spell::make(124);
constexpr nw::Spell spell_negative_energy_protection = nw::Spell::make(125);
constexpr nw::Spell spell_neutralize_poison = nw::Spell::make(126);
constexpr nw::Spell spell_phantasmal_killer = nw::Spell::make(127);
constexpr nw::Spell spell_planar_binding = nw::Spell::make(128);
constexpr nw::Spell spell_poison = nw::Spell::make(129);
constexpr nw::Spell spell_polymorph_self = nw::Spell::make(130);
constexpr nw::Spell spell_power_word_kill = nw::Spell::make(131);
constexpr nw::Spell spell_power_word_stun = nw::Spell::make(132);
constexpr nw::Spell spell_prayer = nw::Spell::make(133);
constexpr nw::Spell spell_premonition = nw::Spell::make(134);
constexpr nw::Spell spell_prismatic_spray = nw::Spell::make(135);
constexpr nw::Spell spell_protection__from_chaos = nw::Spell::make(136);
constexpr nw::Spell spell_protection_from_elements = nw::Spell::make(137);
constexpr nw::Spell spell_protection_from_evil = nw::Spell::make(138);
constexpr nw::Spell spell_protection_from_good = nw::Spell::make(139);
constexpr nw::Spell spell_protection_from_law = nw::Spell::make(140);
constexpr nw::Spell spell_protection_from_spells = nw::Spell::make(141);
constexpr nw::Spell spell_raise_dead = nw::Spell::make(142);
constexpr nw::Spell spell_ray_of_enfeeblement = nw::Spell::make(143);
constexpr nw::Spell spell_ray_of_frost = nw::Spell::make(144);
constexpr nw::Spell spell_remove_blindness_and_deafness = nw::Spell::make(145);
constexpr nw::Spell spell_remove_curse = nw::Spell::make(146);
constexpr nw::Spell spell_remove_disease = nw::Spell::make(147);
constexpr nw::Spell spell_remove_fear = nw::Spell::make(148);
constexpr nw::Spell spell_remove_paralysis = nw::Spell::make(149);
constexpr nw::Spell spell_resist_elements = nw::Spell::make(150);
constexpr nw::Spell spell_resistance = nw::Spell::make(151);
constexpr nw::Spell spell_restoration = nw::Spell::make(152);
constexpr nw::Spell spell_resurrection = nw::Spell::make(153);
constexpr nw::Spell spell_sanctuary = nw::Spell::make(154);
constexpr nw::Spell spell_scare = nw::Spell::make(155);
constexpr nw::Spell spell_searing_light = nw::Spell::make(156);
constexpr nw::Spell spell_see_invisibility = nw::Spell::make(157);
// constexpr nw::Spell spell_shades =nw::Spell::make( 158);
// constexpr nw::Spell spell_shadow_conjuration =nw::Spell::make( 159);
constexpr nw::Spell spell_shadow_shield = nw::Spell::make(160);
constexpr nw::Spell spell_shapechange = nw::Spell::make(161);
constexpr nw::Spell spell_shield_of_law = nw::Spell::make(162);
constexpr nw::Spell spell_silence = nw::Spell::make(163);
constexpr nw::Spell spell_slay_living = nw::Spell::make(164);
constexpr nw::Spell spell_sleep = nw::Spell::make(165);
constexpr nw::Spell spell_slow = nw::Spell::make(166);
constexpr nw::Spell spell_sound_burst = nw::Spell::make(167);
constexpr nw::Spell spell_spell_resistance = nw::Spell::make(168);
constexpr nw::Spell spell_spell_mantle = nw::Spell::make(169);
constexpr nw::Spell spell_sphere_of_chaos = nw::Spell::make(170);
constexpr nw::Spell spell_stinking_cloud = nw::Spell::make(171);
constexpr nw::Spell spell_stoneskin = nw::Spell::make(172);
constexpr nw::Spell spell_storm_of_vengeance = nw::Spell::make(173);
constexpr nw::Spell spell_summon_creature_i = nw::Spell::make(174);
constexpr nw::Spell spell_summon_creature_ii = nw::Spell::make(175);
constexpr nw::Spell spell_summon_creature_iii = nw::Spell::make(176);
constexpr nw::Spell spell_summon_creature_iv = nw::Spell::make(177);
constexpr nw::Spell spell_summon_creature_ix = nw::Spell::make(178);
constexpr nw::Spell spell_summon_creature_v = nw::Spell::make(179);
constexpr nw::Spell spell_summon_creature_vi = nw::Spell::make(180);
constexpr nw::Spell spell_summon_creature_vii = nw::Spell::make(181);
constexpr nw::Spell spell_summon_creature_viii = nw::Spell::make(182);
constexpr nw::Spell spell_sunbeam = nw::Spell::make(183);
constexpr nw::Spell spell_tensers_transformation = nw::Spell::make(184);
constexpr nw::Spell spell_time_stop = nw::Spell::make(185);
constexpr nw::Spell spell_true_seeing = nw::Spell::make(186);
constexpr nw::Spell spell_unholy_aura = nw::Spell::make(187);
constexpr nw::Spell spell_vampiric_touch = nw::Spell::make(188);
constexpr nw::Spell spell_virtue = nw::Spell::make(189);
constexpr nw::Spell spell_wail_of_the_banshee = nw::Spell::make(190);
constexpr nw::Spell spell_wall_of_fire = nw::Spell::make(191);
constexpr nw::Spell spell_web = nw::Spell::make(192);
constexpr nw::Spell spell_weird = nw::Spell::make(193);
constexpr nw::Spell spell_word_of_faith = nw::Spell::make(194);
constexpr nw::Spell spellability_aura_blinding = nw::Spell::make(195);
constexpr nw::Spell spellability_aura_cold = nw::Spell::make(196);
constexpr nw::Spell spellability_aura_electricity = nw::Spell::make(197);
constexpr nw::Spell spellability_aura_fear = nw::Spell::make(198);
constexpr nw::Spell spellability_aura_fire = nw::Spell::make(199);
constexpr nw::Spell spellability_aura_menace = nw::Spell::make(200);
constexpr nw::Spell spellability_aura_protection = nw::Spell::make(201);
constexpr nw::Spell spellability_aura_stun = nw::Spell::make(202);
constexpr nw::Spell spellability_aura_unearthly_visage = nw::Spell::make(203);
constexpr nw::Spell spellability_aura_unnatural = nw::Spell::make(204);
constexpr nw::Spell spellability_bolt_ability_drain_charisma = nw::Spell::make(205);
constexpr nw::Spell spellability_bolt_ability_drain_constitution = nw::Spell::make(206);
constexpr nw::Spell spellability_bolt_ability_drain_dexterity = nw::Spell::make(207);
constexpr nw::Spell spellability_bolt_ability_drain_intelligence = nw::Spell::make(208);
constexpr nw::Spell spellability_bolt_ability_drain_strength = nw::Spell::make(209);
constexpr nw::Spell spellability_bolt_ability_drain_wisdom = nw::Spell::make(210);
constexpr nw::Spell spellability_bolt_acid = nw::Spell::make(211);
constexpr nw::Spell spellability_bolt_charm = nw::Spell::make(212);
constexpr nw::Spell spellability_bolt_cold = nw::Spell::make(213);
constexpr nw::Spell spellability_bolt_confuse = nw::Spell::make(214);
constexpr nw::Spell spellability_bolt_daze = nw::Spell::make(215);
constexpr nw::Spell spellability_bolt_death = nw::Spell::make(216);
constexpr nw::Spell spellability_bolt_disease = nw::Spell::make(217);
constexpr nw::Spell spellability_bolt_dominate = nw::Spell::make(218);
constexpr nw::Spell spellability_bolt_fire = nw::Spell::make(219);
constexpr nw::Spell spellability_bolt_knockdown = nw::Spell::make(220);
constexpr nw::Spell spellability_bolt_level_drain = nw::Spell::make(221);
constexpr nw::Spell spellability_bolt_lightning = nw::Spell::make(222);
constexpr nw::Spell spellability_bolt_paralyze = nw::Spell::make(223);
constexpr nw::Spell spellability_bolt_poison = nw::Spell::make(224);
constexpr nw::Spell spellability_bolt_shards = nw::Spell::make(225);
constexpr nw::Spell spellability_bolt_slow = nw::Spell::make(226);
constexpr nw::Spell spellability_bolt_stun = nw::Spell::make(227);
constexpr nw::Spell spellability_bolt_web = nw::Spell::make(228);
constexpr nw::Spell spellability_cone_acid = nw::Spell::make(229);
constexpr nw::Spell spellability_cone_cold = nw::Spell::make(230);
constexpr nw::Spell spellability_cone_disease = nw::Spell::make(231);
constexpr nw::Spell spellability_cone_fire = nw::Spell::make(232);
constexpr nw::Spell spellability_cone_lightning = nw::Spell::make(233);
constexpr nw::Spell spellability_cone_poison = nw::Spell::make(234);
constexpr nw::Spell spellability_cone_sonic = nw::Spell::make(235);
constexpr nw::Spell spellability_dragon_breath_acid = nw::Spell::make(236);
constexpr nw::Spell spellability_dragon_breath_cold = nw::Spell::make(237);
constexpr nw::Spell spellability_dragon_breath_fear = nw::Spell::make(238);
constexpr nw::Spell spellability_dragon_breath_fire = nw::Spell::make(239);
constexpr nw::Spell spellability_dragon_breath_gas = nw::Spell::make(240);
constexpr nw::Spell spellability_dragon_breath_lightning = nw::Spell::make(241);
constexpr nw::Spell spellability_dragon_breath_paralyze = nw::Spell::make(242);
constexpr nw::Spell spellability_dragon_breath_sleep = nw::Spell::make(243);
constexpr nw::Spell spellability_dragon_breath_slow = nw::Spell::make(244);
constexpr nw::Spell spellability_dragon_breath_weaken = nw::Spell::make(245);
constexpr nw::Spell spellability_dragon_wing_buffet = nw::Spell::make(246);
constexpr nw::Spell spellability_ferocity_1 = nw::Spell::make(247);
constexpr nw::Spell spellability_ferocity_2 = nw::Spell::make(248);
constexpr nw::Spell spellability_ferocity_3 = nw::Spell::make(249);
constexpr nw::Spell spellability_gaze_charm = nw::Spell::make(250);
constexpr nw::Spell spellability_gaze_confusion = nw::Spell::make(251);
constexpr nw::Spell spellability_gaze_daze = nw::Spell::make(252);
constexpr nw::Spell spellability_gaze_death = nw::Spell::make(253);
constexpr nw::Spell spellability_gaze_destroy_chaos = nw::Spell::make(254);
constexpr nw::Spell spellability_gaze_destroy_evil = nw::Spell::make(255);
constexpr nw::Spell spellability_gaze_destroy_good = nw::Spell::make(256);
constexpr nw::Spell spellability_gaze_destroy_law = nw::Spell::make(257);
constexpr nw::Spell spellability_gaze_dominate = nw::Spell::make(258);
constexpr nw::Spell spellability_gaze_doom = nw::Spell::make(259);
constexpr nw::Spell spellability_gaze_fear = nw::Spell::make(260);
constexpr nw::Spell spellability_gaze_paralysis = nw::Spell::make(261);
constexpr nw::Spell spellability_gaze_stunned = nw::Spell::make(262);
constexpr nw::Spell spellability_golem_breath_gas = nw::Spell::make(263);
constexpr nw::Spell spellability_hell_hound_firebreath = nw::Spell::make(264);
constexpr nw::Spell spellability_howl_confuse = nw::Spell::make(265);
constexpr nw::Spell spellability_howl_daze = nw::Spell::make(266);
constexpr nw::Spell spellability_howl_death = nw::Spell::make(267);
constexpr nw::Spell spellability_howl_doom = nw::Spell::make(268);
constexpr nw::Spell spellability_howl_fear = nw::Spell::make(269);
constexpr nw::Spell spellability_howl_paralysis = nw::Spell::make(270);
constexpr nw::Spell spellability_howl_sonic = nw::Spell::make(271);
constexpr nw::Spell spellability_howl_stun = nw::Spell::make(272);
constexpr nw::Spell spellability_intensity_1 = nw::Spell::make(273);
constexpr nw::Spell spellability_intensity_2 = nw::Spell::make(274);
constexpr nw::Spell spellability_intensity_3 = nw::Spell::make(275);
constexpr nw::Spell spellability_krenshar_scare = nw::Spell::make(276);
constexpr nw::Spell spellability_lesser_body_adjustment = nw::Spell::make(277);
constexpr nw::Spell spellability_mephit_salt_breath = nw::Spell::make(278);
constexpr nw::Spell spellability_mephit_steam_breath = nw::Spell::make(279);
constexpr nw::Spell spellability_mummy_bolster_undead = nw::Spell::make(280);
constexpr nw::Spell spellability_pulse_drown = nw::Spell::make(281);
constexpr nw::Spell spellability_pulse_spores = nw::Spell::make(282);
constexpr nw::Spell spellability_pulse_whirlwind = nw::Spell::make(283);
constexpr nw::Spell spellability_pulse_fire = nw::Spell::make(284);
constexpr nw::Spell spellability_pulse_lightning = nw::Spell::make(285);
constexpr nw::Spell spellability_pulse_cold = nw::Spell::make(286);
constexpr nw::Spell spellability_pulse_negative = nw::Spell::make(287);
constexpr nw::Spell spellability_pulse_holy = nw::Spell::make(288);
constexpr nw::Spell spellability_pulse_death = nw::Spell::make(289);
constexpr nw::Spell spellability_pulse_level_drain = nw::Spell::make(290);
constexpr nw::Spell spellability_pulse_ability_drain_intelligence = nw::Spell::make(291);
constexpr nw::Spell spellability_pulse_ability_drain_charisma = nw::Spell::make(292);
constexpr nw::Spell spellability_pulse_ability_drain_constitution = nw::Spell::make(293);
constexpr nw::Spell spellability_pulse_ability_drain_dexterity = nw::Spell::make(294);
constexpr nw::Spell spellability_pulse_ability_drain_strength = nw::Spell::make(295);
constexpr nw::Spell spellability_pulse_ability_drain_wisdom = nw::Spell::make(296);
constexpr nw::Spell spellability_pulse_poison = nw::Spell::make(297);
constexpr nw::Spell spellability_pulse_disease = nw::Spell::make(298);
constexpr nw::Spell spellability_rage_3 = nw::Spell::make(299);
constexpr nw::Spell spellability_rage_4 = nw::Spell::make(300);
constexpr nw::Spell spellability_rage_5 = nw::Spell::make(301);
constexpr nw::Spell spellability_smoke_claw = nw::Spell::make(302);
constexpr nw::Spell spellability_summon_slaad = nw::Spell::make(303);
constexpr nw::Spell spellability_summon_tanarri = nw::Spell::make(304);
constexpr nw::Spell spellability_trumpet_blast = nw::Spell::make(305);
constexpr nw::Spell spellability_tyrant_fog_mist = nw::Spell::make(306);
constexpr nw::Spell spellability_barbarian_rage = nw::Spell::make(307);
constexpr nw::Spell spellability_turn_undead = nw::Spell::make(308);
constexpr nw::Spell spellability_wholeness_of_body = nw::Spell::make(309);
constexpr nw::Spell spellability_quivering_palm = nw::Spell::make(310);
constexpr nw::Spell spellability_empty_body = nw::Spell::make(311);
constexpr nw::Spell spellability_detect_evil = nw::Spell::make(312);
constexpr nw::Spell spellability_lay_on_hands = nw::Spell::make(313);
constexpr nw::Spell spellability_aura_of_courage = nw::Spell::make(314);
constexpr nw::Spell spellability_smite_evil = nw::Spell::make(315);
constexpr nw::Spell spellability_remove_disease = nw::Spell::make(316);
constexpr nw::Spell spellability_summon_animal_companion = nw::Spell::make(317);
constexpr nw::Spell spellability_summon_familiar = nw::Spell::make(318);
constexpr nw::Spell spellability_elemental_shape = nw::Spell::make(319);
constexpr nw::Spell spellability_wild_shape = nw::Spell::make(320);
// constexpr nw::Spell spell_protection_from_alignment =nw::Spell::make( 321);
// constexpr nw::Spell spell_magic_circle_against_alignment =nw::Spell::make( 322);
// constexpr nw::Spell spell_aura_versus_alignment =nw::Spell::make( 323);
constexpr nw::Spell spell_shades_summon_shadow = nw::Spell::make(324);
// constexpr nw::Spell spell_protection_from_elements_cold =nw::Spell::make( 325);
// constexpr nw::Spell spell_protection_from_elements_fire =nw::Spell::make( 326);
// constexpr nw::Spell spell_protection_from_elements_acid =nw::Spell::make( 327);
// constexpr nw::Spell spell_protection_from_elements_sonic =nw::Spell::make( 328);
// constexpr nw::Spell spell_protection_from_elements_electricity =nw::Spell::make( 329);
// constexpr nw::Spell spell_endure_elements_cold =nw::Spell::make( 330);
// constexpr nw::Spell spell_endure_elements_fire =nw::Spell::make( 331);
// constexpr nw::Spell spell_endure_elements_acid =nw::Spell::make( 332);
// constexpr nw::Spell spell_endure_elements_sonic =nw::Spell::make( 333);
// constexpr nw::Spell spell_endure_elements_electricity =nw::Spell::make( 334);
// constexpr nw::Spell spell_resist_elements_cold =nw::Spell::make( 335);
// constexpr nw::Spell spell_resist_elements_fire =nw::Spell::make( 336);
// constexpr nw::Spell spell_resist_elements_acid =nw::Spell::make( 337);
// constexpr nw::Spell spell_resist_elements_sonic =nw::Spell::make( 338);
// constexpr nw::Spell spell_resist_elements_electricity =nw::Spell::make( 339);
constexpr nw::Spell spell_shades_cone_of_cold = nw::Spell::make(340);
constexpr nw::Spell spell_shades_fireball = nw::Spell::make(341);
constexpr nw::Spell spell_shades_stoneskin = nw::Spell::make(342);
constexpr nw::Spell spell_shades_wall_of_fire = nw::Spell::make(343);
constexpr nw::Spell spell_shadow_conjuration_summon_shadow = nw::Spell::make(344);
constexpr nw::Spell spell_shadow_conjuration_darkness = nw::Spell::make(345);
constexpr nw::Spell spell_shadow_conjuration_inivsibility = nw::Spell::make(346);
constexpr nw::Spell spell_shadow_conjuration_mage_armor = nw::Spell::make(347);
constexpr nw::Spell spell_shadow_conjuration_magic_missile = nw::Spell::make(348);
constexpr nw::Spell spell_greater_shadow_conjuration_summon_shadow = nw::Spell::make(349);
constexpr nw::Spell spell_greater_shadow_conjuration_acid_arrow = nw::Spell::make(350);
constexpr nw::Spell spell_greater_shadow_conjuration_mirror_image = nw::Spell::make(351);
constexpr nw::Spell spell_greater_shadow_conjuration_web = nw::Spell::make(352);
constexpr nw::Spell spell_greater_shadow_conjuration_minor_globe = nw::Spell::make(353);
constexpr nw::Spell spell_eagle_spledor = nw::Spell::make(354);
constexpr nw::Spell spell_owls_wisdom = nw::Spell::make(355);
constexpr nw::Spell spell_foxs_cunning = nw::Spell::make(356);
constexpr nw::Spell spell_greater_eagle_splendor = nw::Spell::make(357);
constexpr nw::Spell spell_greater_owls_wisdom = nw::Spell::make(358);
constexpr nw::Spell spell_greater_foxs_cunning = nw::Spell::make(359);
constexpr nw::Spell spell_greater_bulls_strength = nw::Spell::make(360);
constexpr nw::Spell spell_greater_cats_grace = nw::Spell::make(361);
constexpr nw::Spell spell_greater_endurance = nw::Spell::make(362);
constexpr nw::Spell spell_awaken = nw::Spell::make(363);
constexpr nw::Spell spell_creeping_doom = nw::Spell::make(364);
constexpr nw::Spell spell_darkvision = nw::Spell::make(365);
constexpr nw::Spell spell_destruction = nw::Spell::make(366);
constexpr nw::Spell spell_horrid_wilting = nw::Spell::make(367);
constexpr nw::Spell spell_ice_storm = nw::Spell::make(368);
constexpr nw::Spell spell_energy_buffer = nw::Spell::make(369);
constexpr nw::Spell spell_negative_energy_burst = nw::Spell::make(370);
constexpr nw::Spell spell_negative_energy_ray = nw::Spell::make(371);
constexpr nw::Spell spell_aura_of_vitality = nw::Spell::make(372);
constexpr nw::Spell spell_war_cry = nw::Spell::make(373);
constexpr nw::Spell spell_regenerate = nw::Spell::make(374);
constexpr nw::Spell spell_evards_black_tentacles = nw::Spell::make(375);
constexpr nw::Spell spell_legend_lore = nw::Spell::make(376);
constexpr nw::Spell spell_find_traps = nw::Spell::make(377);
constexpr nw::Spell spellability_summon_mephit = nw::Spell::make(378);

constexpr nw::Spell spellability_summon_celestial = nw::Spell::make(379);
constexpr nw::Spell spellability_battle_mastery = nw::Spell::make(380);
constexpr nw::Spell spellability_divine_strength = nw::Spell::make(381);
constexpr nw::Spell spellability_divine_protection = nw::Spell::make(382);
constexpr nw::Spell spellability_negative_plane_avatar = nw::Spell::make(383);
constexpr nw::Spell spellability_divine_trickery = nw::Spell::make(384);
constexpr nw::Spell spellability_rogues_cunning = nw::Spell::make(385);
constexpr nw::Spell spellability_activate_item = nw::Spell::make(386);
constexpr nw::Spell spellability_dragon_fear = nw::Spell::make(412);

constexpr nw::Spell spell_divine_favor = nw::Spell::make(414);
constexpr nw::Spell spell_true_strike = nw::Spell::make(415);
constexpr nw::Spell spell_flare = nw::Spell::make(416);
constexpr nw::Spell spell_shield = nw::Spell::make(417);
constexpr nw::Spell spell_entropic_shield = nw::Spell::make(418);
constexpr nw::Spell spell_continual_flame = nw::Spell::make(419);
constexpr nw::Spell spell_one_with_the_land = nw::Spell::make(420);
constexpr nw::Spell spell_camoflage = nw::Spell::make(421);
constexpr nw::Spell spell_blood_frenzy = nw::Spell::make(422);
constexpr nw::Spell spell_bombardment = nw::Spell::make(423);
constexpr nw::Spell spell_acid_splash = nw::Spell::make(424);
constexpr nw::Spell spell_quillfire = nw::Spell::make(425);
constexpr nw::Spell spell_earthquake = nw::Spell::make(426);
constexpr nw::Spell spell_sunburst = nw::Spell::make(427);
constexpr nw::Spell spell_activate_item_self2 = nw::Spell::make(428);
constexpr nw::Spell spell_auraofglory = nw::Spell::make(429);
constexpr nw::Spell spell_banishment = nw::Spell::make(430);
constexpr nw::Spell spell_inflict_minor_wounds = nw::Spell::make(431);
constexpr nw::Spell spell_inflict_light_wounds = nw::Spell::make(432);
constexpr nw::Spell spell_inflict_moderate_wounds = nw::Spell::make(433);
constexpr nw::Spell spell_inflict_serious_wounds = nw::Spell::make(434);
constexpr nw::Spell spell_inflict_critical_wounds = nw::Spell::make(435);
constexpr nw::Spell spell_balagarnsironhorn = nw::Spell::make(436);
constexpr nw::Spell spell_drown = nw::Spell::make(437);
constexpr nw::Spell spell_owls_insight = nw::Spell::make(438);
constexpr nw::Spell spell_electric_jolt = nw::Spell::make(439);
constexpr nw::Spell spell_firebrand = nw::Spell::make(440);
constexpr nw::Spell spell_wounding_whispers = nw::Spell::make(441);
constexpr nw::Spell spell_amplify = nw::Spell::make(442);
constexpr nw::Spell spell_etherealness = nw::Spell::make(443);
constexpr nw::Spell spell_undeaths_eternal_foe = nw::Spell::make(444);
constexpr nw::Spell spell_dirge = nw::Spell::make(445);
constexpr nw::Spell spell_inferno = nw::Spell::make(446);
constexpr nw::Spell spell_isaacs_lesser_missile_storm = nw::Spell::make(447);
constexpr nw::Spell spell_isaacs_greater_missile_storm = nw::Spell::make(448);
constexpr nw::Spell spell_bane = nw::Spell::make(449);
constexpr nw::Spell spell_shield_of_faith = nw::Spell::make(450);
constexpr nw::Spell spell_planar_ally = nw::Spell::make(451);
constexpr nw::Spell spell_magic_fang = nw::Spell::make(452);
constexpr nw::Spell spell_greater_magic_fang = nw::Spell::make(453);
constexpr nw::Spell spell_spike_growth = nw::Spell::make(454);
constexpr nw::Spell spell_mass_camoflage = nw::Spell::make(455);
constexpr nw::Spell spell_expeditious_retreat = nw::Spell::make(456);
constexpr nw::Spell spell_tashas_hideous_laughter = nw::Spell::make(457);
constexpr nw::Spell spell_displacement = nw::Spell::make(458);
constexpr nw::Spell spell_bigbys_interposing_hand = nw::Spell::make(459);
constexpr nw::Spell spell_bigbys_forceful_hand = nw::Spell::make(460);
constexpr nw::Spell spell_bigbys_grasping_hand = nw::Spell::make(461);
constexpr nw::Spell spell_bigbys_clenched_fist = nw::Spell::make(462);
constexpr nw::Spell spell_bigbys_crushing_hand = nw::Spell::make(463);
constexpr nw::Spell spell_grenade_fire = nw::Spell::make(464);
constexpr nw::Spell spell_grenade_tangle = nw::Spell::make(465);
constexpr nw::Spell spell_grenade_holy = nw::Spell::make(466);
constexpr nw::Spell spell_grenade_choking = nw::Spell::make(467);
constexpr nw::Spell spell_grenade_thunderstone = nw::Spell::make(468);
constexpr nw::Spell spell_grenade_acid = nw::Spell::make(469);
constexpr nw::Spell spell_grenade_chicken = nw::Spell::make(470);
constexpr nw::Spell spell_grenade_caltrops = nw::Spell::make(471);
constexpr nw::Spell spell_activate_item_portal = nw::Spell::make(472);
constexpr nw::Spell spell_divine_might = nw::Spell::make(473);
constexpr nw::Spell spell_divine_shield = nw::Spell::make(474);
constexpr nw::Spell spell_shadow_daze = nw::Spell::make(475);
constexpr nw::Spell spell_summon_shadow = nw::Spell::make(476);
constexpr nw::Spell spell_shadow_evade = nw::Spell::make(477);
constexpr nw::Spell spell_tymoras_smile = nw::Spell::make(478);
constexpr nw::Spell spell_craft_harper_item = nw::Spell::make(479);
constexpr nw::Spell spell_flesh_to_stone = nw::Spell::make(485);
constexpr nw::Spell spell_stone_to_flesh = nw::Spell::make(486);
constexpr nw::Spell spell_trap_arrow = nw::Spell::make(487);
constexpr nw::Spell spell_trap_bolt = nw::Spell::make(488);
constexpr nw::Spell spell_trap_dart = nw::Spell::make(493);
constexpr nw::Spell spell_trap_shuriken = nw::Spell::make(494);

constexpr nw::Spell spellability_breath_petrify = nw::Spell::make(495);
constexpr nw::Spell spellability_touch_petrify = nw::Spell::make(496);
constexpr nw::Spell spellability_gaze_petrify = nw::Spell::make(497);
constexpr nw::Spell spellability_manticore_spikes = nw::Spell::make(498);

constexpr nw::Spell spell_rod_of_wonder = nw::Spell::make(499);
constexpr nw::Spell spell_deck_of_many_things = nw::Spell::make(500);
constexpr nw::Spell spell_elemental_summoning_item = nw::Spell::make(502);
constexpr nw::Spell spell_deck_avatar = nw::Spell::make(503);
constexpr nw::Spell spell_deck_gemspray = nw::Spell::make(504);
constexpr nw::Spell spell_deck_butterflyspray = nw::Spell::make(505);

constexpr nw::Spell spell_healingkit = nw::Spell::make(506);
constexpr nw::Spell spell_powerstone = nw::Spell::make(507);
constexpr nw::Spell spell_spellstaff = nw::Spell::make(508);
constexpr nw::Spell spell_charger = nw::Spell::make(500);
constexpr nw::Spell spell_decharger = nw::Spell::make(510);

constexpr nw::Spell spell_kobold_jump = nw::Spell::make(511);
constexpr nw::Spell spell_crumble = nw::Spell::make(512);
constexpr nw::Spell spell_infestation_of_maggots = nw::Spell::make(513);
constexpr nw::Spell spell_healing_sting = nw::Spell::make(514);
constexpr nw::Spell spell_great_thunderclap = nw::Spell::make(515);
constexpr nw::Spell spell_ball_lightning = nw::Spell::make(516);
constexpr nw::Spell spell_battletide = nw::Spell::make(517);
constexpr nw::Spell spell_combust = nw::Spell::make(518);
constexpr nw::Spell spell_death_armor = nw::Spell::make(519);
constexpr nw::Spell spell_gedlees_electric_loop = nw::Spell::make(520);
constexpr nw::Spell spell_horizikauls_boom = nw::Spell::make(521);
constexpr nw::Spell spell_ironguts = nw::Spell::make(522);
constexpr nw::Spell spell_mestils_acid_breath = nw::Spell::make(523);
constexpr nw::Spell spell_mestils_acid_sheath = nw::Spell::make(524);
constexpr nw::Spell spell_monstrous_regeneration = nw::Spell::make(525);
constexpr nw::Spell spell_scintillating_sphere = nw::Spell::make(526);
constexpr nw::Spell spell_stone_bones = nw::Spell::make(527);
constexpr nw::Spell spell_undeath_to_death = nw::Spell::make(528);
constexpr nw::Spell spell_vine_mine = nw::Spell::make(529);
constexpr nw::Spell spell_vine_mine_entangle = nw::Spell::make(530);
constexpr nw::Spell spell_vine_mine_hamper_movement = nw::Spell::make(531);
constexpr nw::Spell spell_vine_mine_camouflage = nw::Spell::make(532);
constexpr nw::Spell spell_black_blade_of_disaster = nw::Spell::make(533);
constexpr nw::Spell spell_shelgarns_persistent_blade = nw::Spell::make(534);
constexpr nw::Spell spell_blade_thirst = nw::Spell::make(535);
constexpr nw::Spell spell_deafening_clang = nw::Spell::make(536);
constexpr nw::Spell spell_cloud_of_bewilderment = nw::Spell::make(569);

constexpr nw::Spell spell_keen_edge = nw::Spell::make(539);
constexpr nw::Spell spell_blackstaff = nw::Spell::make(541);
constexpr nw::Spell spell_flame_weapon = nw::Spell::make(542);
constexpr nw::Spell spell_ice_dagger = nw::Spell::make(543);
constexpr nw::Spell spell_magic_weapon = nw::Spell::make(544);
constexpr nw::Spell spell_greater_magic_weapon = nw::Spell::make(545);

constexpr nw::Spell spell_stonehold = nw::Spell::make(547);
constexpr nw::Spell spell_darkfire = nw::Spell::make(548);
constexpr nw::Spell spell_glyph_of_warding = nw::Spell::make(549);

constexpr nw::Spell spellability_mindblast = nw::Spell::make(551);
constexpr nw::Spell spellability_charmmonster = nw::Spell::make(552);

constexpr nw::Spell spell_ioun_stone_dusty_rose = nw::Spell::make(554);
constexpr nw::Spell spell_ioun_stone_pale_blue = nw::Spell::make(555);
constexpr nw::Spell spell_ioun_stone_scarlet_blue = nw::Spell::make(556);
constexpr nw::Spell spell_ioun_stone_blue = nw::Spell::make(557);
constexpr nw::Spell spell_ioun_stone_deep_red = nw::Spell::make(558);
constexpr nw::Spell spell_ioun_stone_pink = nw::Spell::make(559);
constexpr nw::Spell spell_ioun_stone_pink_green = nw::Spell::make(560);

constexpr nw::Spell spellability_whirlwind = nw::Spell::make(561);
constexpr nw::Spell spellability_command_the_horde = nw::Spell::make(571);

constexpr nw::Spell spellability_aa_imbue_arrow = nw::Spell::make(600);
constexpr nw::Spell spellability_aa_seeker_arrow_1 = nw::Spell::make(601);
constexpr nw::Spell spellability_aa_seeker_arrow_2 = nw::Spell::make(602);
constexpr nw::Spell spellability_aa_hail_of_arrows = nw::Spell::make(603);
constexpr nw::Spell spellability_aa_arrow_of_death = nw::Spell::make(604);

constexpr nw::Spell spellability_as_ghostly_visage = nw::Spell::make(605);
constexpr nw::Spell spellability_as_darkness = nw::Spell::make(606);
constexpr nw::Spell spellability_as_invisibility = nw::Spell::make(607);
constexpr nw::Spell spellability_as_improved_invisiblity = nw::Spell::make(608);

constexpr nw::Spell spellability_bg_createdead = nw::Spell::make(609);
constexpr nw::Spell spellability_bg_fiendish_servant = nw::Spell::make(610);
constexpr nw::Spell spellability_bg_inflict_serious_wounds = nw::Spell::make(611);
constexpr nw::Spell spellability_bg_inflict_critical_wounds = nw::Spell::make(612);
constexpr nw::Spell spellability_bg_contagion = nw::Spell::make(613);
constexpr nw::Spell spellability_bg_bulls_strength = nw::Spell::make(614);

constexpr nw::Spell spell_flying_debris = nw::Spell::make(620);

constexpr nw::Spell spellability_dc_divine_wrath = nw::Spell::make(622);
constexpr nw::Spell spellability_pm_animate_dead = nw::Spell::make(623);
constexpr nw::Spell spellability_pm_summon_undead = nw::Spell::make(624);
constexpr nw::Spell spellability_pm_undead_graft_1 = nw::Spell::make(625);
constexpr nw::Spell spellability_pm_undead_graft_2 = nw::Spell::make(626);
constexpr nw::Spell spellability_pm_summon_greater_undead = nw::Spell::make(627);
constexpr nw::Spell spellability_pm_deathless_master_touch = nw::Spell::make(628);
constexpr nw::Spell spell_epic_hellball = nw::Spell::make(636);
constexpr nw::Spell spell_epic_mummy_dust = nw::Spell::make(637);
constexpr nw::Spell spell_epic_dragon_knight = nw::Spell::make(638);
constexpr nw::Spell spell_epic_mage_armor = nw::Spell::make(639);
constexpr nw::Spell spell_epic_ruin = nw::Spell::make(640);
constexpr nw::Spell spellability_dw_defensive_stance = nw::Spell::make(641);
constexpr nw::Spell spellability_epic_mighty_rage = nw::Spell::make(642);
constexpr nw::Spell spellability_epic_curse_song = nw::Spell::make(644);
constexpr nw::Spell spellability_epic_improved_whirlwind = nw::Spell::make(645);
constexpr nw::Spell spellability_epic_shape_dragonkin = nw::Spell::make(646);
constexpr nw::Spell spellability_epic_shape_dragon = nw::Spell::make(647);
constexpr nw::Spell spell_craft_dye_clothcolor_1 = nw::Spell::make(648);
constexpr nw::Spell spell_craft_dye_clothcolor_2 = nw::Spell::make(649);
constexpr nw::Spell spell_craft_dye_leathercolor_1 = nw::Spell::make(650);
constexpr nw::Spell spell_craft_dye_leathercolor_2 = nw::Spell::make(651);
constexpr nw::Spell spell_craft_dye_metalcolor_1 = nw::Spell::make(652);
constexpr nw::Spell spell_craft_dye_metalcolor_2 = nw::Spell::make(653);
constexpr nw::Spell spell_craft_add_item_property = nw::Spell::make(654);
constexpr nw::Spell spell_craft_poison_weapon_or_ammo = nw::Spell::make(655);
constexpr nw::Spell spell_craft_craft_weapon_skill = nw::Spell::make(656);
constexpr nw::Spell spell_craft_craft_armor_skill = nw::Spell::make(657);
constexpr nw::Spell spellability_dragon_breath_negative = nw::Spell::make(698);
constexpr nw::Spell spellability_seahag_evileye = nw::Spell::make(803);
constexpr nw::Spell spellability_aura_horrificappearance = nw::Spell::make(804);
constexpr nw::Spell spellability_troglodyte_stench = nw::Spell::make(805);
constexpr nw::Spell spell_horse_menu = nw::Spell::make(812);
constexpr nw::Spell spell_horse_mount = nw::Spell::make(813);
constexpr nw::Spell spell_horse_dismount = nw::Spell::make(814);
constexpr nw::Spell spell_horse_party_mount = nw::Spell::make(815);
constexpr nw::Spell spell_horse_party_dismount = nw::Spell::make(816);
constexpr nw::Spell spell_horse_assign_mount = nw::Spell::make(817);
constexpr nw::Spell spell_paladin_summon_mount = nw::Spell::make(818);

} // namespace nwn1
