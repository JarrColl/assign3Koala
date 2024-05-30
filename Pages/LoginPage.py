# Ask user if the are a customer or a staff member. Staff must login.
#
#
import os

from Managers.LoginManager import LoginManager
from Pages.Page import Page


class LoginPage(Page):
    @staticmethod
    def display(login_manager: LoginManager) -> bool:
        os.system("cls" if os.name == "nt" else "clear")
        print("Login")

        while True:
            username: str = input("Enter your Username: ")
            password: str = input("Enter your Password: ")
            success: bool = login_manager.login(username, password)
            if success:
                return True
            else:
                print("Username and Password do not match please try again.")
