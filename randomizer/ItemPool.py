"""Contains functions related to setting up the pool of shuffled items."""
import itertools

from randomizer.Enums.Items import Items
from randomizer.Enums.Locations import Locations
from randomizer.Location import LocationList
from randomizer.Item import ItemFromKong


def PlaceConstants(settings):
    """Place items which are to be put in a hard-coded location."""
    # Banana Hoard: Pseudo-item used to represent game completion by defeating K. Rool
    LocationList[Locations.BananaHoard].PlaceItem(Items.BananaHoard)
    # Keys kept at key locations so boss completion requires
    LocationList[Locations.JapesKey].PlaceItem(Items.JungleJapesKey)
    LocationList[Locations.AztecKey].PlaceItem(Items.AngryAztecKey)
    LocationList[Locations.FactoryKey].PlaceItem(Items.FranticFactoryKey)
    LocationList[Locations.GalleonKey].PlaceItem(Items.GloomyGalleonKey)
    LocationList[Locations.ForestKey].PlaceItem(Items.FungiForestKey)
    LocationList[Locations.CavesKey].PlaceItem(Items.CrystalCavesKey)
    LocationList[Locations.CastleKey].PlaceItem(Items.CreepyCastleKey)
    LocationList[Locations.HelmKey].PlaceItem(Items.HideoutHelmKey)
    # Settings-dependent locations
    if settings.TrainingBarrels == "normal":
        LocationList[Locations.IslesVinesTrainingBarrel].PlaceItem(Items.Vines)
        LocationList[Locations.IslesSwimTrainingBarrel].PlaceItem(Items.Swim)
        LocationList[Locations.IslesOrangesTrainingBarrel].PlaceItem(Items.Oranges)
        LocationList[Locations.IslesBarrelsTrainingBarrel].PlaceItem(Items.Barrels)
    elif settings.TrainingBarrels == "startwith":
        LocationList[Locations.IslesVinesTrainingBarrel].PlaceItem(Items.NoItem)
        LocationList[Locations.IslesSwimTrainingBarrel].PlaceItem(Items.NoItem)
        LocationList[Locations.IslesOrangesTrainingBarrel].PlaceItem(Items.NoItem)
        LocationList[Locations.IslesBarrelsTrainingBarrel].PlaceItem(Items.NoItem)
    if settings.StartWithKongs:
        LocationList[Locations.DiddyKong].PlaceItem(Items.NoItem)
        LocationList[Locations.LankyKong].PlaceItem(Items.NoItem)
        LocationList[Locations.TinyKong].PlaceItem(Items.NoItem)
        LocationList[Locations.ChunkyKong].PlaceItem(Items.NoItem)
    if settings.StartWithCrankyMoves:
        LocationList[Locations.SimianSlam].PlaceItem(Items.NoItem)
        LocationList[Locations.SuperSimianSlam].PlaceItem(Items.NoItem)
        LocationList[Locations.SuperDuperSimianSlam].PlaceItem(Items.NoItem)
        LocationList[Locations.BaboonBlast].PlaceItem(Items.NoItem)
        LocationList[Locations.StrongKong].PlaceItem(Items.NoItem)
        LocationList[Locations.GorillaGrab].PlaceItem(Items.NoItem)
        LocationList[Locations.ChimpyCharge].PlaceItem(Items.NoItem)
        LocationList[Locations.RocketbarrelBoost].PlaceItem(Items.NoItem)
        LocationList[Locations.SimianSpring].PlaceItem(Items.NoItem)
        LocationList[Locations.Orangstand].PlaceItem(Items.NoItem)
        LocationList[Locations.BaboonBalloon].PlaceItem(Items.NoItem)
        LocationList[Locations.OrangstandSprint].PlaceItem(Items.NoItem)
        LocationList[Locations.MiniMonkey].PlaceItem(Items.NoItem)
        LocationList[Locations.PonyTailTwirl].PlaceItem(Items.NoItem)
        LocationList[Locations.Monkeyport].PlaceItem(Items.NoItem)
        LocationList[Locations.HunkyChunky].PlaceItem(Items.NoItem)
        LocationList[Locations.PrimatePunch].PlaceItem(Items.NoItem)
        LocationList[Locations.GorillaGone].PlaceItem(Items.NoItem)

def Blueprints():
    """Return all blueprint items."""
    blueprints = [
        Items.DKIslesDonkeyBlueprint,
        Items.DKIslesDiddyBlueprint,
        Items.DKIslesLankyBlueprint,
        Items.DKIslesTinyBlueprint,
        Items.DKIslesChunkyBlueprint,
        Items.JungleJapesDonkeyBlueprint,
        Items.JungleJapesDiddyBlueprint,
        Items.JungleJapesLankyBlueprint,
        Items.JungleJapesTinyBlueprint,
        Items.JungleJapesChunkyBlueprint,
        Items.AngryAztecDonkeyBlueprint,
        Items.AngryAztecDiddyBlueprint,
        Items.AngryAztecLankyBlueprint,
        Items.AngryAztecTinyBlueprint,
        Items.AngryAztecChunkyBlueprint,
        Items.FranticFactoryDonkeyBlueprint,
        Items.FranticFactoryDiddyBlueprint,
        Items.FranticFactoryLankyBlueprint,
        Items.FranticFactoryTinyBlueprint,
        Items.FranticFactoryChunkyBlueprint,
        Items.GloomyGalleonDonkeyBlueprint,
        Items.GloomyGalleonDiddyBlueprint,
        Items.GloomyGalleonLankyBlueprint,
        Items.GloomyGalleonTinyBlueprint,
        Items.GloomyGalleonChunkyBlueprint,
        Items.FungiForestDonkeyBlueprint,
        Items.FungiForestDiddyBlueprint,
        Items.FungiForestLankyBlueprint,
        Items.FungiForestTinyBlueprint,
        Items.FungiForestChunkyBlueprint,
        Items.CrystalCavesDonkeyBlueprint,
        Items.CrystalCavesDiddyBlueprint,
        Items.CrystalCavesLankyBlueprint,
        Items.CrystalCavesTinyBlueprint,
        Items.CrystalCavesChunkyBlueprint,
        Items.CreepyCastleDonkeyBlueprint,
        Items.CreepyCastleDiddyBlueprint,
        Items.CreepyCastleLankyBlueprint,
        Items.CreepyCastleTinyBlueprint,
        Items.CreepyCastleChunkyBlueprint,
    ]
    return blueprints


