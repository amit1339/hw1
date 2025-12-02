from item import Item


class ResearchSample(Item):
    """
    Represents a research sample in the space station inventory.
    
    Research samples are scientific items used for experiments. Each sample
    has an associated experiment name and hazard level indicating potential danger.
    """

    def __init__(self, experiment_name: str, hazard_level: int, price: float) -> None:
        """
        Constructor for ResearchSample.
        
        :param experiment_name: the name of the experiment.
        :param hazard_level: hazard level from 1 to 10.
        :param price: the cost of the sample.
        """
        super().__init__("RESEARCH_SAMPLE", price)
        self._experiment_name: str = experiment_name
        self._hazard_level: int = hazard_level

    def store(self, module_name: str) -> None:
        """
        Stores the research sample in the specified module.
        
        :param module_name: the name of the station module where the item is stored.
        """
        print(f"Research sample for experiment {self._experiment_name} is stored in module {module_name} with hazard level {self._hazard_level}.")

    def get_category(self) -> str:
        """
        Returns the category of the research sample.
        
        :return: the string "SCIENCE".
        """
        return "SCIENCE"

    def is_critical(self) -> bool:
        """
        Determines if the research sample is critical.
        
        :return: True if hazard level is >= 8, False otherwise.
        """
        return self._hazard_level >= 8

    def print_details(self) -> None:
        """
        Prints full details for the research sample.
        """
        print(f"Item #{self.get_id()} - {self.get_name()} '{self._experiment_name}' belongs to {self.get_category()} category.")
        print(f"Hazard level: {self._hazard_level}.")
        print(f"Cost: {self.get_price()} credits.")
        print(f"Critical: {self.is_critical()}.")

    """
    Your code goes here!
    """