from item import Item


class CargoCrate(Item):
    """
    Represents a cargo crate in the space station inventory.
    
    Cargo crates are logistics items that contain various supplies such as
    food, tools, or research materials. The price is calculated based on
    weight and price per kilogram.
    """

    def __init__(self, content_type: str, price_per_kg: float, weight_kg: float) -> None:
        """
        Constructor for CargoCrate.
        
        :param content_type: what is inside (e.g. "food", "tools", "research").
        :param price_per_kg: the price per kilogram.
        :param weight_kg: the weight in kilograms.
        """
        super().__init__("CARGO_CRATE", price_per_kg * weight_kg)
        self._content_type: str = content_type
        self._weight_kg: float = weight_kg

    def store(self, module_name: str) -> None:
        """
        Stores the cargo crate in the specified module.
        
        :param module_name: the name of the station module where the item is stored.
        """
        print(f"Cargo crate with {self._content_type} is stored in module {module_name}.")

    def get_category(self) -> str:
        """
        Returns the category of the cargo crate.
        
        :return: the string "LOGISTICS".
        """
        return "LOGISTICS"

    def is_critical(self) -> bool:
        """
        Determines if the cargo crate is critical.
        
        :return: True if content type is "food" or "medical", False otherwise.
        """
        return self._content_type in ["food", "medical"]

    def print_details(self) -> None:
        """
        Prints full details for the cargo crate.
        """
        print(f"Item #{self.get_id()} - {self.get_name()} ({self._content_type}) belongs to {self.get_category()} category.")
        print(f"Weight: {self._weight_kg} kg,")
        print(f"Total cost: {self.get_price()} credits.")
        print(f"Critical: {self.is_critical()}.")

    """
    Your code goes here!
    """
