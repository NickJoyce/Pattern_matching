class UserInput:
    __match_args__ = ('action', 'value')

    def __init__(self, action, value):
        self.action = action
        self.value = value


def run_horizontally(user_input: UserInput | dict) -> None:
    match user_input:
        case UserInput('left' | 'right', value):
            print(f"Moving horizontally on {value}px")
        case _:
            print("Error")

if __name__ == "__main__":
    input1 = UserInput("left", 200)
    input2 = UserInput('top', 250)

    run_horizontally(input1)
    run_horizontally(input2)
