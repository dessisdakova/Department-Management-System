from .manager import Manager
from .developer import Developer
from .designer import Designer
import json
import os
from typing import List


class Department:
    """A class managing managers and their teams"""
    def __init__(self, managers: List[Manager] = None):
        """(Constructor) Creates an object that saves a list of managers"""
        self._managers = managers if managers is not None else []

    @property
    def managers(self):
        return self._managers

    def add_manager(self, *managers: Manager):
        """Adds manager to the list"""
        for new_manager in managers:
            if not isinstance(new_manager, Manager):
                raise TypeError("Only Manages can be added to the list.")

            for current_manager in self.managers:
                if new_manager.first_name == current_manager.first_name and \
                        new_manager.last_name == current_manager.last_name:
                    raise ValueError(f"{new_manager.first_name} {new_manager.last_name} is already in the list.")
            self.managers.append(new_manager)

    def remove_manager(self, *managers: Manager):
        """Removes manager from the list"""
        for manager_to_remove in managers:
            for current_manager in self.managers:
                if manager_to_remove.first_name != current_manager.first_name and \
                        manager_to_remove.last_name != current_manager.last_name:
                    raise ValueError(f"{manager_to_remove.first_name} {manager_to_remove.last_name} isn't in the list.")
                elif manager_to_remove.first_name == current_manager.first_name and \
                        manager_to_remove.last_name == current_manager.last_name:
                    self.managers.remove(current_manager)

    def give_salary(self):
        """Prints all the employees in the department and their calculated salary"""
        for manager in self.managers:
            print(f"{manager.first_name} {manager.last_name} received {round(manager.calculate_salary())} money.")
            for employee in manager.team:
                print(f"{employee.first_name} {employee.last_name} received "
                      f"{round(employee.calculate_salary())} money.")

    def print_employees_sorted_by_name(self):
        """Returns all employees sorted by name."""
        all_employees = []
        for manager in self.managers:
            all_employees.append(manager)
            all_employees.extend(manager.team)
        sorted_employees = sorted(all_employees, key=lambda emp: (emp.first_name, emp.last_name))
        for employee in sorted_employees:
            print(f"{employee.first_name} {employee.last_name} - {type(employee).__name__}")

    def serialize_employee(self, emp):
        """Serializes one object into dictionary and adds its class"""
        employee_dictionary = emp.__dict__.copy()  # Serializes object using dunder method __dict__

        if isinstance(emp, Developer):  # Check which class the object belongs to and adds an additional key
            employee_dictionary["class"] = str(type(emp).__name__)
        if isinstance(emp, Designer):
            employee_dictionary["class"] = str(type(emp).__name__)
        if isinstance(emp, Manager):
            employee_dictionary["class"] = str(type(emp).__name__)

        return employee_dictionary

    def save_employees(self, filename="employees.json"):
        """Creates a file, saves serialized objects in a list and writes the list in a JSON file"""
        full_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data", filename)

        all_employees = []
        for manager in self.managers:
            manager_data = self.serialize_employee(manager)
            manager_data["_team"] = [self.serialize_employee(employee) for employee in manager.team]
            all_employees.append(manager_data)

        with open(full_filename, "w") as file:
            json.dump(all_employees, file, indent=4)

        print(f"Data saved to '{filename}' in data folder.")

    def deserialize_employee(self, employee_data):
        """Deserializes dictionary and creates an object of corresponding class"""
        if employee_data["class"] == "Manager":
            employee = Manager(employee_data["_first_name"], employee_data["_last_name"],
                               employee_data["_base_salary"], employee_data["_experience"])
        elif employee_data["class"] == "Developer":
            employee = Developer(employee_data["_first_name"], employee_data["_last_name"],
                                 employee_data["_base_salary"], employee_data["_experience"])
        elif employee_data["class"] == "Designer":
            employee = Designer(employee_data["_first_name"], employee_data["_last_name"],
                                employee_data["_base_salary"], employee_data["_experience"],
                                employee_data["_eff_coeff"])
        return employee

    def load_employees(self, filename: str = "employees.json"):
        """Reads a file and creates the structure for employees"""
        full_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data", filename)
        try:
            with open(full_filename, "r") as file:
                all_employees = json.load(file)

            for manager_data in all_employees:
                manager = self.deserialize_employee(manager_data)

                for employee_data in manager_data["_team"]:
                    employee = self.deserialize_employee(employee_data)
                    manager.add_employees_to_team(employee)

                self.add_manager(manager)

            print(f"Data loaded successfully from {filename}.")
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
