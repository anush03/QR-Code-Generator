def validate_input(data: str) -> bool:
    if not data:
        return False

    if len(data.strip()) < 3:
        return False

    return True
