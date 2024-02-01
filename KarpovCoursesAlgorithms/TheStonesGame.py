"""
Task 8.

You have a list of int values (aka stones) which indicates weights of each rock.

You play the game with these rocks. For each turn you need to choose the two weightiest rocks which hits each other.
If the two rocks has equal weights then you destroy both of them in other way you destroy the lightest rock and for
other rock you need to find the result diff.

In other words, let x and y to be weights of the rocks. Then you will have next options:
    1. If x == y we delete both rocks.
    2. Elif x > y then we save x = x - y.
    3. Elif y > x then we save y = y - x.

The game will be finished only if you have left 1 rock or none.


Write function "last_stone(stones)" which take list of values and return value of the latest rock in the game or 0 if
none."""


def last_stone(stones: list[int]) -> int:
    if len(stones) == 1:
        return stones[0]
    elif len(stones) == 0:
        return 0
    else:
        first_rock = 0
        first_rock_ind = None
        second_rock = 0
        second_rock_ind = None
        for ind_val, val in enumerate(stones):
            if val >= first_rock:
                first_rock = val
                first_rock_ind = ind_val
        for ind_val, val in enumerate(stones):
            if val >= second_rock and ind_val != first_rock_ind:
                second_rock = val
                second_rock_ind = ind_val
        if first_rock > second_rock:
            first_rock = first_rock - second_rock
            stones[first_rock_ind] = first_rock
            stones.pop(second_rock_ind)
        elif second_rock > first_rock:
            second_rock = second_rock - first_rock
            stones[second_rock_ind] = second_rock
            stones.pop(first_rock_ind)
        else:
            stones.pop(first_rock_ind)
            stones.pop(second_rock_ind)
        return last_stone(stones)


if __name__ == "__main__":
    stones = [2, 3, 3, 1]
    if last_stone(stones) == 1:
        print("OK")
    else:
        print("Failed")
