use resource_info_table::resource_info;
use reader_writer::{
    FourCC,
    Reader,
    Writable,
};
use structs::{res_id, ResId, Resource, ResourceKind};

use crate::{
    patch_config::{PatchConfig, GenericTexture},
    elevators::{World, SpawnRoomData},
    pickup_meta::{self, PickupType, PickupModel},
    door_meta::{DoorType, BlastShieldType},
    ResourceData,
    GcDiscLookupExtensions,
    extern_assets::ExternPickupModel,
    patches::{WaterType, Version},
};

use std::{
    borrow::Cow,
    collections::{HashMap, HashSet},
};

#[derive(Debug, Clone, Copy, Hash, PartialEq, Eq)]
pub struct PickupHashKey {
    pub level_id: u32,
    pub room_id: u32,
    pub pickup_idx: u32,
}

impl PickupHashKey {
    fn from_location(level_name: &str, room_name: &str, pickup_idx: u32) -> Self
    {
        let level = World::from_json_key(level_name);
        PickupHashKey {
            level_id: level.mlvl(),
            room_id: SpawnRoomData::from_str(&format!("{}:{}", level.to_str(), room_name).as_str()).mrea, // TODO: this is suboptimal
            pickup_idx,
        }
    }
}

macro_rules! def_asset_ids {
    (@Build { $prev:expr } $id:ident: $fc:ident, $($rest:tt)*) => {
        def_asset_ids!(@Build { $prev } $id: $fc = $prev + 1, $($rest)*);
    };
    (@Build { $_prev:expr } $id:ident: $fc:ident = $e:expr, $($rest:tt)*) => {
        pub const $id: structs::ResId<structs::res_id::$fc> = structs::ResId::new($e);
        def_asset_ids!(@Build { $id.to_u32() } $($rest)*);
    };
    (@Build { $prev:expr }) => {
    };
    ($($tokens:tt)*) => {
        def_asset_ids!(@Build { 0 } $($tokens)*);
    };
}

pub mod custom_asset_ids {
    def_asset_ids! {
        // Item Assets //
        PHAZON_SUIT_TXTR1: TXTR = 0xDEAF0000,
        PHAZON_SUIT_TXTR2: TXTR,
        PHAZON_SUIT_CMDL: CMDL,
        PHAZON_SUIT_ANCS: ANCS,
        NOTHING_TXTR: TXTR,
        NOTHING_CMDL: CMDL,
        NOTHING_ANCS: ANCS,
        THERMAL_CMDL: CMDL,
        THERMAL_ANCS: ANCS,
        XRAY_CMDL: CMDL,
        XRAY_ANCS: ANCS,
        COMBAT_CMDL: CMDL,
        COMBAT_ANCS: ANCS,
        SHINY_MISSILE_TXTR0: TXTR,
        SHINY_MISSILE_TXTR1: TXTR,
        SHINY_MISSILE_TXTR2: TXTR,
        SHINY_MISSILE_CMDL: CMDL,
        SHINY_MISSILE_ANCS: ANCS,
        SHINY_MISSILE_EVNT: EVNT,
        SHINY_MISSILE_ANIM: ANIM,
        SHORELINES_POI_SCAN: SCAN,
        SHORELINES_POI_STRG: STRG,
        CFLDG_POI_SCAN: SCAN,
        CFLDG_POI_STRG: STRG,
        TOURNEY_WINNERS_SCAN: SCAN,
        TOURNEY_WINNERS_STRG: STRG,

        // Starting items memo
        STARTING_ITEMS_HUDMEMO_STRG: STRG,

        // Warping
        WARPING_TO_START_STRG: STRG,
        GENERIC_WARP_STRG: STRG,
        WARPING_TO_START_DELAY_STRG: STRG,
        WARPING_TO_OTHER_STRG: STRG,

        // Blocks
        BLOCK_COLOR_0: CMDL,
        BLOCK_COLOR_1: CMDL,
        BLOCK_COLOR_2: CMDL,
        BLOCK_COLOR_3: CMDL,
        BLOCK_COLOR_4: CMDL,

        // Door Assets //
        MORPH_BALL_BOMB_DOOR_CMDL: CMDL,
        POWER_BOMB_DOOR_CMDL: CMDL,
        MISSILE_DOOR_CMDL: CMDL,
        CHARGE_DOOR_CMDL: CMDL,
        SUPER_MISSILE_DOOR_CMDL: CMDL,
        WAVEBUSTER_DOOR_CMDL: CMDL,
        ICESPREADER_DOOR_CMDL: CMDL,
        FLAMETHROWER_DOOR_CMDL: CMDL,
        DISABLED_DOOR_CMDL: CMDL,
        AI_DOOR_CMDL: CMDL,

        VERTICAL_RED_DOOR_CMDL: CMDL,
        VERTICAL_BOOST_DOOR_CMDL: CMDL,
        VERTICAL_POWER_BOMB_DOOR_CMDL: CMDL,
        VERTICAL_MORPH_BALL_BOMB_DOOR_CMDL: CMDL,
        VERTICAL_MISSILE_DOOR_CMDL: CMDL,
        VERTICAL_CHARGE_DOOR_CMDL: CMDL,
        VERTICAL_SUPER_MISSILE_DOOR_CMDL: CMDL,
        VERTICAL_DISABLED_DOOR_CMDL: CMDL,
        VERTICAL_WAVEBUSTER_DOOR_CMDL: CMDL,
        VERTICAL_ICESPREADER_DOOR_CMDL: CMDL,
        VERTICAL_FLAMETHROWER_DOOR_CMDL: CMDL,
        VERTICAL_AI_DOOR_CMDL: CMDL,

        MORPH_BALL_BOMB_DOOR_TXTR: TXTR,
        POWER_BOMB_DOOR_TXTR: TXTR,
        MISSILE_DOOR_TXTR: TXTR,
        CHARGE_DOOR_TXTR: TXTR,
        SUPER_MISSILE_DOOR_TXTR: TXTR,
        WAVEBUSTER_DOOR_TXTR: TXTR,
        ICESPREADER_DOOR_TXTR: TXTR,
        FLAMETHROWER_DOOR_TXTR: TXTR,
        DISABLED_DOOR_TXTR: TXTR,
        AI_DOOR_TXTR: TXTR,

        BOOST_DOOR_SCAN: SCAN,
        BOOST_DOOR_STRG: STRG,
        POWER_BOMB_DOOR_SCAN: SCAN,
        POWER_BOMB_DOOR_STRG: STRG,
        BOMB_DOOR_SCAN: SCAN,
        BOMB_DOOR_STRG: STRG,
        MISSILE_DOOR_SCAN: SCAN,
        MISSILE_DOOR_STRG: STRG,
        CHARGE_DOOR_SCAN: SCAN,
        CHARGE_DOOR_STRG: STRG,
        SUPER_MISSILE_DOOR_SCAN: SCAN,
        SUPER_MISSILE_DOOR_STRG: STRG,
        WAVEBUSTER_DOOR_SCAN: SCAN,
        WAVEBUSTER_DOOR_STRG: STRG,
        ICESPREADER_DOOR_SCAN: SCAN,
        ICESPREADER_DOOR_STRG: STRG,
        FLAMETHROWER_DOOR_SCAN: SCAN,
        FLAMETHROWER_DOOR_STRG: STRG,
        DISABLED_DOOR_SCAN: SCAN,
        DISABLED_DOOR_STRG: STRG,
        AI_DOOR_SCAN: SCAN,
        AI_DOOR_STRG: STRG,

        // blast shield assets //
        POWER_BOMB_BLAST_SHIELD_CMDL: CMDL,
        SUPER_BLAST_SHIELD_CMDL: CMDL,
        WAVEBUSTER_BLAST_SHIELD_CMDL: CMDL,
        ICESPREADER_BLAST_SHIELD_CMDL: CMDL,
        FLAMETHROWER_BLAST_SHIELD_CMDL: CMDL,

        BLAST_SHIELD_ALT_TXTR0: TXTR,
        BLAST_SHIELD_ALT_TXTR1: TXTR,
        BLAST_SHIELD_ALT_TXTR2: TXTR,

        POWER_BOMB_BLAST_SHIELD_TXTR: TXTR,
        SUPER_BLAST_SHIELD_TXTR: TXTR,
        WAVEBUSTER_BLAST_SHIELD_TXTR: TXTR,
        ICESPREADER_BLAST_SHIELD_TXTR: TXTR,
        FLAMETHROWER_BLAST_SHIELD_TXTR: TXTR,

        POWER_BOMB_BLAST_SHIELD_SCAN: SCAN,
        SUPER_BLAST_SHIELD_SCAN: SCAN,
        WAVEBUSTER_BLAST_SHIELD_SCAN: SCAN,
        ICESPREADER_BLAST_SHIELD_SCAN: SCAN,
        FLAMETHROWER_BLAST_SHIELD_SCAN: SCAN,

        POWER_BOMB_BLAST_SHIELD_STRG: STRG,
        SUPER_BLAST_SHIELD_STRG: STRG,
        WAVEBUSTER_BLAST_SHIELD_STRG: STRG,
        ICESPREADER_BLAST_SHIELD_STRG: STRG,
        FLAMETHROWER_BLAST_SHIELD_STRG: STRG,

        // Pickup dot icon
        MAP_PICKUP_ICON_TXTR: TXTR,

        // Strings to use if none are specified
        DEFAULT_PICKUP_SCAN_STRGS: STRG,
        DEFAULT_PICKUP_SCANS: SCAN = DEFAULT_PICKUP_SCAN_STRGS.to_u32() + 50,
        DEFAULT_PICKUP_HUDMEMO_STRGS: STRG = DEFAULT_PICKUP_SCANS.to_u32() + 50,

        EXTRA_IDS_START: STRG = DEFAULT_PICKUP_HUDMEMO_STRGS.to_u32() + 50,
    }
}

