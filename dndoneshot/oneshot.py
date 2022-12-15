"""Main function for helping write a one shot. Rolls all the needed dice to make
some of the decisions for the DM.
"""

import sys
import numpy as np
from random import seed, shuffle

from dndoneshot.io import read_in_config
from dndoneshot.location import location_adventure

xp_per_level = {1: np.array([25, 50, 75, 100]),
                2: np.array([50, 100, 150, 200]),
                3: np.array([75, 150, 225, 400]),
                4: np.array([125, 250, 375, 500]),
                5: np.array([250, 500, 750, 1100]),
                6: np.array([300, 600, 900, 1400]),
                7: np.array([350, 750, 1100, 1700]),
                8: np.array([450, 900, 1400, 2100]),
                9: np.array([550, 1100, 1600, 2400]),
                10: np.array([600, 1200, 1900, 2800]),
                11: np.array([800, 1600, 2400, 3600]),
                12: np.array([1000, 2000, 3000, 4500]),
                13: np.array([1100, 2200, 3400, 5100]),
                14: np.array([1250, 2500, 3800, 5700]),
                15: np.array([1400, 2800, 4300, 6400]),
                16: np.array([1600, 3200, 4800, 7200]),
                17: np.array([2000, 3900, 5900, 8800]),
                18: np.array([2100, 4200, 6300, 9500]),
                19: np.array([2400, 4900, 7300, 10900]),
                20: np.array([2800, 5700, 8500, 12700])}

def set_seed(rseed):
    """Sets the random seed.

    Args:
        rseed (int): The seed to use for random number generation.
    """

    seed(rseed)
    np.random.seed(rseed)

def xp_setup_calculator(player_levels):
    """Calculates the daily and the difficulty leves xp modifiers for the party.

    Args:
        player_levels (list): A list of the players levels.

    Returns:
        expected daily xp and the xp amount per encounter difficulty level.
    """

    daily_xp_dict = {1: 300, 2: 600, 3: 1200, 4: 1700, 5: 3500, 6: 4000,
                    7: 5000, 8: 6000, 9: 7500, 10: 9000, 11: 10500,
                    12: 11500, 13: 13500, 14: 1500, 15: 1800, 16: 20000,
                    17: 2500, 18: 2700, 19: 30000, 20: 40000}

    daily_xp_max = 0
    xp_diff_levels = np.array([0, 0, 0, 0])
    for l in player_levels:
        daily_xp_max += daily_xp_dict[l]
        xp_diff_levels += xp_per_level[l]

    return daily_xp_max, xp_diff_levels

def build_one_shot(input_file):
    """Builds a one shot from the supplied input file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        The information for the one shot which will also be
    written to a file.
    """

    input_data = read_in_config(input_file)

    # set starting fields
    kingdom = None

    if "seed" in input_data:
        set_seed(input_data["seed"])

    # calculate the xp targets
    daily_xp_max, encount_xp_level = xp_setup_calculator(input_data["player_levels"])


    # find region data
    if "kingdoms" in input_data:
        kingdoms = input_data["kingdoms"]
        shuffle(kingdoms)
        kingdom = kingdoms[0]

    # Determine type of oneshot.
    type_methods = {"location": location_adventure}
    if "type" in input_data:
        type = input_data["type"]
    else:
        types = ["location"]
        shuffle(types)
        type = types[0]

    type_res = type_methods[type](**input_data)


    print("The adventure will take place in {}.".format(kingdom))
    print(type_res)

    return kingdom

if __name__ == '__main__': # pragma: no cover
    build_one_shot(sys.argv[1])
