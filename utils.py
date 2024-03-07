def wait_for_enter() -> None:
    input("Press enter to continue.")


def print_and_wait(message: str) -> None:
    print(message)
    wait_for_enter()
