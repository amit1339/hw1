import abc


class Item(abc.ABC):
    """
    An abstract base class representing a general inventory item on the space station.
    
    This class serves as a blueprint for all inventory items, providing common attributes
    such as item ID, name, and price. Each item is automatically assigned a unique ID
    upon creation.
    """
    
    _item_counter: int = 0

    def __init__(self, name: str, price: float) -> None:
        """
        Constructor.

        :param name: the name of the item.
        :param price: the price of the item.
        """
        ##########################
        # Do not change this part
        self._name = name
        self._price = price
        ##########################

        # PART 5: You can (and SHOULD) change the following line, and add more line(s) if needed.
        Item._item_counter += 1
        self._item_id = Item._item_counter

        """
        Your code goes here (if needed)
        """

    def get_id(self) -> int:
        """
        Returns the item's id.

        :return: the item's id.
        """
        return self._item_id

    def get_name(self) -> str:
        """
        Returns the item's name.

        :return: the item's name.
        """
        return self._name

    def get_price(self) -> float:
        """
        Returns the item's price.

        :return: the item's price.
        """
        return self._price

    @abc.abstractmethod
    def store(self, module_name: str) -> None:
        pass

    @abc.abstractmethod
    def get_category(self) -> str:
        pass

    @abc.abstractmethod
    def print_details(self) -> None:
        pass

    @abc.abstractmethod
    def is_critical(self) -> bool:
        pass

    @staticmethod
    def get_number_of_created_items() -> int:
        """
        This method returns the total number of Item instances that were created so far (including all subclasses).
        """
        return Item._item_counter
