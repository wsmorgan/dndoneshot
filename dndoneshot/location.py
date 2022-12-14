"""Code for generating location based adventures."""

from random import randrange, shuffle

def location_adventure(custom_goals=None, sub_loc=None, custom_npcs=None,
                        custom_climax=None, custom_intros=None):
    """Generates suggestions for a location based one shot adventure.

    Args:
        custom_goals (dict): A dictionary of goals and sub locations, i.e.,
            dungeons, settlement..., where the keys are the sub locations and
            the values are a list of goals.
        sub_loc (str): The name of the users desired sub_location.
        custom_npcs (dict): A dictionary of custom npcs defined by the user.
            Keys may include `villians`, `allies`, `patrons`. Values are a list.
        costum_intros (list): A list of potential intros.
        custom_climax (list): A list of potential climax events.

    Returns:
        An adventures goals, sub location, important NPCs, a suggested intro
        and a suggested climax.
    """

    loc, goals = generate_goals(custom_goals=custom_goals, sub_loc=sub_loc)
    npcs = generate_NPCs(custom_npcs=custom_npcs)
    intro = generate_intro(custom_intros=custom_intros)
    climax = generate_climax(custom_climax=custom_climax)

    return goals, loc, npcs, intro, climax

def generate_goals(custom_goals=None, sub_loc=None):
    """Selects more detailed location and a goal either from the set of
    goals provided by the user, or from the DMG supplied suggestions.

    Args:
        custom_goals (dict): A dictionary of goals and sub locations, i.e.,
            dungeons, settlement..., where the keys are the sub locations and
            the values are a list of goals.
        sub_loc (str): The name of the users desired sub_location.

    Returns:
        The sub location, i.e., dungeon, wilderness, .., and the goal, or goals,
        selected.
    """

    goals_by_sub_loc = {"dungeon": ["Stop the dungeons monstrous inhabitants from raiding the surface world.",
                        "Foil a villain's evil scheme.",
                        "Destroy a magical threat inside the dungeon.",
                        "Acquire Treasure.",
                        "Find a particular item for a specific purpose.",
                        "Rescue a captive.",
                        "Discover the fato of a previouse adventuring party.",
                        "Find an NPC who disappeared in the area.",
                        "Slay a dragon or another chalenging monster.",
                        "Discover the nature and origin of a strange location or phenomenon.",
                        "Pursue fleeing foes taking refuge in he dungeon.",
                        "Escape from captivity in the dungeon.",
                        "Clear a ruin so it can be rebuilt and reoccupied.",
                        "Discover why a villian is interested in the dungeon.",
                        "Win a bet or complete a rite of passage by surviving in the dungeon for a certain amount of time.",
                        "Parley with a villain in the dungeon.",
                        "Hide from a threat outside the dungeon.",
                        "pick_2."],
            "wilderness":, ["Locate a dungeon or other site of interest.",
                            "Assess the scope of a natural or unnatural disaster.",
                            "Escort an NPC to a destination.",
                            "Arrive at a destination without being seen by the villain's forces.",
                            "Stop monsters from raiding caravants and farms.",
                            "Establish trade with a distant town.",
                            "Protect a caravan traveling to a distant town.",
                            "Map a new land.",
                            "Find a place to establish a colony.",
                            "Find a natureal resource.",
                            "Hunt a specific monster.",
                            "Return home from a distant place.",
                            "Obtain information from a reclusive hermit.",
                            "Find an object that was lost in the wilds.",
                            "Discover the fate of a missing group of explorers.",
                            "Pursue fleeing foes.",
                            "Assess the size of an approaching army.",
                            "Escape the reign of a tyrant.",
                            "Protect a wilderness site from attackers.",
                            "pick_2"],
            "other": ["Seize control of a fortified location such as a fortress, town, or ship.",
                    "Defend a location from attackers.",
                    "Retrieve an object from inside a secure location in a settlement.",
                    "Retrieve an object from a caravan.",
                    "Salvage an object or goods from a lost vessel or caravan.",
                    "Break a prisoner out of a jail or prison comp.",
                    "Escape from a jail or prison camp.",
                    "Successfully travel through an obstacle course to gain recognition or reward.",
                    "Infiltrate a fortified location.",
                    "Find the source of strange occurrences in a haunted house or other location.",
                    "Interfere with the operation of a business.",
                    "Rescue a character, monster, or object from a natural or unnatural disaster."]}


    if user_defined_goals is None or len(user_defined_goals.keys()) < 1:
        this_goals = goals_by_sub_loc
    else:
        this_goals = user_defined_goals

    if sub_loc is None:
        available_sub_locs = list(this_goals.keys())
        shuffle(available_sub_locs)
        sub_loc = available_sub_locs[0]

    if sub_loc not in this_goals.keys():
        raise IOError("The sub location {0} is not in the goals dictionary.".format(sub_loc))

    available_goals = this_goals[sub_loc]

    goal = randrange(len(available_goals))

    goal = available_goals[goal]

    if goal == "pick_2":
        new_goal = []
        while len(new_goal) < 2:
            ng = randrange(len(available_goals))
            ng = available_goals[ng]
            if ng == "pick_2":
                continue

            new_goal.append(ng)

        goal = new_goal
    else:
        goal = [goal]

    final_goals = []
    for g in goal:
        sub_new_goals = None
        if g == "Locate a dungeon or other site of interest.":
            if "dungeon" not in this_goals.keys():
                raise IOError("Dungeons must be a sub location for the goal: {0} to be used.".format(g))

            available_goals = this_goals["dungeon"]

            ng = randrange(len(available_goals))
            ng = available_goals[ng]

            if ng == "pick_2":
                sub_new_goals = []
                while len(sub_new_goals) < 2:
                    sub_ng = randrange(len(available_goals))
                    sub_ng = available_goals[sub_ng]
                    if sub_ng == "pick_2":
                        continue

                    sub_new_goals.append(sub_ng)
            else:
                sub_new_goals = [sub_new_goals]

        final_goals.append(g)
        if sub_new_goals is not None:
            final_goals.exentd(sub_new_goals)

    return sub_loc, final_goals

