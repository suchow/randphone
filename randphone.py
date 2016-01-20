"""Generate a random valid US phone number."""
import random

def phone():

    valid = False
    while not valid:

        # Generate a random phone number.
        number = [random.randint(0, 9) for i in range(10)]

        # Assume it is valid.
        valid = True

        # The format of an area code is NXX, where N is any digit 2 through 9 and X
        # is any digit 0 through 9.
        if (number[0] == 0) or (number[0] == 1):
            valid = False

        # When the second and third digits of an area code are the same, that code
        # is called an easily recognizable code (ERC). ERCs designate special
        # services; e.g., 888 for toll-free service.
        if number[1] == number[2]:
            valid = False

        # N11: These 8 ERCs, called service codes, are not used as area codes.
        # (This is redundant with the previous rule.)
        if (number[1] == 1) and (number[2] == 1):
            valid = False

        # N9X: The 80 codes in this format, called expansion codes, have been
        # reserved for use during the period when the current 10-digit NANP number
        # format undergoes expansion.
        if number[1] == 9:
            valid = False

        # N11s are not used as area codes.
        if number[1] == 1 and number[2] == 1:
            valid = False

        # 37X and 96X: Two blocks of 10 codes each have been set aside by the INC
        # for unanticipated purposes where it may be important to have a full range
        # of 10 contiguous codes available.
        if ((number[0] == 3 and number[1] == 7) or
            (number[0] == 9 and number[1] == 6)):
            valid == False

        # First digit of exchange code cannot be 0 or 1.
        if (number[3] == 0) or (number[3] == 1):
            valid = False

        # Second and third digits of exchange code cannot both be 1.
        if (number[4] == 1) and (number[5] == 1):
            valid = False

    return "({}) {}-{}".format(
        "".join([str(d) for d in number[:3]]),
        "".join([str(d) for d in number[3:6]]),
        "".join([str(d) for d in number[6:]]))
