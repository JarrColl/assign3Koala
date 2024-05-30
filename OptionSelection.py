from typing import List, Optional


class OptionSelection:
    @staticmethod
    def show(
        options: List[str], prompt: Optional[str] = None, back_msg: Optional[str] = None
    ):
        if prompt:
            print(prompt)

        if back_msg:
            print(f"(q): {back_msg}")
        for index, option in enumerate(options):
            print(f"({index}): {option}")

        while True:
            user_input = input("Selection: ")
            if user_input.isdigit():
                user_input_int = int(user_input)
                if user_input_int >= 0 and user_input_int < len(options):
                    return user_input_int
            elif user_input == "q":
                return -1