pub fn build_resource<'r, K>(file_id: ResId<K>, kind: ResourceKind<'r>) -> Resource<'r>
    where K: res_id::ResIdKind,
{
    assert_eq!(K::FOURCC, kind.fourcc());
    build_resource_raw(file_id.to_u32(), kind)
}

#[cfg(not(debug_assertions))]
pub fn build_resource_raw<'r>(file_id: u32, kind: ResourceKind<'r>) -> Resource<'r>
{
    Resource {
        compressed: false,
        file_id,
        kind,
    }
}

#[cfg(debug_assertions)]
pub fn build_resource_raw<'r>(file_id: u32, kind: ResourceKind<'r>) -> Resource<'r>
{
    Resource {
        compressed: false,
        file_id,
        kind,
        original_offset: 0,
    }
}

// Assets defined in an external file at RUNTIME
fn extern_assets_runtime<'r>(extern_assets_dir: Option<String>)
 -> Result<
     (Vec<Resource<'r>>, HashMap<String, ExternPickupModel>),
     String>
{
    let (extern_models, extern_assets) = ExternPickupModel::parse(&extern_assets_dir.clone().unwrap())?;

    let mut resources = Vec::<Resource<'r>>::new();
    for (id, asset) in extern_assets.iter() {
        let resource = ResourceKind::External(asset.bytes.clone(), asset.fourcc);
        resources.push(
            build_resource_raw(*id, resource)
        );
    }

    Ok((resources, extern_models))
}

// Assets defined in an external file at COMPILE TIME
fn extern_assets_compile_time<'r>() -> Vec<Resource<'r>>
{
    let extern_assets: &[(ResId<res_id::TXTR>, [u8; 4], &[u8])] = &[
        (custom_asset_ids::PHAZON_SUIT_TXTR1             , *b"TXTR", include_bytes!("../extra_assets/phazon_suit_texure_1.txtr")),
        (custom_asset_ids::PHAZON_SUIT_TXTR2             , *b"TXTR", include_bytes!("../extra_assets/phazon_suit_texure_2.txtr")),
        (custom_asset_ids::NOTHING_TXTR                  , *b"TXTR", include_bytes!("../extra_assets/nothing_texture.txtr"     )),
        (custom_asset_ids::SHINY_MISSILE_TXTR0           , *b"TXTR", include_bytes!("../extra_assets/shiny-missile0.txtr"      )),
        (custom_asset_ids::SHINY_MISSILE_TXTR1           , *b"TXTR", include_bytes!("../extra_assets/shiny-missile1.txtr"      )),
        (custom_asset_ids::SHINY_MISSILE_TXTR2           , *b"TXTR", include_bytes!("../extra_assets/shiny-missile2.txtr"      )),
        (custom_asset_ids::AI_DOOR_TXTR                  , *b"TXTR", include_bytes!("../extra_assets/holorim_ai.txtr"          )),
        (custom_asset_ids::MORPH_BALL_BOMB_DOOR_TXTR     , *b"TXTR", include_bytes!("../extra_assets/holorim_bombs.txtr"       )),
        (custom_asset_ids::POWER_BOMB_DOOR_TXTR          , *b"TXTR", include_bytes!("../extra_assets/holorim_powerbomb.txtr"   )),
        (custom_asset_ids::SUPER_MISSILE_DOOR_TXTR       , *b"TXTR", include_bytes!("../extra_assets/holorim_super.txtr"       )),
        (custom_asset_ids::WAVEBUSTER_DOOR_TXTR          , *b"TXTR", include_bytes!("../extra_assets/holorim_wavebuster.txtr"  )),
        (custom_asset_ids::ICESPREADER_DOOR_TXTR         , *b"TXTR", include_bytes!("../extra_assets/holorim_icespreader.txtr" )),
        (custom_asset_ids::FLAMETHROWER_DOOR_TXTR        , *b"TXTR", include_bytes!("../extra_assets/holorim_flamethrower.txtr")),
        (custom_asset_ids::BLAST_SHIELD_ALT_TXTR0        , *b"TXTR", include_bytes!("../extra_assets/blast_shield_alt_0.txtr"  )),
        (custom_asset_ids::BLAST_SHIELD_ALT_TXTR1        , *b"TXTR", include_bytes!("../extra_assets/blast_shield_alt_1.txtr"  )),
        (custom_asset_ids::BLAST_SHIELD_ALT_TXTR2        , *b"TXTR", include_bytes!("../extra_assets/blast_shield_alt_2.txtr"  )),
        (custom_asset_ids::POWER_BOMB_BLAST_SHIELD_TXTR  , *b"TXTR", include_bytes!("../extra_assets/blast_shield_pbm.txtr"    )),
        (custom_asset_ids::SUPER_BLAST_SHIELD_TXTR       , *b"TXTR", include_bytes!("../extra_assets/blast_shield_spr.txtr"    )),
        (custom_asset_ids::WAVEBUSTER_BLAST_SHIELD_TXTR  , *b"TXTR", include_bytes!("../extra_assets/blast_shield_wvb.txtr"    )),
        (custom_asset_ids::ICESPREADER_BLAST_SHIELD_TXTR , *b"TXTR", include_bytes!("../extra_assets/blast_shield_ice.txtr"    )),
        (custom_asset_ids::FLAMETHROWER_BLAST_SHIELD_TXTR, *b"TXTR", include_bytes!("../extra_assets/blast_shield_flm.txtr"    )),
        (custom_asset_ids::MAP_PICKUP_ICON_TXTR          , *b"TXTR", include_bytes!("../extra_assets/map_pickupdot.txtr"       )),
    ];

    extern_assets.iter().map(|&(res, ref fourcc, bytes)| {
        build_resource(res, ResourceKind::Unknown(Reader::new(bytes), fourcc.into()))
    }).collect()
}

// Assets not found in the base game
pub fn custom_assets<'r>(
    resources: &HashMap<(u32, FourCC),
    structs::Resource<'r>>,
    starting_memo: Option<&str>,
    pickup_hudmemos: &mut HashMap::<PickupHashKey, ResId<res_id::STRG>>,
    pickup_scans: &mut HashMap<PickupHashKey, (ResId<res_id::SCAN>, ResId<res_id::STRG>)>,
    extra_scans: &mut HashMap<PickupHashKey, (ResId<res_id::SCAN>, ResId<res_id::STRG>)>,
    config: &PatchConfig,
    version: Version,

)
->
    Result<
    (
        Vec<Resource<'r>>,
        Vec<ResId<res_id::SCAN>>,
        Vec<Vec<ResId<res_id::SCAN>>>,
        HashMap::<u32, u32>,
        HashMap<String, ExternPickupModel>,
    ),
    String>
{
    /*  List of all custom SCAN IDs which might be used throughout the game.
        We need to patch these into a SAVW file so that the game engine allocates enough space
        on initialization to store each individual scan's completion %. This first list is for
        scans which could appear in any world.
    */
    let mut global_savw_scans_to_add: Vec<ResId<res_id::SCAN>> = Vec::new();

    /* Per-world lists of scans that are garaunteed to only appear in said world.
       Index with World enum
    */
    let mut local_savw_scans_to_add: Vec<Vec<ResId<res_id::SCAN>>> = vec![
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
    ];

    /* Mapping of strings and their corresponding scan_id. Use this to avoid
       redundant usage of percious memory card space
    */
    let mut string_to_scan_strg: HashMap::<String, (ResId<res_id::SCAN>, ResId<res_id::STRG>)> = HashMap::new();

    /* Mapping of SCAN id to logbook category for easier SAVW entry creation */
    let mut savw_scan_logbook_category: HashMap::<u32, u32> = HashMap::new();

    // External assets
    let mut assets = extern_assets_compile_time();
    let extern_models = if config.extern_assets_dir.is_some() {
        let (more_assets, extern_models) = extern_assets_runtime(config.extern_assets_dir.clone())?;
        assets.extend_from_slice(&more_assets);
        extern_models // HashMap of extern models available for use
    } else {
        HashMap::<String, ExternPickupModel>::new() // empty hashmap (no models available)
    };
    // Custom pickup model assets
    assets.extend_from_slice(&create_nothing_icon_cmdl_and_ancs(
        resources,
        custom_asset_ids::NOTHING_CMDL,
        custom_asset_ids::NOTHING_ANCS,
        custom_asset_ids::NOTHING_TXTR,
        ResId::<res_id::TXTR>::new(0xF68DF7F1),
    ));
    assets.extend_from_slice(&create_suit_icon_cmdl_and_ancs(
        resources,
        custom_asset_ids::PHAZON_SUIT_CMDL,
        custom_asset_ids::PHAZON_SUIT_ANCS,
        custom_asset_ids::PHAZON_SUIT_TXTR1,
        custom_asset_ids::PHAZON_SUIT_TXTR2,
    ));
    assets.extend_from_slice(&create_visor_cmdl_and_ancs(
        resources,
        custom_asset_ids::THERMAL_CMDL,
        custom_asset_ids::THERMAL_ANCS,
        ResId::<res_id::TXTR>::new(0xFC095F6C),
    ));
    assets.extend_from_slice(&create_visor_cmdl_and_ancs(
        resources,
        custom_asset_ids::XRAY_CMDL,
        custom_asset_ids::XRAY_ANCS,
        ResId::<res_id::TXTR>::new(0xBE4CD99D),
    ));
    assets.extend_from_slice(&create_visor_cmdl_and_ancs(
        resources,
        custom_asset_ids::COMBAT_CMDL,
        custom_asset_ids::COMBAT_ANCS,
        ResId::<res_id::TXTR>::new(0x1D588B22),
    ));
    assets.extend_from_slice(&create_shiny_missile_assets(resources));
    assets.extend_from_slice(&create_item_scan_strg_pair(
        custom_asset_ids::SHORELINES_POI_SCAN,
        custom_asset_ids::SHORELINES_POI_STRG,
        "task failed successfully\0".to_string(),
        version,
    ));
    local_savw_scans_to_add[World::PhendranaDrifts as usize].push(custom_asset_ids::SHORELINES_POI_SCAN);
    assets.extend_from_slice(&create_item_scan_strg_pair_2(
        custom_asset_ids::CFLDG_POI_SCAN,
        custom_asset_ids::CFLDG_POI_STRG,
        vec![
            "Toaster's Champions: Awp82, DiggleWrath, Yeti2000, freak532486, AlphaRage, Csabi,\0".to_string(),
            "\0".to_string(),
            "BajaBlood, hammergoboom, Firemetroid, Lokir, MeriKatt, Cosmonawt, Haldadrin, RXM027\0".to_string(),
        ],
        1,
        0,
        version,
    ));
    local_savw_scans_to_add[World::TallonOverworld as usize].push(custom_asset_ids::CFLDG_POI_SCAN);
    assets.extend_from_slice(&create_item_scan_strg_pair_2(
        custom_asset_ids::TOURNEY_WINNERS_SCAN,
        custom_asset_ids::TOURNEY_WINNERS_STRG,
        vec![
            "Chozo script translated.\0".to_string(),
            "Racing\0".to_string(),
            "As we have done for millennia, we Chozo work constantly on our speed. Our fastest are our sentinels; They are, and have always been, repositories for our most precious secrets and strongest powers.\n\n2022 (CGC) - Cosmo + Cestrion\n2021 - Dinopony\n2020 - Interslice\n2019 - TheWeakestLink64\0".to_string(),
        ],
        1,
        0,
        version,
    ));
    local_savw_scans_to_add[World::TallonOverworld as usize].push(custom_asset_ids::TOURNEY_WINNERS_SCAN);

    if starting_memo.is_some() {
        assets.push(build_resource(
            custom_asset_ids::STARTING_ITEMS_HUDMEMO_STRG,
            structs::ResourceKind::Strg(structs::Strg::from_strings(vec![
                format!("&just=center;{}\0", starting_memo.clone().unwrap()),
            ])),
        ));
    }

    // Create fallback/default scan/scan-text/hudmemo assets //
    for pt in PickupType::iter() {
        let name: &str = pt.name();
        assets.extend_from_slice(&create_item_scan_strg_pair_2(
            pt.scan(),
            pt.scan_strg(),
            vec![format!("{}\0", name)],
            1,
            0,
            version,
        ));
        global_savw_scans_to_add.push(pt.scan());

        assets.push(build_resource(
            pt.hudmemo_strg(),
            structs::ResourceKind::Strg(structs::Strg::from_strings(vec![
                format!("&just=center;{} acquired!\0", name),
            ])),
        ));
    }

    // Create user-defined hudmemo and scan strings and map to locations //
    let mut custom_asset_offset = 0;
    for (level_name, level) in config.level_data.iter() {
        let world = World::from_json_key(level_name);
        for (room_name, room) in level.rooms.iter() {
            let mut pickup_idx = 0;
            let mut extra_scans_idx = 0;

            if room.extra_scans.is_some() {
                for custom_scan in room.extra_scans.as_ref().unwrap().iter() {
                    let contents = &custom_scan.text;

                    // Check if this string already has a scan_id //
                    if string_to_scan_strg.contains_key(contents) {
                        let (scan_id, strg_id) = string_to_scan_strg.get(contents).unwrap();

                        // Add this scan_id as a dep of this world if it wasn't already //
                        if !local_savw_scans_to_add[world as usize].contains(scan_id) {
                            local_savw_scans_to_add[world as usize].push(scan_id.clone());
                        }

                        let key = PickupHashKey::from_location(level_name, room_name, extra_scans_idx);
                        extra_scans.insert(key, (scan_id.clone(), strg_id.clone()));
                        extra_scans_idx = extra_scans_idx + 1;
                        continue;
                    }

                    // Get next 2 IDs //
                    let scan_id = ResId::<res_id::SCAN>::new(custom_asset_ids::EXTRA_IDS_START.to_u32() + custom_asset_offset);
                    custom_asset_offset = custom_asset_offset + 1;
                    let strg_id = ResId::<res_id::STRG>::new(custom_asset_ids::EXTRA_IDS_START.to_u32() + custom_asset_offset);
                    custom_asset_offset = custom_asset_offset + 1;

                    let is_red = {
                        if *custom_scan.is_red.as_ref().unwrap_or(&false) {
                            1
                        } else {
                            0
                        }
                    };

                    let mut strings: Vec<String> = vec![];
                    let mut contents = contents.to_string() + "\0";
                    let mut content_len = contents.len();

                    // "The &push;&main-color=#c300ff;Phazon Suit&pop; can be found in &push;&main-color=#89a1ff;Phazon Mines - Processing Center Access&pop;.",
                    // TODO: the game will actually crash if we paginate the color wrong
                    for x in contents.split("&") {
                        let semicolon_index = x.find(";").unwrap_or(0);
                        if semicolon_index != 0 {
                            content_len -= semicolon_index + 2;
                        }
                    }

                    let mut category = false;
                    const PAGINATION_SIZE: usize = 123;
                    while content_len > PAGINATION_SIZE {
                        let mut i = PAGINATION_SIZE - 1;
                        while contents.chars().nth(i).unwrap_or(' ') != ' ' {
                            i -= 1;
                        }

                        i += 1;

                        let page = (contents.clone().to_string())[..i].to_string();
                        strings.push(page + "\0");

                        contents = (contents.clone().to_string())[i..].to_string();
                        content_len -= i;

                        if !category {
                            strings.push("\0".to_string()); // logbook category
                            category = true;
                        }
                    }

                    if content_len > 0 {
                        strings.push(contents.clone() + "\0");
                    }

                    if !category {
                        strings.push("\0".to_string()); // logbook category
                    }

                    if custom_scan.logbook_title.is_some() || custom_scan.logbook_category.is_some() {
                        if !custom_scan.logbook_title.is_some() || !custom_scan.logbook_category.is_some() {
                            panic!("Both logbook title and logbook category are required.");
                        }
                        strings[1] = custom_scan.logbook_title.clone().unwrap() + "\0";
                        savw_scan_logbook_category.insert(scan_id.to_u32(), custom_scan.logbook_category.clone().unwrap());
                    }

                    assets.extend_from_slice(
                        &create_item_scan_strg_pair_2(
                        scan_id,
                        strg_id,
                        strings,
                        is_red,
                        *custom_scan.logbook_category.as_ref().unwrap_or(&0),
                        version,
                        )
                    );

                    // Map for easy lookup when patching //
                    let key = PickupHashKey::from_location(level_name, room_name, extra_scans_idx);
                    extra_scans.insert(key, (scan_id, strg_id));
                    local_savw_scans_to_add[world as usize].push(scan_id);

                    // Cache this scan/strg pair for re-use //
                    string_to_scan_strg.insert(contents, (scan_id, strg_id));

                    extra_scans_idx = extra_scans_idx + 1;
                }
            }

            if room.doors.is_some() {
                for (_, door) in room.doors.as_ref().unwrap().iter() {
                    if door.destination.is_none() { continue; }

                    let string = door.destination.as_ref().unwrap().room_name.clone() + "\0";

                    // Check if this string already has a scan_id //
                    if string_to_scan_strg.contains_key(&string.clone()) {
                        let (scan_id, strg_id) = string_to_scan_strg.get(&string.clone()).unwrap();

                        // Add this scan_id as a dep of this world if it wasn't already //
                        if !local_savw_scans_to_add[world as usize].contains(scan_id) {
                            local_savw_scans_to_add[world as usize].push(scan_id.clone());
                        }

                        let key = PickupHashKey::from_location(level_name, room_name, extra_scans_idx);
                        extra_scans.insert(key, (scan_id.clone(), strg_id.clone()));
                        extra_scans_idx = extra_scans_idx + 1;

                        continue;
                    }

                    // Get next 2 IDs //
                    let scan_id = ResId::<res_id::SCAN>::new(custom_asset_ids::EXTRA_IDS_START.to_u32() + custom_asset_offset);
                    custom_asset_offset = custom_asset_offset + 1;
                    let strg_id = ResId::<res_id::STRG>::new(custom_asset_ids::EXTRA_IDS_START.to_u32() + custom_asset_offset);
                    custom_asset_offset = custom_asset_offset + 1;

                    // Create scan/strg pair for destination
                    assets.extend_from_slice(&create_item_scan_strg_pair(
                        scan_id,
                        strg_id,
                        string.clone(),
                        version,
                    ));
                    local_savw_scans_to_add[world as usize].push(scan_id);

                    // Map for easy lookup when patching //
                    let key = PickupHashKey::from_location(level_name, room_name, extra_scans_idx);
                    extra_scans.insert(key, (scan_id, strg_id));

                    // Cache this scan/strg pair for re-use //
                    string_to_scan_strg.insert(string.clone(), (scan_id, strg_id));

                    extra_scans_idx = extra_scans_idx + 1;
                }
            }

            if room.pickups.is_none() { continue };
            for pickup in room.pickups.as_ref().unwrap().iter() {
                // custom hudmemo string
                if pickup.hudmemo_text.is_some()
                {
                    let hudmemo_text = pickup.hudmemo_text.as_ref().unwrap();

                    // Get next ID //
                    let strg_id = ResId::<res_id::STRG>::new(custom_asset_ids::EXTRA_IDS_START.to_u32() + custom_asset_offset);
                    custom_asset_offset = custom_asset_offset + 1;

                    // Build resource //
                    let strg = structs::ResourceKind::Strg(structs::Strg {
                        string_tables: vec![
                            structs::StrgStringTable {
                                lang: b"ENGL".into(),
                                strings: vec![format!("&just=center;{}\u{0}",
                                                        hudmemo_text).into()].into(),
                            },
                        ].into(),
                    });
                    let resource = build_resource(strg_id, strg);
                    assets.push(resource);

                    // Map for easy lookup when patching //
                    let key = PickupHashKey::from_location(level_name, room_name, pickup_idx);
                    pickup_hudmemos.insert(key, strg_id);
                }

                // Custom scan string
                if pickup.scan_text.is_some()
                {
                    let scan_text = pickup.scan_text.as_ref().unwrap();

                    // Check if this string already has a scan_id //
                    if string_to_scan_strg.contains_key(scan_text) {
                        let (scan_id, strg_id) = string_to_scan_strg.get(scan_text).unwrap();

                        // Add this scan_id as a dep of this world if it wasn't already //
                        if !local_savw_scans_to_add[world as usize].contains(scan_id) {
                            local_savw_scans_to_add[world as usize].push(scan_id.clone());
                        }

                        // Map for easy lookup when patching //
                        let key = PickupHashKey::from_location(level_name, room_name, pickup_idx);
                        pickup_scans.insert(key, (*scan_id, *strg_id));
                    }
                    else
                    {
                        // Get next 2 IDs //
                        let scan_id = ResId::<res_id::SCAN>::new(custom_asset_ids::EXTRA_IDS_START.to_u32() + custom_asset_offset);
                        custom_asset_offset = custom_asset_offset + 1;
                        let strg_id = ResId::<res_id::STRG>::new(custom_asset_ids::EXTRA_IDS_START.to_u32() + custom_asset_offset);
                        custom_asset_offset = custom_asset_offset + 1;

                        // Build resource //
                        if room_name.trim().to_lowercase() == "research core" // make the research core scan red because it goes on the terminal
                        {
                            assets.extend_from_slice(&create_item_scan_strg_pair_2(
                                scan_id,
                                strg_id,
                                vec![format!("{}\0", scan_text)],
                                1,
                                0,
                                version,
                            ));
                        }
                        else
                        {
                            assets.extend_from_slice(&create_item_scan_strg_pair(
                                scan_id,
                                strg_id,
                                format!("{}\0", scan_text),
                                version,
                            ));
                        }

                        // Map for easy lookup when patching //
                        let key = PickupHashKey::from_location(level_name, room_name, pickup_idx);
                        pickup_scans.insert(key, (scan_id, strg_id));
                        local_savw_scans_to_add[world as usize].push(scan_id);

                        // Cache this scan/strg pair for re-use //
                        string_to_scan_strg.insert(scan_text.to_string(), (scan_id, strg_id));
                    }
                }

                pickup_idx = pickup_idx + 1;
            }
        }
    }

    // Warping to starting area
    assets.push(build_resource(
        custom_asset_ids::WARPING_TO_START_STRG,
        structs::ResourceKind::Strg(structs::Strg::from_strings(vec![
            "&just=center;Returning to starting room...\0".to_string().to_owned(),
        ])),
    ));

    assets.push(build_resource(
        custom_asset_ids::GENERIC_WARP_STRG,
        structs::ResourceKind::Strg(structs::Strg::from_strings(vec![
            "&just=center;Warping...\0".to_string().to_owned(),
        ])),
    ));

    let mut warp_to_start_delay_s = config.warp_to_start_delay_s;
    if warp_to_start_delay_s < 3.0 {
        warp_to_start_delay_s = 3.0
    }
    assets.push(build_resource(
        custom_asset_ids::WARPING_TO_START_DELAY_STRG,
        structs::ResourceKind::Strg(structs::Strg::from_strings(vec![
            format!("&just=center;Warping in {}s...\0", warp_to_start_delay_s as u32).to_owned(),
        ])),
    ));
    assets.push(build_resource(
        custom_asset_ids::WARPING_TO_OTHER_STRG,
        structs::ResourceKind::Strg(structs::Strg::from_strings(vec![
            format!("&just=center;Warping in 6s...\0").to_owned(),
        ])),
    ));

    // Custom block asset
    for gt in GenericTexture::iter() {
        assets.push(
            create_custom_block_cmdl(
                resources,
                gt.txtr(),
                gt.cmdl(),
            )
        );
    }

    // Custom door assets
    for door_type in DoorType::iter() {
        if door_type.shield_cmdl().to_u32() >= 0xDEAF0000 && door_type.shield_cmdl().to_u32() <= custom_asset_ids::EXTRA_IDS_START.to_u32() + 50 { // only if it doesn't exist in-game already
            assets.push(create_custom_door_cmdl(resources, door_type));

            if door_type.scan() != ResId::invalid() || door_type.strg() != ResId::invalid() {
                if door_type.scan() == ResId::invalid() || door_type.strg() == ResId::invalid() {
                    panic!("strg/scan do not make a pair");
                }

                if global_savw_scans_to_add.contains(&door_type.scan()) {
                    continue; // Duplicate scan point
                }

                assets.extend_from_slice(
                    &create_item_scan_strg_pair_2(
                        door_type.scan(),
                        door_type.strg(),
                        door_type.scan_text(),
                        1,
                        0,
                        version,
                    )
                );
                global_savw_scans_to_add.push(door_type.scan());
            }
        }
    }

    // Custom blast shield assets
    for blast_shield in BlastShieldType::iter() {
        if blast_shield.cmdl().to_u32() >= 0xDEAF0000 && blast_shield.cmdl().to_u32() <= custom_asset_ids::EXTRA_IDS_START.to_u32() + 50 { // only if it doesn't exist in-game already
            assets.push(create_custom_blast_shield_cmdl(resources, blast_shield));

            if blast_shield.scan() != ResId::invalid() || blast_shield.strg() != ResId::invalid() {
                if blast_shield.scan() == ResId::invalid() || blast_shield.strg() == ResId::invalid() {
                    panic!("strg/scan do not make a pair");
                }

                if global_savw_scans_to_add.contains(&blast_shield.scan()) {
                    continue; // Duplicate scan point
                }

                assets.extend_from_slice(
                    &create_item_scan_strg_pair_2(
                        blast_shield.scan(),
                        blast_shield.strg(),
                        blast_shield.scan_text(),
                        1,
                        0,
                        version,
                    )
                );
                global_savw_scans_to_add.push(blast_shield.scan());
            }
        } else {
            // If vanilla CMDL, then it can't depend on custom textures
            assert!(
                blast_shield.dependencies()
                .iter()
                .find(|d| d.0 >= 0xDEAF0000 && d.0 <= custom_asset_ids::EXTRA_IDS_START.to_u32() + 50)
                .is_none()
            );
        }
    }

    /* Set 0 as the default logbook category */
    for scan_id in global_savw_scans_to_add.iter() {
        if savw_scan_logbook_category.contains_key(&scan_id.to_u32()) {
            continue;
        }

        savw_scan_logbook_category.insert(scan_id.to_u32(), 0);
    }

    for world_savws in local_savw_scans_to_add.iter() {
        for scan_id in world_savws {
            if savw_scan_logbook_category.contains_key(&scan_id.to_u32()) {
                continue;
            }

            savw_scan_logbook_category.insert(scan_id.to_u32(), 0);
        }
    }


    Ok((assets, global_savw_scans_to_add, local_savw_scans_to_add, savw_scan_logbook_category, extern_models))
}

