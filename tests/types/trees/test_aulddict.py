# SPDX-FileCopyrightText: 2023 Alex Lemna <git@alexanderlemna.com>
#
# SPDX-License-Identifier: MIT

#
# AuldDict public API tests
# -------------------------
# See: https://docs.python.org/3/library/stdtypes.html#dict
#


def test_api_str():
    """"""


def test_api_repr():
    """"""


def test_api_len():
    """"""


def test_api_getitem():
    """"""


def test_api_getitem_missing():
    """"""


def test_api_setitem():
    """"""


def test_api_delitem():
    """"""


def test_api_iter():
    """"""


def test_api_reversed():
    """"""


def test_api_contains():
    """"""


def test_api_does_not_contain():
    """"""


def test_api_get_items():
    """"""


def test_api_get_keys():
    """"""


def test_api_get_values():
    """"""


def test_api_merge():
    """"""


def test_api_merge_with_symbols():
    """"""


def test_api_update():
    """"""


def test_api_update_with_symbols():
    """"""


def test_api_pop():
    """"""


def test_api_pop_item():
    """"""


def test_api_clear():
    """"""


def test_api_copy():
    """"""


def test_api_from_keys():
    """"""


def test_api_set_default():
    """"""


#
# Key-splitting tests
# -------------------
#


def test_key_splitting():
    """
    ```
    >>> foo = AuldDict()
    >>> foo["key1 key2 key3 key4"] = "foobar"
    >>> foo["key1"]["key2"]["key3"]["key4"]
    "foobar"
    ```"""


def test_key_splitting_custom_delimiter():
    """
    ```
    >>> foo = AuldDict(delimiter=".")
    >>> foo["key1.key2.key3.key4"] = "foobar"
    >>> foo["key1"]["key2"]["key3"]["key4"]
    "foobar"
    ```"""


def test_key_splitting_custom_delimiter_overrides_default():
    """
    ```
    >>> foo = AuldDict(delimiter=".")
    >>> foo["key1 key2 key3 key4"] = "foobar"
    >>> assert foo["key1"]["key2"]["key3"]["key4"].exists()
    AssertionError
    ```"""


#
# Combining AuldDicts tests
# -------------------------
#


def test_merging():
    """You should be able to merge dictionaries without destroying
    nested dictionaries."""
