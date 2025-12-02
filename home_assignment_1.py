"""
Home Assignment #1 - Advanced Python
"""

###################################
# General Guidelines
###################################
"""
In this Homework assignment we will use Python (and OOP in Python) to maintain
a space station inventory system, and perform various operations on it.

Guidelines:
    - After completing each part, you should be able to run the program and test your results.
    - Your program MUST run (if it will not, you will lose most of the points).
    - You can use the code from the lectures and recitations as a baseline.
    - Make sure to add documentation - as we saw in class.
    - Keep the code clean and readable.
"""

###################################
# The Assignment
###################################
"""
The assignment contains 6 files:
- home_assignment_1.py -
    This file - contains guidelines and the task description.
- hw1_main.py -
    - Contains the main file that you will run.
    - Make sure to run it after you complete each part.
    - Change ONLY the parts you are asked to change or add code to.
- item.py
- oxygen_tank.py
- cargo_crate.py
- research_sample.py
"""

###################################
# Part 0 - Personal Details
###################################
"""
In hw1_main.py print the id, name and email of the submitters.
Replace the details in the "Part 0 - Personal Details" section.
"""

###################################
# Part 1 - The Item class
###################################
"""
---
Task 1.0 (nothing to do - only read!)
---
The Item class represents a general inventory item on the space station.

In the file item.py - create an Abstract Class - and call it Item (already done for you).

In Item class - you already have 3 methods:
- get_id         - returns the item's id (will be set later).
- get_price      - returns the item's price.
- get_name       - returns the item's name.

Note:
The constructor for the class was already built for you (you will change its body later in this assignment).
Make sure you do NOT change its signature.

---
Task 1.1
---
Add documentation for the Item class (class-level docstring) explaining its purpose in the
space station inventory system.

---
Task 1.2
---
Add 4 ABSTRACT methods to the class:

1. store
    - Parameters:
        module_name: str - the name of the station module where the item is stored.
    - Returns: nothing.
    - Behavior: Stores the item in the specified module.

2. get_category
    - Parameters: none.
    - Returns: a string that represents the item's category (for example: "LIFE_SUPPORT", "LOGISTICS", etc.).

3. print_details
    - Parameters: none.
    - Returns: nothing.
    - Behavior: Prints full details for the item.

4. is_critical
    - Parameters: No parameters.
    - Returns: bool.
    - Behavior: returns True if the item is critical for the station operation, and False otherwise.
      The logic will be implemented in each concrete subclass.
"""

###################################
# Part 2 - The OxygenTank
###################################
"""
In this part you will implement the OxygenTank class.

---
Task 2.0 (nothing to do - only read!)
---
In the file oxygen_tank.py - create a class - and call it OxygenTank (already done for you).

---
Task 2.1
---
Add documentation for the OxygenTank class explaining what it represents.

---
Task 2.2
---
Make OxygenTank inherit from Item.

---
Task 2.3
---
Add a constructor to OxygenTank class:

- Call the super class constructor.
  The name for all OxygenTank objects should be "OXYGEN_TANK".
  The price is received as a parameter.

- The constructor should receive 3 parameters:
    * price: float                - the cost of this tank (in station credits).
    * capacity_liters: float      - total oxygen capacity in liters.
    * expiration_date: str        - string representing the expiration date.

- The constructor should declare 2 PROTECTED attributes:
    * _capacity_liters
    * _expiration_date

  These attributes are initialized using the received parameters.

- Make sure you add type hints and documentation to the constructor.

---
Task 2.4
---
Implement the store abstract method:

- store - receives a single str parameter `module_name`,
          prints the following message:

    Oxygen tank is stored in module <module_name>.

  Where:
    * <module_name> - is the received parameter.

---
Task 2.5
---
Implement the get_category abstract method:

- get_category - receives no parameters and returns the string:
    LIFE_SUPPORT

---
Task 2.6
---
Implement the is_critical abstract method:

- is_critical - receives no parameters and returns a bool.
- For OxygenTank, always return True (every oxygen tank is critical).

---
Task 2.7
---
Implement the print_details abstract method:

- print_details - receives no parameters, prints data for the oxygen tank:

    Item #<id> - <name> costs <price> credits.
    Category: <category>.
    Capacity: <capacity_liters> liters. 
    Expires on <expiration_date>.
    Critical: <critical_flag>.

  Where:
    * <id>              - the item's id (use get_id method)
    * <name>            - the item's name (use get_name method)
    * <price>           - the item's price (use get_price method)
    * <category>        - the item's category (use get_category method)
    * <capacity_liters> - the <_capacity_liters> attribute
    * <expiration_date> - the <_expiration_date> attribute
    * <critical_flag>   - the result of calling is_critical() (True/False)
"""

