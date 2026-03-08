def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    error_occured = False
    try:
        for plant in plant_list:
            if plant is None or plant.strip() == "":
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
        error_occured = True
    finally:
        print("Closing watering system (cleanup)")
    if not error_occured:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    good_plants = ["tomato", "lettuce", "carrots"]
    bad_plants = ["tomato", None, ""]
    print("Testing normal watering...")
    water_plants(good_plants)
    print()
    print("Testing with error...")
    water_plants(bad_plants)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
