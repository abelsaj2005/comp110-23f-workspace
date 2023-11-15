"""Testing all the functions in dictionary.py."""
__author__ = "730673903"


# Imports all the functions.
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


# Testing 'invert' function.
def test_keys_to_values():
    """Testing if the invert function works given a dictionary."""
    assert invert({"hello": "world", "cat": "mouse"}) == {"world": "hello", "mouse": "cat"}


def test_lastname_to_firstname():
    """Test if the invert function reverses first and last names."""
    assert invert({"Abel": "Saj", "Asmita": "Nayak", "Sanya": "Arya"}) == {"Saj": "Abel", "Nayak": "Asmita", "Arya": "Sanya"}


def test_invert_edgecase():
    """Tests inputs when there is nothing for inputs."""
    assert invert({}) == {}


# Testing 'favorite_color' function.
def test_favcolor_case1():
    """Basic check if the function works to see which color is the favorite among people."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favcolor_case2():
    """Basic check if the function works to see which color is the favorite among people."""
    assert favorite_color({"Abel": "red", "Lalith": "red", "Rishi": "blue"}) == "red"


def test_favcolor_edgecase():
    """Checks what to do when there is a tie between multiple colors. It should return the first item in the dictionary."""
    assert favorite_color({"Abel": "green", "Alan": "green", "Ezri": "blue", "Kris": "blue"}) == "green"


# Testing 'count' function.
def test_count_case1():
    """Basic check if the function works to return how many times a value appeared in a list."""
    assert count(["yellow", "green", "blue", "blue"]) == {'yellow': 1, 'green': 1, 'blue': 2}


def test_count_case2():
    """Basic check if the function works to return how many times a value appeared in a list."""
    assert count(["Abel", "Alan", "Aiden", "Abel", "Aiden"]) == {'Abel': 2, 'Alan': 1, 'Aiden': 2}


def test_count_edgecase():
    """Tests with only two items."""
    test_edge_list: list[str] = ["tarheel", "chapel"]
    assert count(test_edge_list) == {"tarheel": 1, "chapel": 1}


# Testing 'alphabetizer' function.
def test_alphabetizer_case1():
    """Checks if the function returns the starting alphabet as the key and returns words that start with the letter as a value."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_case2():
    """Organizes the dictionary even if there is a capitalized letter."""
    assert alphabetizer(["Python", "sugar", "Turtle", "party", "table"]) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_alphabetizer_edgecase():
    """Tests a list with the words starting with the same letter."""
    test_edge_alphabetizer: list[str] = ["apple", "army", "anger"]
    assert alphabetizer(test_edge_alphabetizer) == {"a": ["apple", "army", "anger"]}


# Testing 'update_attendance' function.
def test_update_attendance_case1():
    """Updates the attendance log by letting the user add students to the corresponding day."""
    test_attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_attendance_log, "Tuesday", "Vrinda") == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_case2():
    """Updates the attendance log by letting the user add students to the corresponding day."""
    test_attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_attendance_log, "Tuesday", "Vrinda") == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_edgecase():
    """Updates the attendance log with an empty name."""
    test_attendance_log: dict = {"Monday": ["Abel", "Alan"], "Tuesday": ["Aiden"]}
    assert update_attendance(test_attendance_log, "Tuesday", "Aiden") == {"Monday": ["Abel", "Alan"], "Tuesday": ["Aiden"]}