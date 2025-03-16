from typing import Dict, Set

from .names import region_names as rname
from .names import shell_names as sname

ACT_regions: Dict[str, Set[str]] = {
    rname.menu: {
        rname.tide_pool
    },
    rname.tide_pool: {
        rname.starting_cave
    },
    rname.starting_cave: {
        rname.central_shallows
    },
    rname.central_shallows: {
        rname.slacktide_before,
    },
    rname.slacktide_before: {
        rname.snail_cave,
        sname.soda_can,
        sname.coconut,
        sname.banana_peel,
        sname.tin_can
    },
    rname.snail_cave: {
        rname.slacktide_after,
        sname.soda_can,
        sname.bottle_cap,
        sname.shot_glass,
        sname.party_hat,
    },
    rname.slacktide_after: {
        rname.reefs_edge,
        sname.teacup
    },
    rname.reefs_edge: {
        rname.new_carcinia,
        sname.salt_shaker,
        sname.thimble,
        sname.tennis_ball,
        sname.sauce_nozzle
    },
    rname.new_carcinia: {
        rname.sands_between,
        sname.f_key
    },
    rname.sands_between: {
        rname.post_pag,
        rname.secluded_ridge,
        rname.grove_main,
        rname.flotsam_vale,
        sname.coffee_pod,
        sname.cascadia_roll,
        sname.ink_cartridge,
        sname.yoccult,
        sname.legal_brick,
        sname.mason_jar,
        sname.valve,
        sname.bebop_cup,
        sname.wafer_cone,
        sname.shotgun_shell,
        sname.egg_shell,
        sname.disco_ball
    },
    rname.post_pag: set(),
    rname.secluded_ridge: set(),
    rname.grove_main: {
        rname.grove_village,
        sname.coffee_mug,
    },
    rname.grove_village: {
        sname.skull,
        sname.ham_tin,
        sname.crab_husk
    },
    rname.flotsam_vale: {
        rname.grove_village,
        rname.scuttleport,
        sname.boxing_glove,
        sname.spring,
        sname.rubber_duck,
        sname.tissue_box,
        sname.cardboard_box
    },
    rname.scuttleport: {
        rname.pinbarge,
        sname.dumptruck,
        sname.plug_fuse
    },
    rname.pinbarge: {
        rname.unfathom,
        sname.gacha_capsule
    },
    rname.unfathom: {
        rname.plains,
        sname.doll_head,
        sname.lightbulb,
        sname.mouse
    },
    rname.plains: {
        rname.old_ocean
    },
    rname.old_ocean: {
        rname.drain_bottom,
        sname.ultrasoft,
        sname.pill_bottle,
        sname.scrub_aggie,
        sname.knights_helmet,
        sname.snow_globe,
        sname.detergent_cap,
        sname.champagne_flute,
        sname.dentures
    },
    rname.drain_bottom: {
        rname.trash_island
    },
    rname.trash_island: {
        rname.carcinia_ruins
    },
    rname.carcinia_ruins: set(),
    sname.soda_can: set(),
    sname.bottle_cap: set(),
    sname.tin_can : set(),
    sname.shot_glass : set(),
    sname.banana_peel : set(),
    sname.party_hat : set(),
    sname.coconut: set(),
    sname.teacup: set(),
    sname.sauce_nozzle : set(),
    sname.thimble: set(),
    sname.bebop_cup : set(),
    sname.tennis_ball: set(),
    sname.f_key : set(),
    sname.mason_jar : set(),
    sname.salt_shaker : set(),
    sname.conchiglie : set(),
    sname.bartholomew : set(),
    sname.disco_ball : set(),
    sname.baby_shoe : set(),
    sname.lil_bro : set(),
    sname.matryoshka_large : set(),
    sname.matryoshka_medium : set(),
    sname.matryoshka_small : set(),
    sname.shuttlecock : set(),
    sname.felix_cube : set(),
    sname.piggy_bank : set(),
    sname.trophy : set(),
    sname.imposter : set(),
    sname.lil_red_cup : set(),
    sname.wafer_cone : set(),
    sname.yoccult : set(),
    sname.coffee_pod : set(),
    sname.egg_shell : set(),
    sname.coffee_mug : set(),
    sname.cascadia_roll : set(),
    sname.ham_tin : set(),
    sname.skull : set(),
    sname.crab_husk : set(),
    sname.legal_brick : set(),
    sname.spring : set(),
    sname.shotgun_shell : set(),
    sname.rubber_duck: set(),
    sname.boxing_glove : set(),
    sname.cardboard_box : set(),
    sname.tissue_box: set(),
    sname.valve : set(),
    sname.dumptruck: set(),
    sname.ink_cartridge: set(),
    sname.gacha_capsule: set(),
    sname.lightbulb: set(),
    sname.mouse : set(),
    sname.going_under_64 : set(),
    sname.sock : set(),
    sname.doll_head : set(),
    sname.service_bell : set(),
    sname.party_popper : set(),
    sname.scrub_aggie : set(),
    sname.dentures: set(),
    sname.pill_bottle : set(),
    sname.detergent_cap: set(),
    sname.ultrasoft: set(),
    sname.champagne_flute: set(),
    sname.dish_scrubber: set(),
    sname.snow_globe : set(),
    sname.knights_helmet : set(),
    sname.plug_fuse: set()


}

