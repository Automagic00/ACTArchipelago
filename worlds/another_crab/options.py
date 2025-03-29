from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

class Goal(Choice):
    """Choose your goal for the multiworld"""
    display_name: str = "Goal"
    option_firth = 0
    option_roland = 1
    default = 0

# might be worth finding a way to combine ForkLocation and AllowForkless into one option for simplicity's sake

class ForkLocation(Choice):
    """Choose where the Fork(weapon) location is set. Does nothing if [Allow Forkless] option is enabled.
    - Shuffled Early Local: Forces Fork location to be somewhere early in your own game.
    - Shuffled Early Global: Forces Fork location to be somewhere early in any game.
    - Vanilla Location: Forces Fork to be placed at its intended location."""
    display_name: str = "Fork Location"
    option_vanilla_location = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    default = 0

class AllowForkless(Choice):
    """If enabled, allows for the Fork to not be required early on, meaning you may have to play some amount of the game without it. Ignores [Fork Location] option and shuffles Fork into item pool if enabled.
    - Disabled: Fork is required to fight early bosses, meaning that it will be placed early in your run.
    - Forkless Easy: Ensures that the intended forkless strategy is not too advanced (Includes logic for adaptation and shellspell focused builds)
    - Forkless Hard: Allows for the possibility of more advanced forkless strategies to be necessary (Includes logic for rolling attack and summon focused builds)"""
    display_name: str = "Allow Forkless"
    option_disabled = 0
    option_forkless_easy = 1
    option_forkless_hard = 2
    default = 0

# class LogicRules(Choice):
#    """Set the preferred logic rules for your game
#    - Restricted: Standard logic, no skips/glitches required to complete goal.
#    - No Major Glitches: Allows for {list of easy logic rules here} to be needed to complete goal.
#    - Unrestricted: In addition to the list under No Major Glitches allows for {list of more advanced rules here} to be needed to complete goal."""
#    display_name:str = "Logic Rules"
#    option_restricted = 0
#    option_no_major_glitches = 1
#    option_unrestricted = 2
#    default = 0
 
class ShelleportLocation(Choice):
    """Choose where the Shelleport (fast travel) skill location is set
    - Shuffled: Shelleport is placed into the item pool.
    - Shuffled Early Local: Forces Shelleport location to be somewhere early in your own game.
    - Shuffled Early Global: Forces Shelleport location to somewhere early in any game.
    - Starting Items: Places Shelleport in your starting inventory.
    - Vanilla Location: Forces Shelleport to be placed at its intended location"""
    display_name: str = "Shelleport Location"
    option_shuffled = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    option_starting_items = 3
    option_vanilla_location = 4
    default = 1

class FishingLineLocation(Choice):
    """Choose where the Fishing Line (grapple) location is set
    - Shuffled: Fishing Line is placed into item pool.
    - Vanilla Location: Forces Fishing Line to be placed at its intended location"""
    display_name: str = "Fishing Line Location"
    option_shuffled = 0
    option_vanilla_location = 1
    default = 0

class RandomShells(Toggle):
    """Choose whether or not shells will be randomized. Only randomizes shells within other shell locations."""
    display_name: str = "Random Shells"
    default: bool = True

class RemoveCostumes(Toggle):
    """Set to true to remove costumes from the item pool."""
    display_name: str = "Remove Costumes"
    default: bool = False

class MicroplasticMultiplier(Range):
    """Multiplies the ammount of microplastics you recieve. Decimal values currently not supported."""
    display_name: str = "Microplastic Multiplier"
    range_start: float = 1
    range_end: float = 100
    default: float = 1

class TrapAmount(Range):
    """Defines a percentage of the filler items to be replaced with trap items
    Set to 0 to not include any traps"""
    display_name: str = "Trap Amount"
    range_start: int = 0
    range_end: int = 100
    default: int = 0

class DeathLink(Toggle):
    """Enables Death Link"""
    display_name: str = "Death Link"
    default: bool = False

@dataclass
class ACTGameOptions(PerGameCommonOptions):
    goal: Goal
    fork_location: ForkLocation
    allow_forkless: AllowForkless
    #logic_rules: LogicRules
    shelleport_location: ShelleportLocation
    fishing_line_location: FishingLineLocation
    randomshells: RandomShells
    remove_costumes: RemoveCostumes
    microplasticMultiplier: MicroplasticMultiplier
    trapamount: TrapAmount
    deathlink: DeathLink