def generate_NPCs(custom_npcs=None):
    """Generates important NPC's for the one shot including a villian,
    allies, and patrons.

    Args:
        custom_npcs (dict): A dictionary of custom npcs defined by the user.
            Keys may include `villians`, `allies`, `patrons`. Values are a list.

    Returns:
        The selecetd villian, allies and patrons for the one shot.

    """
    suggested_npcs = {"villians": ["Beast or monstrosity with no particular angenda.",
                                    "Aberration bent on coruption or domination.",
                                    "Fiend bent on corruption or destruction.",
                                    "Drangon bent on domination and plunder.",
                                    "Giant bent on plunder.",
                                    "Undead with any agenda.",
                                    "Undead with any agenda.",
                                    "Fey with mysterious goal.",
                                    "Humanoid cultist.",
                                    "Humanoid cultist.",
                                    "Humanoid conqueror.",
                                    "Humanoid conqueror.",
                                    "Humanoid seeking revenge.",
                                    "Humanoid schemer seeking to rule.",
                                    "Humanoid scheme seeking to rule.",
                                    "Humanoid criminal mastermind.",
                                    "Humanoid raider or ravager.",
                                    "Humanoid under a curse.",
                                    "Misguided Humanoid zealot."],
                    "allies": ["Skilled adventurer.",
                                "Inexperienced adventurer.",
                                "Enthusiastic commoner.",
                                "Soldier.",
                                "Priest.",
                                "Sage.",
                                "Revenge seeker.",
                                "Raving lunatic.",
                                "Celestial ally.",
                                "Fey ally.",
                                "Disguised monster.",
                                "Villain posing as an ally."],
                    "patrons": ["Retired adventurer.",
                                "Retired adventurer.",
                                "Local ruler.",
                                "Local ruler.",
                                "Military officer.",
                                "Military officer.",
                                "Temple official.",
                                "Temple official.",
                                "Sage.",
                                "Sage.",
                                "Respected Elder.",
                                "Respected Elder.",
                                "Deity or Celestial.",
                                "Mysterious fey.",
                                "Old friend.",
                                "Former teacher.",
                                "Parent or other family member.",
                                "Desperate commoner.",
                                "Embattled merchant.",
                                "Villain posing as patron."]}

    if custom_npcs is None:
        npc_data = suggested_npcs
    else:
        npc_data = custom_npcs

    npcs_selected = {}
    for npc in ["villians", "allies", "patrons"]:
        if npc not in npc_data.keys():
            candidates = suggested_npcs[npc]
        else:
            candidates = npc_data[npc]

        selected = randrange(len(candidates))
        selecetd = candidates[selecetd]

        npcs_selected[npc] = selecetd

    return npcs_selected

