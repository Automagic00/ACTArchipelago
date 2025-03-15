from typing import Dict, List, NamedTuple, Set, Optional
from BaseClasses import Location

from .names import location_names as lname, region_names as rname, shell_names as sname

class ACTLocation(Location):
    game: str = "Another Crabs Treasure"

location_base_id: int = 483021700

class ACTLocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None


location_table: Dict[str, ACTLocationData] = {
    # starting item locations (will probably just include heartkelp_initial and fork pickup because they are the items you pick up right at the beginning of the game)


    # Last used number: 619; 618 is available

    #lname.heartkelp_inital: ACTLocationData("Tide Pools", "Starting Items"),#950e628c-f657-48d4-b93b-f8717627f6b3-2_A-ShallowsTidePools
    lname.fork_pickup: ACTLocationData(rname.starting_cave,0, "Starting Items"),#73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools

    # progression item locations
    lname.fishing_line: ACTLocationData(rname.slacktide_before, 2, "Fort Slacktide"),
    #lname.pristine_pearl: ACTLocationData(rname.snail_cave, x, "Moon Snail's Cave"), #Redundant, overlaps with Platoon Pathfinder
    lname.map_piece_heikea_arena: ACTLocationData(rname.grove_main, 252, "Expired Grove Main"),
    lname.map_piece_vale: ACTLocationData(rname.flotsam_vale, 396, "Flotsam Vale"),

    # boss locations
    lname.nephro: ACTLocationData(rname.central_shallows, 3, "Central Shallows"),
    lname.platoon_pathfinder: ACTLocationData(rname.snail_cave, 46, "Moon Snail's Cave"),
    lname.magista: ACTLocationData(rname.slacktide_after, 44, "Fort Slacktide - After Destruction"),
    lname.royal_shellsplitter: ACTLocationData(rname.central_shallows, 47, "Central Shallows"),
    lname.pagurus: ACTLocationData(rname.sands_between, 48, "Sands Between"),
    lname.lichenthrope: ACTLocationData(rname.grove_main, 49, "Expired Grove Main"), #must fix region name and location group before re-adding
    lname.carbonara_connoisseur: ACTLocationData(rname.grove_main, 50, "Expired Grove Main"),
    lname.heikea: ACTLocationData(rname.grove_main, 51, "Expired Grove Main"),
    lname.topoda: ACTLocationData(rname.grove_village, 52, "Expired Grove Village"),
    lname.consortium: ACTLocationData(rname.flotsam_vale, 53, "Flotsam Vale"),
    lname.sludge_steamroller: ACTLocationData(rname.flotsam_vale, 54, "Flotsam Vale"),
    lname.ceviche_sisters: ACTLocationData(rname.flotsam_vale, 55, "Flotsam Vale"),
    lname.voltai: ACTLocationData(rname.scuttleport, 56, "Scuttleport"),
    lname.roland: ACTLocationData(rname.pinbarge, 57, "Pinbarge"),
    lname.petroch: ACTLocationData(rname.unfathom, 58, "The Unfathom"),
    lname.inkerton: ACTLocationData(rname.plains, 59, "Abyssal Plains"),
    lname.camtscha: ACTLocationData(rname.old_ocean, 60, "The Old Ocean"),
    lname.praya_dubia: ACTLocationData(rname.drain_bottom, 61, "Bottom of The Drain"),
    lname.firth: ACTLocationData(rname.trash_island, 62, "Trash Island"),
    
    ##### currency item locations

    lname.breadclaw_caveofrespite_ledge: ACTLocationData(rname.starting_cave, 4,"Cave of Respite"), #73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools
    lname.chipclaw_caveofrespite_forkroomfishing: ACTLocationData(rname.starting_cave, 120,"Cave of Respite"), #d985ffba-0ece-414d-8161-fa65241dd2b1-2_B-ShallowsBigSand
    lname.mussel_caveofrespite_crabfightfishing: ACTLocationData(rname.starting_cave, 121,"Cave of Respite"), #d1af097b-c6c9-44a4-9ced-4a09a973c0d5-2_B-ShallowsBigSand
    lname.clothesclaw_caveofrespite_entrancefishing: ACTLocationData(rname.starting_cave, 122,"Cave of Respite"), #0ac3fa03-5aab-4f12-86e4-8e9dfde8c04f-2_B-ShallowsBigSand
    lname.sanddollar_caveofrespite_pathfishing: ACTLocationData(rname.starting_cave, 123,"Cave of Respite"), #9ef4b1f3-5a80-408c-962a-b3fed8c68770-2_B-ShallowsBigSand

    lname.breadclaw_shallows_southsandal: ACTLocationData(rname.central_shallows, 5, "Central Shallows"),#0171a152-809a-47cf-9fcc-60ddb61511bb-2_B-ShallowsBigSand
    lname.breadclaw_shallows_westwall: ACTLocationData(rname.central_shallows, 6, "Central Shallows"), #ae27274c-c3f7-4721-9ddb-7c5a880578a4-2_B-ShallowsBigSand
    lname.breadclaw_shallows_bridge: ACTLocationData(rname.central_shallows, 7, "Central Shallows"), #8b269a88-c6d1-4b2a-8e5f-9d60c6d6fd15-2_B-ShallowsBigSand
    lname.breadclaw_shallows_eastwall: ACTLocationData(rname.central_shallows, 8, "Central Shallows"), #6aba5604-8269-46a5-b734-ef4dc3983265-2_B-ShallowsBigSand
    lname.breadclaw_shallows_eastsandal: ACTLocationData(rname.central_shallows, 9, "Central Shallows"), #889c343a-b969-4295-b059-a837fc457444-2_B-ShallowsBigSand
    lname.breadclaw_shallows_cigarette: ACTLocationData(rname.central_shallows, 10, "Central Shallows"), #d1ddf122-d283-4509-8bfa-bff8fa209f35-2_B-ShallowsBigSand
    lname.breadclaw_shallows_fortwall: ACTLocationData(rname.central_shallows, 11, "Central Shallows"), #20bede55-9eae-40a3-a80a-63ee5b52d0bf-2_B-ShallowsBigSand
    lname.breadclaw_shallows_wallpiece: ACTLocationData(rname.central_shallows, 12, "Central Shallows"), #5732b602-c599-41b5-bc5d-93e88277a4b7-2_B-ShallowsBigSand
    lname.breadclaw_shallows_sandcastle: ACTLocationData(rname.central_shallows, 13, "Central Shallows"), #984eda06-d10e-4b2b-a5c4-389784ed18f6-2_B-ShallowsBigSand
    lname.breadclaw_shallows_eastledge: ACTLocationData(rname.central_shallows, 14, "Central Shallows"), #51dbcbfd-4a82-4c22-b2ee-1a03deeca4cc-2_B-ShallowsBigSand
    lname.hairclaw_shallows_turret: ACTLocationData(rname.central_shallows, 15, "Central Shallows"), #b2d21ade-41ab-47fc-960b-0beb6d07359d-2_B-ShallowsBigSand
    lname.chipclaw_shallows_sandcastle: ACTLocationData(rname.central_shallows, 16, "Central Shallows"), #12c6e5c5-eee1-4f9a-a3c4-68c2bd098a14-2_B-ShallowsBigSand
    #lname.clothesclaw_shallows_shellsplitter: ACTLocationData(rname.central_shallows, 17, "Central Shallows"), #AUTO NEEDS TO DO BOSS SCRIPT
    lname.clothesclaw_shallows_southwestfort: ACTLocationData(rname.central_shallows, 45, "Central Shallows"), #e13e2c76-a638-4023-aa84-f6f29fd7bf65-2_B-ShallowsBigSand
    lname.breadclaw_shallows_sunkentower: ACTLocationData(rname.central_shallows, 124, "Central Shallows"), #1e33dfd0-6445-47f9-b1bf-3e8be7897a79-2_B-ShallowsBigSand
    lname.breadclaw_shallows_slacktidesouthfish: ACTLocationData(rname.central_shallows, 126, "Central Shallows"), #0f64d031-4163-4979-9497-116cac06e234-2_B-ShallowsBigSand


    lname.breadclaw_slacktide_crates: ACTLocationData(rname.slacktide_before, 18, "Fort Slacktide - Before Destruction"), #8c1e68dc-eb15-41f4-9a5d-c1b20dd76f52-2_B-ShallowsBigSand
    lname.breadclaw_slacktide_training: ACTLocationData(rname.slacktide_before, 130, "Fort Slacktide - Before Destruction"), #0ad90b46-ca8b-46ed-9cc6-f72ffcdb9d33-2_B-ShallowsBigSand

    lname.breadclaw_snailcave_entrance: ACTLocationData(rname.snail_cave, 19, "Moon Snail's Cave"), #5bb2169d-f820-41f0-9783-336c006861c6-2_D-MoonSnailShellCave
    lname.breadclaw_snailcave_shortcut: ACTLocationData(rname.snail_cave, 20, "Moon Snail's Cave"), #436eff44-09df-451e-93c8-3a5714ec55c2-2_D-MoonSnailShellCave
    lname.breadclaw_snailcave_jelly: ACTLocationData(rname.snail_cave, 21, "Moon Snail's Cave"), #07977d86-44ec-40d0-b331-8b45b1d44838-2_D-MoonSnailShellCave

    lname.breadclaw_slacktide_crabtrio: ACTLocationData(rname.slacktide_after, 22, "Fort Slacktide - After Destruction"), #2af7f575-51f3-4da9-b3bf-eab9d32a3bd8-2_C-Slacktide2
    lname.chipclaw_slacktide_brokenwall: ACTLocationData(rname.slacktide_after, 23, "Fort Slacktide - After Destruction"), #45f42ae3-41b6-4333-875f-3a9e8387e087-2_C-Slacktide2
    lname.breadclaw_slacktide_roofhiddenfish: ACTLocationData(rname.slacktide_after, 131, "Fort Slacktide - After Destruction"), #59e2ec5a-b650-43fa-879d-3af1569fb640-2_B-ShallowsBigSand

    lname.chipclaw_reefsedge_brokenbridge: ACTLocationData(rname.reefs_edge, 63, "Reef's Edge"), #e9bf56b8-1362-42a9-87a2-00bed3a6f5d2-2_A-NCTradeRoute
    lname.breadclaw_reefsedge_thimblecrab: ACTLocationData(rname.reefs_edge, 67, "Reef's Edge"), #1f5a8d6b-10ab-4e4e-b240-284e2ec2c77a-2_A-NCTradeRoute
    lname.hairclaw_reefsedge_sign: ACTLocationData(rname.reefs_edge, 71, "Reef's Edge"), #b478df52-084c-4c14-8a55-215fdbaeaffe-2_A-NCTradeRoute

    lname.breadclaw_newcarcinia_entrance: ACTLocationData(rname.new_carcinia, 74, "New Carcinia"), #fb5e2e88-b498-4af4-b7a6-4f176eb4016c-2_B-NCCity
    lname.breadclaw_newcarcinia_hammerhead: ACTLocationData(rname.new_carcinia, 76, "New Carcinia"), #e26a7cee-15af-4f6c-b6fb-253f8dfac6e4-2_B-NCCity
    lname.breadclaw_newcarcinia_bottomalley: ACTLocationData(rname.new_carcinia, 79, "New Carcinia"), #4058fdd6-84f5-4f1e-b8f1-3dcccb288aa2-2_B-NCCity
    lname.breadclaw_newcarcinia_prawnalley: ACTLocationData(rname.new_carcinia, 80, "New Carcinia"), #d538af5f-81e0-452c-8800-756bb635a16b-2_B-NCCity
    lname.chipclaw_newcarcinia_leg: ACTLocationData(rname.new_carcinia, 81, "New Carcinia"), #4f62e34e-df79-4e33-99bb-b65844e50304-2_B-NCCity
    lname.breadclaw_newcarcinia_tallbuilding: ACTLocationData(rname.new_carcinia, 82, "New Carcinia"), #0e59ec85-36b5-4750-baf4-cc9899525ca6-2_B-NCCity
    lname.breadclaw_newcarcinia_shortbuilding: ACTLocationData(rname.new_carcinia, 83, "New Carcinia"), #c91a3fa0-f774-4e5f-a43e-90dd9a1d5e3a-2_B-NCCity
    lname.chipclaw_newcarcinia_prawnshop: ACTLocationData(rname.new_carcinia, 84, "New Carcinia"), #d2b95a55-ec16-48cc-bce4-c7e39a16a78a-2_B-NCCity

    lname.breadclaw_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 87, "The Sands Between"), #4a22c058-bbb2-467a-b204-9c1a82dc0d9c-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southernreef: ACTLocationData(rname.sands_between, 94, "The Sands Between"), #cc1a7d82-3803-474e-8f66-c149055c4cb9-2_A-OOGroveRadius
    lname.chipclaw_sandsbetween_grove: ACTLocationData(rname.sands_between, 102, "The Sands Between"), #0bae76f4-e90b-435b-9089-356ef62ba0fa-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_chains: ACTLocationData(rname.sands_between, 106, "The Sands Between"), #d78747bd-2da0-4421-add8-3c5842fa0f61-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_bobbit: ACTLocationData(rname.sands_between, 107, "The Sands Between"), #e128b8e9-0c20-426f-8f47-783043f829dc-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_bobbit: ACTLocationData(rname.sands_between, 108, "The Sands Between"), #8d9edda5-d554-4e75-8842-8239075a334a-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_northwest: ACTLocationData(rname.sands_between, 111, "The Sands Between"), #7e93197a-47f1-4bdd-b7f0-5d0ecffb39f4-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_grove: ACTLocationData(rname.sands_between, 112, "The Sands Between"), #cd2f3731-b9f4-4f88-abd2-44d142eca493-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_propanecliff: ACTLocationData(rname.sands_between, 135, "The Sands Between"), #f553b94c-14ea-4852-8ae7-564b8d30b24d-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_northchains: ACTLocationData(rname.sands_between, 137, "The Sands Between"), #7e4ef7d0-214a-4358-a0c3-866a869d71e0-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_coolerpitfall: ACTLocationData(rname.sands_between, 138, "The Sands Between"), #9faef117-fd92-47cb-b4d8-cc2a07404a69-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southgrovepit: ACTLocationData(rname.sands_between, 139, "The Sands Between"), #305be10e-d5a7-42e6-88f1-2cebdd524bbb-2_A-OOGroveRadius
    lname.paperclaw_sandsbetween_southeelshortcut: ACTLocationData(rname.sands_between, 147, "The Sands Between"), #0e2d558b-26a7-4213-be83-77355fe06128-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southeel: ACTLocationData(rname.sands_between, 150, "The Sands Between"), #5c8133eb-ddb3-4b24-9849-f4d3f03491e0-2_A-OOGroveRadius
    lname.paperclaw_sandsbetween_trashanchor: ACTLocationData(rname.sands_between, 155, "The Sands Between"), #98e4d994-92c4-4b3b-82b7-f460a49d604b-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_anchorfish: ACTLocationData(rname.sands_between, 156, "The Sands Between"), #cab91803-4006-456d-95c7-6ec17d90c26a-2_A-OOGroveRadius
    lname.chipclaw_sandsbetween_northeastchainfish: ACTLocationData(rname.sands_between, 157, "The Sands Between"), #b0bf9c58-ff96-404c-bd1b-361fb1711b64-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_propanefish: ACTLocationData(rname.sands_between, 158, "The Sands Between"), #17b29697-5b33-4568-a311-2dbfac60317a-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_anchorcentralfish: ACTLocationData(rname.sands_between, 160, "The Sands Between"), #628bf319-c5f3-448b-8ec0-71a173246a09-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_nailfish: ACTLocationData(rname.sands_between, 162, "The Sands Between"), #98c3bf98-c4bd-4c67-8678-0464e7095970-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_palletfish: ACTLocationData(rname.sands_between, 163, "The Sands Between"), #69ac316d-8d42-48a4-8d55-4ec4d6429c7c-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southeelfish: ACTLocationData(rname.sands_between, 164, "The Sands Between"), #38edc1a4-dea8-4000-8683-6cda7f6ba3bc-2_A-OOGroveRadius
    lname.chipclaw_sandsbetween_anchoreelhiddenfish: ACTLocationData(rname.sands_between, 165, "The Sands Between"), #01999bed-4813-4fe3-ab9b-5ed19cce90f1-2_A-OOGroveRadius

    lname.stapleclaw_postpag_litter: ACTLocationData(rname.post_pag, 170, "The Sands Between - Post Pagurus"), #e872d437-5bdb-4e70-820a-030bc21d66d5-2_A-OOGroveRadius
    lname.hairclaw_postpag_chains: ACTLocationData(rname.post_pag, 171, "The Sands Between - Post Pagurus"), #4e9d02aa-75f5-4b87-b029-6ee1e7d62f7a-2_A-OOGroveRadius
    lname.clothesclaw_postpag_chains: ACTLocationData(rname.post_pag, 172, "The Sands Between - Post Pagurus"), #2fa3fdd0-b3da-4c69-b579-a5d316075635-2_A-OOGroveRadius
    lname.hairclaw_postpag_nridge: ACTLocationData(rname.post_pag, 179, "The Sands Between - Post Pagurus"), #55fafe55-5d22-49a8-8b2b-aea149468a61-2_A-OOGroveRadius
    lname.hairclaw_postpag_ecentral: ACTLocationData(rname.post_pag, 180, "The Sands Between - Post Pagurus"), #c2d06d3f-65f4-46cf-b069-0b4098b425d0-2_A-OOGroveRadius
    lname.chipclaw_postpag_nwpropane: ACTLocationData(rname.post_pag, 182, "The Sands Between - Post Pagurus"), #45af0c47-a8e0-498f-8345-9c9ddabbd6b3-2_A-OOGroveRadius
    lname.paperclaw_postpag_schain: ACTLocationData(rname.post_pag, 185, "The Sands Between - Post Pagurus"), #16dfae13-103f-45eb-9661-3e6463a2b805-2_A-OOGroveRadius

    lname.clothesclaw_ridge_neridge: ACTLocationData(rname.secluded_ridge, 189, "The Sands Between - Secluded Ridge"), #e2803d8a-feea-45a7-addf-3330748d9e4b-2_A-OOGroveRadius
    lname.paperclaw_ridge_nearoverlook: ACTLocationData(rname.secluded_ridge, 193, "The Sands Between - Secluded Ridge"), #f6db9d48-5df1-4a7f-9f17-b760901954c9-2_A-OOGroveRadius
    lname.clothesclaw_ridge_broom: ACTLocationData(rname.secluded_ridge, 195, "The Sands Between - Secluded Ridge"), #3f8d4c85-202f-42dc-9105-434d601d1d75-2_A-OOGroveRadius
    lname.breadclaw_ridge_south: ACTLocationData(rname.secluded_ridge, 197, "The Sands Between - Secluded Ridge"), #d1883b57-b339-4c31-826a-e76a3de0ee4b-2_A-OOGroveRadius
    lname.clothesclaw_ridge_overlookfish: ACTLocationData(rname.secluded_ridge, 206, "The Sands Between - Secluded Ridge"), #4f737f9e-a952-490c-b54d-1f74735af9cc-2_A-OOGroveRadius
    lname.chipclaw_ridge_southfish: ACTLocationData(rname.secluded_ridge, 207, "The Sands Between - Secluded Ridge"), #82043889-30eb-45f4-8f87-45dd2f5d69ed-2_A-OOGroveRadius

    lname.stapleclaw_trashbin_eelfish: ACTLocationData(rname.secluded_ridge, 209, "The Sands Between - Trashbin Plateau"), #190034bb-c13e-42ec-bac4-037cc828fde3-2_A-OOGroveRadius

    lname.breadclaw_grovemain_takeout: ACTLocationData(rname.grove_main, 219, "Expired Grove Main"), #4933d4b0-a56a-4472-b9a6-4469fd335fa4-2_A-GroveForestLow
    lname.breadclaw_grovemain_tiretop: ACTLocationData(rname.grove_main, 224, "Expired Grove Main"), #da04ed8f-2d99-48f9-8412-67748d983d2b-2_A-GroveForestLow
    lname.chipclaw_grovemain_plastic: ACTLocationData(rname.grove_main, 225, "Expired Grove Main"), #902c2deb-1b51-4226-9fd0-1c76bea668c3-2_A-GroveForestLow
    lname.clothesclaw_grovemain_choccymilk: ACTLocationData(rname.grove_main, 226, "Expired Grove Main"), #e38ef2da-daaf-4312-bf7f-2e0a97d3d67b-2_A-GroveForestLow
    lname.breadclaw_grovemain_insidetire: ACTLocationData(rname.grove_main, 227, "Expired Grove Main"), #def84515-cfc0-4124-a1e1-81f6953b0c06-2_A-GroveForestLow
    lname.chipclaw_grovemain_sniper: ACTLocationData(rname.grove_main, 245, "Expired Grove Main"), #070b84a6-7a8b-4d88-8216-f55882856713-2_A-GroveForestLow
    lname.hairclaw_grovemain_milkurchins: ACTLocationData(rname.grove_main, 246, "Expired Grove Main"), #e78f03e8-2827-45d7-8cfa-cbaa0f17cd3d-2_A-GroveForestLow
    lname.breadclaw_grovemain_smallhall: ACTLocationData(rname.grove_main, 231, "Expired Grove Main"), #be378f83-9ec2-4a3b-85b2-9a7499e6d693-2_A-GroveForestLow
    lname.chipclaw_grovemain_apples: ACTLocationData(rname.grove_main, 232, "Expired Grove Main"), #faa3c9ce-87c7-4f6d-b07e-be334c3bc447-2_A-GroveForestLow
    lname.chipclaw_grovemain_sodacans: ACTLocationData(rname.grove_main, 233, "Expired Grove Main"), #25737275-a222-4a6e-af6b-0c66c197cab7-2_A-GroveForestLow
    lname.hairclaw_grovemain_moonshine: ACTLocationData(rname.grove_main, 234, "Expired Grove Main"), #fd557b69-ddba-4b14-bd80-f0cb0d786203-2_A-GroveForestLow
    lname.chipclaw_grovemain_circlerock: ACTLocationData(rname.grove_main, 238, "Expired Grove Main"), #1b74ef4f-528c-484b-9a5f-abbb3434f133-2_A-GroveForestLow
    lname.clothesclaw_grovemain_alcove: ACTLocationData(rname.grove_main, 239, "Expired Grove Main"), #f99a120b-43c2-4e65-91fd-71cbfbf3e8f7-2_A-GroveForestLow
    lname.hairclaw_grovemain_sniper: ACTLocationData(rname.grove_main, 240, "Expired Grove Main"), #8f4a1f33-e567-4c84-b34b-739353b3ba08-2_A-GroveForestLow
    lname.breadclaw_grovemain_amongus: ACTLocationData(rname.grove_main, 243, "Expired Grove Main"), #c859129f-cc29-4624-a161-fdeffa00d0ca-2_B-GroveForestHigh
    lname.breadclaw_grovemain_oildrum: ACTLocationData(rname.grove_main, 244, "Expired Grove Main"), #b85cb09c-f1d7-4396-85cb-fde4dc845acd-2_B-GroveForestHigh
    lname.breadclaw_grovemain_oilgrapple: ACTLocationData(rname.grove_main, 249, "Expired Grove Main"), #bc18b92b-a6c6-420c-9095-e15c34c2f921-2_B-GroveForestHigh
    lname.clothesclaw_grovemain_mantisfish: ACTLocationData(rname.grove_main, 256, "Expired Grove Main"), #048736b5-59c1-4dd2-b36a-e11b6bd9304f-2_A-GroveForestLow
    lname.hairclaw_grovemain_fishing: ACTLocationData(rname.grove_main, 257, "Expired Grove Main"), #23907bde-1820-4c4d-9c59-aab72c64139a-2_A-GroveForestLow
    lname.clothesclaw_grovemain_riverfish: ACTLocationData(rname.grove_main, 258, "Expired Grove Main"), #ebad553d-fbff-441e-8c1d-0ccc65fe81ae-2_A-GroveForestLow

    lname.breadclaw_grovevillage_oildrum: ACTLocationData(rname.grove_village, 268, "Expired Grove Village"), #66a4a627-ad3a-45d6-aaf1-1e505dac0495-2_B-GroveForestHigh
    lname.breadclaw_grovevillage_bottle1: ACTLocationData(rname.grove_village, 269, "Expired Grove Village"), #a6e719fc-65b0-4c3a-830e-43065a819c7d-2_B-GroveForestHigh
    lname.breadclaw_grovevillage_bottle2: ACTLocationData(rname.grove_village, 270, "Expired Grove Village"), #507a5ca4-3de6-4d85-ba51-04c1e42c891e-2_B-GroveForestHigh
    lname.chipclaw_grovevillage_netorbs: ACTLocationData(rname.grove_village, 253, "Expired Grove Village"), #df0386e0-99ee-478a-873d-b40e973fc16b-2_D-Caves
    lname.hairclaw_grovevillage_river: ACTLocationData(rname.grove_village, 272, "Expired Grove Village"), #ec08fee3-e62f-45ee-9fbe-9101522d4f30-2_B-GroveForestHigh
    lname.chipclaw_grovevillage_NWcarton: ACTLocationData(rname.grove_village, 276, "Expired Grove Village"), #84c9cc27-0876-4e4d-a9e2-c28f06abdfc3-2_C-Village
    lname.chipclaw_grovevillage_SEcarton: ACTLocationData(rname.grove_village, 281, "Expired Grove Village"), #c83c8f42-474a-4dd4-bbae-99df2ad1681a-2_C-Village
    lname.chipclaw_grovevillage_NEcarton: ACTLocationData(rname.grove_village, 283, "Expired Grove Village"), #1cd62e82-14b4-4a8a-8dc1-7e8f0ff9b11b-2_C-Village
    lname.breadclaw_grovevillage_shortcut: ACTLocationData(rname.grove_village, 289, "Expired Grove Village"), #ff8f29f4-2859-4ff7-857f-54e0a9c185fa-2_D-Caves
    lname.chipclaw_grovevillage_cave: ACTLocationData(rname.grove_village, 291, "Expired Grove Village"), #6dbab2ee-2440-4b3d-944e-688f11a88199-2_D-Caves
    lname.hairclaw_grovevillage_entrance: ACTLocationData(rname.grove_village, 292, "Expired Grove Village"), #7434f4f5-8e47-40f0-b3a3-507ada236333-2_D-Caves
    lname.breadclaw_grovevillage_Scarton: ACTLocationData(rname.grove_village, 293, "Expired Grove Village"), #b1b6be9e-1973-4562-8e96-43adf0d8fcd5-2_C-Village
    lname.breadclaw_grovevillage_entrance: ACTLocationData(rname.grove_village, 294, "Expired Grove Village"), #dc39a6c7-45be-4e9a-9ac2-4da3094395dd-2_C-Village
    lname.hairclaw_grovevillage_NEcarton: ACTLocationData(rname.grove_village, 297, "Expired Grove Village"), #3eee4944-4b1e-4680-92de-0ee564c91330-2_C-Village
    lname.clothesclaw_grovevillage_upsidedown: ACTLocationData(rname.grove_village, 299, "Expired Grove Village"), #8e368d78-572e-4fed-8607-2fb4c35b23e8-2_C-Village
    lname.clothesclaw_grovevillage_dock: ACTLocationData(rname.grove_village, 311, "Expired Grove Village"), #2a160afc-7439-4e22-9f2b-62fa152f6626-2_C-Village
    lname.hairclaw_grovevillage_dock: ACTLocationData(rname.grove_village, 312, "Expired Grove Village"), #08e5033e-a401-4e90-a1a5-7e9e76ed72a5-2_C-Village
    lname.clothesclaw_grovevillage_hidden: ACTLocationData(rname.grove_village, 314, "Expired Grove Village"), #3bd305d9-8d6b-43c4-99c7-1f2be904de06-2_E-Cliffs
    lname.carclaw_grovevillage_topoda: ACTLocationData(rname.grove_village, 315, "Expired Grove Village"), #2601baa3-999e-443b-ae33-ea619346413b-2_E-Cliffs

    lname.chipclaw_flotsamvale_sheetmetal: ACTLocationData(rname.flotsam_vale, 340, "Flotsam Vale"),#2f65dc9d-5ea6-4480-b8fb-c9a9bcd779d6-2_B-LowSwamp
    lname.chipclaw_flotsamvale_beach: ACTLocationData(rname.flotsam_vale, 341, "Flotsam Vale"), #39365f04-a3c8-44e8-a398-bff99a84d2a7-2_B-LowSwamp
    lname.breadclaw_flotsamvale_northgunk: ACTLocationData(rname.flotsam_vale, 342, "Flotsam Vale"), #d0f6546a-c86e-4b9d-aa13-b45ce26abbba-2_B-LowSwamp
    lname.chipclaw_flotsamvale_butaneisland: ACTLocationData(rname.flotsam_vale, 345, "Flotsam Vale"), #fbc91e55-5d3e-4c76-8566-458a9f3d1b20-2_B-LowSwamp
    lname.clothesclaw_flotsamvale_butaneisland: ACTLocationData(rname.flotsam_vale, 347, "Flotsam Vale"), #ee9133b1-c508-41d7-8a7d-0b19241e4ccf-2_B-LowSwamp
    lname.clothesclaw_flotsamvale_alcove: ACTLocationData(rname.flotsam_vale, 351, "Flotsam Vale"), #6aa68025-641d-4fd7-a43b-7c0f3ccf4da4-2_B-LowSwamp
    lname.chipclaw_flotsamvale_cavepath: ACTLocationData(rname.flotsam_vale, 352, "Flotsam Vale"), #06b1bae1-7bf1-4b78-97f7-82ac6d6de47f-2_A-HighSwamp
    lname.clothesclaw_flotsamvale_cavepath: ACTLocationData(rname.flotsam_vale, 353, "Flotsam Vale"), #282e7092-dc21-45f0-805d-78ea29dfb0bd-2_A-HighSwamp
    lname.paperclaw_flotsamvale_uppersnail: ACTLocationData(rname.flotsam_vale, 355, "Flotsam Vale"), #99e59ba9-3c41-4133-bf7e-d09bc1957f04-2_A-HighSwamp
    lname.breadclaw_flotsamvale_woodplatform: ACTLocationData(rname.flotsam_vale, 359, "Flotsam Vale"), #36d0180d-dfa2-49be-b5f0-9b65c5f05d7a-2_A-HighSwamp
    lname.clothesclaw_flotsamvale_woodplatform: ACTLocationData(rname.flotsam_vale, 361, "Flotsam Vale"), #2546c006-fb9c-412e-99da-e1533b6c388e-2_A-HighSwamp
    lname.hairclaw_flotsamvale_woodplatform: ACTLocationData(rname.flotsam_vale, 365, "Flotsam Vale"), #19644b3e-d9b8-4cae-be53-7c2cae5a5ac8-2_A-HighSwamp
    lname.clothesclaw_flotsamvale_trashpile: ACTLocationData(rname.flotsam_vale, 366, "Flotsam Vale"), #00718126-9001-4bba-980c-e1d20298a13e-2_A-HighSwamp
    lname.paperclaw_flotsamvale_southbutane: ACTLocationData(rname.flotsam_vale, 369, "Flotsam Vale"), #cd5c1ed2-6f66-4d40-a23e-a4099f7890b1-2_A-HighSwamp
    lname.chipclaw_flotsamvale_westbutane: ACTLocationData(rname.flotsam_vale, 373, "Flotsam Vale"), #b361630f-a4b5-46fd-8bb3-faa583d0aa3b-2_A-HighSwamp
    lname.breadclaw_flotsamvale_crane: ACTLocationData(rname.flotsam_vale, 374, "Flotsam Vale"), #cc22f484-88bf-4a0a-bf32-d5aa0d17ed32-2_A-HighSwamp
    lname.hairclaw_flotsamvale_mailboxbutane: ACTLocationData(rname.flotsam_vale, 376, "Flotsam Vale"), #39e6038f-740f-4e90-acf5-2f1125ae318b-2_A-HighSwamp
    lname.paperclaw_flotsamvale_mailboxplatform: ACTLocationData(rname.flotsam_vale, 380, "Flotsam Vale"), #0696b1bf-ecc4-41c3-84fe-df54a0fcbccf-2_B-LowSwamp
    lname.chipclaw_flotsamvale_APunder1: ACTLocationData(rname.flotsam_vale, 381, "Flotsam Vale"), #3190747b-d224-4e01-874f-3dbbac197adc-2_A-HighSwamp
    lname.hairclaw_flotsamvale_APabove1: ACTLocationData(rname.flotsam_vale, 383, "Flotsam Vale"), #ad3bbd24-6760-4afc-b988-40943e6f331f-2_A-HighSwamp
    lname.hairclaw_flotsamvale_APunder1: ACTLocationData(rname.flotsam_vale, 384, "Flotsam Vale"), #1704b510-b12f-4156-b688-e82cb02bd933-2_A-HighSwamp
    lname.hairclaw_flotsamvale_APunder2: ACTLocationData(rname.flotsam_vale, 386, "Flotsam Vale"), #6adbf701-160e-4112-a275-223bffeffb01-2_A-HighSwamp
    lname.chipclaw_flotsamvale_APunder2: ACTLocationData(rname.flotsam_vale, 388, "Flotsam Vale"), #3e57df65-8b77-4402-b23e-b1eb7012e88c-2_A-HighSwamp
    lname.clothesclaw_flotsamvale_APabove: ACTLocationData(rname.flotsam_vale, 389, "Flotsam Vale"), #5c219ab5-99f1-4b63-88d0-684a6c5d68aa-2_A-HighSwamp
    lname.hairclaw_flotsamvale_APabove2: ACTLocationData(rname.flotsam_vale, 394, "Flotsam Vale"), #2112465c-60b4-423a-8bb7-301a64aec108-2_A-HighSwamp
    lname.paperclaw_flotsamvale_shippingdock: ACTLocationData(rname.flotsam_vale, 400, "Flotsam Vale"), #771c0772-2715-42c1-90b1-e033997895d1-2_A-HighSwamp
    lname.hairclaw_flotsamvale_trashpile: ACTLocationData(rname.flotsam_vale, 401, "Flotsam Vale"), #3ef191f5-0296-4760-b9ef-8d2fa99ac914-2_A-HighSwamp
    lname.clothesclaw_flotsamvale_consortium: ACTLocationData(rname.flotsam_vale, 404, "Flotsam Vale"), #9d34e68d-94a3-417c-a919-ddaf13b1c257-2_B-LowSwamp
    lname.paperclaw_flotsamvale_billboard: ACTLocationData(rname.flotsam_vale, 406, "Flotsam Vale"), #92744ee7-94a9-4abf-a3e2-93d91b82d02f-2_A-HighSwamp
    lname.chipclaw_flotsamvale_consortiumgrapple: ACTLocationData(rname.flotsam_vale, 409, "Flotsam Vale"), #ececfd87-e180-425f-9aaa-3a569bbfb5ea-2_B-LowSwamp
    lname.clothesclaw_flotsamvale_northfish: ACTLocationData(rname.flotsam_vale, 415, "Flotsam Vale"), #98e712ca-a037-4b20-81b6-e18d8221581a-2_B-LowSwamp
    lname.breadclaw_flotsamvale_westfish: ACTLocationData(rname.flotsam_vale, 417, "Flotsam Vale"), #2cd9c105-6c9e-4225-92d0-68a3d9488a4c-2_B-LowSwamp
    lname.clothesclaw_flotsamvale_northshorefish: ACTLocationData(rname.flotsam_vale, 418, "Flotsam Vale"), #d4dcf093-3098-419f-83c6-72a4d0626cc3-2_B-LowSwamp
    lname.clothesclaw_flotsamvale_southfish: ACTLocationData(rname.flotsam_vale, 419, "Flotsam Vale"), #4cce8eec-cc51-43c3-b629-768b62a16314-2_A-HighSwamp
    lname.hairclaw_flotsamvale_APfish: ACTLocationData(rname.flotsam_vale, 422, "Flotsam Vale"), #df4a99c6-a331-4b68-8ab3-33840fa40519-2_A-HighSwamp
    lname.chipclaw_flotsamvale_consortiumfish: ACTLocationData(rname.flotsam_vale, 423, "Flotsam Vale"), #2fd08de6-99fb-45f8-95e3-d32832180314-2_B-LowSwamp
    lname.paperclaw_flotsamvale_uppervale: ACTLocationData(rname.flotsam_vale, 606, "Flotsam Vale"), #99e59ba9-3c41-4133-bf7e-d09bc1957f04-2_A-HighSwamp
    lname.breadclaw_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 608, "Flotsam Vale"), #669e8494-68f1-4de8-8814-6b41a0a69d18-2_A-HighSwamp
    lname.clothesclaw_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 610, "Flotsam Vale"), #b4a9c83a-b0c6-4606-a785-16f4ff33d66e-2_A-HighSwamp
    lname.hairclaw_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 614, "Flotsam Vale"), #6db7743b-1b30-49c4-983a-bb8256959022-2_A-HighSwamp
    lname.chipclaw_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 615, "Flotsam Vale"), #70b7c84e-2c02-47c4-9e49-a58c78856f9d-2_C-Facilities

    lname.breadclaw_scuttleport_cubby: ACTLocationData(rname.scuttleport, 424, "Scuttleport"), #b5875ab1-4e89-4ba5-a9ea-6eca950d51f0-2_A-HighSwamp
    lname.clothesclaw_scuttleport_cubby: ACTLocationData(rname.scuttleport, 425, "Scuttleport"), #8f06cd49-3b2b-4883-b7a5-a421b38870ba-2_A-HighSwamp
    lname.hairclaw_scuttleport_cubbies: ACTLocationData(rname.scuttleport, 426, "Scuttleport"), #5c795be7-e38a-4986-bcfb-b72ea7e98787-2_A-HighSwamp
    lname.breadclaw_scuttleport_grate: ACTLocationData(rname.scuttleport, 431, "Scuttleport"), #b2821ac0-6087-46a8-9809-61e20afb3a6e-2_C-Facilities
    lname.hairclaw_scuttleport_magnet: ACTLocationData(rname.scuttleport, 435, "Scuttleport"), #62ab5a16-8e1f-411b-91d9-c71b45cd449e-2_C-Facilities
    lname.clothesclaw_scuttleport_electriccrab: ACTLocationData(rname.scuttleport, 436, "Scuttleport"), #12994a0d-c89b-4780-aaa9-48bf996c9348-2_C-Facilities
    lname.clothesclaw_scuttleport_trashisland: ACTLocationData(rname.scuttleport, 446, "Scuttleport"), #6837a37b-eb98-42da-bd99-b589a7bc15a2-2_C-Facilities
    lname.paperclaw_scuttleport_elevator: ACTLocationData(rname.scuttleport, 447, "Scuttleport"), #c2d88bae-4763-4c16-b79e-802f00a519a7-2_C-Facilities
    lname.hairclaw_scuttleport_rooftopedge: ACTLocationData(rname.scuttleport, 449, "Scuttleport"), #bb733ac9-8027-47b6-bea5-f2f66e202da3-2_C-Facilities
    lname.hairclaw_scuttleport_rooftoptrash: ACTLocationData(rname.scuttleport, 450, "Scuttleport"), #d6b71350-5bc1-4b39-a53c-9ff5b93faf2b-2_C-Facilities
    lname.hairclaw_scuttleport_survivorcamp: ACTLocationData(rname.scuttleport, 452, "Scuttleport"), #7126823c-0add-478d-aa4a-fc62c19959b2-2_C-Facilities
    lname.clothesclaw_scuttleport_npccrab: ACTLocationData(rname.scuttleport, 454, "Scuttleport"), #a8fdab67-387d-4d7b-ad71-85cd2e79e307-2_C-Facilities
    lname.chipclaw_scuttleport_survivorcamp: ACTLocationData(rname.scuttleport, 457, "Scuttleport"), #3192f8df-dcfa-4383-b5d5-35c92e4eadf4-2_C-Facilities
    lname.clothesclaw_scuttleport_magrail1: ACTLocationData(rname.scuttleport, 461, "Scuttleport"), #aeaefce5-14fa-4363-b66d-43593a6edc70-2_C-Facilities
    lname.clothesclaw_scuttleport_magrail2: ACTLocationData(rname.scuttleport, 462, "Scuttleport"), #dd2d2ccc-5586-40f6-b151-cd2c1e6bbd0a-2_C-Facilities
    lname.hairclaw_scuttleport_magrailroof1: ACTLocationData(rname.scuttleport, 463, "Scuttleport"), #bdffecf0-4d87-4734-b99a-24200c469d72-2_C-Facilities
    lname.paperclaw_scuttleport_magrail: ACTLocationData(rname.scuttleport, 466, "Scuttleport"), #18840259-0160-447d-991f-4390462801ec-2_C-Facilities
    lname.hairclaw_scuttleport_magrailroof2: ACTLocationData(rname.scuttleport, 467, "Scuttleport"), #b2e0c8a0-def7-47af-add1-22b37a414b8d-2_C-Facilities
    lname.chipclaw_scuttleport_magrail: ACTLocationData(rname.scuttleport, 468, "Scuttleport"), #ca68edae-bc53-4270-b2e5-0b3978300fe0-2_C-Facilities
    lname.hairclaw_scuttleport_magrail: ACTLocationData(rname.scuttleport, 472, "Scuttleport"), #cdd95cfc-844c-4034-9151-51eea2f6592d-2_C-Facilities
    lname.chipclaw_scuttleport_propanebridge: ACTLocationData(rname.scuttleport, 473, "Scuttleport"), #d9bd9604-874b-4eb1-a738-42297eaf16f3-2_C-Facilities
    lname.clothesclaw_scuttleport_propanebridge: ACTLocationData(rname.scuttleport, 475, "Scuttleport"), #affcf5d1-3127-4836-9a78-cea5ae6b9766-2_C-Facilities

    lname.paperclaw_pinbarge: ACTLocationData(rname.pinbarge, 486, "Pinbarge"), #fef13a6e-bf0d-4814-a8f5-965fb9c2cd31-2_A-PinBargeRunup
    lname.stapleclaw_pinbarge: ACTLocationData(rname.pinbarge, 488, "Pinbarge"), #cc630ad8-cb67-4a50-9e84-2c04c0cc3e16-1_A-PinBargeRunup

    lname.stapleclaw_unfathom_eastclam: ACTLocationData(rname.unfathom, 495, "The Unfathom"), #5b51f2af-33e2-4ba2-a4f9-579e56decfbb-2_B-DarkCanyon
    lname.paperclaw_unfathom_vcr: ACTLocationData(rname.unfathom, 497, "The Unfathom"), #bc5df0c3-4f73-41a8-b348-eff29a1bcc15-2_B-DarkCanyon
    lname.paperclaw_unfathom_glowstickclam: ACTLocationData(rname.unfathom, 498, "The Unfathom"), #bcfe64d6-10e9-4075-aa14-a694a798c76b-2_B-DarkCanyon
    lname.clothesclaw_unfathom_cassette: ACTLocationData(rname.unfathom, 499, "The Unfathom"), #163d1846-c7fb-4af8-b5b6-9100a5572f57-2_B-DarkCanyon
    lname.clothesclaw_unfathom_pinbarge1: ACTLocationData(rname.unfathom, 500, "The Unfathom"), #f1ae9c92-60d7-40f1-8018-5041e0943cd7-2_B-DarkCanyon
    lname.clothesclaw_unfathom_pinbarge2: ACTLocationData(rname.unfathom, 501, "The Unfathom"), #619e7f2e-dacb-459a-b942-3b3f9d3981cf-2_B-DarkCanyon
    lname.paperclaw_unfathom_pinbarge: ACTLocationData(rname.unfathom, 502, "The Unfathom"), #434f4643-5f2e-4e5a-810d-280840846d29-2_B-DarkCanyon
    lname.paperclaw_unfathom_shortcut: ACTLocationData(rname.unfathom, 506, "The Unfathom"), #28d4bed3-bba1-43f5-a620-83c4dd4e14f1-2_B-DarkCanyon
    lname.paperclaw_unfathom_glowstick: ACTLocationData(rname.unfathom, 508, "The Unfathom"), #aaa567ea-297b-47ad-8402-8c0d57d10974-2_B-DarkCanyon
    lname.paperclaw_unfathom_northeastbarge: ACTLocationData(rname.unfathom, 511, "The Unfathom"), #b30c36b2-9a59-4dca-9d9b-f851f91070b8-2_B-DarkCanyon
    lname.clothesclaw_unfathom_shortcut: ACTLocationData(rname.unfathom, 513, "The Unfathom"), #d8080e8e-5cbc-4baf-acad-7e71091ccf3e-2_B-DarkCanyon
    lname.chipclaw_unfathom_shortcuthill: ACTLocationData(rname.unfathom, 514, "The Unfathom"), #8b5392a6-4839-4960-858f-d5bddbb23381-2_B-DarkCanyon
    lname.hairclaw_unfathom_shortcut: ACTLocationData(rname.unfathom, 515, "The Unfathom"), #b2d86f0b-884e-4793-b9bd-39923f22205c-2_B-DarkCanyon
    lname.hairclaw_unfathom_styrofoam: ACTLocationData(rname.unfathom, 516, "The Unfathom"), #501f2b1a-2dbe-4082-b537-ccf1f06c9d80-2_B-DarkCanyon

    lname.clothesclaw_plains_entrance: ACTLocationData(rname.plains, 521, "Abyssal Plains"), #ae92760b-940b-4925-a369-4112351781c7-2_D-SilentFlats
    lname.hairclaw_plains_entrance: ACTLocationData(rname.plains, 522, "Abyssal Plains"), #f045426f-2bb7-43d7-8ae9-45d5bd73b3a2-2_D-SilentFlats
    lname.hairclaw_plains_shortcut: ACTLocationData(rname.plains, 524, "Abyssal Plains"), #3c128651-7160-4ff8-9aaa-20f4fe9fa6ef-2_D-SilentFlats
    lname.stapleclaw_plains_fish: ACTLocationData(rname.plains, 537, "Abyssal Plains"), #0fd36d2d-dbac-4284-b471-918f407d09aa-2_D-SilentFlats

    lname.paperclaw_oldocean_northhouse: ACTLocationData(rname.old_ocean, 538, "The Old Ocean"), #bb24e13b-1c43-4def-8d89-a997fb53772e-2_A-BleachedCopse
    lname.hairclaw_oldocean_northhouse: ACTLocationData(rname.old_ocean, 539, "The Old Ocean"), #47f18391-b63c-402e-8787-3cebb4c72224-2_A-BleachedCopse
    lname.paperclaw_oldocean_mainshortcut: ACTLocationData(rname.old_ocean, 540, "The Old Ocean"), #9248df82-ada8-4cd0-a839-3dcfa0443400-2_A-BleachedCopse
    lname.paperclaw_oldocean_islandhouse: ACTLocationData(rname.old_ocean, 543, "The Old Ocean"), #db6e270b-224f-4bd9-9190-f27c522df224-2_A-BleachedCopse
    lname.clothesclaw_oldocean_bubbles: ACTLocationData(rname.old_ocean, 546, "The Old Ocean"), #9fea96c3-97f8-4670-a5c5-fd2bf05aed14-2_A-BleachedCopse
    lname.paperclaw_oldocean_shortcut: ACTLocationData(rname.old_ocean, 547, "The Old Ocean"), #8af465e9-b1df-49fe-a7fc-cfe9eede0e93-2_A-BleachedCopse
    lname.hairclaw_oldocean_shortcut: ACTLocationData(rname.old_ocean, 548, "The Old Ocean"), #9d251937-c0f2-44b4-8247-a80ca0335d8d-2_A-BleachedCopse
    lname.paperclaw_oldocean_southhouse: ACTLocationData(rname.old_ocean, 549, "The Old Ocean"), #0cde8fb4-1c06-4c31-ba70-dfd1906404a0-2_A-BleachedCopse
    lname.carclaw_oldocean_islandclam: ACTLocationData(rname.old_ocean, 553, "The Old Ocean"), #584108d6-147a-4c89-9b42-53eb66c7d779-2_A-BleachedCopse
    lname.stapleclaw_oldocean_brokenbridge: ACTLocationData(rname.old_ocean, 555, "The Old Ocean"), #a612eb7f-28ff-47a7-9576-8e15f3404802-2_A-BleachedCopse
    lname.paperclaw_oldocean_scourcrab: ACTLocationData(rname.old_ocean, 558, "The Old Ocean"), #216137c4-ed27-4bc7-89fd-0818f0b5ce89-2_B-GrandCourtyard
    lname.hairclaw_oldocean_northentrance: ACTLocationData(rname.old_ocean, 559, "The Old Ocean"), #e9e60f3d-0c0f-4481-ad22-827a32d9987e-2_B-GrandCourtyard
    lname.hairclaw_oldocean_cityentrance: ACTLocationData(rname.old_ocean, 560, "The Old Ocean"), #674cd75e-e914-4d6d-9bc3-9ead6219f833-2_B-GrandCourtyard
    lname.paperclaw_oldocean_northentrance: ACTLocationData(rname.old_ocean, 562, "The Old Ocean"), #aa69aafa-0b32-451d-9e5c-b8b0c8be14ff-2_B-GrandCourtyard
    lname.hairclaw_oldocean_citygates: ACTLocationData(rname.old_ocean, 566, "The Old Ocean"), #229063ed-5a23-4126-8b6e-ef7ade57e7b8-2_B-GrandCourtyard
    lname.paperclaw_oldocean_citygates: ACTLocationData(rname.old_ocean, 567, "The Old Ocean"), #7596158d-e76e-4bdb-8e09-7739c73eeb3c-2_B-GrandCourtyard
    lname.clothesclaw_oldocean_citygates: ACTLocationData(rname.old_ocean, 569, "The Old Ocean"), #9a975590-ea4b-4459-bb26-0df4a8cf6cc0-2_B-GrandCourtyard
    lname.clothesclaw_oldocean_seafoam: ACTLocationData(rname.old_ocean, 574, "The Old Ocean"), #6b6e67f0-0d83-4a15-b8b7-30c7627bd0aa-2_B-GrandCourtyard
    lname.carclaw_oldocean_seafoam: ACTLocationData(rname.old_ocean, 575, "The Old Ocean"), #daa4bd21-8cec-4f2a-b259-35635c01c2f4-2_B-GrandCourtyard
    lname.hairclaw_oldocean_brokenshell: ACTLocationData(rname.old_ocean, 577, "The Old Ocean"), #c1520c0d-eed7-4798-a341-f60dc1b99bf3-2_B-GrandCourtyard
    lname.breadclaw_oldocean_teethtrap: ACTLocationData(rname.old_ocean, 578, "The Old Ocean"), #66972460-b506-45ca-86bb-c22ecf939ad2-2_B-GrandCourtyard
    lname.hairclaw_oldocean_woodplank: ACTLocationData(rname.old_ocean, 580, "The Old Ocean"), #a2b25b1c-e993-4087-b8ae-fb6a35c6dd0e-2_B-GrandCourtyard
    lname.carclaw_oldocean_scourcrab: ACTLocationData(rname.old_ocean, 583, "The Old Ocean"), #48b919ed-4365-4459-b36b-faff6e0e3b77-2_B-GrandCourtyard
    lname.paperclaw_oldocean_eastsnail: ACTLocationData(rname.old_ocean, 585, "The Old Ocean"), #9d3c9660-ef88-475b-a2bf-b9af0b80ea43-2_B-GrandCourtyard
    lname.hairclaw_oldocean_scourcrab: ACTLocationData(rname.old_ocean, 586, "The Old Ocean"), #9e62672b-4805-4b2b-8f23-914860ea4d5b-2_B-GrandCourtyard
    lname.paperclaw_oldocean_scourledge: ACTLocationData(rname.old_ocean, 587, "The Old Ocean"), #3ab90ce5-fc9e-435e-b122-39684cc92962-2_B-GrandCourtyard
    lname.stapleclaw_oldocean_parkour: ACTLocationData(rname.old_ocean, 589, "The Old Ocean"), #e815e31b-ec45-4f8b-8a67-fd469cb69dff-2_B-GrandCourtyard
    lname.stapleclaw_oldocean_middlebuilding: ACTLocationData(rname.old_ocean, 590, "The Old Ocean"), #9ef9ab02-0e47-455b-9b29-4e1cadcd2770-2_B-GrandCourtyard
    lname.carclaw_oldocean_eastbuilding: ACTLocationData(rname.old_ocean, 594, "The Old Ocean"), #467682ed-a7cd-4943-a524-07d75ef9fa0e-2_B-GrandCourtyard
    lname.carclaw_oldocean_camtscha: ACTLocationData(rname.old_ocean, 596, "The Old Ocean"), #1cd3a773-d93a-43be-8b14-cb94ab1ae794-2_B-GrandCourtyard
    lname.stapleclaw_oldocean_eastbuilding: ACTLocationData(rname.old_ocean, 597, "The Old Ocean"), #6ab4d5f2-16d8-4212-b86b-4592e30ebb5e-2_B-GrandCourtyard
    lname.carclaw_oldocean_camtschapath: ACTLocationData(rname.old_ocean, 598, "The Old Ocean"), #0aec05f7-d626-4371-9faf-d24e89dc997e-2_B-GrandCourtyard
    lname.stapleclaw_oldocean_camtschastairs: ACTLocationData(rname.old_ocean, 599, "The Old Ocean"), #80bee4b6-92f0-4180-a7c1-090fe510d32d-2_B-GrandCourtyard
    lname.carclaw_oldocean_middlebuilding: ACTLocationData(rname.old_ocean, 603, "The Old Ocean"), #d2452d82-3625-483d-a93e-401ce4745bbb-2_B-GrandCourtyard

    ##### upgrade item locations
    lname.bloodstar_shallows_help: ACTLocationData(rname.central_shallows, 24, "Central Shallows"), #AUTO NEEDS TO DO QUEST SCRIPT
    lname.bloodstar_shallows_parkour: ACTLocationData(rname.central_shallows, 25, "Central Shallows"),#ff9d47b6-7f55-4ad2-a110-e7c4492d87c1-2_B-ShallowsBigSand
    lname.bloodstar_shallows_bridge: ACTLocationData(rname.central_shallows, 26, "Central Shallows"),#32fb25ee-9262-4e87-98f9-2e64d369e7ae-2_B-ShallowsBigSand
    lname.bloodstar_shallows_clam: ACTLocationData(rname.central_shallows, 27, "Central Shallows"), #0474f3a7-0eb7-4d3c-b61e-cbb782ceab03-2_B-ShallowsBigSand

    lname.kelpsprout_snailcave_elevator: ACTLocationData(rname.snail_cave, 28, "Moon Snail's Cave"), #15a2e4c0-4950-4de0-8b5c-e2b1400f76c1-2_D-MoonSnailShellCave
    lname.bloodstar_snailcave_platoon: ACTLocationData(rname.snail_cave, 29, "Moon Snail's Cave"), #00fc94c3-320c-4d0a-a4e0-2b5eccd42d55-2_D-MoonSnailShellCave

    lname.bloodstar_slacktide_clam: ACTLocationData(rname.slacktide_after, 30, "Fort Slacktide - After Destruction"), #451b4cfb-7176-4103-999f-358b09374e0c-2_B-ShallowsBigSand

    lname.stainlessrelic_reefsedge_coral: ACTLocationData(rname.reefs_edge, 64, "Reef's Edge"), #d8433d6b-5400-4dec-aad0-032e27babdeb-2_A-NCTradeRoute

    lname.bloodstar_sandsbetween_playground: ACTLocationData(rname.sands_between, 91, "The Sands Between"), #6801f8fb-6dd9-4129-a182-791a7e66d1c2-2_A-OOGroveRadius
    lname.tacklepouch_sandsbetween_cooler: ACTLocationData(rname.sands_between, 97, "The Sands Between"), #550401bf-30db-4deb-8267-ac73d522236d-2_A-OOGroveRadius
    lname.bloodstar_sandsbetween_southwestcentral: ACTLocationData(rname.sands_between, 133, "The Sands Between"), #956ad9a9-5b43-4f18-a7d9-f67f21c50137-2_A-OOGroveRadius
    lname.oldworldwhorl_sandsbetween_mantispitfall: ACTLocationData(rname.sands_between, 143, "The Sands Between"), #8c7fdc4d-423b-4456-8869-56387a4d7665-2_A-OOGroveRadius
    lname.stainlessrelic_sandsbetween_eelectrocute: ACTLocationData(rname.sands_between, 145, "The Sands Between"), #83daf909-77d3-4302-858b-6e92fe54fe74-2_A-OOGroveRadius
    lname.tacklepouch_sandsbetween_eelnorthchain: ACTLocationData(rname.sands_between, 146, "The Sands Between"), #699b7323-fe71-4bfe-864f-cdd0c9186bbd-2_A-OOGroveRadius
    lname.kelpsprout_sandsbetween_southeelside: ACTLocationData(rname.sands_between, 151, "The Sands Between"), #a7c60b04-8f1b-4833-a6f4-d472e79748c5-2_A-OOGroveRadius

    lname.bloodstar_postpag_anchorswarm: ACTLocationData(rname.post_pag, 169, "The Sands Between - Post Pagurus"), #29e54e45-4248-4a3d-96bf-ddf5cf6046c7-2_A-OOGroveRadius

    lname.stainlessrelic_ridge_overlook: ACTLocationData(rname.secluded_ridge, 186, "The Sands Between - Secluded Ridge"), #c56be461-0e5c-406e-8af0-83021f2f2fb6-2_A-OOGroveRadius
    lname.kelpsprout_ridge_eelend: ACTLocationData(rname.secluded_ridge, 188, "The Sands Between - Secluded Ridge"), #d56339c0-fc26-4f53-a289-2c00b6f7ab38-2_A-OOGroveRadius
    lname.oldworldwhorl_ridge_ncliff: ACTLocationData(rname.secluded_ridge, 190, "The Sands Between - Secluded Ridge"), #8e381b9e-ab7a-44ad-81c3-19157c97e0c6-2_A-OOGroveRadius
    lname.oldworldwhorl_ridge_eelclam: ACTLocationData(rname.secluded_ridge, 205, "The Sands Between - Secluded Ridge"), #80e66e11-8e9a-4896-9db1-f8cd4a25fefc-2_A-OOGroveRadius

    lname.oldworldwhorl_grovemain_southclam: ACTLocationData(rname.grove_main, 217, "Expired Grove Main"), #09b60c18-2172-41bb-9588-a3e764559b15-2_B-GroveForestHigh
    lname.bloodstar_grovemain_waterfall: ACTLocationData(rname.grove_main, 229, "Expired Grove Main"), #f1d3eafe-c252-4768-abcd-7f459e734d35-2_A-GroveForestLow
    lname.kelpsprout_grovemain_carts: ACTLocationData(rname.grove_main, 261, "Expired Grove Main"), #7069eee2-4c77-4a80-a276-1131e6cfe4b8-2_A-GroveForestLow

    lname.bloodstar_grovevillage_carton: ACTLocationData(rname.grove_village, 295, "Expired Grove Village"), #e9f1284d-a5cf-441e-a358-8cabf5e3a7b1-2_C-Village
    lname.tacklepouch_grovevillage_clam: ACTLocationData(rname.grove_village, 298, "Expired Grove Village"), #c69ffc64-04af-44d1-b470-a867c5f06199-2_D-Caves
    lname.stainlessrelic_grovevillage_clam: ACTLocationData(rname.grove_village, 307, "Expired Grove Village"), #269526ef-6bb0-42cf-a93d-e2cac970e424-2_E-Cliffs
    lname.oldworldwhorl_grovevillage_topoda: ACTLocationData(rname.grove_village, 316, "Expired Grove Village"), #8b9b3b77-b95f-46a2-adfd-ca962e8f0cef-2_E-Cliffs

    lname.bloodstar_flotsamvale_submerged: ACTLocationData(rname.flotsam_vale, 344, "Flotsam Vale"), #45cca266-a175-4020-9dd7-e0b844421aff-2_B-LowSwamp
    lname.oldworldwhorl_flotsamvale_cavepath: ACTLocationData(rname.flotsam_vale, 354, "Flotsam Vale"), #53cea11a-cfb6-4894-8e18-375ea895caed-2_A-HighSwamp
    lname.oldworldwhorl_flotsamvale_snail: ACTLocationData(rname.flotsam_vale, 357, "Flotsam Vale"), #32f43e6e-a382-4938-b068-f1eab35a0269-2_A-HighSwamp
    lname.bloodstar_flotsamvale_craneclam: ACTLocationData(rname.flotsam_vale, 397, "Flotsam Vale"), #977f86dc-aeb1-471f-bb86-4db41bcbfc2c-2_A-HighSwamp
    lname.tacklepouch_flotsamvale_waterfall: ACTLocationData(rname.flotsam_vale, 403, "Flotsam Vale"), #b6c01d3a-31e3-457d-b53f-ecf0ff3b7e9f-2_B-LowSwamp

    lname.stainlessrelic_scuttleport_clam: ACTLocationData(rname.scuttleport, 438, "Scuttleport"), #95c7f334-5083-4ee8-bbcb-65033ca154f5-2_C-Facilities
    lname.bloodstar_scuttleport_magrailclam: ACTLocationData(rname.scuttleport, 469, "Scuttleport"), #f5ed972d-9d53-45b3-93b0-a389464d8941-2_C-Facilities
    lname.stainlessrelic_scuttleport_magrail: ACTLocationData(rname.scuttleport, 470, "Scuttleport"), #83173b8a-6a13-44f0-b3be-f81c8830eb06-2_C-Facilities
    lname.stainlessrelic_scuttleport_propanebridge: ACTLocationData(rname.scuttleport, 481, "Scuttleport"), #300de773-3757-4ee9-9e43-03bb1ca51410-2_C-Facilities
    lname.oldworldwhorl_scuttleport_eelectrocute: ACTLocationData(rname.scuttleport, 483, "Scuttleport"), #1af5fbc8-b8d7-47e7-a66d-480feb0c2594-2_C-Facilities

    lname.bloodstar_unfathom_eastpath: ACTLocationData(rname.unfathom, 494, "The Unfathom"), #81a413d0-b588-49c7-9210-86d193c7eb6c-2_B-DarkCanyon
    lname.bloodstar_unfathom_shortcut: ACTLocationData(rname.unfathom, 505, "The Unfathom"), #baba3ba3-395a-4547-b060-ddaf0e9fe966-2_B-DarkCanyon

    lname.stainlessrelic_plains_sponges: ACTLocationData(rname.plains, 518, "Abyssal Plains"), #e1d2aa11-415c-46c1-8a81-0ab60bb39847-2_C-HermitCave
    lname.stainlessrelic_plains_snipers: ACTLocationData(rname.plains, 520, "Abyssal Plains"), #f6f1900f-540b-4068-8c1a-7ca8e3f820d9-2_D-SilentFlats
    lname.oldworldwhorl_plains_shortcut: ACTLocationData(rname.plains, 532, "Abyssal Plains"), #163cdd5b-be02-42e9-852c-0b657db299d8-2_D-SilentFlats
    lname.bloodstar_plains_shortcutclam: ACTLocationData(rname.plains, 534, "Abyssal Plains"), #214419e5-f322-4971-adaa-6f68e62ea0a9-2_D-SilentFlats
    lname.kelpsprout_plains_grappleclam: ACTLocationData(rname.plains, 535, "Abyssal Plains"), #2cb43e11-10dd-49af-8c42-f43ae2742bce-2_C-HermitCave
    lname.tacklepouch_plains_grapplesnail: ACTLocationData(rname.plains, 536, "Abyssal Plains"), #dac6390a-11b4-411e-9c6e-a406ef5ae503-2_D-SilentFlats

    lname.oldworldwhorl_oldocean_ledgeclam: ACTLocationData(rname.old_ocean, 541, "The Old Ocean"), #f1d07afa-7684-4c41-ba1b-e3563cee1302-2_A-BleachedCopse
    lname.bloodstar_oldocean_brokenbridge: ACTLocationData(rname.old_ocean, 556, "The Old Ocean"), #8a4445f5-aaa4-4f73-9aec-adffed944b03-2_A-BleachedCopse
    lname.bloodstar_oldocean_citygates: ACTLocationData(rname.old_ocean, 568, "The Old Ocean"), #76bb55d0-f301-42d2-8933-28613fa84d2f-2_B-GrandCourtyard
    lname.stainlessrelic_oldocean_citywall: ACTLocationData(rname.old_ocean, 572, "The Old Ocean"), #081787e6-513e-4428-847d-618a5a4323dc-2_B-GrandCourtyard
    lname.kelpsprout_oldocean_parkourclam: ACTLocationData(rname.old_ocean, 576, "The Old Ocean"), #1705f88a-fcd1-4229-928f-61f0e4aca852-2_B-GrandCourtyard
    lname.stainlessrelic_oldocean_styrofoamclam: ACTLocationData(rname.old_ocean, 581, "The Old Ocean"), #e8ce25b8-c39a-4892-8573-e390fffc68d9-2_B-GrandCourtyard
    lname.bloodstar_oldocean_easternbuilding: ACTLocationData(rname.old_ocean, 593, "The Old Ocean"), #c0807176-a8e5-4d89-bded-872bfb4660aa-2_B-GrandCourtyard
    lname.oldworldwhorl_oldocean_easternclam: ACTLocationData(rname.old_ocean, 602, "The Old Ocean"), #b373a831-6880-4823-9ba4-c69a72c6e01f-2_B-GrandCourtyard

    ##### consumable item locations
    lname.barbedhook_reefsedge_undercoral: ACTLocationData(rname.reefs_edge, 65, "Reef's Edge"), #c44729ce-4c25-4059-8432-212381ca6835-2_A-NCTradeRoute
    lname.barbedhook_reefsedge_seahorses: ACTLocationData(rname.reefs_edge, 66, "Reef's Edge"), #08434b00-0100-4ea1-8f2a-f1567b84bdf2-2_A-NCTradeRoute
    lname.barbedhook_reefsedge_shortcut: ACTLocationData(rname.reefs_edge, 69, "Reef's Edge"), #2b4849b0-2798-4600-8db1-c5d6bf6952b1-2_A-NCTradeRoute
    lname.barbedhook_reefsedge_cliff: ACTLocationData(rname.reefs_edge, 72, "Reef's Edge"), #76ad26b0-4305-498c-8510-4940ad569210-2_A-NCTradeRoute

    lname.barbedhook_newcarcinia_citycenter: ACTLocationData(rname.new_carcinia, 78, "New Carcinia"), #c3b90e59-5289-4ca3-8639-a5c90d656403-2_B-NCCity

    lname.barbedhook_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 88, "The Sands Between"), #6c5631a3-d941-4990-818f-117140982384-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southernreef: ACTLocationData(rname.sands_between, 95, "The Sands Between"), #20b38e81-1198-4905-809a-e42ac4e4759d-2_A-OOGroveRadius
    lname.barbedhook3_sandsbetween_cooler: ACTLocationData(rname.sands_between, 98, "The Sands Between"), #74dac1c4-2458-4cca-a280-11e643e610ce-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_fence: ACTLocationData(rname.sands_between, 99, "The Sands Between"), #21b40d22-140c-493c-98e0-218a5ff29c02-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_spire: ACTLocationData(rname.sands_between, 115, "The Sands Between"), #c192eaf1-dd16-459b-a489-376899aabb9b-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southcentral: ACTLocationData(rname.sands_between, 132, "The Sands Between"), #4ebb3072-53e8-4cff-9672-5f82f926035e-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_bobbitbase: ACTLocationData(rname.sands_between, 134, "The Sands Between"), #90171fe5-d483-4905-a440-a9ab5a7bc074-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_northofridge: ACTLocationData(rname.sands_between, 136, "The Sands Between"), #f8b96a25-70ba-492b-bb87-7b51c81d6102-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southeel: ACTLocationData(rname.sands_between, 152, "The Sands Between"), #771e0942-ebf4-4938-a7e7-c03ce67f9c16-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southeelshellsplitter: ACTLocationData(rname.sands_between, 154, "The Sands Between"), #a53aefd5-fa6f-4675-a1b5-2f9e43f3fed0-2_A-OOGroveRadius

    lname.barbedhook_postpag_nechain: ACTLocationData(rname.post_pag, 173, "The Sands Between - Post Pagurus"), #a5c14863-82c3-47d0-b0e1-a67c93da96b8-2_A-OOGroveRadius
    lname.barbedhook_postpag_echain: ACTLocationData(rname.post_pag, 174, "The Sands Between - Post Pagurus"), #d2cd8afa-4bf2-490e-8542-cb92331800d6-2_A-OOGroveRadius
    lname.barbedhook_postpag_echainpreserver: ACTLocationData(rname.post_pag, 175, "The Sands Between - Post Pagurus"), #b03e7050-778b-4029-ab54-f82207d724fa-2_A-OOGroveRadius
    lname.barbedhook_postpag_necentral: ACTLocationData(rname.post_pag, 176, "The Sands Between - Post Pagurus"), #2738d986-20cb-4a09-b6c5-7076a3918283-2_A-OOGroveRadius
    lname.barbedhook_postpag_nwridge: ACTLocationData(rname.post_pag, 177, "The Sands Between - Post Pagurus"), #a8513df4-5533-4a1e-8fa0-b0423757f162-2_A-OOGroveRadius
    lname.barbedhook_postpag_neeelpath: ACTLocationData(rname.post_pag, 178, "The Sands Between - Post Pagurus"), #f14d696d-88a4-471e-a512-b5770c3cfbad-2_A-OOGroveRadius
    lname.barbedhook_postpag_ridgeentrance: ACTLocationData(rname.post_pag, 181, "The Sands Between - Post Pagurus"), #9ecea6b6-f3db-48f8-a753-6644bbbf1aaf-2_A-OOGroveRadius
    lname.barbedhook_postpag_wplayground: ACTLocationData(rname.post_pag, 183, "The Sands Between - Post Pagurus"), #ecea05b3-9908-4b63-b422-d999b78c87e1-2_A-OOGroveRadius
    lname.barbedhook_postpag_swcentral: ACTLocationData(rname.post_pag, 184, "The Sands Between - Post Pagurus"), #7563f2eb-e052-4107-b787-de2f67a40f2f-2_A-OOGroveRadius

    lname.barbedhook_ridge_near: ACTLocationData(rname.secluded_ridge, 187, "The Sands Between - Secluded Ridge"), #97a24ab6-20a3-4f21-b0af-55bf243f33f0-2_A-OOGroveRadius
    lname.barbedhook_ridge_overlookpath: ACTLocationData(rname.secluded_ridge, 192, "The Sands Between - Secluded Ridge"), #d9ee8d70-3493-4e7b-91b3-b42278ff0ad4-2_A-OOGroveRadius
    lname.sharkegg_ridge_broomspire: ACTLocationData(rname.secluded_ridge, 212, "The Sands Between - Secluded Ridge"), #dcc6b99e-1d47-481f-86ca-e14a5743f460-2_A-OOGroveRadius

    lname.barbedhook_trashbin_eelgrapple: ACTLocationData(rname.secluded_ridge, 210, "The Sands Between - Trashbin Plateau"), #2bccca10-1f27-4762-9a9b-8e628586e0a4-2_A-OOGroveRadius

    lname.barbedhook_grovemain_sniper: ACTLocationData(rname.secluded_ridge, 214, "Expired Grove Main"), #8fd70034-2415-4934-975b-2303d159f567-2_A-GroveForestLow
    lname.barbedhook_grovemain_riverledge: ACTLocationData(rname.secluded_ridge, 215, "Expired Grove Main"), #0860891c-3db6-4e51-8c0b-58b09ac8ece0-2_A-GroveForestLow
    lname.barbedhook_grovemain_riversand: ACTLocationData(rname.secluded_ridge, 216, "Expired Grove Main"), #2465aea2-9800-49e5-9e7e-d751ca2b3612-2_A-GroveForestLow
    lname.barbedhook_grovemain_lichenthrope: ACTLocationData(rname.secluded_ridge, 221, "Expired Grove Main"), #35455018-8cf6-48db-ba76-4ffbca84b0a8-2_A-GroveForestLow
    lname.barbedhook_grovemain_lichenthropeeast: ACTLocationData(rname.secluded_ridge, 222, "Expired Grove Main"), #5a106f4d-8139-44da-9cdf-8d0bd70c6bf3-2_A-GroveForestLow
    lname.barbedhook_grovemain_sodacans: ACTLocationData(rname.secluded_ridge, 223, "Expired Grove Main"), #10a99891-923e-4bab-8057-b6d5781cb35d-2_A-GroveForestLow
    lname.barbedhook_grovemain_acrossriver: ACTLocationData(rname.secluded_ridge, 228, "Expired Grove Main"), #50f9f7d1-0e70-4333-b8b3-fbc46f04f3ea-2_A-GroveForestLow
    lname.barbedhook_grovemain_afternets: ACTLocationData(rname.secluded_ridge, 230, "Expired Grove Main"), #e7382e22-3232-4380-a734-bef8eb9a2a76-2_A-GroveForestLow
    lname.barbedhook_grovemain_cartledge: ACTLocationData(rname.secluded_ridge, 235, "Expired Grove Main"), #dc13eb69-ac98-4de9-9fe0-7f16a03d4ebb-2_A-GroveForestLow
    lname.barbedhook_grovemain_cartledgebottle: ACTLocationData(rname.secluded_ridge, 237, "Expired Grove Main"), #a5b6f3f6-6e1c-4934-9006-26da6cee47f4-2_A-GroveForestLow
    lname.barbedhook_grovemain_paperplate: ACTLocationData(rname.secluded_ridge, 241, "Expired Grove Main"), #776881ba-f61b-4400-8cf5-f11fb11b6f94-2_B-GroveForestHigh
    lname.barbedhook_grovemain_oildrum: ACTLocationData(rname.secluded_ridge, 242, "Expired Grove Main"), #12c73a88-beef-4bfb-a2d1-c159c91d8304-2_B-GroveForestHigh
    lname.barbedhook_grovemain_canopy: ACTLocationData(rname.grove_main, 248, "Expired Grove Main"), #101eff6d-e09a-471d-86fd-cdc587012c32-2_A-GroveForestLow
    lname.barbedhook_grovemain_drumtop: ACTLocationData(rname.secluded_ridge, 250, "Expired Grove Main"), #3a1e7a2c-5111-4360-b168-cc5e84088b6a-2_B-GroveForestHigh
    lname.barbedhook_grovemain_carts: ACTLocationData(rname.grove_main, 259, "Expired Grove Main"), #d1b73602-aca6-4d33-991d-39110a5e6780-2_A-GroveForestLow
    lname.sharkegg_grovemain_mantis: ACTLocationData(rname.grove_main, 260, "Expired Grove Main"), #f734eb5e-d674-4c84-9493-61d20f70fde3-2_A-GroveForestLow

    lname.barbedhook_grovevillage_heikea: ACTLocationData(rname.grove_village, 287, "Expired Grove Village"), #bcfabbd4-8575-4a6a-8325-7259996a7d68-2_D-Caves
    lname.barbedhook_grovevillage_cartfish: ACTLocationData(rname.grove_village, 271, "Expired Grove Village"), #7a38fbf2-47a9-4bf6-85d1-f8d4f58b8d66-2_B-GroveForestHigh
    lname.barbedhook_grovevillage_riveroil: ACTLocationData(rname.grove_village, 273, "Expired Grove Village"), #9c983d04-ac83-40f0-8220-d92f76ea7099-2_B-GroveForestHigh
    lname.barbedhook_grovevillage_bottles: ACTLocationData(rname.grove_village, 275, "Expired Grove Village"), #5c973136-cfe9-4ea5-bc93-60ffa4b5cc13-2_C-Village
    lname.barbedhook_grovevillage_crabs: ACTLocationData(rname.grove_village, 277, "Expired Grove Village"), #4721ab20-67be-4d5b-b0bb-3f2c2ecb510f-2_C-Village
    lname.barbedhook_grovevillage_centercarton: ACTLocationData(rname.grove_village, 278, "Expired Grove Village"), #bae2eb9a-56a0-4548-8c6d-798d234ba479-2_C-Village
    lname.barbedhook_grovevillage_corpse: ACTLocationData(rname.grove_village, 279, "Expired Grove Village"), #20238db7-8d1e-4045-8e0a-de2aaea1cb49-2_C-Village
    lname.barbedhook_grovevillage_path: ACTLocationData(rname.grove_village, 280, "Expired Grove Village"), #87e729ae-0659-4b6e-9ac1-c1d059719ba8-2_C-Village
    lname.barbedhook_grovevillage_Ncarton: ACTLocationData(rname.grove_village, 282, "Expired Grove Village"), #b29402c2-62e8-4fa3-8c27-4e419750b16f-2_C-Village
    lname.barbedhook_grovevillage_SWcarton: ACTLocationData(rname.grove_village, 284, "Expired Grove Village"), #256daaaa-675c-47e5-bd4e-367dc4abd9e2-2_C-Village
    lname.sharkegg_grovevillage_sniper: ACTLocationData(rname.grove_village, 285, "Expired Grove Village"), #451f2fe5-9c29-4710-9493-0878963547e4-2_C-Village
    lname.barbedhook_grovevillage_boat: ACTLocationData(rname.grove_village, 286, "Expired Grove Village"), #99c33625-2da4-4f69-a0af-8a8d2da3b399-2_D-Caves
    lname.barbedhook_grovevillage_butter: ACTLocationData(rname.grove_village, 290, "Expired Grove Village"), #10eae42f-9cca-447a-8cb8-9cffcba11ecd-2_D-Caves
    lname.barbedhook_grovevillage_above1: ACTLocationData(rname.grove_village, 301, "Expired Grove Village"), #28362ae0-defe-4a04-b449-93d7e5e60676-2_C-Village
    lname.barbedhook_grovevillage_above2: ACTLocationData(rname.grove_village, 302, "Expired Grove Village"), #0177d8ef-8849-4ea4-b1b3-08a1c3134a99-2_E-Cliffs
    lname.barbedhook_grovevillage_above3: ACTLocationData(rname.grove_village, 303, "Expired Grove Village"), #b3a776e1-52ab-4dc8-adc1-55c95eca9972-2_E-Cliffs
    lname.barbedhook_grovevillage_ornament: ACTLocationData(rname.grove_village, 304, "Expired Grove Village"), #ce1700e2-d9d0-462a-af23-cb55828b062a-2_E-Cliffs
    lname.barbedhook_grovevillage_hammer: ACTLocationData(rname.grove_village, 305, "Expired Grove Village"), #235b691b-0f18-4f35-bd8a-7536e12fabfe-2_E-Cliffs
    lname.barbedhook_grovevillage_dock: ACTLocationData(rname.grove_village, 309, "Expired Grove Village"), #aff46c65-7a4a-4b1c-a0ca-840af3898f26-2_C-Village

    lname.barbedhook_flotsamvale_entranceledge: ACTLocationData(rname.flotsam_vale, 338, "Flotsam Vale"), #17ac32ac-f0fc-4613-9e02-5ffdf4eecb63-2_B-LowSwamp
    lname.barbedhook_flotsamvale_entrancerocks: ACTLocationData(rname.flotsam_vale, 339, "Flotsam Vale"), #7aa4931c-e44f-4531-9b5e-eb1a01418fdd-2_B-LowSwamp
    lname.barbedhook_flotsamvale_northbeach: ACTLocationData(rname.flotsam_vale, 343, "Flotsam Vale"), #60c9e9de-af79-4068-a7bf-7005ac760f4b-2_B-LowSwamp
    lname.barbedhook_flotsamvale_butaneisland: ACTLocationData(rname.flotsam_vale, 349, "Flotsam Vale"), #c3ff376c-5f53-4401-a52a-1515dba2a2a3-2_B-LowSwamp
    lname.barbedhook_flotsamvale_snailshell: ACTLocationData(rname.flotsam_vale, 356, "Flotsam Vale"), #2fd87610-e95f-4b28-9521-d3b59fb718f0-2_A-HighSwamp
    lname.barbedhook_flotsamvale_wooddeck: ACTLocationData(rname.flotsam_vale, 358, "Flotsam Vale"), #125b1086-fa58-45bf-a42f-e715781feffa-2_A-HighSwamp
    lname.barbedhook_flotsamvale_woodplatform1: ACTLocationData(rname.flotsam_vale, 362, "Flotsam Vale"), #cf30643f-5b43-4e94-af5d-c879e6531d14-2_A-HighSwamp
    lname.barbedhook_flotsamvale_woodplatform2: ACTLocationData(rname.flotsam_vale, 364, "Flotsam Vale"), #ecbaf918-3632-496e-9598-a9e5da91f495-2_A-HighSwamp
    lname.barbedhook_flotsamvale_westbutane: ACTLocationData(rname.flotsam_vale, 370, "Flotsam Vale"), #0337dc3e-fcf7-4f30-8759-bef7afeb04ca-2_A-HighSwamp
    lname.barbedhook_flotsamvale_mailbox: ACTLocationData(rname.flotsam_vale, 378, "Flotsam Vale"), #90422b9d-ec1b-4be4-a606-54f196dc1f1e-2_A-HighSwamp
    lname.barbedhook_flotsamvale_APunder1: ACTLocationData(rname.flotsam_vale, 385, "Flotsam Vale"), #442a694b-ba12-4f08-ad49-f2a5697d3c19-2_A-HighSwamp
    lname.barbedhook_flotsamvale_APunder2: ACTLocationData(rname.flotsam_vale, 387, "Flotsam Vale"), #8480a51d-bd34-43bb-a348-a3bf69040248-2_A-HighSwamp
    lname.barbedhook_flotsamvale_APabove: ACTLocationData(rname.flotsam_vale, 391, "Flotsam Vale"), #54f7c579-6ea7-402d-b1eb-9ee67d2bbe9a-2_A-HighSwamp
    lname.barbedhook_flotsamvale_shippingsnail: ACTLocationData(rname.flotsam_vale, 398, "Flotsam Vale"), #1abd8a20-f2cc-488b-8e0a-00b12c305667-2_A-HighSwamp
    lname.barbedhook_flotsamvale_shippingbutane: ACTLocationData(rname.flotsam_vale, 399, "Flotsam Vale"), #a76a0b9b-6307-4b71-be91-da385c17a977-2_A-HighSwamp
    lname.barbedhook_flotsamvale_trashpile: ACTLocationData(rname.flotsam_vale, 402, "Flotsam Vale"), #a0549711-5560-4b9c-99d5-65e13911413a-2_A-HighSwamp
    lname.barbedhook_flotsamvale_consortiumcage: ACTLocationData(rname.flotsam_vale, 405, "Flotsam Vale"), #7e76017e-13fa-4a96-a1f8-6d881b20b372-2_B-LowSwamp
    lname.barbedhook_flotsamvale_consortium: ACTLocationData(rname.flotsam_vale, 408, "Flotsam Vale"), #b81ed4dc-3b3e-420d-99e9-d676c88fc120-2_B-LowSwamp
    lname.barbedhook_flotsamvale_snailfish: ACTLocationData(rname.flotsam_vale, 413, "Flotsam Vale"), #cdf2769f-deb3-43dc-841f-a4c1c0081833-2_A-HighSwamp
    lname.barbedhook_flotsamvale_westfish: ACTLocationData(rname.flotsam_vale, 420, "Flotsam Vale"), #698a076c-2661-4731-90c4-211d8b1414c6-2_A-HighSwamp
    lname.barbedhook_flotsamvale_behindcubby: ACTLocationData(rname.flotsam_vale, 605, "Flotsam Vale"), #5b786881-414b-41d4-97ea-b3a850d3633a-2_A-HighSwamp
    lname.barbedhook_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 611, "Flotsam Vale"), #3b49cdc6-b609-49b0-a1c2-57307a398920-2_A-HighSwamp
    lname.barbedhook_flotsamvale_sludgefish: ACTLocationData(rname.flotsam_vale, 612, "Flotsam Vale"), #a6a69a65-21fa-4bdd-8940-e1f1f6c226a0-2_A-HighSwamp

    lname.barbedhook_scuttleport_cubby: ACTLocationData(rname.scuttleport, 429, "Scuttleport"), #a91e708c-89a8-4ef0-bf21-870cd56e652e-2_A-HighSwamp
    lname.barbedhook_scuttleport_magnet: ACTLocationData(rname.scuttleport, 434, "Scuttleport"), #f738e9de-5eb9-41c1-8358-48a6d51a9fff-2_C-Facilities
    lname.barbedhook_scuttleport_sorting: ACTLocationData(rname.scuttleport, 439, "Scuttleport"), #5eefb844-f267-416a-ba6e-c1b8ec945cfa-2_C-Facilities
    lname.barbedhook_scuttleport_magnetdropoff1: ACTLocationData(rname.scuttleport, 442, "Scuttleport"), #631f983b-ebc5-4fa3-aedc-38fd4d1efffb-2_C-Facilities
    lname.barbedhook_scuttleport_trashisland: ACTLocationData(rname.scuttleport, 445, "Scuttleport"), #497aa1a9-1ffa-4ea1-ad17-32fa6654db2e-2_C-Facilities
    lname.barbedhook_scuttleport_magnetdropoff2: ACTLocationData(rname.scuttleport, 448, "Scuttleport"), #e449f43b-dc05-4e13-8f8c-b93adf0e97fa-2_C-Facilities
    lname.barbedhook_scuttleport_trashblock: ACTLocationData(rname.scuttleport, 453, "Scuttleport"), #de7097a4-7028-454b-98e6-c61a03557736-2_C-Facilities
    lname.barbedhook_scuttleport_magrail1: ACTLocationData(rname.scuttleport, 459, "Scuttleport"), #301e305f-fc4c-4bd5-a839-ca1ea6435c13-2_C-Facilities
    lname.barbedhook_scuttleport_magrail2: ACTLocationData(rname.scuttleport, 460, "Scuttleport"), #0710d989-547d-43e3-b8e0-70c634c08441-2_C-Facilities
    lname.barbedhook_scuttleport_magrailroof: ACTLocationData(rname.scuttleport, 465, "Scuttleport"), #0732b3f4-78b7-4584-8459-fab762bd98c5-2_C-Facilities
    lname.barbedhook_scuttleport_magrail3: ACTLocationData(rname.scuttleport, 471, "Scuttleport"), #60db4097-9756-47cc-994c-506ce4069cab-2_C-Facilities
    lname.barbedhook_scuttleport_propanebridge: ACTLocationData(rname.scuttleport, 474, "Scuttleport"), #53d359e0-d707-4585-8d8f-75bf20cdf165-2_C-Facilities
    lname.barbedhook_scuttleport_afterbridge: ACTLocationData(rname.scuttleport, 476, "Scuttleport"), #a4d7a5e4-2374-4a0c-8f5d-421b07ae6e2d-2_C-Facilities
    lname.barbedhook_scuttleport_propaneroof1: ACTLocationData(rname.scuttleport, 477, "Scuttleport"), #df0d5a5c-5391-425d-b250-5c26553f2bfb-2_C-Facilities
    lname.barbedhook_scuttleport_propaneroof2: ACTLocationData(rname.scuttleport, 478, "Scuttleport"), #7f30ac6a-2e29-4ccb-9fd2-eb2491741c6c-2_C-Facilities
    
    lname.barbedhook_pinbarge1: ACTLocationData(rname.pinbarge, 485, "Pinbarge"), #8edddc0a-8caf-48a1-975e-4167e728a4c3-1_A-PinBargeRunup
    lname.barbedhook_pinbarge2: ACTLocationData(rname.pinbarge, 489, "Pinbarge"), #898633d3-36c1-4f61-88b5-8cd4ca33ec2b-2_B-PinBargeArena

    lname.barbedhook_unfathom_mimic: ACTLocationData(rname.unfathom, 492, "The Unfathom"), #98535001-699c-4e64-a07d-74e610f04528-2_B-DarkCanyon
    lname.barbedhook_unfathom_mimichill: ACTLocationData(rname.unfathom, 493, "The Unfathom"), #54a8f869-ff96-45b2-93de-fb1eeeec313f-2_B-DarkCanyon

    lname.barbedhook_oldocean_northwesthouse: ACTLocationData(rname.old_ocean, 542, "The Old Ocean"), #14d445d2-f997-458d-a285-123bf009c223-2_A-BleachedCopse
    lname.barbedhook_oldocean_southhouse: ACTLocationData(rname.old_ocean, 550, "The Old Ocean"), #c9b315b7-28de-4efb-9d0c-608e9629a9a7-2_A-BleachedCopse
    lname.barbedhook_oldocean_secondisland: ACTLocationData(rname.old_ocean, 552, "The Old Ocean"), #2e322c37-6011-41eb-ac2b-7fb67d0d85b1-2_A-BleachedCopse
    lname.barbedhook_oldocean_brokenbridge1: ACTLocationData(rname.old_ocean, 554, "The Old Ocean"), #765f4cdd-d7a5-4954-be69-99ed7c68913b-2_A-BleachedCopse
    lname.barbedhook_oldocean_brokenbridge2: ACTLocationData(rname.old_ocean, 557, "The Old Ocean"), #6a75e525-e399-482b-b21f-42ae8ae63a17-2_A-BleachedCopse
    lname.barbedhook_oldocean_entrance: ACTLocationData(rname.old_ocean, 564, "The Old Ocean"), #f94fbed4-a90c-46e8-a6a3-343f81728eba-2_B-GrandCourtyard
    lname.barbedhook_oldocean_citygates: ACTLocationData(rname.old_ocean, 565, "The Old Ocean"), #20dffb0a-e6b1-4c00-8f25-d66aefedcc22-2_B-GrandCourtyard
    lname.sharkegg_oldocean_citygates: ACTLocationData(rname.old_ocean, 570, "The Old Ocean"), #f8ef34b2-f3b7-44d6-84b6-63749adc075f-2_B-GrandCourtyard
    lname.barbedhook_oldocean_chitan: ACTLocationData(rname.old_ocean, 573, "The Old Ocean"), #b2789002-2749-482b-b64e-4cbba29c6a08-2_B-GrandCourtyard
    lname.barbedhook_oldocean_eastsnail: ACTLocationData(rname.old_ocean, 584, "The Old Ocean"), #082d38e1-09cc-496a-9909-ffe96cc80cb8-2_B-GrandCourtyard
    lname.barbedhook_oldocean_easternbuilding: ACTLocationData(rname.old_ocean, 591, "The Old Ocean"), #824a5720-5565-4804-9838-a674ebd3b1f1-2_B-GrandCourtyard
    lname.barbedhook_oldocean_middlebuilding: ACTLocationData(rname.old_ocean, 595, "The Old Ocean"), #56826edb-20cf-4f5a-bd85-4c4e71ca3fee-2_B-GrandCourtyard

    ##### stowaway locations
    lname.siphonophore_shallows_westwall: ACTLocationData(rname.central_shallows, 31, "Central Shallows"),#4d4ac114-06e4-400f-b888-b500a7348cc9-2_B-ShallowsBigSand
    lname.seastar_shallows_eastledge: ACTLocationData(rname.central_shallows, 32, "Central Shallows"), #e9a5a6cf-2a19-4db5-bb0d-d85b260f3e2b-2_B-ShallowsBigSand
    lname.sponge_shallows_puffer: ACTLocationData(rname.central_shallows, 33, "Central Shallows"), #95c0077d-518f-4ab7-85e2-ac1e0c1bb0b9-2_B-ShallowsBigSand
    lname.anothercrab_shallows_pillar: ACTLocationData(rname.central_shallows, 34, "Central Shallows"), #924670c2-839f-4e42-9cf5-8c081b17f946-2_B-ShallowsBigSand
    lname.sanddollar_shallows_arch: ACTLocationData(rname.central_shallows, 35, "Central Shallows"), #804d3848-3e86-474f-8622-547d020c4cc4-2_B-ShallowsBigSand
    lname.mussel_shallows_southwestcastlefish: ACTLocationData(rname.central_shallows, 125, "Central Shallows"), #41a6780e-55a2-4a0a-96a9-bb279a3b1ec3-2_B-ShallowsBigSand
    lname.anemone_shallows_southwestcastlehiddenfishing: ACTLocationData(rname.central_shallows, 127, "Central Shallows"), #daaa6ab6-8aac-4713-942f-f322e918dd55-2_B-ShallowsBigSand
    lname.razorblade_shallows_slacktidebottlefishing: ACTLocationData(rname.central_shallows, 128, "Central Shallows"), #728b3da1-5b4b-4a7f-885c-b5ed9abfadbc-2_B-ShallowsBigSand
    lname.anemone_shallows_umbrellafishing: ACTLocationData(rname.central_shallows, 129, "Central Shallows"), #b29c140a-08c2-44c6-81c3-5f91e5621e47-2_B-ShallowsBigSand

    lname.limpet_slacktide_stairs: ACTLocationData(rname.slacktide_before, 36, "Fort Slacktide - Before Destruction"), #b5e751fb-8ff5-440e-aa9c-9d9c75977be7-2_B-ShallowsBigSand
    lname.seastar_slacktide_grappleroom: ACTLocationData(rname.slacktide_before, 37, "Fort Slacktide - Before Destruction"), #35603032-802e-4811-ae95-8e8eb11c1dfa-2_B-ShallowsBigSand
    lname.barnacle_slacktide_bigurchin: ACTLocationData(rname.slacktide_before, 38, "Fort Slacktide - Before Destruction"), #98329dde-9889-4cbb-a656-61f83dca2eca-2_B-ShallowsBigSand
    lname.rustynail_slacktide_bigurchin: ACTLocationData(rname.slacktide_before, 317, "Fort Slacktide - Before Destruction"), #87e60901-5489-437e-82c2-d70ca2390364-2_B-ShallowsBigSand

    lname.limpet_snailcave_jelly: ACTLocationData(rname.snail_cave, 39, "Moon Snail's Cave"), #c1a31dc1-9ec5-42e9-8dcf-291f7cdc8a26-2_D-MoonSnailShellCave

    lname.mussel_slacktide_fortentrance: ACTLocationData(rname.slacktide_after, 40, "Fort Slacktide - After Destruction"), #694c4c66-fefc-4539-962f-a343e13b044b-2_C-Slacktide2
    lname.anemone_slacktide_fortwall: ACTLocationData(rname.slacktide_after, 41, "Fort Slacktide - After Destruction"), #557546a8-096b-49cd-b63b-452fb751a8bf-2_C-Slacktide2
    lname.whelk_slacktide_turrettop: ACTLocationData(rname.slacktide_after, 42, "Fort Slacktide - After Destruction"), #e1848736-945b-406d-853e-d213f7c80f14-2_C-Slacktide2

    lname.seastar_reefsedge_crabs: ACTLocationData(rname.reefs_edge, 68, "Reef's Edge"), #d93f0715-7c15-4f74-b376-34468705093c-2_A-NCTradeRoute
    lname.seastarplus_reefsedge_pole: ACTLocationData(rname.reefs_edge, 70, "Reef's Edge"), #3473ed8f-db06-4bb7-9932-862f92258542-2_A-NCTradeRoute
    lname.whelkplus_reefsedge_sponge: ACTLocationData(rname.reefs_edge, 73, "Reef's Edge"), #5e8a3fb6-f3b1-42a0-a8b8-10b57b340138-2_A-NCTradeRoute

    lname.limpet_newcarcinia_entrance: ACTLocationData(rname.new_carcinia, 75, "New Carcinia"), #e7b4c4fc-6208-4326-847e-ee34113f7fe0-2_B-NCCity
    lname.rustynail_newcarcinia_hammerhead: ACTLocationData(rname.new_carcinia, 77, "New Carcinia"), #f2105767-2544-4acc-9703-a47fbe97c3dc-2_B-NCCity

    lname.sanddollar_newcarcinia_hammerhead: ACTLocationData(rname.new_carcinia, 86,"New Carcinia"), #a1194e18-4659-4ac9-aa73-744a6df42fe3-2_B-NCCity

    lname.phytoplankton_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 89, "The Sands Between"), #3197c269-c43d-4bff-b388-a6c3d3e4b5f3-2_A-OOGroveRadius
    lname.anemone_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 90, "The Sands Between"), #73aec841-ee9a-411b-8919-53eeeb33ec59-2_A-OOGroveRadius
    lname.anemone_sandsbetween_playground: ACTLocationData(rname.sands_between, 92, "The Sands Between"), #bd3a89be-89f5-4029-ac76-c1966c70299d-2_A-OOGroveRadius
    lname.rustynail_sandsbetween_fence: ACTLocationData(rname.sands_between, 93, "The Sands Between"), #8778ffd7-a95d-4021-bb90-4a116de9894a-2_A-OOGroveRadius
    lname.googlyeye_sandsbetween_pizza: ACTLocationData(rname.sands_between, 96, "The Sands Between"), #52821431-a6c7-458a-b54f-d42196919993-2_A-OOGroveRadius
    lname.siphonophore_sandsbetween_cooler: ACTLocationData(rname.sands_between, 100, "The Sands Between"), #8d4c2499-b344-4e0f-b4e4-dc2a3e7ccf74-2_A-OOGroveRadius
    lname.limpet_sandsbetween_anchor: ACTLocationData(rname.sands_between, 101, "The Sands Between"), #1f5bc2e0-a613-4afd-bdf6-5ed4805edf29-2_A-OOGroveRadius
    lname.anemone_sandsbetween_chains: ACTLocationData(rname.sands_between, 103, "The Sands Between"), #57559d1c-80ce-4396-afdf-7d7e6af71ff6-2_A-OOGroveRadius
    lname.fredrick_sandsbetween_fredrick: ACTLocationData(rname.sands_between, 104, "The Sands Between"), #6f1f751a-b27c-4eb0-b95c-a89d66dd242a-2_A-OOGroveRadius
    lname.anothercrab_sandsbetween_chains: ACTLocationData(rname.sands_between, 105, "The Sands Between"), #03ba104a-efe3-4294-b378-b2aeff7aa9e3-2_A-OOGroveRadius
    lname.mussel_sandsbetween_anchor: ACTLocationData(rname.sands_between, 110,"The Sands Between"), #a08ac116-549b-4691-8e88-79daf965dff8-2_A-OOGroveRadius
    lname.barnacle_sandsbetween_northeast: ACTLocationData(rname.sands_between, 113,"The Sands Between"), #234f3d49-7fc5-4039-949f-8d95f38d7c79-2_A-OOGroveRadius
    lname.salp_sandsbetween_northeast: ACTLocationData(rname.sands_between, 114,"The Sands Between"), #2dc13e33-724d-41a7-983b-5f3bf010ce89-2_A-OOGroveRadius
    lname.rustynailplus_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 116,"The Sands Between"), #fc6e8558-9515-40a7-9857-9584a196a1ec-2_A-OOGroveRadius
    lname.seastarplus_sandsbetween_flotsam: ACTLocationData(rname.sands_between, 117,"The Sands Between"), #d19ac393-ea1d-4237-9d31-b620c3a2617d-2_A-OOGroveRadius
    lname.seaslug_sandsbetween_crabrave: ACTLocationData(rname.sands_between, 118,"The Sands Between"), #bceed85e-5560-4a77-a498-749af9f76780-2_A-OOGroveRadius
    lname.whelk_sandsbetween_crabrave: ACTLocationData(rname.sands_between, 119,"The Sands Between"), #63b93466-f406-492e-ac12-f243fe6a8165-2_A-OOGroveRadius
    lname.sinkerplus_sandsbetween_northridgemantis: ACTLocationData(rname.sands_between, 141,"The Sands Between"), #a8e01dfb-5dd9-4da0-92b1-39a7b18e8d83-2_A-OOGroveRadius
    lname.limpetplus_sandsbetween_grovemantis: ACTLocationData(rname.sands_between, 142,"The Sands Between"), #56e45097-4ffa-41b0-ac56-cdd6c93b5e88-2_A-OOGroveRadius
    lname.lumpsuckerplus_sandsbetween_anchor: ACTLocationData(rname.sands_between, 144,"The Sands Between"), #859c746b-c52f-4887-aa96-bb19bd7e25dd-2_A-OOGroveRadius
    lname.sinkerplus_sandsbetween_southeel: ACTLocationData(rname.sands_between, 148,"The Sands Between"), #ae4a7ac6-5eb0-4590-a3c7-5d5f236a978d-2_A-OOGroveRadius
    lname.musselplus_sandsbetween_southeel: ACTLocationData(rname.sands_between, 149,"The Sands Between"), #7111735c-772e-4c1f-b255-183e62760ae2-2_A-OOGroveRadius
    lname.oyster_sandsbetween_southeelashtray: ACTLocationData(rname.sands_between, 153,"The Sands Between"), #2ccd3299-d207-4d4d-b5a5-d777c4e8aa29-2_A-OOGroveRadius
    lname.mussel_sandsbetween_bobbitfish: ACTLocationData(rname.sands_between, 159,"The Sands Between"), #da5f126f-e470-432c-b5b0-8eca9918ed77-2_A-OOGroveRadius
    lname.barnacle_sandsbetween_bobbitfish: ACTLocationData(rname.sands_between, 161,"The Sands Between"), #15cf7503-de68-4475-b39c-fe687f85c448-2_A-OOGroveRadius
    lname.whelkplusplus_sandsbetween_southeelpeak: ACTLocationData(rname.sands_between, 166,"The Sands Between"), #d61a21a2-c27d-45d7-8e11-75fcd11e8b78-2_A-OOGroveRadius
    lname.salpplus_sandsbetween_groveeel: ACTLocationData(rname.sands_between, 167,"The Sands Between"), #7faef89f-c78a-4002-9454-c20bf5098229-2_A-OOGroveRadius
    lname.usedbandage_sandsbetween_groveeel: ACTLocationData(rname.sands_between, 168,"The Sands Between"), #3123f8ec-3548-41f5-a777-c10268e06b8b-2_A-OOGroveRadius

    lname.limpet_ridge_ncliffkelp: ACTLocationData(rname.secluded_ridge, 191, "The Sands Between - Secluded Ridge"), #fcb1f0bb-2ebf-449c-b5fd-ebb7d515c7af-2_A-OOGroveRadius
    lname.sanddollar_ridge_broom: ACTLocationData(rname.secluded_ridge, 194, "The Sands Between - Secluded Ridge"), #42686eee-4b9f-4d44-a52d-569d2c814f13-2_A-OOGroveRadius
    lname.musselplus_ridge_togo: ACTLocationData(rname.secluded_ridge, 196, "The Sands Between - Secluded Ridge"), #a59b9d02-9711-48e3-8296-e2164c79f1f2-2_A-OOGroveRadius
    lname.siphonophoreplus_ridge_pitfall: ACTLocationData(rname.secluded_ridge, 203, "The Sands Between - Secluded Ridge"), #e2a1e3e1-8ee4-4539-ab81-98c4d6d99630-2_A-OOGroveRadius
    lname.anemoneplus_ridge_eel: ACTLocationData(rname.secluded_ridge, 204, "The Sands Between - Secluded Ridge"), #1b6f2070-3ff2-4f48-b061-0a41990013e1-2_A-OOGroveRadius
    lname.cockle_ridge_eelfish: ACTLocationData(rname.secluded_ridge, 208, "The Sands Between - Secluded Ridge"), #d32ade52-c34e-4cb7-957c-df605339ee4c-2_A-OOGroveRadius
    lname.bobber_ridge_broomspire: ACTLocationData(rname.secluded_ridge, 211, "The Sands Between - Secluded Ridge"), #fc2cf7ed-6ff6-40bb-987a-936da0afa93b-2_A-OOGroveRadius

    lname.cockle_trashbin_peak: ACTLocationData(rname.secluded_ridge, 199, "The Sands Between - Trashbin Plateau"), #ca4c297f-e9fd-4a78-b89a-811d2394406b-2_A-OOGroveRadius
    lname.sinker_trashbin_peak: ACTLocationData(rname.secluded_ridge, 200, "The Sands Between - Trashbin Plateau"), #36611427-18cc-45f3-ad50-a51cc02ccb1d-2_A-OOGroveRadius
    lname.smallbattery_trashbin_mantis: ACTLocationData(rname.secluded_ridge, 201, "The Sands Between - Trashbin Plateau"), #0d86fe0e-ae41-4fb2-beb2-9bb5e558429a-2_A-OOGroveRadius
    lname.googlyeye_trashbin_pineapple: ACTLocationData(rname.secluded_ridge, 202, "The Sands Between - Trashbin Plateau"), #7935fe1e-318c-4f90-901b-fa001de6e4dc-2_A-OOGroveRadius

    lname.barnacle_grovemain_colander: ACTLocationData(rname.grove_main, 213, "Expired Grove Main"), #74aa4107-6a5a-4868-ae54-942e4421be3f-2_A-GroveForestLow
    lname.seastar_grovemain_eastrock: ACTLocationData(rname.grove_main, 218, "Expired Grove Main"), #17cb1eed-8d88-4464-b33b-215c837035f6-2_A-GroveForestLow
    lname.pufferquill_grovemain_sponges: ACTLocationData(rname.grove_main, 220, "Expired Grove Main"), #c6a56f3d-c134-41cd-83b7-4a755fa32284-2_A-GroveForestLow
    lname.limpet_grovemain_sodacan: ACTLocationData(rname.grove_main, 236, "Expired Grove Main"), #093c4972-ff5e-4ba6-b9a8-136411e1017f-2_A-GroveForestLow
    lname.lumpsucker_grovemain_canopy: ACTLocationData(rname.grove_main, 247, "Expired Grove Main"), #3789e56d-69b5-4d6c-adb1-6454b101840d-2_A-GroveForestLow
    lname.anothercrab_grovemain_sniper: ACTLocationData(rname.grove_main, 619, "Expired Grove Main"), #8e4714bf-cc7f-4bde-9c88-7fcdbf8d0afe-2_A-GroveForestLow
    lname.sharktooth_grovemain_pizza: ACTLocationData(rname.grove_main, 251, "Expired Grove Main"), #8e34f6a5-5844-4767-ab15-4fbaf6c147dc-2_B-GroveForestHigh
    lname.contactlens_grovemain_carts: ACTLocationData(rname.grove_main, 262, "Expired Grove Main"), #0e278f86-0f9d-468f-95b2-586df2a94689-2_A-GroveForestLow
    lname.cottonball_grovemain_mantis: ACTLocationData(rname.grove_main, 263, "Expired Grove Main"), #fa3cfc64-4f87-452c-bf59-4f599cb3f6fa-2_A-GroveForestLow
    lname.mussel_grovemain_fishing: ACTLocationData(rname.grove_main, 264, "Expired Grove Main"), #a1c14883-bc09-441c-a188-20dabf047532-2_A-GroveForestLow
    lname.sponge_grovemain_fishing: ACTLocationData(rname.grove_main, 265, "Expired Grove Main"), #7aa1847-5a38-4f15-a6fc-90c15cd9baf7-2_A-GroveForestLow
    lname.oyster_grovemain_fishing: ACTLocationData(rname.grove_main, 266, "Expired Grove Main"), #6ce4acf2-09a4-43ca-9be7-5d79a9d5c781-2_A-GroveForestLow
    lname.limpet_grovemain_fishing: ACTLocationData(rname.grove_main, 267, "Expired Grove Main"), #027511ce-7f48-480e-91af-18b4c7aaa57d-2_A-GroveForestLow

    lname.anemone_grovevillage_fishing: ACTLocationData(rname.grove_village, 274, "Expired Grove Village"), #5e81380f-3e8f-4d44-a0ef-ebbad0f23fdb-2_B-GroveForestHigh
    lname.phytoplanktonplus_grovevillage_upsidedown: ACTLocationData(rname.grove_village, 300, "Expired Grove Village"), #03bc01f8-4691-40b7-93c6-4d45563b5b46-2_C-Village
    lname.wadofgum_grovevillage_gumpile: ACTLocationData(rname.grove_village, 306, "Expired Grove Village"), #ab2ba852-edf4-467f-a1f5-1825341b7596-2_E-Cliffs
    lname.anemone_grovevillage_seahorse: ACTLocationData(rname.grove_village, 308, "Expired Grove Village"), #32841813-148d-45f7-8c4e-4464f157200d-2_E-Cliffs
    lname.mussel_grovevillage_dock: ACTLocationData(rname.grove_village, 310, "Expired Grove Village"), #3f1f877c-e5ac-40d1-93b7-2245282b0669-2_C-Village
    lname.earthworm_grovevillage_dock: ACTLocationData(rname.grove_village, 313, "Expired Grove Village"), #725998d5-172d-4408-9f70-0f9264a6a6fd-2_C-Village

    lname.anemone_flotsamvale_butaneisland: ACTLocationData(rname.flotsam_vale, 346, "Flotsam Vale"), #76b9b9ce-875c-4136-a6da-dabdfc70d40e-2_B-LowSwamp
    lname.rustynail_flotsamvale_brokenbutane: ACTLocationData(rname.flotsam_vale, 350, "Flotsam Vale"), #d656b2e6-15ec-4e24-bebb-94c1ed7f6c30-2_B-LowSwamp
    lname.sinker_flotsamvale_woodplatform: ACTLocationData(rname.flotsam_vale, 360, "Flotsam Vale"), #19c7932e-9133-4dbc-bc25-9f71aa29c271-2_A-HighSwamp
    lname.mussel_flotsamvale_woodplatform: ACTLocationData(rname.flotsam_vale, 363, "Flotsam Vale"), #e5b02de1-7cb7-4a4d-98a9-369c44302cac-2_A-HighSwamp
    lname.rustynail_flotsamvale_steamroller: ACTLocationData(rname.flotsam_vale, 367, "Flotsam Vale"), #f8d826c0-7319-4f95-ab90-bf28a7218dfb-2_A-HighSwamp
    lname.limpet_flotsamvale_trashpile: ACTLocationData(rname.flotsam_vale, 368, "Flotsam Vale"), #855a1efa-0f38-4e6b-a68d-24a991dcac42-2_A-HighSwamp
    lname.fruitsticker_flotsamvale_westbutane: ACTLocationData(rname.flotsam_vale, 371, "Flotsam Vale"), #0ad3895d-4612-4856-a6ed-7a7b48f2c36f-2_A-HighSwamp
    lname.seacucumber_flotsamvale_westbutane: ACTLocationData(rname.flotsam_vale, 372, "Flotsam Vale"), #5ccf4e25-ff98-4a9a-9e31-2eea57589809-2_A-HighSwamp
    lname.lumpsucker_flotsamvale_shorcut: ACTLocationData(rname.flotsam_vale, 375, "Flotsam Vale"), #a569d9f6-d930-4a9b-8041-8eb8621532ac-2_A-HighSwamp
    lname.oyster_flotsamvale_butanemailbox: ACTLocationData(rname.flotsam_vale, 377, "Flotsam Vale"), #235d8af5-0add-4509-b33c-dd3e3dbd27ff-2_A-HighSwamp
    lname.seastar_flotsamvale_butanemailbox: ACTLocationData(rname.flotsam_vale, 379, "Flotsam Vale"), #2f19d3b2-03ae-4fbe-8821-2dd01f007d11-2_A-HighSwamp
    lname.anemone_flotsamvale_APunder: ACTLocationData(rname.flotsam_vale, 382, "Flotsam Vale"), #cce99207-a255-4e12-ba19-51b5048ac64b-2_A-HighSwamp
    lname.cockle_flotsamvale_APabove: ACTLocationData(rname.flotsam_vale, 390, "Flotsam Vale"), #aeb3f185-eb51-4e68-a0cc-6dafc4b48a11-2_A-HighSwamp
    lname.sanddollar_flotsamvale_APabove: ACTLocationData(rname.flotsam_vale, 392, "Flotsam Vale"), #812367fb-0264-4113-9da5-104ba61d368b-2_A-HighSwamp
    lname.anemoneplus_flotsamvale_APunder: ACTLocationData(rname.flotsam_vale, 393, "Flotsam Vale"), #35d5823c-2da6-48c4-b8f1-074221917090-2_A-HighSwamp
    lname.anothercrab_flotsamvale_mailbox: ACTLocationData(rname.flotsam_vale, 395, "Flotsam Vale"), #daf9fa57-89d6-481f-8a6d-c32c9e8ecb5a-2_A-HighSwamp
    lname.sponge_flotsamvale_cranegrapple: ACTLocationData(rname.flotsam_vale, 407, "Flotsam Vale"), #2cb7f595-94fa-4b7b-a7c6-602808292c48-2_A-HighSwamp
    lname.seastarplus_flotsamvale_submerged: ACTLocationData(rname.flotsam_vale, 410, "Flotsam Vale"), #89d10f86-fcf2-483a-b145-f1576682520c-2_A-HighSwamp
    lname.lamprey_flotsamvale_islandfish: ACTLocationData(rname.flotsam_vale, 411, "Flotsam Vale"), #5a5395f1-e087-4a30-b3ea-b055fd328d40-2_B-LowSwamp
    lname.mussel_flotsamvale_elevatedfish: ACTLocationData(rname.flotsam_vale, 412, "Flotsam Vale"), #e863acfd-d4ee-4d2b-a868-6fe2420f1eda-2_B-LowSwamp
    lname.siphonophoreplus_flotsamvale_waterfall: ACTLocationData(rname.flotsam_vale, 414, "Flotsam Vale"), #491e2dc3-ab0b-4da4-b36d-a3c2e60ea2a3-2_B-LowSwamp
    lname.whelk_flotsamvale_westfish: ACTLocationData(rname.flotsam_vale, 416, "Flotsam Vale"), #aecd0ac5-352e-4ae3-ae6a-3b810e8588d6-2_B-LowSwamp
    lname.anemoneplus_flotsamvale_northwestfish: ACTLocationData(rname.flotsam_vale, 421, "Flotsam Vale"), #f29c22d3-4459-4d21-b76d-dbdd514fe09a-2_A-HighSwamp
    lname.turtleshell_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 609, "Flotsam Vale"), #584ec079-5ecc-409b-bcac-7197b1d04a1c-2_A-HighSwamp
    lname.lilisopod_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 613, "Flotsam Vale"), #6709552a-af26-4b87-a69e-97830fd645be-2_A-HighSwamp
    lname.rustynail_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 616, "Flotsam Vale"), #fa0535e3-55e1-4879-ac12-9327d5858b1a-2_C-Facilities
    lname.barnacle_flotsamvale_gunkfish: ACTLocationData(rname.flotsam_vale, 617, "Flotsam Vale"), #c376ad88-aa83-4923-9652-13fd98a67a19-2_C-Facilities

    lname.googlyeye_scuttleport_cubbies: ACTLocationData(rname.scuttleport, 427, "Scuttleport"), #5736e238-67d5-4215-823d-a0c3b3d60b2a-2_A-HighSwamp
    lname.seastar_scuttleport_cubbies: ACTLocationData(rname.scuttleport, 428, "Scuttleport"), #69c1d4c5-c467-4127-a12a-6277376c47f0-2_A-HighSwamp
    lname.sanddollar_scuttleport_magnet: ACTLocationData(rname.scuttleport, 432, "Scuttleport"), #14992c5b-3377-4664-9309-3f44a31b1ae5-2_C-Facilities
    lname.mussel_scuttleport_magnetfish: ACTLocationData(rname.scuttleport, 433, "Scuttleport"), #6c265bf5-d319-4a6b-8ddf-ad803b9bdde6-2_C-Facilities
    lname.limpet_scuttleport_electricboxes: ACTLocationData(rname.scuttleport, 437, "Scuttleport"), #34e41971-5cef-4947-b6ff-6b1e4da0f2d6-2_C-Facilities
    lname.rubberband_scuttleport_magnetdropoff: ACTLocationData(rname.scuttleport, 440, "Scuttleport"), #f1ce3edd-314d-4cf7-ae79-fdb5cf0a7ac0-2_C-Facilities
    lname.limpet_scuttleport_magnet: ACTLocationData(rname.scuttleport, 441, "Scuttleport"), #1a376ec2-e1bf-44a3-bc18-0ec8d4252b0d-2_C-Facilities
    lname.anemoneplus_scuttleport_magnetdropoff: ACTLocationData(rname.scuttleport, 443, "Scuttleport"), #b0c6c00b-fcbb-4884-83c7-cf655211e599-2_C-Facilities
    lname.lumpsucker_scuttleport_trashisland: ACTLocationData(rname.scuttleport, 444, "Scuttleport"), #555557dd-239a-40da-a89f-82d0cc6adc65-2_C-Facilities
    lname.sinkerplusplus_scuttleport_clam: ACTLocationData(rname.scuttleport, 451, "Scuttleport"), #f2466d53-7e70-4d19-9c12-cb9da07a72fe-2_C-Facilities
    lname.seastar_scuttleport_survivorcamp: ACTLocationData(rname.scuttleport, 455, "Scuttleport"), #17a5b692-c56b-4f43-8ca2-b2909ef9c446-2_C-Facilities
    lname.pufferquill_scuttleport_survivorcamp: ACTLocationData(rname.scuttleport, 456, "Scuttleport"), #08bbdb7b-63dd-4e3d-9499-fc77548c3bd9-2_C-Facilities
    lname.turtleshell_scuttleport_survivorcamp: ACTLocationData(rname.scuttleport, 458, "Scuttleport"), #0e380f83-dc56-468f-aa76-30f049c33fd8-2_C-Facilities
    lname.rustynailplus_scuttleport_magrail: ACTLocationData(rname.scuttleport, 464, "Scuttleport"), #b515d67d-b4fa-4282-a872-9c351d087c85-2_C-Facilities
    lname.barnacleplus_scuttleport_propanebridge: ACTLocationData(rname.scuttleport, 479, "Scuttleport"), #a16b7348-4d15-4bfb-9a0c-ee2f8994deea-2_C-Facilities
    lname.salp_scuttleport_propanebridge: ACTLocationData(rname.scuttleport, 480, "Scuttleport"), #09d1270f-cab8-45dd-af56-0c7220ad9e98-2_C-Facilities
    lname.musselplus_scuttleport_voltai: ACTLocationData(rname.scuttleport, 482, "Scuttleport"), #d8ad97ae-8fa3-4a76-98ef-6cf635627776-2_C-Facilities

    lname.barnacle_pinbarge: ACTLocationData(rname.pinbarge, 484, "Pinbarge"), #98b0e1e4-2548-4b28-948d-b3a05147286a-2_A-PinBargeRunup
    lname.musselplus_pinbarge: ACTLocationData(rname.pinbarge, 487, "Pinbarge"), #29dab0bb-a195-47d3-b553-ebc5a4f03154-2_A-PinBargeRunup

    lname.musselplus_unfathom_telephone: ACTLocationData(rname.unfathom, 491, "The Unfathom"), #87b99366-1eb6-4cd3-af8e-a454cc3c0172-2_B-DarkCanyon
    lname.seastarplus_unfathom_glowstick: ACTLocationData(rname.unfathom, 496, "The Unfathom"), #bf3b5664-5805-403b-af6f-98f4557c532b-2_B-DarkCanyon
    lname.lanternfish_unfathom_styrofoam: ACTLocationData(rname.unfathom, 503, "The Unfathom"), #9de638f7-ee53-4b14-8b12-8880c9a11631-2_B-DarkCanyon
    lname.lampreyplus_unfathom_pinbargeclam: ACTLocationData(rname.unfathom, 509, "The Unfathom"), #fa136387-6988-46e4-9915-fc0a6f11ec6a-2_B-DarkCanyon
    lname.limpet_unfathom_pinbarge: ACTLocationData(rname.unfathom, 510, "The Unfathom"), #ecc7eed3-27e2-4168-8f6e-6733375b7c99-2_B-DarkCanyon
    lname.siphonophoreplus_unfathom_shortcut: ACTLocationData(rname.unfathom, 512, "The Unfathom"), #75e64603-4664-467d-b2d4-579448396fd4-2_B-DarkCanyon
    lname.salp_unfathom_glowstickfish: ACTLocationData(rname.unfathom, 517, "The Unfathom"), #e9fe66b6-b7db-492a-9b64-66f19bfda0c1-2_B-DarkCanyon
    lname.barnacleplus_unfathom_pinbargefish: ACTLocationData(rname.unfathom, 504, "The Unfathom"), #8ed2ebbb-d383-43ab-8530-f3c1cd714763-2_B-DarkCanyon

    lname.sinkerplus_plains_petroch: ACTLocationData(rname.plains, 519, "Abyssal Plains"), #41d32998-d9d9-4b64-bedd-23889b575ec4-2_C-HermitCave
    lname.pufferquill_plains_inkerton: ACTLocationData(rname.plains, 523, "Abyssal Plains"), #ce72bf4f-67a6-4ce9-b094-08abfd7fb973-2_D-SilentFlats
    lname.rustynailplus_plains_shortcut: ACTLocationData(rname.plains, 525, "Abyssal Plains"), #a348d1db-7fb6-460a-b327-a09b3effacd9-2_D-SilentFlats
    lname.limpetplus_plains_inkerton: ACTLocationData(rname.plains, 526, "Abyssal Plains"), #a36e3443-c030-4021-8022-df892e62328b-2_D-SilentFlats
    lname.whelkplus_plains_shortcut: ACTLocationData(rname.plains, 527, "Abyssal Plains"), #b3cc9d26-0b24-438b-ba96-084ba135230a-2_D-SilentFlats
    lname.zooplanktonplus_plains_shortcut: ACTLocationData(rname.plains, 528, "Abyssal Plains"), #42a14e36-7015-455e-a2b9-95fc02893e1f-2_D-SilentFlats
    lname.salpplus_plains_entrance: ACTLocationData(rname.plains, 529, "Abyssal Plains"), #09879ffa-ec2f-4723-b157-6efbef8f364b-2_D-SilentFlats
    lname.anothercrab_plains_shortcutclam: ACTLocationData(rname.plains, 530, "Abyssal Plains"), #689ac44f-d0f2-4c33-9aad-686823303bff-2_D-SilentFlats
    lname.seacucumber_plains_entrance: ACTLocationData(rname.plains, 531, "Abyssal Plains"), #82554ff8-c8f1-42b3-8018-f84f5ec94c55-2_D-SilentFlats
    lname.fruitsticker_plains_entrance: ACTLocationData(rname.plains, 533, "Abyssal Plains"), #fda1ad5d-5abb-4351-b682-8e91036ccddd-2_D-SilentFlats

    lname.sanddollar_oldocean_ledge: ACTLocationData(rname.plains, 544, "The Old Ocean"), #5f0809f4-5a0f-4b4d-be76-1386bc665a16-2_A-BleachedCopse
    lname.barnacleplusplus_oldocean_styrofoam: ACTLocationData(rname.plains, 545, "The Old Ocean"), #19a53c5e-497f-4e5e-a947-6a065747c92a-2_A-BleachedCopse
    lname.seastarplusplus_oldocean_entranceclam: ACTLocationData(rname.plains, 561, "The Old Ocean"), #6df4f101-e0f2-4147-94e8-54235e8b803f-2_B-GrandCourtyard
    lname.spongeplus_oldocean_entrance: ACTLocationData(rname.plains, 563, "The Old Ocean"), #9cd5413b-91c2-421a-92de-8a703922f888-2_B-GrandCourtyard
    lname.sanddollar_oldocean_citywall: ACTLocationData(rname.plains, 571, "The Old Ocean"), #b27f8f08-2a6d-4f78-8ef5-ca01d2b968ef-2_B-GrandCourtyard
    lname.usedbandageplus_oldocean_citywall: ACTLocationData(rname.plains, 579, "The Old Ocean"), #5988e9dd-dc40-4f00-af63-66da9db0e7b4-2_B-GrandCourtyard
    lname.cockleplus_oldocean_snaileast: ACTLocationData(rname.plains, 582, "The Old Ocean"), #3e336fbb-9830-4772-a1b3-55dc039380dd-2_B-GrandCourtyard
    lname.anothercrab_oldocean_elevator: ACTLocationData(rname.plains, 588, "The Old Ocean"), #b7757de2-ce70-474e-a332-cef609bdf42f-2_B-GrandCourtyard
    lname.sanddollar_oldocean_easternbuilding: ACTLocationData(rname.plains, 592, "The Old Ocean"), #4babc398-17b9-4197-958e-c6bebc12a6c6-2_B-GrandCourtyard
    lname.phytoplanktonplus_oldocean_clam: ACTLocationData(rname.plains, 600, "The Old Ocean"), #a9ac0a98-889e-4138-a62b-0d59f63af118-2_B-GrandCourtyard
    lname.musselplusplus_oldocean_woodplank: ACTLocationData(rname.plains, 601, "The Old Ocean"), #df538a5c-9108-4210-8b9d-89e777116ec4-2_B-GrandCourtyard
    lname.whelkplusplus_oldocean_mantis: ACTLocationData(rname.plains, 604, "The Old Ocean"), #21387127-4e04-4017-bb58-3aafb9537876-2_B-GrandCourtyard

    ##### costume locations
    lname.captain_costume_pickup: ACTLocationData(rname.central_shallows, 43, "Central Shallows"), #7c307763-a7b4-4e81-88d6-e1baf1b04608-2_B-ShallowsBigSand
    lname.clown_costume_pickup: ACTLocationData(rname.sands_between, 140,"The Sands Between"), #cd2d0535-6c06-4530-bf60-afbffc2d5086-2_A-OOGroveRadius
    lname.sunlight_costume_pickup: ACTLocationData(rname.secluded_ridge, 198, "The Sands Between - Secluded Ridge"), #35aa72f2-fa50-4efc-b600-b597382ed877-2_A-OOGroveRadius
    lname.intern_costume_pickup: ACTLocationData(rname.grove_village, 296, "Expired Grove Village"), #4ba7f2ff-ff35-4d74-b5ac-d9c59fe1c94d-2_C-Village
    lname.cowfishboy_costume_pickup: ACTLocationData(rname.flotsam_vale, 348, "Flotsam Vale"), #b1f8794b-d43d-41b9-827a-75bb4c7a57bf-NickGym
    lname.bluecollar_costume_pickup: ACTLocationData(rname.scuttleport, 430, "Scuttleport"), #f37cb96e-df05-4aed-b2b5-7d8d5af32483-NickGym
    lname.krillionaire_costume_pickup: ACTLocationData(rname.unfathom, 490, "The Unfathom"), #c762c7f8-33b6-4701-9f4c-7ad7938a5d11-2_B-DarkCanyon
    lname.exiledflame_costume_pickup: ACTLocationData(rname.unfathom, 507, "The Unfathom"), #1b7cb531-3a0a-4957-ab59-da5c9f1da705-2_B-DarkCanyon
    lname.drkril_costume_pickup: ACTLocationData(rname.old_ocean, 551, "The Old Ocean"), #d5fed7e0-cd33-4a81-9688-1e7ca948139f-2_A-BleachedCopse

    ##### non-boss adaptation locations
    lname.urchin_toss_quest: ACTLocationData(rname.new_carcinia, 85,"New Carcinia"), #AUTO NEEDS TO MAKE A CUSTOM SCRIPT
    lname.bobbit_trap_pickup: ACTLocationData(rname.sands_between, 109,"The Sands Between"), #3bb06349-c151-4333-8305-ba0eb7512bc3-2_A-OOGroveRadius
    #lname.royal_wave_reward: ACTLocationData(rname.slacktide_after, x, "Fort Slacktide - After Destruction") #Redundant, overlaps with Magista

    ##### skill locations
    lname.shelleport_skill: ACTLocationData(rname.snail_cave, 254, "Moon Snail Skills"),
    lname.skedaddle_skill: ACTLocationData(rname.snail_cave, 255, "Moon Snail Skills"),
    lname.parry_skill: ACTLocationData(rname.snail_cave, 318, "Moon Snail Skills"),
    lname.riposte_skill: ACTLocationData(rname.snail_cave, 319, "Moon Snail Skills"),
    lname.natural_defenses_skill: ACTLocationData(rname.snail_cave, 320, "Moon Snail Skills"),
    lname.aggravation_skill: ACTLocationData(rname.snail_cave, 321, "Moon Snail Skills"),
    lname.self_repair_skill: ACTLocationData(rname.snail_cave, 322, "Moon Snail Skills"),
    lname.kintsugi_skill: ACTLocationData(rname.snail_cave, 323, "Moon Snail Skills"),
    lname.skewer_skill: ACTLocationData(rname.snail_cave, 324, "Moon Snail Skills"),
    lname.plunge_skill: ACTLocationData(rname.snail_cave, 325, "Moon Snail Skills"),
    lname.scrap_hammer_skill: ACTLocationData(rname.snail_cave, 326, "Moon Snail Skills"),
    lname.dispatch_skill: ACTLocationData(rname.snail_cave, 327, "Moon Snail Skills"),
    lname.spearfishing_skill: ACTLocationData(rname.snail_cave, 328, "Moon Snail Skills"),
    lname.wave_breaker_skill: ACTLocationData(rname.snail_cave, 329, "Moon Snail Skills"),
    lname.streamline_skill: ACTLocationData(rname.snail_cave, 330, "Moon Snail Skills"),
    lname.housewarming_skill: ACTLocationData(rname.snail_cave, 331, "Moon Snail Skills"),
    lname.circle_of_life_skill: ACTLocationData(rname.snail_cave, 332, "Moon Snail Skills"),
    lname.elusive_prey_skill: ACTLocationData(rname.snail_cave, 333, "Moon Snail Skills"),
    lname.ebb_and_flow_skill: ACTLocationData(rname.snail_cave, 334, "Moon Snail Skills"),
    lname.umami_training1_skill: ACTLocationData(rname.snail_cave, 335, "Moon Snail Skills"),
    lname.umami_training2_skill: ACTLocationData(rname.snail_cave, 336, "Moon Snail Skills"),
    lname.umami_training3_skill: ACTLocationData(rname.snail_cave, 337, "Moon Snail Skills"),

    ##### shell locations
    # not even sure if the regions will work like that
    sname.soda_can: ACTLocationData(sname.soda_can, None, "Shells"),
    sname.bottle_cap: ACTLocationData(sname.bottle_cap, None, "Shells")
    
    # sname.tin_can: ACTLocationData({}, None, "Shells"),
    # sname.shot_glass: ACTLocationData({}, None, "Shells"),
    # sname.banana_peel: ACTLocationData({}, None, "Shells"),
    # sname.party_hat: ACTLocationData({}, None, "Shells"),
    # sname.coconut: ACTLocationData({}, None, "Shells"),
    # sname.teacup: ACTLocationData({}, None, "Shells"),
    # sname.sauce_nozzle: ACTLocationData({}, None, "Shells"),
    # sname.thimble: ACTLocationData({}, None, "Shells"),
    # sname.bebop_cup: ACTLocationData({}, None, "Shells"),
    # sname.tennis_ball: ACTLocationData({}, None, "Shells"),
    # sname.f_key: ACTLocationData({}, None, "Shells"),
    # sname.mason_jar: ACTLocationData({}, None, "Shells"),
    # sname.salt_shaker: ACTLocationData({}, None, "Shells"),
    # sname.conchiglie: ACTLocationData({}, None, "Shells"),
    # sname.bartholomew: ACTLocationData({}, None, "Shells"),
    # sname.disco_ball: ACTLocationData({}, None, "Shells"),
    # sname.baby_shoe: ACTLocationData({}, None, "Shells"),
    # sname.lil_bro: ACTLocationData({}, None, "Shells"),
    # sname.matryoshka_large: ACTLocationData({}, None, "Shells"),
    # sname.matryoshka_medium: ACTLocationData({}, None, "Shells"),
    # sname.matryoshka_small: ACTLocationData({}, None, "Shells"),
    # sname.shuttlecock: ACTLocationData({}, None, "Shells"),
    # sname.felix_cube: ACTLocationData({}, None, "Shells"),
    # sname.piggy_bank: ACTLocationData({}, None, "Shells"),
    # sname.trophy: ACTLocationData({}, None, "Shells"),
    # sname.imposter: ACTLocationData({}, None, "Shells"),
    # sname.lil_red_cup: ACTLocationData({}, None, "Shells"),
    # sname.wafer_cone: ACTLocationData({}, None, "Shells"),
    # sname.yoccult: ACTLocationData({}, None, "Shells"),
    # sname.coffee_pod: ACTLocationData({}, None, "Shells"),
    # sname.egg_shell: ACTLocationData({}, None, "Shells"),
    # sname.coffee_mug: ACTLocationData({}, None, "Shells"),
    # sname.cascadia_roll: ACTLocationData({}, None, "Shells"),
    # sname.ham_tin: ACTLocationData({}, None, "Shells"),
    # sname.skull: ACTLocationData({}, None, "Shells"),
    # sname.crab_husk: ACTLocationData({}, None, "Shells"),
    # sname.legal_brick: ACTLocationData({}, None, "Shells"),
    # sname.spring: ACTLocationData({}, None, "Shells"),
    # sname.shotgun_shell: ACTLocationData({}, None, "Shells"),
    # sname.rubber_duck: ACTLocationData({}, None, "Shells"),
    # sname.boxing_glove: ACTLocationData({}, None, "Shells"),
    # sname.cardboard_box: ACTLocationData({}, None, "Shells"),
    # sname.tissue_box: ACTLocationData({}, None, "Shells"),
    # sname.valve: ACTLocationData({}, None, "Shells"),
    # sname.dumptruck: ACTLocationData({}, None, "Shells"),
    # sname.ink_cartridge: ACTLocationData({}, None, "Shells"),
    # sname.gacha_capsule: ACTLocationData({}, None, "Shells"),
    # sname.lightbulb: ACTLocationData({}, None, "Shells"),
    # sname.mouse: ACTLocationData({}, None, "Shells"),
    # sname.going_under_64: ACTLocationData({}, None, "Shells"),
    # sname.sock: ACTLocationData({}, None, "Shells"),
    # sname.doll_head: ACTLocationData({}, None, "Shells"),
    # sname.service_bell: ACTLocationData({}, None, "Shells"),
    # sname.party_popper: ACTLocationData({}, None, "Shells"),
    # sname.scrub_aggie: ACTLocationData({}, None, "Shells"),
    # sname.dentures: ACTLocationData({}, None, "Shells"),
    # sname.pill_bottle: ACTLocationData({}, None, "Shells"),
    # sname.detergent_cap: ACTLocationData({}, None, "Shells"),
    # sname.ultrasoft: ACTLocationData({}, None, "Shells"),
    # sname.champagne_flute: ACTLocationData({}, None, "Shells"),
    # sname.dish_scrubber: ACTLocationData({}, None, "Shells"),
    # sname.snow_globe: ACTLocationData({}, None, "Shells"),
    # sname.knights_helmet: ACTLocationData({}, None, "Shells"),
    # sname.spirit_conch: ACTLocationData({}, None, "Shells"),
    # sname.plug_fuse: ACTLocationData({}, None, "Shells")
    
}
# def combine_location_id(location: ACTLocationData) -> int:
#     if location.location_id_offset == None:
#         return None
#     else:
#         return location.location_id_offset + location_base_id

location_name_to_id: Dict[str, int] = {} #= {name: combine_location_id(data) for name, data in location_table.items()}

for name, data in location_table.items():
    if data.location_id_offset != None:
        location_name_to_id.update({name:data.location_id_offset + location_base_id})

def get_location_group(location_name: str) -> str:
    return location_table[location_name].location_group

shell_locations: List[str] = [name for name, data in location_table.items() if data.location_group == "Shells"]

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)

location_total: int = len(location_table)