from DatabaseConnection import DatabaseConnection
from Pages.Page import Page

db = DatabaseConnection()

class PaymentPage(Page):
    @staticmethod
    def display(login_manager):
        payment_methods = [
            PaymentMethod("Card"),
            PaymentMethod("Cash"),
            PaymentMethod("Gift Card")
        ]

        options = [method.name for method in payment_methods]
        while True:
            selection_index = PaymentPage.show_options(options, "Payment Menu: ", "Return")
            if selection_index is not None and selection_index != -1:
                selected_method = payment_methods[selection_index]
                PaymentPage.make_payment(selected_method)
            else:
                break

    @staticmethod
    def show_options(options, title, return_option):
        print(title)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        print(f"{len(options) + 1}. {return_option}")

        while True:
            try:
                selection = int(input("Select an option: "))
                if 1 <= selection <= len(options):
                    return selection - 1
                elif selection == len(options) + 1:
                    return -1
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def make_payment(payment_method):
        payment_method.makePayment()
        PaymentPage.record_payment(payment_method)
        print(f"Payment made using {payment_method.name}.")