def generate_intro(custom_intros=None):
    """Suggested introductions for the one shot.

    Args:
        custom_intros (list): A list of potential intros.

    Returns:
        One of the introductions.
    """

    suggested_intros = ["While traveling in the wilderness, the characters fall into a sinkhole that open beneath their feet, dropping them into the adventure location.",
                        "While traveling in the wilderness, the characters notice the entrance to the adventure location.",
                        "While traveling on a road, the characters are attacked by monsters that flee into the nearby adventure location.",
                        "The adventurers find a map on a dead body. In addition to the map setting up the adventure, the adventure's villian want the map.",
                        "A mysterious magic item or cruel villian teleports the charactes to the adventure location.",
                        "A stranger approaches the characters in a tavern and urges them toward the adventure location.",
                        "A town or village needs volunteers to go to the adventure location.",
                        "An NPC the characters care about needs them to go to the adventure location.",
                        "An NPC the characters must obey orders them to go to the adventure location.",
                        "An NPC the characters respect asks them to go to the adventure location.",
                        "One night, the characters all dream about entering the adventure location.",
                        "A ghost appears and terrorizes a village. Research reveals that it can be put to rest only by entering the adventure location."]

    if costum_intros is None or (isinstance(custom_intros, list) and len(costum_intros) < 1):
        intros = suggested_intros
    else:
        intros = custom_intros

    shuffle(intros)

    return intros[0]

def generate_climax(custom_climax=None):
    """Suggests a climax for the adventure one shot.

    Args:
        custom_climax (list): A list of potential climax events.

    Returns:
        A selected climax.
    """

    suggested_climax = ["The adventurers confront the main villain and a group of minions in a bloody battle to the finish.",
                        "The adventurers chase the villain while dodging obstacles designed to thwart them, leading ot a final confrontation in or outside the villain's refuge.",
                        "The actions of the adventurers or the villain result in a cataclysmic event that the adventurers must escape.",
                        "The adventurers race to the site where the villain is brining a master plan to its conclusion, arriving just as the plan is about to be completed.",
                        "The villain and two or three lieutenants perform seperate rites in a large room. The adventurers must disrupt all the rites at the same time.",
                        "An ally betrays the adventurers as thy're about to achieve their goal.",
                        "A portal open to another plane of existence. Creatures on the other side spill out, forcing the adventurers to close the portal and deal with the villain at the same time.",
                        "Traps, hazards, or animated objects turn against the adventurers while the main villain attacks.",
                        "The dungeon begins to collapse while the adventurers face the main villain, who attempts to escape inthe chaos.",
                        "A threat more powerful than the adventurers appears, destroys the main villain, and then tuns its attention on the characters.",
                        "The adventurers must choose whether to pursue the fleeing main villain or save an NPC they care about on a group of innocents.",
                        "The adventurers must discover the main villain's secret weakness before they can hope to defeat that villain."]

    if custom_climax is None or (isinstance(custom_climax, list) and len(custom_climax) < 1):
        climaxes = suggested_climax

    else:
        climaxes = custom_climax

    shuffle(climaxes)
    return climaxes[0]
