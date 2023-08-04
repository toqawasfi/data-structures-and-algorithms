import pytest
from hashmap_left_join.hashmap_left_join import left_join

def test_left_join():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger"
    }

    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight"
    }

    expected_output = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"]
    ]

    result = left_join(synonyms, antonyms)

    assert result == expected_output
    assert len(result) == len(expected_output)

    # Additional assertion for checking individual rows
    assert result[2] == ["guide", "usher", "follow"]