def collect_interests(minimum: int = 3) -> list[str]:
    """Ask the user for interests until the minimum count is reached."""
    print("Enter your interests one by one.")
    print(f"Please enter at least {minimum} interests. Press Enter after each interest.\n")

    interests: list[str] = []

    while len(interests) < minimum:
        value = input(f"Interest {len(interests) + 1}: ").strip()

        if not value:
            print("Interest cannot be empty.")
            continue

        interests.append(value)

    while True:
        value = input("Add another interest or press Enter to continue: ").strip()

        if not value:
            break

        interests.append(value)

    return interests
