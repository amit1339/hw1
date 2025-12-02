from typing import List

from item import Item
from oxygen_tank import OxygenTank
from cargo_crate import CargoCrate
from research_sample import ResearchSample

###################################
# Part 0 - Personal Details
###################################
print("314649187")        # replace with the id of the first student
print("Amit Ben Yosef")            # replace with the name of the first student
print("amit1339@email.com")  # replace with the email of the first student

print("313571838")        # replace with the id of the second student (or remove if only one)
print("Idan Asulin")            # replace with the name of the second student
print("asulinidan15@gmail.com")  # replace with the email of the second student

###################################
# Part 6.1 - HW1 main
###################################

print("Welcome to advanced Python course - HW 1 - SPACE STATION INVENTORY")

"""
The space station inventory items list
"""
station_inventory: List[Item] = []

"""
The main loop
"""
while True:
    command = input("Please enter a command: ")

    if command == "add_oxygen_tank":
        """
        Receive price
        """
        price = float(input("Please insert the price of the oxygen tank: "))

        """
        Receive capacity (liters)
        """
        capacity = float(input("Please insert the capacity (liters) of the oxygen tank: "))

        """
        Receive expiration date
        """
        expiration_date = input("Please insert the expiration date of the oxygen tank: ")

        """
        Create a new OxygenTank object, and add it to the <station_inventory> list.
        """
        tank = OxygenTank(price, capacity, expiration_date)
        station_inventory.append(tank)

    elif command == "add_cargo_crate":
        """
        Receive content_type from the user
        """
        content_type = input("Please insert the content type of the cargo crate: ")

        """
        Receive price_per_kg from the user
        """
        price_per_kg = float(input("Please insert the cargo crate price per KG: "))

        """
        Receive weight from the user
        """
        weight_kg = float(input("Please insert the cargo crate weight (in KG): "))

        """
        Create a new CargoCrate object, and add it to the <station_inventory> list.
        """
        crate = CargoCrate(content_type, price_per_kg, weight_kg)
        station_inventory.append(crate)

    elif command == "add_research_sample":
        """
        Receive experiment_name from the user
        """
        experiment_name = input("Please insert the experiment name of the research sample: ")

        """
        Receive hazard_level from the user
        """
        hazard_level = int(input("Please insert the hazard level (1-10) of the research sample: "))

        """
        Receive price from the user
        """
        price = float(input("Please insert the price of the research sample: "))

        """
        Create a new ResearchSample object, and add it to the <station_inventory> list.
        """
        sample = ResearchSample(experiment_name, hazard_level, price)
        station_inventory.append(sample)

    elif command == "print":
        """
        Prints all the items in the <station_inventory> list, using the "print_details" method.
        """
        for item in station_inventory:
            item.print_details()

    elif command == "store":
        """
        Receives module_name from the user
        """
        module_name = input("Please insert the module name: ")

        """
        Call `store` method with the received <module_name> for all the items in the list.
        """
        for item in station_inventory:
            item.store(module_name)

    elif command == "total_value":
        """
        Prints the TOTAL price of all the items in the <station_inventory> list.
        """
        total_price = sum(item.get_price() for item in station_inventory)
        print(f"The total price is {total_price}.")

    elif command == "avg_value":
        """
        Prints the AVERAGE price of all the items in the <station_inventory> list.
        """
        if len(station_inventory) == 0:
            print("No items in the station inventory.")
        else:
            avg_price = sum(item.get_price() for item in station_inventory) / len(station_inventory)
            print(f"The average price is {avg_price:.2f}.")

    elif command == "remove":
        """
        Receive the id of the item to remove from the user
        """
        item_id = int(input("Please insert the id of the item you want to remove: "))

        """
        If an item with the received id exists - remove the item.
        In any case - print an appropriate message.
        """
        found = False
        for item in station_inventory:
            if item.get_id() == item_id:
                station_inventory.remove(item)
                print(f"Item #{item_id} was removed from the list.")
                found = True
                break
        if not found:
            print(f"Item #{item_id} was not found in the list.")

    elif command == "critical":
        """
        Prints only the critical items in the inventory.
        """
        critical_items = [item for item in station_inventory if item.is_critical()]
        if len(critical_items) == 0:
            print("No critical items in the station inventory.")
        else:
            for item in critical_items:
                item.print_details()
    elif command == "created_items":
        """
        Prints the number of items created so far.
        """
        num_items = Item.get_number_of_created_items()
        print(f"{num_items} Items created so far.")
    elif command == "exit":
        break
    else:
        print(f"Sorry! The command {command} is unknown. Please try again.")

print("Thank you for using the SPACE STATION INVENTORY system!")
