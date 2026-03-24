from pages.login_page import LoginPage
from pathlib import Path

"""
This module contains utility functions for the test suite. 
These utilities help to keep the test code clean and reusable 
across multiple test cases.
"""


# Function to verify that a user is logged in by checking the URL
# and performing a login if necessary.
def verify_login(page):
    if "dashboard" not in page.url:
        login = LoginPage(page)
        login.login("admin", "admin")
        assert "dashboard" in page.url


# Function to read data from a CSV file and return it as a list of rows.
def get_csv_data(csv_file) -> list:
    import csv
    data = []
    p = Path(csv_file)
    if not p.is_absolute():
        # Resolve relative paths against the tests folder
        p = Path(__file__).parent.joinpath(csv_file)
    with p.open(newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


# Function to convert a string representation of a boolean value to an actual boolean.
def str_to_bool(s):
    s = s.strip().lower()
    if s == "true":
        return True
    else:
        return False


# Function to convert an event type string to a more descriptive format
def event_type_conversion(event_type):
    match event_type:
        case "attack":
            return "Attack event"
        case "assault":
            return "Assault event"
        case "breach":
            return "Breach event"
        case "red":
            return "Red event"
        case _:
            return "Unknown event type"
