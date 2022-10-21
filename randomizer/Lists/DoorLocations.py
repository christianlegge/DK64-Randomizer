"""Stores the data for each potential T&S and Wrinkly door location."""
from randomizer.Enums.Events import Events
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Time import Time
from randomizer.Enums.Kongs import Kongs
from randomizer.Logic import Regions as RegionList
from randomizer.LogicClasses import TransitionFront


class DoorData:
    """Stores information about a door location."""

    def __init__(
        self,
        *,
        name="",
        map=0,
        logicregion="",
        location=[0, 0, 0, 0],
        rx=0,
        rz=0,
        scale=1,
        kong_lst=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
        group = 0,
        moveless = True,
        logic=lambda l: True, 
        placed="none",
        door_type="both",
    ):
        """Initialize with provided data."""
        self.name = name
        self.map = map
        self.logicregion = logicregion
        self.location = location
        self.rx = rx
        self.rz = rz
        self.scale = scale
        self.kongs = kong_lst
        self.group = group # groups door locations to ensure troff n scoff portals don't generate right next to each other
        self.moveless = moveless # moveless means that a door location can be accessed without any moves (except vines for in Aztec)
        self.logic = logic
        self.placed = placed
        self.default_placed = placed # info about what door_type a door location is in vanilla
        self.door_type = door_type  # denotes whether it can be tns, wrinkly or both
        self.assigned_kong = None

    def assignDoor(self, kong):
        """Assign door to kong."""
        self.placed = "wrinkly"
        self.assigned_kong = kong

    def assignPortal(self):
        """Assign T&S Portal to slot."""
        self.placed = "tns"
        portal_region = RegionList[self.logicregion]
        boss_region_id = GetBossLobbyRegionIdForRegion(self.logicregion, portal_region)
        portal_region.exits.append(TransitionFront(boss_region_id, lambda l: self.logic))


def GetBossLobbyRegionIdForRegion(region_id, region):
    """Return the region id of the boss lobby the given region id and Region object should take you to."""
    if region_id == Regions.JungleJapesLobby or region.level == Levels.JungleJapes:
        return Regions.JapesBossLobby
    elif region_id == Regions.AngryAztecLobby or region.level == Levels.AngryAztec:
        return Regions.AztecBossLobby
    elif region_id == Regions.FranticFactoryLobby or region.level == Levels.FranticFactory:
        return Regions.FactoryBossLobby
    elif region_id == Regions.GloomyGalleonLobby or region.level == Levels.GloomyGalleon:
        return Regions.GalleonBossLobby
    elif region_id == Regions.FungiForestLobby or region.level == Levels.FungiForest:
        return Regions.ForestBossLobby
    elif region_id == Regions.CrystalCavesLobby or region.level == Levels.CrystalCaves:
        return Regions.CavesBossLobby
    elif region_id == Regions.CreepyCastleLobby or region.level == Levels.CreepyCastle:
        return Regions.CastleBossLobby
    else:
        return None