def BlueprintAssumedItems():
    """Items which are assumed to be owned while placing blueprints."""
    return LowPriorityItems() + ExcessItems()


def Keys():
    """Return all key items."""
    keys = [
        Items.JungleJapesKey,
        Items.AngryAztecKey,
        Items.FranticFactoryKey,
        Items.GloomyGalleonKey,
        Items.FungiForestKey,
        Items.CrystalCavesKey,
        Items.CreepyCastleKey,
        Items.HideoutHelmKey,
    ]
    return keys


def Kongs(settings):
    """Return Kong items depending on settings."""
    kongs = []
    if not settings.StartWithKongs:
        kongs = [
            Items.Donkey,
            Items.Diddy,
            Items.Lanky,
            Items.Tiny,
            Items.Chunky
        ]
        kongs.remove(ItemFromKong(settings.StartingKong))
    return kongs


def Guns():
    """Return all gun items."""
    guns = [
        Items.Coconut,
        Items.Peanut,
        Items.Grape,
        Items.Feather,
        Items.Pineapple,
    ]
    return guns


def Instruments():
    """Return all instrument items."""
    instruments = [
        Items.Bongos,
        Items.Guitar,
        Items.Trombone,
        Items.Saxophone,
        Items.Triangle,
    ]
    return instruments

def TrainingBarrelAbilities():
    """Return all training barrel abilities."""
    barrelAbilities = [
        Items.Vines,
        Items.Swim,
        Items.Oranges,
        Items.Barrels,
    ]
    return barrelAbilities


def Upgrades(settings):
    """Return all upgrade items."""
    upgrades = []
    # Add training barrel items to item pool if shuffled
    if settings.TrainingBarrels == "shuffled":
        upgrades.extend(TrainingBarrelAbilities())
    # Add either progressive upgrade items or individual ones depending on settings
    if not settings.StartWithCrankyMoves:
        upgrades.extend(itertools.repeat(Items.ProgressiveSlam, 3))
        if settings.ProgressiveUpgrades:
            upgrades.extend(itertools.repeat(Items.ProgressiveDonkeyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveDiddyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveLankyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveTinyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveChunkyPotion, 3))
        else:
            upgrades.extend([
                Items.BaboonBlast,
                Items.StrongKong,
                Items.GorillaGrab,
                Items.ChimpyCharge,
                Items.RocketbarrelBoost,
                Items.SimianSpring,
                Items.Orangstand,
                Items.BaboonBalloon,
                Items.OrangstandSprint,
                Items.MiniMonkey,
                Items.PonyTailTwirl,
                Items.Monkeyport,
                Items.HunkyChunky,
                Items.PrimatePunch,
                Items.GorillaGone,
            ])
    upgrades.append(Items.CameraAndShockwave)
    
    return upgrades


def HighPriorityItems(settings):
    """Get all items which are of high importance logically.

    Placing these first prevents fill failures.
    """
    itemPool = []
    itemPool.extend(Kongs(settings))
    itemPool.extend(Guns())
    itemPool.extend(Instruments())
    itemPool.extend(Upgrades(settings))
    return itemPool


def HighPriorityAssumedItems():
    """Items which are assumed to be owned while placing high priority items."""
    return Blueprints() + LowPriorityItems() + ExcessItems()


def LowPriorityItems():
    """While most of these items still have logical value they are not as important."""
    itemPool = []

    itemPool.extend(itertools.repeat(Items.GoldenBanana, 100))
    itemPool.extend(itertools.repeat(Items.BananaFairy, 20))
    itemPool.extend(itertools.repeat(Items.BananaMedal, 15))
    itemPool.extend(itertools.repeat(Items.BattleCrown, 4))
    itemPool.append(Items.NintendoCoin)
    itemPool.append(Items.RarewareCoin)

    return itemPool


def ExcessItems():
    """Items which either have no logical value or are excess copies of those that do."""
    itemPool = []

    # Weapon upgrades
    itemPool.append(Items.HomingAmmo)
    itemPool.append(Items.SniperSight)
    itemPool.extend(itertools.repeat(Items.ProgressiveAmmoBelt, 2))

    # Instrument upgrades
    itemPool.extend(itertools.repeat(Items.ProgressiveInstrumentUpgrade, 3))

    # Collectables
    itemPool.extend(itertools.repeat(Items.GoldenBanana, 101))
    itemPool.extend(itertools.repeat(Items.BattleCrown, 6))
    itemPool.extend(itertools.repeat(Items.BananaMedal, 25))

    return itemPool
