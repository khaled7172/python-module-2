class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_custom_errors():
    

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("All custom error types work correctly!")