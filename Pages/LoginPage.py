# Ask user if the are a customer or a staff member. Staff must login.
#
#
from Page import Page
import os
from ..Managers.LoginManager import LoginManager


class LoginPage(Page):
    def display(self, login_manager):
        os.system("cls" if os.name == "nt" else "clear")



        print("Login")
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")

        login_manager.login(username, password)





login_manager = LoginManager()
l = LoginPage(login_manager)
l.display()
