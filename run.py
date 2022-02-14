import gspread
from google.oauth2.service_account import Credentials
import os
from os import system, name

# ----- EMAIL SETTINGS ----- #
import smtplib  # SMTP protocol client (sending emails)
from email.mime.multipart import MIMEMultipart  # MIME (sending emails)
from email.mime.text import MIMEText  # Multipurpose Internet Mail Extensions
if os.path.exists("env.py"):
    import env  # noqa
MY_ADDRESS = os.environ.get("MY_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")

FULL_NAME = ""
GAME_DATA = ""
USER_EMAIL = ""
START_DATE = ""
END_DATE = ""
READER_INFO = []

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('household_game')

def submit_game():
 
    """
    Call email, username, and game_info functions one by one
 
    This function handles the automated python email sent to user
 
    The email is sent from household game to the user email given.
 
    As it is an automatic email, it is the user's responsibility
 
    to enter valid information.
 
    The credits of raw-python email code is mentioned in README.md
    """
def get_games_data():
    print("Please enter game data")
    print("data should be as requested, seperated by commas")
    print("i.e. Email, users name, game, genre, hours played, star rating\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_games_data()

   
def update_games_worksheet(data, worksheet):
    """
    Update the games worksheet, by adding new row with the 
    data provided.
    """
    print("updating games worksheet...\n")
    games_worksheet = SHEET.worksheet("games")
    games_worksheet.append_row(data)
    print("Games worksheet updated successfully.\n")

data = get_games_data()
games_data = ()
update_games_worksheet(games_data)