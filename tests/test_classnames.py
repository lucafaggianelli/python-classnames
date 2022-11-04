#!/usr/bin/env python

"""Tests for `classnames` package."""


import unittest

from classnames import class_names


class TestClassnames(unittest.TestCase):
    """Tests for `classnames` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_keeps_object_keys_with_truthy_values(self):
        assert class_names({"a": True, "b": False, "c": 0, "d": None, "f": 1}) == "a f"

    def test_joins_arrays_of_class_names_and_ignore_falsy_values(self):
        assert class_names("a", 0, None, True, 1, "b") == "a 1 b"

    def test_supports_heterogenous_arguments(self):
        assert class_names({"a": True}, "b", 0) == "a b"

    def test_should_be_trimmed(self):
        assert class_names("", "b", {}, "") == "b"

    def test_returns_an_empty_string_for_an_empty_configuration(self):
        assert class_names({}) == ""

    def test_supports_an_array_of_class_names(self):
        assert class_names(["a", "b"]) == "a b"

    def test_joins_array_arguments_with_string_arguments(self):
        assert class_names(["a", "b"], "c") == "a b c"
        assert class_names("c", ["a", "b"]) == "c a b"

    def test_handles_multiple_array_arguments(self):
        assert class_names(["a", "b"], ["c", "d"]) == "a b c d"

    def test_handles_arrays_that_include_falsy_and_true_values(self):
        assert class_names(["a", 0, None, None, False, True, "b"]) == "a b"

    def test_handles_arrays_that_include_arrays(self):
        assert class_names(["a", ["b", "c"]]) == "a b c"

    def test_handles_arrays_that_include_objects(self):
        assert class_names(["a", {"b": True, "c": False}]) == "a b"

    def test_handles_deep_array_recursion(self):
        assert class_names(["a", ["b", ["c", {"d": True}]]]) == "a b c d"

    def test_handles_arrays_that_are_empty(self):
        assert class_names("a", []) == "a"

    def test_handles_nested_arrays_that_have_empty_nested_arrays(self):
        self.assertEqual(class_names("a", [[]]), "a")

    def test_handles_all_types_of_truthy_and_falsy_property_values_as_expected(self):
        self.assertEqual(
            class_names(
                {
                    None: None,
                    "emptyString": "",
                    "noNumber": None,
                    "zero": 0,
                    "negativeZero": -0,
                    False: False,
                    "nonEmptyString": "foobar",
                    "whitespace": " ",
                    "emptyObject": {},
                    "nonEmptyObject": {"a": 1, "b": 2},
                    "emptyList": [],
                    "nonEmptyList": [1, 2, 3],
                    "greaterZero": 1,
                }
            ),
            "nonEmptyString whitespace nonEmptyObject nonEmptyList greaterZero",
        )