###################################
# Part 3 - The CargoCrate
###################################
"""
In this part you will create the CargoCrate class.

In the file - cargo_crate.py - you should create the CargoCrate class

Guidelines:
1. The CargoCrate class inherits from Item class.
2. The CargoCrate class receives 3 parameters in its constructor:
    * content_type: str      - what is inside (e.g. "food", "tools", "research").
    * price_per_kg: float
    * weight_kg: float
3. The name for all CargoCrate objects should be "CARGO_CRATE".
4. The price for all CargoCrate objects should be: <price_per_kg> * <weight_kg>.
5. The CargoCrate class has 2 PROTECTED attributes:
        _content_type and _weight_kg.
6. The CargoCrate class implements the 4 abstract methods of Item:

    6.1 store
        - receives a single str parameter `module_name`,
          prints the following message:

            Cargo crate with <content_type> is stored in module <module_name>.

          Where:
            * <content_type> - is the crate's content type.
            * <module_name>  - is the received parameter.

    6.2 get_category
        - receives no parameters and returns the string:
            LOGISTICS

    6.3 is_critical
        - receives no parameters and returns True if the content type is one of:
            "food", "medical"
          and False otherwise.

    6.4 print_details
        - receives no parameters, prints data for the cargo crate:

            Item #<id> - <name> (<content_type>) belongs to <category> category.
            Weight: <weight_kg> kg, 
            Total cost: <price> credits.
            Critical: <critical_flag>.

        Where:
            * <id>           - should be the item's id (use get_id method)
            * <name>         - should be the item's name (use get_name method)
            * <content_type> - should be the <_content_type> attribute
            * <category>     - should be the item's category name (use get_category method)
            * <weight_kg>    - should be the <_weight_kg> attribute
            * <price>        - should be the item's price (use get_price method)
            * <critical_flag> - the result of calling is_critical()

7. Make sure you add type hints and documentation to the class and to all its methods!
"""

###################################
# Part 4 - The ResearchSample
###################################
"""
In this part you will create the ResearchSample class.

In the file - research_sample.py - you should create the ResearchSample class.

Guidelines:
1. The ResearchSample class inherits from Item class.
2. The ResearchSample class receives 3 parameters in its constructor:
    * experiment_name: str   - the name of the experiment.
    * hazard_level: int      - hazard level from 1 to 10.
    * price: float           - the cost of the sample.
3. The name for all ResearchSample objects should be "RESEARCH_SAMPLE".
4. The ResearchSample class has 2 PROTECTED attributes:
        * _experiment_name 
        * _hazard_level
5. The ResearchSample class implements the 4 abstract methods of Item:

    5.1 store
        - receives a single str parameter `module_name`,
          prints the following message:

            Research sample for experiment <experiment_name> is stored in module <module_name> with hazard level <hazard_level>.

          Where:
            * <experiment_name> - is the experiment name.
            * <module_name>     - is the received parameter.
            * <hazard_level>     - is the hazard level of the sample.

    5.2 get_category
        - receives no parameters and returns the string:
            SCIENCE

    5.3 is_critical
        - receives no parameters and returns True if hazard_level is greater than or equal to 8
          and False otherwise.

    5.4 print_details
        - receives no parameters, prints data for the research sample:

            Item #<id> - <name> '<experiment_name>' belongs to <category> category.
            Hazard level: <hazard_level>.
            Cost: <price> credits.
            Critical: <critical_flag>.

        Where:
            * <id>             - should be the item's id (use get_id method)
            * <name>           - should be the item's name (use get_name method)
            * <experiment_name> - should be the <_experiment_name> attribute
            * <category>       - should be the item's category name (use get_category method)
            * <hazard_level>   - should be the <_hazard_level> attribute
            * <price>          - should be the item's price (use get_price method)
            * <critical_flag>  - the result of calling is_critical()

6. Make sure you add type hints and documentation to the class and to all its methods!
"""

