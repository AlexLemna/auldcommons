# SPDX-FileCopyrightText: 2018 Brad Solomon <stackoverflow.com/q/50932755>
#
# SPDX-License-Identifier: CC-BY-SA-4.0


# FROM: https://stackoverflow.com/q/50932755
def set_arbitrary_nest(keys, value):
    """
    >>> keys = 1, 2, 3
    >>> value = 5
    result --> {1: {2: {3: 5}}}
    """

    it = iter(keys)
    last = next(it)
    res = {last: {}}
    lvl = res
    while True:
        try:
            k = next(it)
            lvl = lvl[last]
            lvl[k] = {}
            last = k
        except StopIteration:
            lvl[k] = value
            return res


if __name__ == "__main__":
    print(set_arbitrary_nest(["foo", "baz", "bar", "bic", "yo"], 5))