// When modifying resources in an MREA, we need to give the room a copy of the resources/
// assests used. Create a cache of all the resources needed by any pickup, door, etc...
pub fn collect_game_resources<'r>(
    gc_disc: &structs::GcDisc<'r>,
    starting_memo: Option<&str>,
    config: &PatchConfig,
    version: Version,
)
    ->
    Result<
    (
        HashMap<(u32, FourCC), structs::Resource<'r>>,
        HashMap<PickupHashKey, ResId<res_id::STRG>>,
        HashMap<PickupHashKey, (ResId<res_id::SCAN>, ResId<res_id::STRG>)>,
        HashMap<PickupHashKey, (ResId<res_id::SCAN>, ResId<res_id::STRG>)>,
        Vec<ResId<res_id::SCAN>>,
        Vec<Vec<ResId<res_id::SCAN>>>,
        HashMap::<u32, u32>,
        HashMap<String, ExternPickupModel>,
    ),
    String>
{
    // Get list of all dependencies patcher needs //
    let mut looking_for = HashSet::<_>::new();
    looking_for.extend(PickupModel::iter().flat_map(|x| x.dependencies().iter().cloned()));
    looking_for.extend(DoorType::iter().flat_map(|x| x.dependencies()));
    looking_for.extend(BlastShieldType::iter().flat_map(|x| x.dependencies()));
    looking_for.extend(GenericTexture::iter().flat_map(|x| x.dependencies()));
    looking_for.extend(WaterType::iter().flat_map(|x| x.dependencies()));

    let platform_deps: Vec<(u32,FourCC)> = vec![
        (0x48DF38A3, FourCC::from_bytes(b"CMDL")),
        (0xB2D50628, FourCC::from_bytes(b"DCLN")),
        (0x19C17D5C, FourCC::from_bytes(b"TXTR")),
        (0x0259F5F6, FourCC::from_bytes(b"TXTR")),
        (0x71190250, FourCC::from_bytes(b"TXTR")),
        (0xD0BA0FA8, FourCC::from_bytes(b"TXTR")),
        (0xF1478D6A, FourCC::from_bytes(b"TXTR")),
    ];
    looking_for.extend(platform_deps);

    let platform_deps: Vec<(u32,FourCC)> = vec![
        (0x27D0663B, FourCC::from_bytes(b"CMDL")), // actually the block model but I'm lazy
        (0xDCDFD386, FourCC::from_bytes(b"CMDL")),
        (0x6D412D11, FourCC::from_bytes(b"DCLN")),
        (0xEED972E7, FourCC::from_bytes(b"TXTR")),
        (0xF1478D6A, FourCC::from_bytes(b"TXTR")),
        (0xF89D34EF, FourCC::from_bytes(b"TXTR")),
    ];
    looking_for.extend(platform_deps);

    let glow_ring: Vec<(u32,FourCC)> = vec![ // mapstation_beams.CMDL
        (0x12771AF0, FourCC::from_bytes(b"CMDL")),
        (0xA6114429, FourCC::from_bytes(b"TXTR")),
    ];
    looking_for.extend(glow_ring);

    let orange_light: Vec<(u32,FourCC)> = vec![
        (0xB4A658C3, FourCC::from_bytes(b"PART")),
    ];
    looking_for.extend(orange_light);

    let ghost_ball: Vec<(u32,FourCC)> = vec![ // used for lock on point model
        (0xBFE4DAA0, FourCC::from_bytes(b"CMDL")),
        (0x57C7107D, FourCC::from_bytes(b"TXTR")),
        (0xE580D665, FourCC::from_bytes(b"TXTR")),
    ];
    looking_for.extend(ghost_ball);

    let custom_scan_point_deps: Vec<(u32, FourCC)> = vec![
        (0xDCEC3E77, FourCC::from_bytes(b"FRME")),
        (0x98DAB29C, FourCC::from_bytes(b"ANCS")),
        (0x2A0FA4F9, FourCC::from_bytes(b"CMDL")),
        (0x336B78E8, FourCC::from_bytes(b"TXTR")),
        (0x41200B2F, FourCC::from_bytes(b"CSKR")),
        (0xE436418D, FourCC::from_bytes(b"CINF")),
        (0xA1ED00B6, FourCC::from_bytes(b"ANIM")),
        (0xA7DDBDC4, FourCC::from_bytes(b"EVNT")),

        (0x3abe45a6, FourCC::from_bytes(b"SCAN")),
        (0x191a6881, FourCC::from_bytes(b"STRG")),
        (0x748c37a5, FourCC::from_bytes(b"SCAN")),
        (0x50ac3b9a, FourCC::from_bytes(b"STRG")),
        (0xA482DBD1, FourCC::from_bytes(b"TXTR")),
        (0xC9A36445, FourCC::from_bytes(b"TXTR")),
        (0x2702E5E0, FourCC::from_bytes(b"TXTR")),
        (0x34E79314, FourCC::from_bytes(b"TXTR")),
        (0x46434ED3, FourCC::from_bytes(b"TXTR")),
        (0x4F944876, FourCC::from_bytes(b"TXTR")),
    ];
    looking_for.extend(custom_scan_point_deps);

    // Dependencies read from paks and custom assets will go here //
    let mut found = HashMap::with_capacity(looking_for.len());

    // Iterate through every level Pak //
    for pak_name in pickup_meta::ROOM_INFO.iter().map(|(name, _)| name) {
        let file_entry = gc_disc.find_file(pak_name).unwrap();
        let pak = match *file_entry.file().unwrap() {
            structs::FstEntryFile::Pak(ref pak) => Cow::Borrowed(pak),
            structs::FstEntryFile::Unknown(ref reader) => Cow::Owned(reader.clone().read(())),
            _ => panic!(),
        };

        // Iterate through all resources in level Pak //
        for res in pak.resources.iter() {
            // If this resource is a dependency needed by the patcher, add the resource to the output list //
            let key = (res.file_id, res.fourcc());
            if looking_for.remove(&key) {
                found.insert(key, res.into_owned());
            }
        }
    }

    // Maps pickup location to STRG to use
    let mut pickup_hudmemos = HashMap::<PickupHashKey, ResId<res_id::STRG>>::new();
    let mut pickup_scans = HashMap::<PickupHashKey, (ResId<res_id::SCAN>, ResId<res_id::STRG>)>::new();
    let mut extra_scans = HashMap::<PickupHashKey, (ResId<res_id::SCAN>, ResId<res_id::STRG>)>::new();

    // Remove extra assets from dependency search since they won't appear     //
    // in any pak. Instead add them to the output resource pool. These assets //
    // are provided as external files checked into the repository.            //
    let (custom_assets, global_savw_scans_to_add, local_savw_scans_to_add, savw_scan_logbook_category, extern_models) = custom_assets(&found, starting_memo, &mut pickup_hudmemos, &mut pickup_scans, &mut extra_scans, config, version)?;
    for res in custom_assets {
        let key = (res.file_id, res.fourcc());
        looking_for.remove(&key);
        found.insert(key, res);
    }

    if !looking_for.is_empty() {
        panic!("error - still looking for {:?}", looking_for);
    }

    Ok((found, pickup_hudmemos, pickup_scans, extra_scans, global_savw_scans_to_add, local_savw_scans_to_add, savw_scan_logbook_category, extern_models))
}

