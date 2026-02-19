def garden_operations():
    my_dict = {}
    print("Testing ValueError...")
    try:
        x = int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        print()
    print("Testing ZeroDivisionError...")
    try:
        y = 6 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        print()
    try:
        print("Testing FileNotFoundError...")
        name = "missing.txt"
        open(name)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
        print()
    try:
        print("Testing KeyError...")
        k = "missing_plant"
        val = my_dict['missing_key']
    except KeyError as e:
        print(f"Caught KeyError: {e}")
        print()
    try:
        print("Testing multiple errors together...")
        x = int("abc")
        y = 6 / 0
        open('file.txt')
        value = my_dict['missing_key']
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