def run_action(user_input: list) -> None:
    match user_input:
        case "left", value if int(value) > 50:
            print("Something...")
        case 'left' | 'right' | 'top' | 'bottom' as action, value:
            print(f"Go to {action} to {value}px")
        case "shoot", *coords:
            print(f"Shoot by coord: {coords}")
        case "quit", :
            print('Bye')
        case _:
            print("Wrong command")

if __name__ == "__main__":
    run_action("left 49".split())
    run_action("shoot 300 1 3 4".split())
    run_action("quit".split())
    run_action("fff".split())