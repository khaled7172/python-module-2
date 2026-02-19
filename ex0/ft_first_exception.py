def check_temperature(temp_str):
    try:
        num = int(temp_str)
        return (test_temperature_input(num))
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"

def test_temperature_input(n):
    if n >= 0 and n <= 40:
        return f"Temperature {n}℃ is perfect for plants!"
    elif n > 40:
        return f"Error: {n}℃ is too hot for plants (max 40℃)"
    elif n < 0:
        return f"Error: {n}℃ is too cold for plants (min 0℃)"



if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    lst = ["25", "abc", "100", "-50"]
    for i in lst:
        print(f"Testing temperature: {i}")
        print(check_temperature(i))
    print("All tests completed - program didn't crash")
