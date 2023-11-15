"""EX06 - Dictionary Utils."""
__author__ = "730673903"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary to switch the keys and the values."""
    mod_dict: dict[str, str] = dict()
    values = list(inp_dict.values())
        
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                raise KeyError("duplicate values")
            
    for idx in inp_dict:
        key = inp_dict[idx]
        mod_dict[key] = idx
    return mod_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Checks through a dictionary to see what most people's favorite color is."""
    # Create a dict that assigns the key to the value of inp_dict and assigns the value to the number of appearances dict[color, num_appearances]
    mod_dict: dict[str, str] = dict()
    for key in inp_dict:
        mod_dict[inp_dict[key]] = 0
    # Iterate through the inp_dict and everytime a color is iterated, add 1 to the num_appearances
    for key in inp_dict:
        mod_dict[inp_dict[key]] += 1
    # Find the color that appears most in the dict.
    max: int = 0
    num_appearances: int
    color: str
    for color, num_appearances in mod_dict.items():
        if num_appearances > max:
            max = num_appearances
            most_popular_color = color
    return most_popular_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Checks how many times a value has appeared in the list."""
    res_dict: dict[str, int] = dict()
    for i in inp_list:
        if i in res_dict:
            res_dict[i] += 1
        else:
            res_dict[i] = 1
    return res_dict


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Groups words based on the starting letter of the word."""
    # Create a resulting dictionary to return at the end
    res_dict: dict[str, list[str]] = dict()

    # Iterate through every word in the input list
    for word in inp_list:
        # Set the starting letter of a word to a variable
        starting_letter = word[0]
        # If the starting letter is already in res_dict, then add the whole word to that key
        if starting_letter.lower() in res_dict:
            res_dict[starting_letter.lower()].append(word)
        # If it's not in res_dict, then create a key-value pair
        else:
            res_dict[starting_letter.lower()] = [word]
    # Return the resulting dictionary at the end
    return res_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance by adding students to the corresponding day."""
    # If the day is already in the dict, just add the student to that corresponding day.
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    # If the day is not already in the dict, then create a key-value pair with a day and student
    else:
        attendance_dict[day] = [student]
    # Return the updated attendance_dict
    return attendance_dict
