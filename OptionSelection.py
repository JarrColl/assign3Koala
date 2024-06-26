from typing import List, Optional


class OptionSelection:
    @staticmethod
    def show(
        options: List[str], prompt: Optional[str] = None, back_msg: Optional[str] = None
    ) -> int:
        if prompt:
            print(prompt)

        if back_msg:
            print(f"(q): {back_msg}")
        for index, option in enumerate(options):
            print(f"({index + 1}): {option}")

        while True:
            user_input = input("Selection: ")
            if user_input.isdigit():
                user_input_int = int(user_input) - 1
                if user_input_int >= 0 and user_input_int < len(options):
                    return user_input_int
                else:
                    print("Invalid input, try again.")
            elif back_msg and user_input == "q":
                return -1
            else:
                print("Invalid input, try again.")