fn create_custom_block_cmdl<'r>(
    resources: &HashMap<(u32, FourCC),
    structs::Resource<'r>>,
    txtr_id: ResId::<res_id::TXTR>,
    new_cmdl_id: ResId::<res_id::CMDL>,
) -> structs::Resource<'r>
{
    // Find and read the vanilla block cmdl
    let old_cmdl = ResourceData::new(&resources[&resource_info!("27D0663B.CMDL").into()]);

    // Create a copy
    let old_cmdl_bytes = old_cmdl.decompress().into_owned();
    let mut new_cmdl = Reader::new(&old_cmdl_bytes[..]).read::<structs::Cmdl>(());

    // Modify the new CMDL to use custom textures
    new_cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[0] = txtr_id;

    // Re-serialize the CMDL
    let mut new_cmdl_bytes = vec![];
    new_cmdl.write_to(&mut new_cmdl_bytes).unwrap();

    // Pad length to multiple of 32 bytes
    new_cmdl_bytes.extend(reader_writer::pad_bytes(32, new_cmdl_bytes.len()).iter());

    // Return resource
    build_resource(
        new_cmdl_id,
        structs::ResourceKind::External(new_cmdl_bytes, b"CMDL".into())
    )
}

fn create_custom_blast_shield_cmdl<'r>(
    resources: &HashMap<(u32, FourCC),
    structs::Resource<'r>>,
    blast_shield_type: BlastShieldType,
) -> structs::Resource<'r>
{
    // Find and read the vanilla blast shield cmdl
    let old_cmdl = ResourceData::new(&resources[&resource_info!("EFDFFB8C.CMDL").into()]);

    // Create a copy
    let old_cmdl_bytes = old_cmdl.decompress().into_owned();
    let mut new_cmdl = Reader::new(&old_cmdl_bytes[..]).read::<structs::Cmdl>(());

    // Modify the new CMDL to use custom textures
    new_cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[0] = blast_shield_type.glow_border_txtr();
    new_cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[1] = blast_shield_type.glow_trim_txtr();
    new_cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[2] = blast_shield_type.metal_body_txtr();
    new_cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[3] = blast_shield_type.animated_glow_txtr();
    new_cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[4] = blast_shield_type.metal_trim_txtr();

    // Re-serialize the CMDL
    let mut new_cmdl_bytes = vec![];
    new_cmdl.write_to(&mut new_cmdl_bytes).unwrap();

    // Pad length to multiple of 32 bytes
    new_cmdl_bytes.extend(reader_writer::pad_bytes(32, new_cmdl_bytes.len()).iter());

    // Return resource
    build_resource(
        blast_shield_type.cmdl(),
        structs::ResourceKind::External(new_cmdl_bytes, b"CMDL".into())
    )
}

