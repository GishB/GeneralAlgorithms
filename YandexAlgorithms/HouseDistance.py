"""
Task:
    Find max distance between nearest shop and house.

Input:
    Expected an array of shape (10,1) where each value represents building type. 1 is living house, 2 is a shop and
    0 is an office building.

    ***Guaranteed that each array contains one living house and one office building values.***

Output:
    Expected one int value which represents max distance between house and nearest shop.

Notes:
    Distance between two nearest buildings equal to 1. For example:
     1) if two buildings are close to each other than distance equals to 1.
     2) if two buildings are close but between them located one more building than distance equals to 2 (we count this
     additional building).
     3) Keep in mind that it is expected to see maximum distance over all minimum distances between living houses and
     shops (the same nearest shop and house).

Test example:
    input:
        >> 2 0 1 1 0 1 0 2 1 2
    output:
        >> 3
"""


def max_distance_between_shop_and_living_house(array: list[int]) -> int:
    """ Find maximum distance between types 1 and 2.

    Note:
        - Complexity is O(N)*O(k). Where N is a number of living houses and k is a number of shops in array.

    Arg:
        array: list of buildings in 1D representation.

    Return:
        max distance between nearest shop and living house.
    """
    living_house_indexes: list[int] = [i for i, v in enumerate(array) if int(v) == 1]
    shop_indexes: list[int] = [i for i, v in enumerate(array) if int(v) == 2]
    list_of_min_distances_for_all_houses_and_shops: list[int] = []
    for i in living_house_indexes:
        minimum_distance_for_curent_house_index = min([abs(i - g) for g in shop_indexes])
        list_of_min_distances_for_all_houses_and_shops.append(minimum_distance_for_curent_house_index)
    return max(list_of_min_distances_for_all_houses_and_shops)


if __name__ == "__main__":
    # number_list = input().split()
    test_array = [2, 0, 1, 1, 0, 1, 0, 2, 1, 2]
    out = max_distance_between_shop_and_living_house(test_array)
    print(out)