door_locations = {
    Levels.JungleJapes: [
        DoorData(name="Jungle Japes: Lobby - Middle Right", map=Maps.JungleJapesLobby, logicregion=Regions.JungleJapesLobby, location=[169.075, 10.833, 594.613, 90.0], group=1, logic=lambda l: True, placed="wrinkly"),  # DK Door
        DoorData(name="Jungle Japes: Lobby - Far Left", map=Maps.JungleJapesLobby, logicregion=Regions.JungleJapesLobby, location=[647.565, 0.0, 791.912, 183.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Diddy Door
        DoorData(name="Jungle Japes: Lobby - Close Right", map=Maps.JungleJapesLobby, logicregion=Regions.JungleJapesLobby, location=[156.565, 10.833, 494.73, 98.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Lanky Door
        DoorData(name="Jungle Japes: Lobby - Far Right", map=Maps.JungleJapesLobby, logicregion=Regions.JungleJapesLobby, location=[252.558, 0.0, 760.733, 163.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Tiny Door
        DoorData(name="Jungle Japes: Lobby - Close Left", map=Maps.JungleJapesLobby, logicregion=Regions.JungleJapesLobby, location=[821.85, 0.0, 615.167, 264.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Chunky Door
        DoorData(name="Jungle Japes: Diddy Cave", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondPeanutGate, location=[2489.96, 280.0, 736.892, 179.0], group=2, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Door in Diddy Cave
        # DoorData(name="Jungle Japes: Near Painting Room", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[722.473, 538.0, 2386.608, 141.0], group=3, moveless=False, logic=lambda l: l.vines, placed="tns"),  # T&S Door in Near Painting Room. Omitted because the indicator is weird
        DoorData(name="Jungle Japes: Fairy Cave", map=Maps.JungleJapes, logicregion=Regions.BeyondRambiGate, location=[901.203, 279.0, 3795.889, 202.0], group=4, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Door in Fairy Cave
        DoorData(name="Jungle Japes: Next to Diddy Cage - right", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[896.0, 852.0, 2427.0, 90.75], group=5, logic=lambda l: True),
        DoorData(name="Jungle Japes: Alcove Above Diddy Tunnel - right", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[703.0, 538.0, 2293.0, 54.0], group=3, moveless=False, logic=lambda l: l.vines),
        DoorData(name="Jungle Japes: Alcove Above Diddy Tunnel - left", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[817.0, 538.0, 2372.0, 232.0], group=3, moveless=False, logic=lambda l: l.vines),
        DoorData(name="Jungle Japes: Next to Minecart Exit -right", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[1029.0, 287.0, 2032.0, 251.5], rx=-10, group=3, logic=lambda l: True),
        DoorData(name="Jungle Japes: Across From Minecart Exit", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[958.5, 288.0, 1616.0, 45.0], group=3, logic=lambda l: True),
        DoorData(name="Jungle Japes: Main Area - Next to Tunnel to Tiny Gate", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[2563.0, 286.0, 1567.0, 253.0], rx=-8, rz=9, group=5, logic=lambda l: True),
        DoorData(name="Jungle Japes: Beehive Area - Next to Beehive - far left", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondFeatherGate, location=[1904.5, 539.0, 3369.0, 134.25], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Beehive Area - Next to Beehive - left", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondFeatherGate, location=[1857.0, 539.0, 3196.0, 79.5], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Behind Rambi Door - watery room - left", map=Maps.JungleJapes, logicregion=Regions.BeyondRambiGate, location=[611.0, 240.0, 3164.0, 201.75], group=4, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Behind Rambi Door - watery room - right", map=Maps.JungleJapes, logicregion=Regions.BeyondRambiGate, location=[803.0, 240.0, 2957.0, 280.0], group=4, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Top of Lanky's Useless Slope - left", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[2299.0, 338.0, 3135.0, 296.0], kong_lst=[Kongs.lanky], group=7, moveless=False, logic=lambda l: l.islanky and l.handstand),
        DoorData(name="Jungle Japes: Top of Lanky's Useless Slope - right", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[2095.5, 338.0, 3227.0, 118.7], kong_lst=[Kongs.lanky], group=7, moveless=False, logic=lambda l: l.islanky and l.handstand),
        DoorData(name="Jungle Japes: Underwater by Warp 2", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[1475.0, 160.0, 1605.0, 351.0], group=5, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Jungle Japes: Underwater by Chunky's underground", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[2151.0, 160.0, 1587.0, 350.0], group=5, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Jungle Japes: Next to Funky - right", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[1928.0, 520.0, 2283.4, 140.0], group=5, logic=lambda l: True),
        DoorData(name="Jungle Japes: Next to Lanky's Painting Room - left", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[538.0, 370.0, 1991.0, 179.5], kong_lst=[Kongs.lanky], group=3, moveless=False, logic=lambda l: (l.handstand and l.islanky) or (l.twirl and l.istiny)),
        DoorData(name="Jungle Japes: Next to Lanky's Painting Room - right", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[551.0, 370.0, 1752.0, 6.5], kong_lst=[Kongs.lanky], group=3, moveless=False, logic=lambda l: (l.handstand and l.islanky) or (l.twirl and l.istiny)),
        DoorData(name="Jungle Japes: Outside Diddy Cave Switch - left", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[2133.0, 280.0, 421.0, 1.0], group=2, logic=lambda l: True),
        DoorData(name="Jungle Japes: Outside Diddy Cave Switch - right", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[2119.0, 280.0, 599.0, 180.0], group=2, logic=lambda l: True),
        DoorData(name="Jungle Japes: Entrance Tunnel - Near Diddy Cave - back left", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[1891.0, 280.0, 879.0, 180.0], group=2, logic=lambda l: True),
        DoorData(name="Jungle Japes: Entrance Tunnel - Near Diddy Cave - front left", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[2022.0, 280.0, 357.0, 295.6], group=2, logic=lambda l: True),
        DoorData(name="Jungle Japes: Entrance Tunnel - Near Warppad 1 and 2", map=Maps.JungleJapes, logicregion=Regions.JungleJapesMain, location=[1432.8, 280.0, 1056.0, 89.2], group=2, logic=lambda l: True),
        DoorData(name="Jungle Japes: Diddy Tunnel - next to hole - river side", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1329.0, 281.0, 2686.5, 183.5], group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Diddy Tunnel - river side", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[683.5, 288.0, 2348.0, 61.0], rx=6, group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Near Warp 4 and Tunnel Threeway crossing", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1570.0, 280.0, 2522.0, 242.0], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Cranky Tunnel - Crossroad", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1754.4, 210.0, 3102.0, 279.7], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Cranky Area - front-right", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1414.0, 280.0, 3646.0, 55.0], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Cranky Area - front left", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1955.5, 280.0, 3646.0, 314.5], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Cranky Area - center left", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[2126.5, 280.0, 4082.0, 253.0], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Cranky Area - center right", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1278.0, 280.0, 4114.0, 106.0], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Cranky Area - back left", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1930.0, 280.0, 4401.7, 147.8], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Cranky Area - back right", map=Maps.JungleJapes, logicregion=Regions.JapesBeyondCoconutGate2, location=[1405.0, 280.0, 4416.2, 175.5], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Beehive Room 2 - left", map=Maps.JapesTinyHive, logicregion=Regions.TinyHive, location=[1248.75, 186.0, 336.0, 34.5], rx=8, rz=-1.4, scale=2, kong_lst=[Kongs.tiny], group=8, moveless=False, logic=lambda l: l.Slam, door_type="wrinkly"),
        DoorData(name="Jungle Japes: Beehive Room 2 - right", map=Maps.JapesTinyHive, logicregion=Regions.TinyHive, location=[1589.7, 195.5, 463.0, 289.7], rx=1, rz=7, scale=2, kong_lst=[Kongs.tiny], group=8, moveless=False, logic=lambda l: l.Slam, door_type="wrinkly"),
        DoorData(name="Jungle Japes: Painting Room - Next to the Entrance", map=Maps.JapesLankyCave, logicregion=Regions.JapesLankyCave, location=[305.0, 25.0, 63.0, 311.5], kong_lst=[Kongs.lanky], group=9, moveless=False, logic=lambda l: True),
        DoorData(name="Jungle Japes: Diddy Mountain - Next to Conveyor Controls", map=Maps.JapesMountain, logicregion=Regions.Mine, location=[331.9, 100.0, 1451.0, 60.0], kong_lst=[Kongs.diddy], group=10, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Jungle Japes: Diddy Mountain - between River and GB switch", map=Maps.JapesMountain, logicregion=Regions.Mine, location=[643.0, 40.0, 148.0, 323.0], kong_lst=[Kongs.diddy], group=10, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Jungle Japes: Diddy Mountain - between River and Peanut Switch", map=Maps.JapesMountain, logicregion=Regions.Mine, location=[801.0, 39.0, 268.0, 322.0], kong_lst=[Kongs.diddy], group=10, moveless=False, logic=lambda l: True, door_type="wrinkly"),
    ],
    Levels.AngryAztec: [
        DoorData(name="Angry Aztec: Lobby - Pillar Wall", map=Maps.AngryAztecLobby, logicregion=Regions.AngryAztecLobby, location=[499.179, 0.0, 499.179, 0.0], group=1, logic=lambda l: True, placed="wrinkly"),  # DK Door
        DoorData(name="Angry Aztec: Lobby - Lower Right", map=Maps.AngryAztecLobby, logicregion=Regions.AngryAztecLobby, location=[441.456, 0.0, 614.029, 180.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Diddy Door
        DoorData(name="Angry Aztec: Lobby - Left of Portal", map=Maps.AngryAztecLobby, logicregion=Regions.AngryAztecLobby, location=[628.762, 80.0, 713.93, 177.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Lanky Door
        DoorData(name="Angry Aztec: Lobby - Right of Portal", map=Maps.AngryAztecLobby, logicregion=Regions.AngryAztecLobby, location=[377.124, 80.0, 712.484, 179.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Tiny Door
        DoorData(name="Angry Aztec: Lobby - Behind Feather Door", map=Maps.AngryAztecLobby, logicregion=Regions.AngryAztecLobby, location=[1070.018, 0.0, 738.609, 190.0], group=1, moveless=False, logic=lambda l: l.tiny and l.feather, placed="wrinkly"),  # Custom Chunky Door
        DoorData(name="Angry Aztec: Near Funky's", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[2801.765, 121.333, 4439.293, 66.0], group=2, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal by Funky
        DoorData(name="Angry Aztec: Near Cranky's", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[2787.908, 120.0, 2674.299, 198.0], group=3, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal by Cranky
        DoorData(name="Angry Aztec: Near Candy's", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[2268.343, 120.0, 448.669, 59.0], group=4, logic=lambda l: l.vines, placed="tns"),  # T&S Portal by Candy
        DoorData(name="Angry Aztec: Near Snide's", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[3573.712, 120.0, 4456.399, 285.0], group=2, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal by Snide
        DoorData(name="Angry Aztec: Behind 5DT", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[1968.329, 180.0, 3457.189, 244.0], group=5, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal behind 5DT
        DoorData(name="Angry Aztec: Next to Candy - right", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[2468.0, 120.0, 473.5, 298.75], group=4, logic=lambda l: l.vines),
        DoorData(name="Angry Aztec: Under Diddy's Tiny Temple Switch", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[3053.0, 214.0, 605.5, 217.5], group=4, logic=lambda l: True, door_type="tns"),
        DoorData(name="Angry Aztec: Under Chunky's Tiny Temple Switch", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[3149.0, 212.0, 532.0, 217.5], group=4, logic=lambda l: True, door_type="tns"),
        DoorData(name="Angry Aztec: Under Tiny's Tiny Temple Switch", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[3183.0, 213.0, 773.0, 37.5], group=4, logic=lambda l: True, door_type="tns"),
        DoorData(name="Angry Aztec: Under Lanky's Tiny Temple Switch", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[3282.0, 213.0, 697.0, 37.5], group=4, logic=lambda l: True, door_type="tns"),
        DoorData(name="Angry Aztec: Diddy Tower Stairs - left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[4206.0, 80.0, 3367.0, 240.0], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Next to Tag Barrel near Snides", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[4067.0, 190.0, 4050.0, 263.0], group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Under the Vulture Cage", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[4005.0, 120.0, 4598.0, 155.0], group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: 5Door Temple's 6th Door", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[2212.0, 180.0, 3687.3, 62.9], scale=1.47, group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Cranky Tunnel - Near Chunky Barrel - left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[3182.5, 120.0, 1440.0, 41.0], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Cranky Tunnel - Near Chunky Barrel - right", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[3358.0, 120.0, 1445.5, 318.5], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Cranky Tunnel - Near Road to Cranky - left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[3366.8, 120.0, 2032.0, 241.43], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Cranky Tunnel - Near Road to Cranky - right", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[3166.25, 120.0, 2028.0, 118.5], group=7, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: 5Door Temple Staircase - front", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[2031.0, 180.0, 3826.0, 63.5], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: 5Door Temple Staircase - back", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[1921.0, 180.0, 3770.0, 244.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Entrance Tunnel - next to Coconut Switch", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[1514.0, 120.0, 1107.8, 4.8], group=8, logic=lambda l: True),
        DoorData(name="Angry Aztec: Entrance Tunnel - left (near the oasis end)", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[1820.0, 120.0, 816.5, 19.0], group=8, logic=lambda l: True),
        DoorData(name="Angry Aztec: Strong Kong Tunnel", map=Maps.AngryAztec, logicregion=Regions.AztecDonkeyQuicksandCave, location=[3208.25, 118.0, 4752.0, 225.0], kong_lst=[Kongs.donkey], group=2, moveless=False, logic=lambda l: l.isdonkey and l.strongKong, door_type="wrinkly"),
        DoorData(name="Angry Aztec: Near Tag Barrel near Snides - strong kong", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[3940.0, 112.0, 4099.0, 323.5], kong_lst=[Kongs.donkey], group=2, moveless=False, logic=lambda l: l.isdonkey and l.strongKong, door_type="wrinkly"),
        DoorData(name="Angry Aztec: In Face Matching Game - right", map=Maps.AztecLlamaTemple, logicregion=Regions.LlamaTemple, location=[1074.0, 641.0, 2086.0, 0.26], kong_lst=[Kongs.lanky], group=9, moveless=False, logic=lambda l: l.islanky and l.grape, door_type="wrinkly"),
        DoorData(name="Angry Aztec: In Face Matching Game - left", map=Maps.AztecLlamaTemple, logicregion=Regions.LlamaTemple, location=[1074.0, 641.0, 2683.7, 179.74], kong_lst=[Kongs.lanky], group=9, moveless=False, logic=lambda l: l.islanky and l.grape, door_type="wrinkly"),
        DoorData(name="Angry Aztec: Next to Tiny Temple - front left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[2893.0, 153.0, 478.0, 28.0], group=4, logic=lambda l: True),
        DoorData(name="Angry Aztec: Next to Tiny Temple - back left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[3209.2, 153.0, 312.2, 307.0], group=4, logic=lambda l: True),
        DoorData(name="Angry Aztec: Oasis - Next to Tunnel - far left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[2923.0, 120.0, 1205.0, 243.5], group=4, logic=lambda l: True),
        DoorData(name="Angry Aztec: Oasis - Next to Tunnel - left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecOasis, location=[2836.0, 120.0, 1370.0, 237.5], group=4, logic=lambda l: True),
        DoorData(name="Angry Aztec: Between Snides and Diddy Gong Tower", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[4183.0, 120.0, 3830.0, 239.5], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Next to Llama Temple - left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[2794.75, 120.0, 3566.0, 64.0], group=10, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Llama Temple's switchless side", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[2997.6, 250.0, 2906.0, 105.0], group=10, moveless=False, logic=lambda l: True, door_type="tns"),
        DoorData(name="Angry Aztec: Tiny Temple - Main Room - left", map=Maps.AztecTinyTemple, logicregion=Regions.TempleStart, location=[1571.0, 289.0, 610.9, 0.0], group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Tiny Temple - Main Room - back", map=Maps.AztecTinyTemple, logicregion=Regions.TempleStart, location=[1789.0, 287.0, 813.0, 270.0], group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Tiny Temple - Across from Slope to Tiny Cage - left", map=Maps.AztecTinyTemple, logicregion=Regions.TempleUnderwater, location=[1672.5, 122.0, 1359.0, 270.0], group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Tiny Temple - Across from Slope to Tiny Cage - right", map=Maps.AztecTinyTemple, logicregion=Regions.TempleUnderwater, location=[1672.5, 122.0, 1571.0, 270.0], group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Tiny Temple - Next to Opening to Underwater Room", map=Maps.AztecTinyTemple, logicregion=Regions.TempleUnderwater, location=[1375.0, 145.0, 949.5, 180.0], group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Tiny Temple - Across from Opening to Underwater Room", map=Maps.AztecTinyTemple, logicregion=Regions.TempleUnderwater, location=[1450.0, 145.0, 751.1, 0.0], group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Llama Temple Stairs - left", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[2902.0, 160.0, 3214.8, 285.1], scale=0.95, group=9, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Llama Temple Stairs - right", map=Maps.AngryAztec, logicregion=Regions.AngryAztecMain, location=[3020.0, 160.0, 3183.0, 105.1], scale=0.95, group=9, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Llama Temple - Entrance Staircase - left", map=Maps.AztecLlamaTemple, logicregion=Regions.LlamaTemple, location=[2694.9, 371.0, 2310.0, 270.0], group=9, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Llama Temple - Entrance Staircase - right", map=Maps.AztecLlamaTemple, logicregion=Regions.LlamaTemple, location=[2694.9, 371.0, 2546.0, 270.0], group=9, moveless=False, logic=lambda l: True),
        DoorData(name="Angry Aztec: Llama Temple - Across from the Spit Gate", map=Maps.AztecLlamaTemple, logicregion=Regions.LlamaTemple, location=[2224.0, 203.0, 2704.0, 180.0], group=9, moveless=False, logic=lambda l: Events.AztecLlamaSpit in l.events and l.swim),
    ],
    Levels.FranticFactory: [
        DoorData(name="Frantic Factory: Lobby - Low Left", map=Maps.FranticFactoryLobby, logicregion=Regions.FranticFactoryLobby, location=[544.362, 0.0, 660.802, 182.0], group=1, logic=lambda l: True, placed="wrinkly"),  # DK Door
        DoorData(name="Frantic Factory: Lobby - Top Left", map=Maps.FranticFactoryLobby, logicregion=Regions.FranticFactoryLobby, location=[660.685, 133.5, 660.774, 182.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # Diddy Door
        DoorData(name="Frantic Factory: Lobby - Top Center", map=Maps.FranticFactoryLobby, logicregion=Regions.FranticFactoryLobby, location=[468.047, 85.833, 662.907, 180.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # Lanky Door
        DoorData(name="Frantic Factory: Lobby - Top Right", map=Maps.FranticFactoryLobby, logicregion=Regions.FranticFactoryLobby, location=[275.533, 133.5, 661.908, 180.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # Tiny Door
        DoorData(name="Frantic Factory: Lobby - Low Right", map=Maps.FranticFactoryLobby, logicregion=Regions.FranticFactoryLobby, location=[393.114, 0.0, 662.562, 182.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Chunky Door
        DoorData(name="Frantic Factory: Arcade Room", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[1778.702, 1106.667, 1220.515, 357.0], group=2, logic=lambda l: True, placed="tns"),  # T&S Portal in Arcade Room
        DoorData(name="Frantic Factory: Production Room", map=Maps.FranticFactory, logicregion=Regions.UpperCore, location=[381.573, 605.0, 1032.929, 45.0], group=3, logic=lambda l: True, placed="tns"),  # T&S Portal in Production Room
        DoorData(name="Frantic Factory: R&D", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[3827.127, 1264.0, 847.458, 222.0], group=4, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal in R&D
        DoorData(name="Frantic Factory: Block Tower", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[2259.067, 1126.824, 1614.609, 182.0], group=5, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal in Block Tower Room
        DoorData(name="Frantic Factory: Storage Room", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[1176.912, 6.5, 472.114, 1.0], group=6, logic=lambda l: True, placed="tns"),  # T&S Portal in Storage Room
        DoorData(name="Frantic Factory: Behind Chunky's Toy Box - big", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[5016.0, 1336.0, 1780.0, 236.0], scale=2, kong_lst=[Kongs.chunky], group=4, moveless=False, logic=lambda l: l.ischunky and l.punch and l.triangle, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Next to Hatch with Tall Pole - left", map=Maps.FranticFactory, logicregion=Regions.FranticFactoryStart, location=[489.5, 804.0, 1867.0, 49.0], group=7, logic=lambda l: True),
        DoorData(name="Frantic Factory: Next to Hatch with Tall Pole - right", map=Maps.FranticFactory, logicregion=Regions.FranticFactoryStart, location=[800.0, 804.0, 1867.0, 310.0], group=7, logic=lambda l: True),
        DoorData(name="Frantic Factory: Bottom of the Tall Pole", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[528.0, 167.0, 1770.8, 35.0], group=7, logic=lambda l: True),
        DoorData(name="Frantic Factory: Production Room - Under Tiny Conveyors", map=Maps.FranticFactory, logicregion=Regions.UpperCore, location=[860.0, 605.0, 1011.0, 314.5], group=3, logic=lambda l: True),
        DoorData(name="Frantic Factory: Kong Cage Room - Behind Tag Barrel", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[1633.0, 6.0, 845.0, 270.0], group=6, logic=lambda l: True),
        DoorData(name="Frantic Factory: Under Cranky's Lab", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[267.7, 165.0, 805.0, 90.0], group=6, logic=lambda l: True),
        DoorData(name="Frantic Factory: Under Candy's Store", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[267.0, 165.0, 649.0, 90.0], group=6, logic=lambda l: True),
        DoorData(name="Frantic Factory: Next to DK's Count to 16 Puzzle", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[2526.0, 1002.0, 1990.6, 180.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: R&D Room - Next to Tunnel to Car Race", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[4006.7, 1264.0, 1454.0, 253.7], group=4, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: Block Tower Room - Under Tunnel to Funky's", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[2044.0, 1026.0, 978.0, 0.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: R&D Room - Dead End", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[3824.0, 1264.0, 528.8, 340.5], group=4, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: R&D Room - Blind Corner Next to Tunnel to Car Race", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[3790.0, 1264.0, 1476.0, 52.5], group=4, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Funky's Room - Across from Melon Crate", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[1589.0, 1113.0, 816.2, 182.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: Block Tower Room - Air Vent Under Arcade Window", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[2002.5, 1027.0, 1180.5, 90.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: Block Tower Room - Under Arcade Window - left", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[1957.1, 1026.0, 1448.0, 90.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: Block Tower Room - Behind Tag Barrel", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[2717.0, 1106.0, 838.0, 0.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: R&D Room - Next to Diddy's Pincode Room", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[4046.0, 1336.0, 608.0, 340.0], group=4, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: Tiny's Race Entry Area", map=Maps.FranticFactory, logicregion=Regions.FactoryTinyRaceLobby, location=[3540.25, 1264.0, 1413.0, 141.0], kong_lst=[Kongs.tiny], group=4, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Kong Cage Room - Next to Tag Barrel", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[1421.0, 6.0, 927.3, 180.0], group=6, logic=lambda l: True),
        DoorData(name="Frantic Factory: Production Room - in Alcove Next to Tiny's Barrel", map=Maps.FranticFactory, logicregion=Regions.UpperCore, location=[215.0, 858.0, 1444.5, 90.0], scale=0.84, kong_lst=[Kongs.tiny], group=3, moveless=False, logic=lambda l: l.istiny and l.twirl, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Production Room - Next to Diddy's Switch", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[430.6, 0.0, 980.6, 45.0], group=3, logic=lambda l: True),
        DoorData(name="Frantic Factory: Arcade Room - in a corner", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[1652.5, 1106.0, 1253.75, 43.0], scale=0.8669, group=2, logic=lambda l: True),
        DoorData(name="Frantic Factory: Block Tower Room - Next to Tiny Barrel", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[2237.0, 1106.0, 943.0, 90.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: Block Tower Room - at the Base of the Block Tower", map=Maps.FranticFactory, logicregion=Regions.Testing, location=[2517.0, 1026.0, 1315.0, 90.0], group=5, moveless=False, logic=lambda l: True),
        DoorData(name="Frantic Factory: Clock Room - Under Clock", map=Maps.FranticFactory, logicregion=Regions.FranticFactoryStart, location=[1262.0, 867.0, 2025.0, 0.0], scale=0.48, group=7, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Clock Room - front left", map=Maps.FranticFactory, logicregion=Regions.FranticFactoryStart, location=[1044.65, 842.0, 2223.0, 90.0], group=7, logic=lambda l: True),
        DoorData(name="Frantic Factory: Clock Room - back left", map=Maps.FranticFactory, logicregion=Regions.FranticFactoryStart, location=[1044.65, 842.0, 2105.0, 90.0], group=7, logic=lambda l: True),
        DoorData(name="Frantic Factory: Clock Room - front right", map=Maps.FranticFactory, logicregion=Regions.FranticFactoryStart, location=[1447.0, 842.0, 2283.5, 180.0], group=7, logic=lambda l: True),
        DoorData(name="Frantic Factory: Top of Pipe Near Kong-freeing Switch", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[1632.8, 197.0, 488.0, 270.0], scale=0.82, kong_lst=[Kongs.lanky], group=6, moveless=False, logic=lambda l: l.islanky and l.handstand, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Pin Code Room - front-right", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[4386.2, 1336.0, 771.0, 124.0], kong_lst=[Kongs.diddy], group=4, moveless=False, logic=lambda l: l.isdiddy and l.guitar, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Lanky's Piano Room - right", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[3610.0, 1264.0, 306.2, 325.0], kong_lst=[Kongs.lanky], group=4, moveless=False, logic=lambda l: l.islanky and l.trombone, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Lanky's Piano Room - left", map=Maps.FranticFactory, logicregion=Regions.RandD, location=[3320.0, 1264.0, 662.0, 145.25], kong_lst=[Kongs.lanky], group=4, moveless=False, logic=lambda l: l.islanky and l.trombone, door_type="wrinkly"),
        DoorData(name="Frantic Factory: Chunky's Dark Room", map=Maps.FranticFactory, logicregion=Regions.BeyondHatch, location=[2149.6, 6.0, 598.0, 270.0], kong_lst=[Kongs.chunky], group=6, moveless=False, logic=lambda l: l.chunky and l.punch),
        DoorData(name="Frantic Factory: Crusher Room - start", map=Maps.FactoryCrusher, logicregion=Regions.InsideCore, location=[475.0, 0.0, 539.0, 180.0], group=3, logic=lambda l: True),
    ],
    Levels.GloomyGalleon: [
        DoorData(name="Gloomy Galleon: Lobby - Far Left", map=Maps.GloomyGalleonLobby, logicregion=Regions.GloomyGalleonLobby, location=[1022.133, 139.667, 846.41, 276.0], group=1, logic=lambda l: True, placed="wrinkly"),  # DK Door
        DoorData(name="Gloomy Galleon: Lobby - Far Right", map=Maps.GloomyGalleonLobby, logicregion=Regions.GloomyGalleonLobby, location=[345.039, 139.667, 884.162, 92.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Diddy Door
        DoorData(name="Gloomy Galleon: Lobby - Close Right", map=Maps.GloomyGalleonLobby, logicregion=Regions.GloomyGalleonLobby, location=[464.68, 159.667, 1069.446, 161.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Lanky Door
        DoorData(name="Gloomy Galleon: Lobby - Near DK Portal", map=Maps.GloomyGalleonLobby, logicregion=Regions.GloomyGalleonLobby, location=[582.36, 159.667, 1088.258, 180.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Tiny Door
        DoorData(name="Gloomy Galleon: Lobby - Close Left", map=Maps.GloomyGalleonLobby, logicregion=Regions.GloomyGalleonLobby, location=[876.388, 178.667, 1063.828, 192.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Chunky Door
        DoorData(name="Gloomy Galleon: Near Cranky's", map=Maps.GloomyGalleon, logicregion=Regions.GalleonPastVines, location=[3423.707, 1890.471, 3098.15, 243.0], group=2, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Door Near Cranky's
        DoorData(name="Gloomy Galleon: Deep Hole", map=Maps.GloomyGalleon, logicregion=Regions.LighthouseUnderwater, location=[1975.898, 100.0, 4498.375, 256.0], group=3, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Door in meme hole
        DoorData(name="Gloomy Galleon: Behind 2DS", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[803.636, 1053.997, 1955.268, 92.0], group=4, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Door behind 2DS
        DoorData(name="Gloomy Galleon: Behind Enguarde Door", map=Maps.GloomyGalleon, logicregion=Regions.LighthouseUnderwater, location=[645.832, 1460.0, 4960.476, 133.0], group=5, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Door behind Enguarde Door
        DoorData(name="Gloomy Galleon: Cactus", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[4517.923, 1290.0, 894.527, 308.0], group=6, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Door near Cactus
        DoorData(name="Gloomy Galleon: In hallway to Shipyard - Tiny switch", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[2205.0, 1620.0, 2700.0, 90.0], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: In hallway to Shipyard - Lanky switch", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[2615.0, 1620.0, 2844.0, 302.0], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: In hallway to Primate Punch Chests", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[3007.0, 1670.0, 3866.0, 135.42], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Under Baboon Blast pad", map=Maps.GloomyGalleon, logicregion=Regions.LighthousePlatform, location=[1674.5, 1610.0, 4042.5, 261.15], group=7, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Under RocketBarrel barrel", map=Maps.GloomyGalleon, logicregion=Regions.LighthousePlatform, location=[1360.0, 1609.0, 4048.0, 86.0], group=7, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Next to Cannonball game", map=Maps.GloomyGalleon, logicregion=Regions.GalleonBeyondPineappleGate, location=[1334.0, 1610.0, 2523.0, 0.0], group=8, moveless=False, logic=lambda l: Events.WaterSwitch in l.Events),
        DoorData(name="Gloomy Galleon: Next to Coconut switch", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[2065.75, 1628.0, 3418.75, 28.0], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Entrance Tunnel - near entrance", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[2112.0, 1628.0, 3223.0, 135.0], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Next to Peanut switch", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[2462.0, 1619.0, 2688.0, 270.0], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Music Cactus - bottom back left", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[4444.0, 1290.0, 803.0, 307.7], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Music Cactus - bottom front left", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[4239.0, 1289.0, 880.0, 38.31], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Music Cactus - bottom back right", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[4587.0, 1290.0, 972.0, 307.85], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Music Cactus - bottom front right", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[4524.0, 1290.0, 1145.0, 218.31], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: On top of Seal cage", map=Maps.GloomyGalleon, logicregion=Regions.LighthousePlatform, location=[2238.0, 1837.0, 4099.0, 251.7], kong_lst=[Kongs.diddy], group=7, moveless=False, logic=lambda l: l.isdiddy and l.jetpack, door_type="wrinkly"),
        DoorData(name="Gloomy Galleon: Treasure Chest Exterior", map=Maps.GloomyGalleon, logicregion=Regions.TreasureRoom, location=[1938.0, 1440.0, 524.0, 330.0], group=9, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Next to Warp 3 in Cranky's Area", map=Maps.GloomyGalleon, logicregion=Regions.GalleonPastVines, location=[3071.0, 1890.0, 2838.0, 0.0], group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: In Primate Punch Chest Room - right", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[3460.0, 1670.0, 4001.0, 180.0], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Behind Chunky punch gate in Cranky Area", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[3275.0, 1670.0, 2353.65, 13.65], kong_lst=[Kongs.chunky], group=2, moveless=False, logic=lambda l: l.chunky and l.punch),
        DoorData(name="Gloomy Galleon: Low water alcove in lighthouse area", map=Maps.GloomyGalleon, logicregion=Regions.LighthouseSurface, location=[540.3, 1564.0, 4094.0, 110.0], group=7, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Behind boxes in Cranky Area", map=Maps.GloomyGalleon, logicregion=Regions.GloomyGalleonStart, location=[2891.5, 1688.0, 3493.0, 124.0], group=2, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Mech Fish Gate - far left", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[2651.0, 140.5, 503.0, 92.0], group=10, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Mech Fish Gate - left", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[2792.0, 175.0, 299.3, 15.9], rz=7.3, group=10, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Mech Fish Gate - middle", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[3225.0, 205.0, 303.0, 329.0], rz=-4.7, group=10, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Mech Fish Gate - right", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[3406.0, 166.0, 531.0, 260.0], rx=290, rz=-290, group=10, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Mech Fish Gate - far right", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[3310.0, 147.0, 828.0, 216.5], rx=16, rz=-16, group=10, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Cannonball Area Exit", map=Maps.GloomyGalleon, logicregion=Regions.GalleonBeyondPineappleGate, location=[1524.1, 1461.0, 2898.0, 278.0], group=8, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: 2Dship's secret 3rd door", map=Maps.GloomyGalleon, logicregion=Regions.ShipyardUnderwater, location=[1109.0, 1189.9, 1978.0, 95.0], rz=-47, group=4, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Near Mermaid's Palace - right", map=Maps.GloomyGalleon, logicregion=Regions.LighthouseUnderwater, location=[1445.0, 141.0, 4859.0, 180.0], group=3, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Near Mermaid's Palace - left", map=Maps.GloomyGalleon, logicregion=Regions.LighthouseUnderwater, location=[1400.0, 112.8, 4215.0, 346.5], rz=3, group=3, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Near Mermaid's Palace - Under Tag Barrel", map=Maps.GloomyGalleon, logicregion=Regions.LighthouseUnderwater, location=[915.0, 164.0, 3967.0, 30.0], rx=7, rz=3, group=3, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: Lighthouse Interior", map=Maps.GalleonLighthouse, logicregion=Regions.Lighthouse, location=[508.0, 200.0, 409.0, 135.2], kong_lst=[Kongs.donkey], group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Gloomy Galleon: In Mermaid's Palace", map=Maps.GalleonMermaidRoom, logicregion=Regions.MermaidRoom, location=[274.0, 0.0, 481.0, 150.0], kong_lst=[Kongs.tiny], group=12, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Gloomy Galleon: Tiny's 5D ship", map=Maps.Galleon5DShipDKTiny, logicregion=Regions.SaxophoneShip, location=[735.0, 0.0, 1336.0, 270.0], kong_lst=[Kongs.tiny], group=13, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Gloomy Galleon: Lanky's 5D ship", map=Maps.Galleon5DShipDiddyLankyChunky, logicregion=Regions.TromboneShip, location=[1099.0, 0.0, 1051.0, 270.0], kong_lst=[Kongs.lanky], group=14, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Gloomy Galleon: Lanky's 2D ship", map=Maps.Galleon2DShip, logicregion=Regions.LankyShip, location=[1616.0, 0.0, 939.0, 179.5], kong_lst=[Kongs.lanky], group=15, moveless=False, logic=lambda l: True),
    ],
    Levels.FungiForest: [
        DoorData(name="Fungi Forest: Lobby - On High Box", map=Maps.FungiForestLobby, logicregion=Regions.FungiForestLobby, location=[449.866, 45.922, 254.6, 270.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Custom Location (Removing Wheel)
        DoorData(name="Fungi Forest: Lobby - Near Gorilla Gone Door", map=Maps.FungiForestLobby, logicregion=Regions.FungiForestLobby, location=[136.842, 0.0, 669.81, 90.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Custom Location (Removing Wheel)
        DoorData(name="Fungi Forest: Lobby - Opposite Gorilla Gone Door", map=Maps.FungiForestLobby, logicregion=Regions.FungiForestLobby, location=[450.219, 0.0, 689.048, 270.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Custom Location (Removing Wheel)
        DoorData(name="Fungi Forest: Lobby - Near B. Locker", map=Maps.FungiForestLobby, logicregion=Regions.FungiForestLobby, location=[293.0, 0.0, 154.197, 0.0], scale=1.2, group=1, logic=lambda l: True, placed="wrinkly"),  # Custom Location (Removing Wheel)
        DoorData(name="Fungi Forest: Lobby - Near Entrance", map=Maps.FungiForestLobby, logicregion=Regions.FungiForestLobby, location=[450.862, 0.0, 565.029, 270.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Custom Location (Removing Wheel)
        DoorData(name="Fungi Forest: Behind DK Barn", map=Maps.FungiForest, logicregion=Regions.ThornvineArea, location=[3515.885, 115.009, 1248.55, 31.0], group=2, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal behind DK Barn
        DoorData(name="Fungi Forest: Beanstalk Area", map=Maps.FungiForest, logicregion=Regions.WormArea, location=[3665.871, 186.833, 945.745, 252.0], group=3, moveless=False, logic=lambda l: Events.Night in l.Events, placed="tns"),  # T&S Portal in Beanstalk Area
        DoorData(name="Fungi Forest: Near Snide's", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[3240.033, 268.5, 3718.017, 178.0], group=4, logic=lambda l: True, placed="tns"),  # T&S Portal near Snide's
        DoorData(name="Fungi Forest: Top of Giant Mushroom", map=Maps.FungiForest, logicregion=Regions.MushroomUpperExterior, location=[1171.791, 1250.0, 1236.572, 52.0], group=5, logic=lambda l: True, placed="tns"),  # T&S Portal at Top of GMush
        DoorData(name="Fungi Forest: Owl Area", map=Maps.FungiForest, logicregion=Regions.HollowTreeArea, location=[203.663, 199.333, 3844.253, 92.0], group=6, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal near Owl Race
        DoorData(name="Fungi Forest: On top of Cage outside Conveyor Belt", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[4312.0, 224.0, 3493.0, 134.82], group=4, logic=lambda l: True),
        DoorData(name="Fungi Forest: Watermill - front - right", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[4261.0, 162.0, 3804.0, 314.12], group=4, logic=lambda l: True),
        DoorData(name="Fungi Forest: Watermill - right - left", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[4367.0, 162.0, 3806.0, 44.0], group=4, logic=lambda l: True),
        DoorData(name="Fungi Forest: Watermill - right - right", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[4450.0, 162.0, 3724.0, 44.5], group=4, logic=lambda l: True),
        DoorData(name="Fungi Forest: Watermill Roof - tower", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[4444.0, 321.0, 3628.0, 316.0], rx=-4, group=4, logic=lambda l: True),
        DoorData(name="Fungi Forest: Boxes outside of Diddy's Barn", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[3469.0, 272.0, 4504.0, 122.5], group=4, logic=lambda l: True),
        DoorData(name="Fungi Forest: Outside Diddy's Barn", map=Maps.FungiForest, logicregion=Regions.MillArea, location=[3434.0, 271.0, 4316.0, 123.25], rx=-4, group=4, logic=lambda l: True),
        DoorData(name="Fungi Forest: Immediately Inside the Thornvine Area - right", map=Maps.FungiForest, logicregion=Regions.ThornvineArea, location=[4648.0, 205.0, 2836.0, 280.0], group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Immediately Inside the Thornvine Area - left", map=Maps.FungiForest, logicregion=Regions.ThornvineArea, location=[4114.0, 202.0, 2654.5, 40.5], group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Outside DK's Barn", map=Maps.FungiForest, logicregion=Regions.ThornvineArea, location=[4077.0, 115.0, 1954.0, 33.5], rx=-5, group=2, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Next to Rabbit's House", map=Maps.FungiForest, logicregion=Regions.HollowTreeArea, location=[2277.0, 167.3, 3500.6, 0.0], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Owl Area - Near Rocketbarrel Barrel - far left", map=Maps.FungiForest, logicregion=Regions.HollowTreeArea, location=[562.0, 199.0, 4147.25, 180.0], group=6, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Funky Area - Near Tiny Coins", map=Maps.FungiForest, logicregion=Regions.WormArea, location=[1939.0, 224.0, 261.0, 31.5], group=3, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Mushroom Area - Next to Tag Barrel near Cranky's", map=Maps.FungiForest, logicregion=Regions.GiantMushroomArea, location=[1754.2, 234.0, 972.0, 270.0], rx=-10, group=7, logic=lambda l: True),
        DoorData(name="Fungi Forest: Mushroom Area - Next to Rocketbarrel Barrel - left", map=Maps.FungiForest, logicregion=Regions.GiantMushroomArea, location=[67.0, 250.0, 719.0, 89.5], rx=-10, group=7, logic=lambda l: True),
        DoorData(name="Fungi Forest: Mushroom Area - Next to Rocketbarrel Barrel - right", map=Maps.FungiForest, logicregion=Regions.GiantMushroomArea, location=[254.0, 250.0, 386.0, 51.4], group=7, logic=lambda l: True),
        DoorData(name="Fungi Forest: Mushroom Area - Next to Cranky", map=Maps.FungiForest, logicregion=Regions.GiantMushroomArea, location=[1451.0, 179.0, 504.6, 321.5], group=7, logic=lambda l: True),
        DoorData(name="Fungi Forest: Clock Area - Next to Purple Tunnel - left", map=Maps.FungiForest, logicregion=Regions.FungiForestStart, location=[1795.7, 181.0, 2217.0, 117.6], group=8, logic=lambda l: True),
        DoorData(name="Fungi Forest: Clock Area - Next to Purple Tunnel - right", map=Maps.FungiForest, logicregion=Regions.FungiForestStart, location=[1876.0, 185.0, 1823.0, 39.5], group=8, logic=lambda l: True),
        DoorData(name="Fungi Forest: Clock Area - Next to Clock - left", map=Maps.FungiForest, logicregion=Regions.FungiForestStart, location=[2431.0, 603.0, 2410.0, 0.0], rx=10, group=8, logic=lambda l: True),
        DoorData(name="Fungi Forest: Clock Area - Next to Clock - right", map=Maps.FungiForest, logicregion=Regions.FungiForestStart, location=[2431.0, 603.0, 2238.0, 180.0], rx=10, group=8, logic=lambda l: True),
        DoorData(name="Fungi Forest: Funky Area - Near Beanstalk - left", map=Maps.FungiForest, logicregion=Regions.WormArea, location=[1830.0, 230.0, 822.0, 154.0], group=3, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Funky Area - Near Beanstalk - back", map=Maps.FungiForest, logicregion=Regions.WormArea, location=[1766.1, 228.0, 637.0, 90.5], group=3, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Inside the Mushroom - All Kong Gun Switch - right", map=Maps.ForestGiantMushroom, logicregion=Regions.MushroomLower, location=[558.0, 74.0, 135.5, 353.0], rz=-5.5, group=5, logic=lambda l: True),
        DoorData(name="Fungi Forest: Inside the Mushroom - All Kong Gun Switch - left", map=Maps.ForestGiantMushroom, logicregion=Regions.MushroomLower, location=[340.0, 74.0, 135.5, 6.9], rz=5.5, group=5, logic=lambda l: True),
        DoorData(name="Fungi Forest: Inside the Mushroom - halfway along the Dead End", map=Maps.ForestGiantMushroom, logicregion=Regions.MushroomLower, location=[229.0, 217.0, 880.2, 147.5], rx=-3, rz=-3, group=5, logic=lambda l: True),
        DoorData(name="Fungi Forest: Inside the Mushroom - Along the Wall near Diddy's Kasplat", map=Maps.ForestGiantMushroom, logicregion=Regions.MushroomUpper, location=[396.0, 610.0, 929.0, 174.0], group=5, logic=lambda l: True),
        DoorData(name="Fungi Forest: Inside the Mushroom - Along the Wall near Klump and Oranges", map=Maps.ForestGiantMushroom, logicregion=Regions.MushroomUpper, location=[847.25, 1169.0, 575.0, 264.0], group=5, logic=lambda l: True),
        DoorData(name="Fungi Forest: Chunky's Face Puzzle", map=Maps.ForestChunkyFaceRoom, logicregion=Regions.MushroomChunkyRoom, location=[427.4, 0.0, 182.0, 307.5], rx=5, kong_lst=[Kongs.chunky], group=9, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Fungi Forest: Lanky's 2-Mushroom Room", map=Maps.ForestLankyZingersRoom, logicregion=Regions.MushroomLankyZingersRoom, location=[196.0, 0.0, 484.45, 157.4], rx=5, kong_lst=[Kongs.lanky], group=10, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: DK Lever puzzle Area", map=Maps.ForestMillFront, logicregion=Regions.GrinderRoom, location=[548.0, 45.0, 73.5, 0.0], scale=0.88, kong_lst=[Kongs.donkey], group=11, moveless=False, logic=lambda l: l.isdonkey and l.superSlam, door_type="wrinkly"),
        DoorData(name="Fungi Forest: Mill - back side - Near Chunky Coins", map=Maps.ForestMillBack, logicregion=Regions.MillChunkyArea, location=[450.0, 0.0, 673.3, 180.0], kong_lst=[Kongs.tiny, Kongs.chunky], group=11, moveless=False, logic=lambda l: True),  # might be accessible by all kongs post-punch?
        DoorData(name="Fungi Forest: Winch Room - on the Winch", map=Maps.ForestWinchRoom, logicregion=Regions.WinchRoom, location=[238.0, 49.0, 124.0, 0.0], kong_lst=[Kongs.diddy], group=12, moveless=False, logic=lambda l: True),
        DoorData(name="Fungi Forest: Lanky's Attic", map=Maps.ForestMillAttic, logicregion=Regions.MillAttic, location=[125.0, 0.0, 453.3, 180.0], group=13, logic=lambda l: True),
        DoorData(name="Fungi Forest: DK's Barn - Between 2 Barrels near Switch", map=Maps.ForestThornvineBarn, logicregion=Regions.ThornvineBarn, location=[12.7, 4.0, 301.5, 90.0], kong_lst=[Kongs.donkey], group=14, moveless=False, logic=lambda l: True),
    ],
    Levels.CrystalCaves: [
        DoorData(name="Crystal Caves: Lobby - Far Left", map=Maps.CrystalCavesLobby, logicregion=Regions.CrystalCavesLobby, location=[1103.665, 146.5, 823.872, 194.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # DK Door
        DoorData(name="Crystal Caves: Lobby - Top Ledge", map=Maps.CrystalCavesLobby, logicregion=Regions.CrystalCavesLobby, location=[731.84, 280.5, 704.935, 120.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # Diddy Door
        DoorData(name="Crystal Caves: Lobby - Near Left", map=Maps.CrystalCavesLobby, logicregion=Regions.CrystalCavesLobby, location=[1046.523, 13.5, 476.611, 189.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # Lanky Door
        DoorData(name="Crystal Caves: Lobby - Far Right", map=Maps.CrystalCavesLobby, logicregion=Regions.CrystalCavesLobby, location=[955.407, 146.664, 843.472, 187.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # Tiny Door
        DoorData(name="Crystal Caves: Lobby - Near Right", map=Maps.CrystalCavesLobby, logicregion=Regions.CrystalCavesLobby, location=[881.545, 13.466, 508.666, 193.0], group=1, moveless=False, logic=lambda l: True, placed="wrinkly"),  # Chunky Door
        DoorData(name="Crystal Caves: On Rotating Room", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[2853.776, 436.949, 2541.475, 207.0], kong_lst=[Kongs.diddy], group=2, moveless=False, logic=lambda l: l.isdiddy and l.jetpack, placed="tns"),  # T&S Portal on Rotating Room
        DoorData(name="Crystal Caves: Near Snide's", map=Maps.CrystalCaves, logicregion=Regions.CavesSnideArea, location=[1101.019, 64.5, 467.76, 69.0], group=3, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal near Snide's
        DoorData(name="Crystal Caves: Giant Boulder Room", map=Maps.CrystalCaves, logicregion=Regions.BoulderCave, location=[1993.556, 277.108, 2795.365, 193.0], group=4, moveless=False, logic=lambda l: True, placed="tns"),  # T&S Portal in Giant Boulder Room
        DoorData(name="Crystal Caves: On Sprint Cabin", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[2196.449, 394.167, 1937.031, 93.0], kong_lst=[Kongs.diddy, Kongs.lanky], group=2, moveless=False, logic=lambda l: (l.isdiddy and l.jetpack) or (l.islanky and l.balloon), placed="tns"),  # T&S Portal on Sprint Cabin
        DoorData(name="Crystal Caves: Near 5DI", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[120.997, 50.167, 1182.974, 75.146], group=5, logic=lambda l: True, placed="tns"),  # T&S Portal near 5DI (Custom)
        DoorData(name="Crystal Caves: Outside Lanky's Cabin", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[2400.0, 276.0, 1892.5, 21.75], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Outside Chunky's Cabin", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[3515.65, 175.0, 1893.0, 273.7], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Outside Diddy's Lower Cabin", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[3697.5, 260.0, 1505.0, 291.0], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Outside Diddy's Upper Cabin", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[3666.7, 343.0, 1762.0, 273.8], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Under the Waterfall (Cabin Area)", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[2230.0, 0.0, 2178.0, 100.0], group=2, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Across from the 5Door Cabin", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[2970.0, 128.0, 1499.0, 68.5], rx=9, rz=11, group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: 5Door Igloo - DK's right", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[585.0, 48.0, 1396.0, 5.0], scale=0.95, group=5, logic=lambda l: True, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Diddy's right", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[684.9, 48.0, 1312.0, 75.0], scale=0.95, group=5, logic=lambda l: True, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Tiny's right", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[635.0, 48.0, 1190.0, 148.0], scale=0.95, group=5, logic=lambda l: True, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Chunky's right", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[504.5, 48.0, 1200.0, 220.3], scale=0.95, group=5, logic=lambda l: True, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Lanky's right", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[473.1, 48.0, 1327.0, 292.7], scale=0.95, group=5, logic=lambda l: True, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - DK's instrument pad", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[481.0, 0.0, 1444.0, 328.0], group=5, moveless=False, logic=lambda l: l.swim, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Diddy's instrument pad", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[698.5, 0.0, 1424.5, 40.5], group=5, moveless=False, logic=lambda l: l.swim, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Tiny's instrument pad", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[747.0, 0.0, 1212.5, 111.8], group=5, moveless=False, logic=lambda l: l.swim, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Chunky's instrument pad", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[561.0, 0.0, 1101.0, 184.0], group=5, moveless=False, logic=lambda l: l.swim, door_type="tns"),
        DoorData(name="Crystal Caves: 5Door Igloo - Lanky's instrument pad", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[396.0, 0.0, 1244.0, 256.0], group=5, moveless=False, logic=lambda l: l.swim, door_type="tns"),
        DoorData(name="Crystal Caves: Ice Castle Area - Near Rock Switch", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1349.6, 330.0, 1079.0, 86.7], rx=4, group=6, logic=lambda l: True),
        DoorData(name="Crystal Caves: Between Funky and Ice Castle - on land", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[2240.65, 65.8, 1185.0, 89.25], group=6, logic=lambda l: True),
        DoorData(name="Crystal Caves: Between Funky and Ice Castle - underwater", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[2370.0, 0.0, 1096.0, 196.0], group=6, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: In Water Near W4 Opposite Cranky - right", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1187.0, 0.0, 2410.0, 133.5], group=7, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: In Water Near W4 Opposite Cranky - left", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1441.0, 0.0, 2385.0, 208.0], group=7, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Under Bridge to Cranky", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1140.0, 0.0, 1704.0, 350.4], group=7, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Under Handstand Slope", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1263.3, 93.0, 1291.0, 73.5], group=8, logic=lambda l: True),
        DoorData(name="Crystal Caves: Mini Monkey Ledge", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[3112.3, 257.0, 1142.0, 262.0], rx=5, scale=0.4, group=6, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Crystal Caves: Across from Snide", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1818.5, 82.0, 1450.0, 218.5], rx=-14, rz=21, group=7, logic=lambda l: True),
        DoorData(name="Crystal Caves: Slope to Cranky with Mini Monkey Hole", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1047.0, 190.0, 2426.0, 175.0], rz=5.5, group=8, logic=lambda l: True),
        DoorData(name="Crystal Caves: Level Entrance - right", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1827.0, -29.0, 342.0, 225.0], group=8, logic=lambda l: True),
        DoorData(name="Crystal Caves: Level Entrance - left", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1828.0, -29.0, 91.0, 315.5], group=8, logic=lambda l: True),
        DoorData(name="Crystal Caves: Ice Castle - left", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[2190.5, 343.0, 986.5, 314.2], scale=0.67, kong_lst=[Kongs.diddy, Kongs.lanky], group=6, moveless=False, logic=lambda l: l.isdiddy or (l.islanky and l.balloon), door_type="tns"),
        DoorData(name="Crystal Caves: Ice Castle - right", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[2221.0, 343.0, 957.0, 134.2], scale=0.67, kong_lst=[Kongs.diddy, Kongs.lanky], group=6, moveless=False, logic=lambda l: l.isdiddy or (l.islanky and l.balloon), door_type="tns"),
        DoorData(name="Crystal Caves: Igloo Area - left of entrance", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[637.0, 0.0, 1605.0, 174.75], rx=-4, group=5, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Igloo Area - Behind Tag Barrel Island", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[157.0, 0.0, 1575.0, 122.0], group=5, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Igloo Area - Behind Warp 1", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[282.5, 0.0, 892.0, 58.0], group=5, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Igloo Area - right of entrance", map=Maps.CrystalCaves, logicregion=Regions.IglooArea, location=[956.0, 0.0, 1222.0, 270.5], group=5, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Under Funky's Store", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[2868.0, 0.0, 1246.0, 113.0], group=6, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Next to Waterfall that's Next to Funky", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[3093.0, 0.0, 1262.0, 268.0], group=6, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: In Water Under Funky - left", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[3055.0, 0.0, 658.0, 1.28], group=6, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: In Water Under Funky - center", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[3221.0, 0.0, 820.0, 292.5], group=6, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: In Water Under Funky - right", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[3218.0, 0.0, 933.0, 256.3], group=6, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Crystal Caves: Ice Castle Interior - left", map=Maps.CavesFrozenCastle, logicregion=Regions.FrozenCastle, location=[340.0, 0.0, 146.0, 338.0], rx=6, kong_lst=[Kongs.lanky], group=9, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Crystal Caves: Ice Castle Interior - right", map=Maps.CavesFrozenCastle, logicregion=Regions.FrozenCastle, location=[202.0, 0.0, 456.5, 158.0], rx=6, kong_lst=[Kongs.lanky], group=9, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Crystal Caves: In Chunky's 5Door Cabin on a Book Shelf", map=Maps.CavesChunkyCabin, logicregion=Regions.ChunkyCabin, location=[403.5, 44.0, 579.0, 180.0], kong_lst=[Kongs.chunky], group=10, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Crystal Caves: Cabin Area - Near Candy - right", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[2907.0, 156.0, 2279.0, 171.0], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Cabin Area - Near Candy - far right", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[2813.0, 158.0, 2291.0, 200.0], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Outside Tiny's Cabin", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[3553.0, 260.0, 1940.0, 188.0], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Cabin Area - Next to Tag Barrel on 2nd Floor", map=Maps.CrystalCaves, logicregion=Regions.CabinArea, location=[3603.0, 260.0, 1457.0, 345.0], group=2, logic=lambda l: True),
        DoorData(name="Crystal Caves: Under Cranky Slope - small", map=Maps.CrystalCaves, logicregion=Regions.CrystalCavesMain, location=[1407.5, 95.0, 1519.0, 188.0], scale=0.43, group=8, logic=lambda l: True, door_type="wrinkly"),
    ],
    Levels.CreepyCastle: [
        DoorData(name="Creepy Castle: Lobby - Central Pillar (1)", map=Maps.CreepyCastleLobby, logicregion=Regions.CreepyCastleLobby, location=[499.978, 71.833, 634.25, 240.0], group=1, logic=lambda l: True, placed="wrinkly"),  # DK Door
        DoorData(name="Creepy Castle: Lobby - Central Pillar (2)", map=Maps.CreepyCastleLobby, logicregion=Regions.CreepyCastleLobby, location=[499.545, 71.833, 725.653, 300.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Diddy Door
        DoorData(name="Creepy Castle: Lobby - Central Pillar (3)", map=Maps.CreepyCastleLobby, logicregion=Regions.CreepyCastleLobby, location=[661.738, 71.833, 726.433, 60.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Lanky Door
        DoorData(name="Creepy Castle: Lobby - Central Pillar (4)", map=Maps.CreepyCastleLobby, logicregion=Regions.CreepyCastleLobby, location=[660.732, 71.833, 635.288, 118.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Tiny Door
        DoorData(name="Creepy Castle: Lobby - Central Pillar (5)", map=Maps.CreepyCastleLobby, logicregion=Regions.CreepyCastleLobby, location=[581.215, 71.833, 588.444, 182.0], group=1, logic=lambda l: True, placed="wrinkly"),  # Chunky Door
        DoorData(name="Creepy Castle: Near Greenhouse", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1543.986, 1381.167, 1629.089, 3.0], group=2, logic=lambda l: True, placed="tns"),  # T&S Portal by Greenhouse
        DoorData(name="Creepy Castle: Small Plateau", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1759.241, 903.75, 1060.8, 138.0], group=3, logic=lambda l: True, placed="tns"),  # T&S Portal by W2
        DoorData(name="Creepy Castle: Back of Castle", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1704.55, 368.026, 1896.767, 4.0], group=4, logic=lambda l: True, placed="tns"),  # T&S Portal around back
        DoorData(name="Creepy Castle: Near Funky's", map=Maps.CreepyCastle, logicregion=Regions.LowerCave, location=[1619.429, 200.0, 313.484, 299.0], group=5, logic=lambda l: True, placed="tns"),  # T&S Portal in Crypt Hub
        DoorData(name="Creepy Castle: Near Candy's", map=Maps.CreepyCastle, logicregion=Regions.UpperCave, location=[1025.262, 300.0, 1960.308, 359.0], group=6, logic=lambda l: True, placed="tns"),  # T&S Portal in Dungeon Tunnel
        DoorData(name="Creepy Castle: Next to Small Pool outside of the Big Tree", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1020.0, 391.0, 181.0, 270.0], group=7, logic=lambda l: True, door_type="tns"),
        DoorData(name="Creepy Castle: Against the Big Tree", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1200.0, 471.0, 254.0, 261.5], rx=-6, group=7, logic=lambda l: True),
        DoorData(name="Creepy Castle: Next to Tag Barrel at the Warp Pad Hub", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1545.0, 673.0, 944.0, 168.0], group=8, logic=lambda l: True),
        DoorData(name="Creepy Castle: Next to Cranky's", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[557.0, 1136.0, 1379.5, 273.0], group=9, logic=lambda l: True),
        DoorData(name="Creepy Castle: Outside Lanky's Greenhouse", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1606.0, 1391.0, 1906.0, 205.0], scale=0.95, group=2, logic=lambda l: True),
        DoorData(name="Creepy Castle: On Stairs to Tag Barrel at the Warp Pad Hub", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1724.0, 728.0, 874.0, 203.46], scale=0.5, group=8, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Next to Castle Moat - Above Tiny's Kasplat", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[296.0, 548.0, 1014.5, 230.0], group=8, logic=lambda l: True),
        DoorData(name="Creepy Castle: Snide's Battlement - left", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[792.0, 1794.0, 1535.5, 224.7], scale=0.75, group=10, logic=lambda l: True),
        DoorData(name="Creepy Castle: Snide's Battlement - center", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[593.0, 1794.0, 1449.0, 118.0], scale=0.75, group=10, logic=lambda l: True),
        DoorData(name="Creepy Castle: Snide's Battlement - right", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[684.0, 1794.0, 1192.0, 28.5], scale=0.75, group=10, logic=lambda l: True),
        DoorData(name="Creepy Castle: Next to Stairs to Drawing Drawbridge", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[738.25, 548.0, 549.0, 239.5], group=8, logic=lambda l: True),
        DoorData(name="Creepy Castle: Battlement with Rocketbarrel Barrel - left", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[160.0, 548.0, 654.0, 325.0], group=8, logic=lambda l: True),
        DoorData(name="Creepy Castle: Battlement with Rocketbarrel Barrel - right", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[280.0, 548.0, 460.0, 145.0], group=8, logic=lambda l: True),
        DoorData(name="Creepy Castle: Moat - Underwater by Diddy Barrel", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[532.0, 424.0, 844.0, 210.0], group=8, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Creepy Castle: Moat - Under Drawing Drawbridge", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[766.0, 424.0, 663.0, 323.0], group=8, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Creepy Castle: Moat - Next to Tunnel Entrance - left", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1328.0, 424.0, 956.0, 188.5], group=8, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Creepy Castle: Moat - Next to Tunnel Entrance - right", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[969.0, 424.0, 1008.5, 188.5], group=8, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Creepy Castle: Moat - Next to Ladder - left", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1075.0, 424.0, 647.0, 3.5], group=8, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Creepy Castle: Moat - Next to Ladder - right", map=Maps.CreepyCastle, logicregion=Regions.CreepyCastleMain, location=[1329.0, 424.0, 659.7, 337.2], group=8, moveless=False, logic=lambda l: l.swim),
        DoorData(name="Creepy Castle: Inside the Tree", map=Maps.CastleTree, logicregion=Regions.CastleTree, location=[1124.0, 400.0, 963.0, 247.3], rx=-3, group=11, moveless=False, logic=lambda l: True),
        DoorData(name="Creepy Castle: Library - Room with Big Books - left", map=Maps.CastleLibrary, logicregion=Regions.Library, location=[287.0, 190.0, 624.0, 180.0], kong_lst=[Kongs.donkey], group=12, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Library - Room with big Books - back", map=Maps.CastleLibrary, logicregion=Regions.Library, location=[103.4, 190.0, 209.0, 90.0], kong_lst=[Kongs.donkey], group=12, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Library - Next to Exit - left", map=Maps.CastleLibrary, logicregion=Regions.Library, location=[2817.0, 180.0, 201.0, 0.0], kong_lst=[Kongs.donkey], group=12, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Library - Next to Exit - right", map=Maps.CastleLibrary, logicregion=Regions.Library, location=[2826.0, 180.0, 549.0, 180.0], kong_lst=[Kongs.donkey], group=12, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Ballroom - Left Candle - left", map=Maps.CastleBallroom, logicregion=Regions.Ballroom, location=[113.7, 40.0, 692.0, 90.0], group=13, moveless=False, logic=lambda l: True),
        DoorData(name="Creepy Castle: Ballroom - Left Candle - right", map=Maps.CastleBallroom, logicregion=Regions.Ballroom, location=[113.7, 40.0, 497.0, 90.0], group=13, moveless=False, logic=lambda l: True),
        DoorData(name="Creepy Castle: Ballroom - Back Candle - left", map=Maps.CastleBallroom, logicregion=Regions.Ballroom, location=[455.0, 40.0, 107.4, 0.0], group=13, moveless=False, logic=lambda l: True),
        DoorData(name="Creepy Castle: Ballroom - Back Candle - right", map=Maps.CastleBallroom, logicregion=Regions.Ballroom, location=[652.0, 40.0, 107.4, 0.0], group=13, moveless=False, logic=lambda l: True),
        DoorData(name="Creepy Castle: Ballroom - Right Candle - left", map=Maps.CastleBallroom, logicregion=Regions.Ballroom, location=[987.0, 40.0, 501.0, 270.0], group=13, moveless=False, logic=lambda l: True),
        DoorData(name="Creepy Castle: Ballroom - Right Candle - right", map=Maps.CastleBallroom, logicregion=Regions.Ballroom, location=[987.0, 40.0, 705.0, 270.0], group=13, moveless=False, logic=lambda l: True),
        DoorData(name="Creepy Castle: Trash Can - Cheese", map=Maps.CastleTrashCan, logicregion=Regions.TrashCan, location=[592.0, 15.0, 576.6, 180.0], kong_lst=[Kongs.tiny], group=14, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Inside Chunky's Shed", map=Maps.CastleShed, logicregion=Regions.Shed, location=[397.0, 0.0, 160.0, 0.0], kong_lst=[Kongs.chunky], group=15, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Lower Tunnel - Under Peanut Switch", map=Maps.CastleLowerCave, logicregion=Regions.LowerCave, location=[120.0, 90.0, 1375.0, 88.75], group=16, logic=lambda l: True),
        DoorData(name="Creepy Castle: Lower Tunnel - Under Coconut and Pineapple Switches", map=Maps.CastleLowerCave, logicregion=Regions.LowerCave, location=[119.5, 90.0, 1149.0, 88.75], group=16, logic=lambda l: True),
        DoorData(name="Creepy Castle: Crypt - Under Lanky's Switch", map=Maps.CastleMausoleum, logicregion=Regions.Mausoleum, location=[803.6, 240.0, 1068.0, 270.0], scale=0.79, kong_lst=[Kongs.lanky, Kongs.tiny], group=17, moveless=False, logic=lambda l: True, door_type="wrinkly"),
        DoorData(name="Creepy Castle: Dungeon - Diddy's Chain Swinging Room - Behind Throne", map=Maps.CastleDungeon, logicregion=Regions.Dungeon, location=[535.0, 93.0, 3580.0, 180.0], scale=0.64, kong_lst=[Kongs.diddy], group=18, moveless=False, logic=lambda l: l.isdiddy and l.superDuperSlam, door_type="wrinkly"),  # A tad too easy to accidentally activate perhaps
    ],
}