###################################
# Part 5 - Item ID and Item Counter
###################################
"""
In this task you will add the item's ID and a static counter.

The task is to make sure each item is created with a unique (int) ID,
and this id is generated automatically by the Item's class constructor.

You will also keep a counter of how many items were created.

---
Task 5.1
---
Change the constructor of Item so each item is created with a unique integer ID.

    IMPORTANT NOTES:
    - You are NOT allowed to add parameters to the constructor SIGNATURE!!
    - You MUST have an attribute "self._item_id" in class Item.
    - You can (and SHOULD) add static members to the Item class.
    - You can (and should) add code in __init__ method (constructor) of Item.

---
Task 5.2
---
Add a static method to Item:

    def get_number_of_created_items() -> int

This method returns the total number of Item instances that were created so far (including all subclasses).
"""

###################################
# Part 6 - HW1 main
###################################
"""
In this part you will create a small program that receives input from the user.
Based on the input the program will maintain a list of items - <station_inventory> list -
and will be able to print data on this list.

In every iteration - the program will ask the user for a command.

You will code this part in "hw1_main.py".

Note that the main loop and the program's skeleton were already written for you.
You have to fill the code based on the commands list below.

You will see the:
    # Your code goes here
comment in every place you need to add code.

Possible commands and what the program should do:

1. "add_oxygen_tank"
    * The program will ask the user for the tank's price, with the following message:
        Please insert the price of the oxygen tank:
    * The program will ask the user for the tank's capacity, with the following message:
        Please insert the capacity (liters) of the oxygen tank:
    * The program will ask the user for the tank's expiration date, with the following message:
        Please insert the expiration date of the oxygen tank:
    * The program will create a new OxygenTank with the received data,
      and will add it to the <station_inventory> list.

2. "add_cargo_crate"
    * The program will ask the user for the crate's content type:
        Please insert the content type of the cargo crate:
    * The program will ask the user for the crate's price per kg:
        Please insert the cargo crate price per KG:
    * The program will ask the user for the crate's weight:
        Please insert the cargo crate weight (in KG):
    * The program will create a new CargoCrate with the received data,
      and will add it to the <station_inventory> list.

3. "add_research_sample"
    * The program will ask the user for the experiment name:
        Please insert the experiment name of the research sample:
    * The program will ask the user for the hazard level:
        Please insert the hazard level (1-10) of the research sample:
    * The program will ask the user for the price:
        Please insert the price of the research sample:
    * The program will create a new ResearchSample with the received data,
      and will add it to the <station_inventory> list.

4. "print"
    * The program will print all the items in the list, using the "print_details" method.

5. "store"
    * The program will ask the user for the module name to use, with the following message:
        Please insert the module name:
    * The program will call the `store` method with the received <module_name>
      for all the items in the list.

6. "total_value"
    * The program will print the TOTAL price of all the items in the <station_inventory> list:
        The total price is <total_price>.

        * Where:
            - <total_price> - is the TOTAL price of all the items in the <station_inventory> list.

7. "avg_value"
    * The program will print the AVERAGE price of all the items in the <station_inventory> list:
        The average price is <average_price>.

        * Where:
            - <average_price> - is the AVERAGE price of all the items in the list.
                                It should be printed with exactly 2 decimal points.

    * If there are no items in the list, the program will print:
        No items in the station inventory.

8. "remove"
    * The program will ask the user for the id of the item to remove:
        Please insert the id of the item you want to remove:
    * If an item with such id exists in the <station_inventory> list, the program will remove it from the list,
      and will print:
        Item #<id> was removed from the list.

      Where:
        - <id> - is the id of the removed item.

    * If an item with such id doesn't exist in the list, the program will print:
        Item #<id> was not found in the list.

9. "critical"
    * The program will print all the items in the list for which `is_critical()` returns True.
      It should print them by calling their "print_details" method.

    * If there are no critical items, the program will print:
        No critical items in the station inventory.

10. "created_items"
    * The program will print the number of items created so far:
        <number_of_created_items> Items created so far.

        * Where:
            - <number_of_created_items> - number of items created so far.
    
    * Note: 
        This includes deleted items. 
        It should be the total number of Item instances that were created in the system.

11. "exit"
    * The program will break the loop.

12. Any other command
    * The program will print an error message - and ask the user for a valid command.
"""

###################################
# GOOD LUCK
###################################
"""
GOOD LUCK!!!
"""