fn create_custom_door_cmdl<'r>(
    resources: &HashMap<(u32, FourCC),
    structs::Resource<'r>>,
    door_type: DoorType,
) -> structs::Resource<'r>
{
    let new_cmdl_id: ResId<res_id::CMDL> = door_type.shield_cmdl();
    let new_txtr_id: ResId<res_id::TXTR> = door_type.holorim_texture();

    let new_door_cmdl = {
        // Find and read the blue door CMDL
        let blue_door_cmdl = {
            if door_type.is_vertical() {
                ResourceData::new(&resources[&resource_info!("18D0AEE6.CMDL").into()]) // actually white door but who cares
            } else {
                ResourceData::new(&resources[&resource_info!("blueShield_v1.CMDL").into()])
            }
        };

        // Deserialize the blue door CMDL into a new mutable CMDL
        let blue_door_cmdl_bytes = blue_door_cmdl.decompress().into_owned();
        let mut new_cmdl = Reader::new(&blue_door_cmdl_bytes[..]).read::<structs::Cmdl>(());

        // Modify the new CMDL to make it unique
        new_cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[0] = new_txtr_id;

        // Re-serialize the CMDL //
        let mut new_cmdl_bytes = vec![];
        new_cmdl.write_to(&mut new_cmdl_bytes).unwrap();

        // Pad length to multiple of 32 bytes //
        let len = new_cmdl_bytes.len();
        new_cmdl_bytes.extend(reader_writer::pad_bytes(32, len).iter());

        // Assemble into a proper resource object
        crate::custom_assets::build_resource(
            new_cmdl_id, // Custom ids start with 0xDEAFxxxx
            structs::ResourceKind::External(new_cmdl_bytes, b"CMDL".into())
        )
    };

    new_door_cmdl
}

