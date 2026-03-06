def garden_operations():
    my_dict = {}
    print("Testing ValueError...")
    try:
        _ = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()
    print("Testing ZeroDivisionError...")
    try:
        _ = 6 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    name = "missing.txt"
    try:
        open(name)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{name}'")
    print()
    print("Testing KeyError...")
    try:
        _ = my_dict['missing_key']
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()
    print("Testing multiple errors together...")
    try:
        _ = int("abc")   # ValueError
        _ = 6 / 0   # ZeroDivisionError
        open("file.txt")   # FileNotFoundError
        _ = my_dict['missing_key']   # KeyError
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()


def test_error_types():
    garden_operations()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
    print("All error types tested successfully!")
