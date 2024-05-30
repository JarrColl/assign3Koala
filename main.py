import os
from typing import List

from DatabaseConnection import DatabaseConnection
from Managers.LoginManager import LoginManager
from OptionSelection import OptionSelection
from Pages.LoginPage import LoginPage

from Pages.DeliveryPage import DeliveryPage
from Pages.KitchenPage import KitchenPage
from Pages.MenuPage import MenuPage
from Pages.OrderPage import OrderPage

from Pages.ReservationPage import ReservationPage
from Pages.StaffPage import StaffPage
from Pages.Page import Page
from Pages.TablePage import TablePage


CUSTOMER_OPTIONS: List[str] = ["View the Menu"]
STAFF_OPTIONS: List[str] = [
    "Deliveries",
    "Kitchen Orders",
    "View the Menu",
    "Order Management",
    "Reservations",
    "Staff Management",
    "Table Management",
]
CUSTOMER_PAGES: List[Page] = [MenuPage]
STAFF_PAGES: List[Page] = [DeliveryPage, KitchenPage, MenuPage, OrderPage, ReservationPage, StaffPage, TablePage]

db = DatabaseConnection()
login_manager = LoginManager(db)

os.system("cls" if os.name == "nt" else "clear")
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

options_list: List[str] = None
page_list: List[Page] = None
if user_type == "staff":
    LoginPage.display(login_manager)
    options_list = STAFF_OPTIONS
    page_list = STAFF_PAGES
elif user_type == "customer":
    options_list = CUSTOMER_OPTIONS
    page_list = CUSTOMER_PAGES

while True:
    os.system("cls" if os.name == "nt" else "clear")
    page_index = OptionSelection.show(options_list, "Main Menu")
    os.system("cls" if os.name == "nt" else "clear")
    page_list[page_index].display(login_manager)
