from item import Item


class OxygenTank(Item):
    """
    Represents an oxygen tank in the space station inventory.
    
    Oxygen tanks are critical life support items that store breathable oxygen
    for the station crew. Each tank has a capacity and an expiration date.
    """

    def __init__(self, price: float, capacity_liters: float, expiration_date: str) -> None:
        """
        Constructor for OxygenTank.
        
        :param price: the cost of this tank (in station credits).
        :param capacity_liters: total oxygen capacity in liters.
        :param expiration_date: string representing the expiration date.
        """
        super().__init__("OXYGEN_TANK", price)
        self._capacity_liters: float = capacity_liters
        self._expiration_date: str = expiration_date

    def store(self, module_name: str) -> None:
        """
        Stores the oxygen tank in the specified module.
        
        :param module_name: the name of the station module where the item is stored.
        """
        print(f"Oxygen tank is stored in module {module_name}.")

    def get_category(self) -> str:
        """
        Returns the category of the oxygen tank.
        
        :return: the string "LIFE_SUPPORT".
        """
        return "LIFE_SUPPORT"

    def is_critical(self) -> bool:
        """
        Determines if the oxygen tank is critical.
        
        :return: True (all oxygen tanks are critical).
        """
        return True

    def print_details(self) -> None:
        """
        Prints full details for the oxygen tank.
        """
        print(f"Item #{self.get_id()} - {self.get_name()} costs {self.get_price()} credits.")
        print(f"Category: {self.get_category()}.")
        print(f"Capacity: {self._capacity_liters} liters.")
        print(f"Expires on {self._expiration_date}.")
        print(f"Critical: {self.is_critical()}.")

    """
    Your code goes here!
    """
