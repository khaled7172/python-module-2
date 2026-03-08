class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():
    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(
            self,
            plant_name: str,
            water_level: int,
            sunlight_hours: int) -> None:
        if plant_name is None or plant_name.strip() == "":
            raise PlantError("Plant name cannot be empty!")
        if 0 > water_level:
            raise ValueError(f"Water level {water_level} cannot be negative")
        if sunlight_hours < 0:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} cannot be negative")
        self.plants[plant_name] = {
            "water": water_level,
            "sunlight": sunlight_hours
        }
        print(f"Added {plant_name} successfuly")

    def water_plants(self) -> None:
        print("Opening watering system")
        error_occured = False
        try:
            for plant_name, data in self.plants.items():
                try:
                    if data["water"] < 3:
                        raise WaterError(
                            f"{plant_name} has insufficient water level!")
                    print(f"Watering {plant_name} - success")
                except WaterError as e:
                    print(f"Error: {e}")
                    error_occured = True
        finally:
            print("Closing watering system (cleanup)")
        if not error_occured:
            print("Watering completed successfully!")

    def check_plant_health(self, plant_name: str) -> None:
        if plant_name not in self.plants:
            raise PlantError(f"{plant_name} does not exist in garden!")
        data = self.plants[plant_name]
        if data["water"] < 1:
            raise PlantError(
                f"Error checking {plant_name}: Water level {
                    data['water']} is too low (min 1)!")
        if data["water"] > 10:
            raise PlantError(
                f"Error checking {plant_name}: Water level {
                    data['water']} is too high (max 10)!")
        if data["sunlight"] < 2:
            raise PlantError(
                f"Error checking {plant_name}: Sunlight hours {
                    data['sunlight']} is too low (min 2)!")
        if data["sunlight"] > 12:
            raise PlantError(
                f"Error checking {plant_name}: Sunlight hours {
                    data['sunlight']} is too high (max 12)!")
        print(
            f"{plant_name}: healthy (water: {
                data['water']}, sun: {
                data['sunlight']})")


def test_garden_management() -> None:
    garden = GardenManager()
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
    except (PlantError, ValueError) as e:
        print(f"Error adding plant: {e}")
    try:
        garden.add_plant("lettuce", 16, 3)
    except (PlantError, ValueError) as e:
        print(f"Error adding plant: {e}")
    try:
        garden.add_plant("", 5, 8)
    except (PlantError, ValueError) as e:
        print(f"Error adding plant: {e}")
    try:
        garden.add_plant("cactus", 1, 10)
    except (PlantError, ValueError) as e:
        print(f"{e}")
    print()
    print("Watering plants...")
    garden.water_plants()
    print()
    print("checking plant health...")
    try:
        garden.check_plant_health("tomato")
    except PlantError as e:
        print(f"{e}")
    try:
        garden.check_plant_health("lettuce")
    except PlantError as e:
        print(f"{e}")
    try:
        garden.check_plant_health("cherry")
    except PlantError as e:
        print(f"{e}")
    print()
    print("Testing error recovery...")
    try:
        if garden.plants["tomato"]["water"] < 7:
            raise WaterError("Caught GardenError: Not enough water in tank")
    except WaterError as e:
        print(f"{e}")
    finally:
        print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
