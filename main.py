import os

from DatabaseConnection import DatabaseConnection
from Managers.LoginManager import LoginManager

from OptionSelection import OptionSelection
from Pages.LoginPage import LoginPage

CUSTOMER_OPTIONS = ["View the Menu"]
STAFF_OPTIONS = [
    "Deliveries",
    "Kitchen Orders",
    "View the Menu",
    "Order Management",
    "Reservations",
    "Staff Management",
    "Table Management",
]

db = DatabaseConnection()
login_manager = LoginManager(db)

# Check if staff or customer
user_type = None
while True:
    user_input = input("Are you a customer? (y/n): ")
    if user_input == "y":
        user_type = "customer"
        break
    elif user_input == "n":
        user_type = "staff"
        break

options_list = None
if user_type == "staff":
    LoginPage.display(login_manager)
    options_list = STAFF_OPTIONS
elif user_type == "customer":
    options_list = CUSTOMER_OPTIONS

while True:
    os.system("cls" if os.name == "nt" else "clear")
    OptionSelection.show(options_list)
