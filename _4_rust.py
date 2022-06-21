class Ok:
    __match_args__ = ('value',)

    def __init__(self, value):
        self.value = value


class Err:
    __match_args__ = ('value',)

    def __init__(self, value):
        self.value = value


Result = Ok | Err


def parse(value: str) -> Result:
    if value.isnumeric():
        return Ok(int(value))
    return Err(f"{value} is not numeric")


if __name__ == "__main__":
    v = "sdsd"

    match parse(v):
        case Ok(value):
            print(f"Result is ok, value is {value}")
        case Err(message):
            print(f"Result is error, message is {message}")