fn create_nothing_icon_cmdl_and_ancs<'r>(
    resources: &HashMap<(u32, FourCC), structs::Resource<'r>>,
    new_cmdl_id: ResId<res_id::CMDL>,
    new_ancs_id: ResId<res_id::ANCS>,
    new_txtr1: ResId<res_id::TXTR>,
    _new_txtr2: ResId<res_id::TXTR>,
) -> [structs::Resource<'r>; 2]
{
    let new_suit_cmdl = {
        let grav_suit_cmdl = ResourceData::new(
            &resources[&resource_info!("Metroid.CMDL").into()]
        );
        let cmdl_bytes = grav_suit_cmdl.decompress().into_owned();
        let mut cmdl: structs::Cmdl = Reader::new(&cmdl_bytes[..]).read::<structs::Cmdl>(());

        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[0] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[1] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[2] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[3] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[4] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[5] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[6] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[7] = new_txtr1;

        let mut new_cmdl_bytes = vec![];
        cmdl.write_to(&mut new_cmdl_bytes).unwrap();

        build_resource(
            new_cmdl_id,
            structs::ResourceKind::External(new_cmdl_bytes, b"CMDL".into())
        )
    };
    let new_suit_ancs = {
        let grav_suit_ancs = ResourceData::new(
            &resources[&resource_info!("Node1_11.ANCS").into()]
        );
        let ancs_bytes = grav_suit_ancs.decompress().into_owned();
        let mut ancs = Reader::new(&ancs_bytes[..]).read::<structs::Ancs>(());

        ancs.char_set.char_info.as_mut_vec()[0].cmdl = new_cmdl_id;

        let mut new_ancs_bytes = vec![];
        ancs.write_to(&mut new_ancs_bytes).unwrap();

        build_resource(
            new_ancs_id,
            structs::ResourceKind::External(new_ancs_bytes, b"ANCS".into())
        )
    };
    [new_suit_cmdl, new_suit_ancs]
}

fn create_visor_cmdl_and_ancs<'r>(
    resources: &HashMap<(u32, FourCC), structs::Resource<'r>>,
    new_cmdl_id: ResId<res_id::CMDL>,
    new_ancs_id: ResId<res_id::ANCS>,
    new_txtr: ResId<res_id::TXTR>,
) -> [structs::Resource<'r>; 2]
{
    let new_cmdl = {
        let old_cmdl = ResourceData::new(
            &resources[&resource_info!("Node1_39_1.CMDL").into()]
        );
        let cmdl_bytes = old_cmdl.decompress().into_owned();
        let mut cmdl = Reader::new(&cmdl_bytes[..]).read::<structs::Cmdl>(());

        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[0] = new_txtr;

        let mut new_cmdl_bytes = vec![];
        cmdl.write_to(&mut new_cmdl_bytes).unwrap();

        build_resource(
            new_cmdl_id,
            structs::ResourceKind::External(new_cmdl_bytes, b"CMDL".into())
        )
    };
    let new_ancs = {
        let old_ancs = ResourceData::new(
            &resources[&resource_info!("Node1_39_1.ANCS").into()]
        );
        let ancs_bytes = old_ancs.decompress().into_owned();
        let mut ancs = Reader::new(&ancs_bytes[..]).read::<structs::Ancs>(());

        ancs.char_set.char_info.as_mut_vec()[0].cmdl = new_cmdl_id;

        let mut new_ancs_bytes = vec![];
        ancs.write_to(&mut new_ancs_bytes).unwrap();

        build_resource(
            new_ancs_id,
            structs::ResourceKind::External(new_ancs_bytes, b"ANCS".into())
        )
    };
    [new_cmdl, new_ancs]
}

fn create_suit_icon_cmdl_and_ancs<'r>(
    resources: &HashMap<(u32, FourCC), structs::Resource<'r>>,
    new_cmdl_id: ResId<res_id::CMDL>,
    new_ancs_id: ResId<res_id::ANCS>,
    new_txtr1: ResId<res_id::TXTR>,
    new_txtr2: ResId<res_id::TXTR>,
) -> [structs::Resource<'r>; 2]
{
    let new_suit_cmdl = {
        let grav_suit_cmdl = ResourceData::new(
            &resources[&resource_info!("Node1_11.CMDL").into()]
        );
        let cmdl_bytes = grav_suit_cmdl.decompress().into_owned();
        let mut cmdl = Reader::new(&cmdl_bytes[..]).read::<structs::Cmdl>(());

        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[0] = new_txtr1;
        cmdl.material_sets.as_mut_vec()[0].texture_ids.as_mut_vec()[3] = new_txtr2;

        let mut new_cmdl_bytes = vec![];
        cmdl.write_to(&mut new_cmdl_bytes).unwrap();

        build_resource(
            new_cmdl_id,
            structs::ResourceKind::External(new_cmdl_bytes, b"CMDL".into())
        )
    };
    let new_suit_ancs = {
        let grav_suit_ancs = ResourceData::new(
            &resources[&resource_info!("Node1_11.ANCS").into()]
        );
        let ancs_bytes = grav_suit_ancs.decompress().into_owned();
        let mut ancs = Reader::new(&ancs_bytes[..]).read::<structs::Ancs>(());

        ancs.char_set.char_info.as_mut_vec()[0].cmdl = new_cmdl_id;

        let mut new_ancs_bytes = vec![];
        ancs.write_to(&mut new_ancs_bytes).unwrap();

        build_resource(
            new_ancs_id,
            structs::ResourceKind::External(new_ancs_bytes, b"ANCS".into())
        )
    };
    [new_suit_cmdl, new_suit_ancs]
}

fn create_shiny_missile_assets<'r>(
    resources: &HashMap<(u32, FourCC), structs::Resource<'r>>,
) -> [structs::Resource<'r>; 4]
{
    let shiny_missile_cmdl = {
        let shiny_missile_cmdl = ResourceData::new(
            &resources[&resource_info!("Node1_36_0.CMDL").into()]
        );
        let cmdl_bytes = shiny_missile_cmdl.decompress().into_owned();
        let mut cmdl = Reader::new(&cmdl_bytes[..]).read::<structs::Cmdl>(());

        cmdl.material_sets.as_mut_vec()[0].texture_ids = vec![
            custom_asset_ids::SHINY_MISSILE_TXTR0,
            custom_asset_ids::SHINY_MISSILE_TXTR1,
            custom_asset_ids::SHINY_MISSILE_TXTR2,
        ].into();

        let mut new_cmdl_bytes = vec![];
        cmdl.write_to(&mut new_cmdl_bytes).unwrap();

        build_resource(
            custom_asset_ids::SHINY_MISSILE_CMDL,
            structs::ResourceKind::External(new_cmdl_bytes, b"CMDL".into())
        )
    };
    let shiny_missile_ancs = {
        let shiny_missile_ancs = ResourceData::new(
            &resources[&resource_info!("Node1_37_0.ANCS").into()]
        );
        let ancs_bytes = shiny_missile_ancs.decompress().into_owned();
        let mut ancs = Reader::new(&ancs_bytes[..]).read::<structs::Ancs>(());

        ancs.char_set.char_info.as_mut_vec()[0].cmdl = custom_asset_ids::SHINY_MISSILE_CMDL;
        ancs.char_set.char_info.as_mut_vec()[0].particles.part_assets = vec![
            resource_info!("healthnew.PART").res_id
        ].into();
        if let Some(animation_resources) = &mut ancs.anim_set.animation_resources {
            animation_resources.as_mut_vec()[0].evnt = custom_asset_ids::SHINY_MISSILE_EVNT;
            animation_resources.as_mut_vec()[0].anim = custom_asset_ids::SHINY_MISSILE_ANIM;
        }

        match &mut ancs.anim_set.animations.as_mut_vec()[..] {
            [structs::Animation { meta: structs::MetaAnimation::Play(play), .. }] => {
                play.get_mut().anim = custom_asset_ids::SHINY_MISSILE_ANIM;
            },
            _ => panic!(),
        }

        let mut new_ancs_bytes = vec![];
        ancs.write_to(&mut new_ancs_bytes).unwrap();

        build_resource(
            custom_asset_ids::SHINY_MISSILE_ANCS,
            structs::ResourceKind::External(new_ancs_bytes, b"ANCS".into())
        )
    };
    let shiny_missile_evnt = {
        let mut evnt = resources[&resource_info!("Missile_Launcher_ready.EVNT").into()]
            .kind.as_evnt()
            .unwrap().into_owned();


        evnt.effect_events.as_mut_vec()[0].effect_file_id = resource_info!("healthnew.PART").res_id;
        evnt.effect_events.as_mut_vec()[1].effect_file_id = resource_info!("healthnew.PART").res_id;

        build_resource(
            custom_asset_ids::SHINY_MISSILE_EVNT,
            structs::ResourceKind::Evnt(evnt)
        )
    };
    let shiny_missile_anim = {
        let shiny_missile_anim = ResourceData::new(
            &resources[&resource_info!("Missile_Launcher_ready.ANIM").into()]
        );
        let mut anim_bytes = shiny_missile_anim.decompress().into_owned();
        custom_asset_ids::SHINY_MISSILE_EVNT.write_to(&mut std::io::Cursor::new(&mut anim_bytes[8..])).unwrap();
        build_resource(
            custom_asset_ids::SHINY_MISSILE_ANIM,
            structs::ResourceKind::External(anim_bytes, b"ANIM".into())
        )
    };
    [shiny_missile_cmdl, shiny_missile_ancs, shiny_missile_evnt, shiny_missile_anim]
}

fn create_item_scan_strg_pair<'r>(
    new_scan: ResId<res_id::SCAN>,
    new_strg: ResId<res_id::STRG>,
    contents: String,
    version: Version,
) -> [structs::Resource<'r>; 2]
{
    create_item_scan_strg_pair_2(new_scan, new_strg, vec![contents], 0, 0, version)
}

fn create_item_scan_strg_pair_2<'r>(
    new_scan: ResId<res_id::SCAN>,
    new_strg: ResId<res_id::STRG>,
    contents: Vec<String>,
    is_important: u8,
    logbook_category: u32,
    version: Version,
) -> [structs::Resource<'r>; 2]
{
    let scan = build_resource(
        new_scan,
        structs::ResourceKind::Scan(structs::Scan {
            frme: ResId::<res_id::FRME>::new(0xDCEC3E77),
            strg: new_strg,
            scan_speed: 0,
            category: logbook_category,
            icon_flag: is_important,
            images: [
                structs::ScanImage {
                    txtr: ResId::invalid(),
                    appearance_percent: 0.25,
                    image_position: 0xFFFFFFFF,
                    width: 0,
                    height: 0,
                    interval: 0.0,
                    fade_duration: 0.0,
                },
                structs::ScanImage {
                    txtr: ResId::invalid(),
                    appearance_percent: 0.50,
                    image_position: 0xFFFFFFFF,
                    width: 0,
                    height: 0,
                    interval: 0.0,
                    fade_duration: 0.0,
                },
                structs::ScanImage {
                    txtr: ResId::invalid(),
                    appearance_percent: 0.75,
                    image_position: 0xFFFFFFFF,
                    width: 0,
                    height: 0,
                    interval: 0.0,
                    fade_duration: 0.0,
                },
                structs::ScanImage {
                    txtr: ResId::invalid(),
                    appearance_percent: 1.0,
                    image_position: 0xFFFFFFFF,
                    width: 0,
                    height: 0,
                    interval: 0.0,
                    fade_duration: 0.0,
                },
            ].into(),
            padding: [255; 23].into(),
            _dummy: std::marker::PhantomData,
        }),
    );

    let kind = if version == Version::Pal {
        structs::ResourceKind::Strg(structs::Strg::from_strings_pal(contents))
    } else {
        structs::ResourceKind::Strg(structs::Strg::from_strings(contents))
    };

    let strg = build_resource(
        new_strg,
        kind,
    );

    [scan, strg]
}
