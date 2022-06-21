def run_action(user_input: dict) -> None:
    match user_input:
        case {"action": str(action), "value": int(value)}:
            print(f"{action=} {value=}")


if __name__ == "__main__":
    user_action = {
        "id": 123,
        "action": "left",
        "value": 50,
        "timestamp": 100000,
        "user_group": 21,
        "cash": 2_000_000
    }
    run_action(user_action)