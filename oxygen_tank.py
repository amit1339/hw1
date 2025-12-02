from item import Item


class OxygenTank(Item):
    """
    Represents an oxygen tank in the space station inventory.
    
    Oxygen tanks are critical life support items that store breathable oxygen
    for the station crew. Each tank has a capacity and an expiration date.
    """

    def __init__(self, price: float, capacity_liters: float, expiration_date: str) -> None:
        super().__init__("OXYGEN_TANK", price)
        self._capacity_liters: float = capacity_liters
        self._expiration_date: str = expiration_date

    def store(self, module_name: str) -> None:
        print(f"Oxygen tank is stored in module {module_name}.")

    def get_category(self) -> str:
        return "LIFE_SUPPORT"
    
    def is_critical(self) -> bool:
        return True

    def print_details(self) -> None:
        print(f"Item #{self.get_id()} - {self.get_name()} costs {self.get_price()} credits.")
        print(f"Category: {self.get_category()}.")
        print(f"Capacity: {self._capacity_liters} liters.")
        print(f"Expires on {self._expiration_date}.")
        print(f"Critical: {self.is_critical()}.")
