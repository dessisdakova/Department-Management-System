import json
import pytest
import os
import re
from models import *
from unittest.mock import patch


class TestInitializing:
    def test_create_instance(self):
        dep = Department()

        assert dep.managers is not None, "List for managers should be created."
        assert len(dep.managers) == 0, "Created manager's list should be empty."


class TestAddManagerAndRemoveManagerFunctions:
    def test_adding_non_manager_object(self):
        dep = Department()
        with pytest.raises(TypeError, match="Only Manages can be added to the list."):
            dep.add_manager(Developer("Deya", "Atanasova", 3500, 2))

    def test_adding_manager_successfully(self):
        dep = Department()
        man = Manager("Deya", "Atanasova", 3500, 2)
        dep.add_manager(man)

        assert len(dep.managers) == 1, "Manager was not added to list."

    def test_adding_already_added_manager(self):
        dep = Department()
        man = Manager("Deya", "Atanasova", 3500, 2)
        dep.add_manager(man)
        with pytest.raises(ValueError,
                           match=re.escape(f"{man.first_name} {man.last_name} is already in the list.")):
            dep.add_manager(man)

    def test_removing_manager_successfully(self):
        dep = Department()
        man = Manager("Deya", "Atanasova", 3500, 2)
        dep.add_manager(man)

        dep.remove_manager(man)

        assert len(dep.managers) == 0, "Manager was not removed from list."

    def test_removing_manager_than_is_not_in_list(self):
        dep = Department()
        man = Manager("Deya", "Atanasova", 3500, 2)
        with pytest.raises(ValueError,
                           match=re.escape(f"{man.first_name} {man.last_name} is not in the list.")):
            dep.remove_manager(man)


class TestGiveSalaryFunction:
    def test_give_salary(self, capsys):
        team = [
            Developer("Krasimir", "Zoykov", 1500, 0),
            Developer("Momchil", "Slavov", 3000, 2)
        ]
        man = Manager("Deya", "Atanasova", 3500, 2, team)
        dep = Department([man])

        dep.give_salary()

        captured = capsys.readouterr()
        expected_output = (
            f"{man.first_name} {man.last_name} received {round(man.calculate_salary())} money.\n"
            f"{man.team[0].first_name} {man.team[0].last_name} received {round(man.team[0].calculate_salary())} money.\n"
            f"{man.team[1].first_name} {man.team[1].last_name} received {round(man.team[1].calculate_salary())} money.\n"
        )
        assert captured.out == expected_output, "The printed output did not match the expected output."


class TestPrintEmployeesSortedByNameFunction:
    def test_print_employee_sorted_by_name(self, capsys):
        team = [
            Developer("Krasimir", "Zoykov", 1500, 0),
            Developer("Momchil", "Slavov", 3000, 2)
        ]
        man = Manager("Deya", "Atanasova", 3500, 2, team)
        dep = Department([man])

        dep.print_employees_sorted_by_name()

        captured = capsys.readouterr()
        expected_output = (
            "Deya Atanasova - Manager\n"
            "Krasimir Zoykov - Developer\n"
            "Momchil Slavov - Developer\n"
        )
        assert captured.out == expected_output, "The printed output did not match the expected output."


class TestSerializationAndDeserializationOfData:
    def test_save_employees(self):
        # Setup sample data
        dev = Developer("Krasimir", "Zoykov", 1500, 2)
        des = Designer("Gabriela", "Stoeva", 1600, 3, 0.9)
        man = Manager("Deya", "Atanasova", 5000, 5, team=[dev, des])
        dep = Department([man])

        # Define a temporary file path

        temp_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data", "testing.json")

        # Call save_employees with the temporary path
        dep.save_employees(filename=str(temp_file))

        # Load the saved JSON data from the temporary file
        with open(temp_file, "r") as file:
            data = json.load(file)

        # Setup expected attributes for each dictionary
        expected_attr_for_manager = ["_first_name", "_last_name", "_base_salary", "_experience", "_team", "class"]
        expected_attr_for_dev = ["_first_name", "_last_name", "_base_salary", "_experience", "class"]
        expected_attr_for_des = ["_first_name", "_last_name", "_base_salary", "_experience", "_eff_coeff", "class"]

        # Verify data structure and content
        assert len(data) == 1, "There should be one manager saved in the list."

        # Verify data structure and content for manager
        for prop in expected_attr_for_manager:
            assert prop in data[0], f"'{prop}' attribute is missing for manager."

        assert data[0]["_first_name"] == "Deya", "Manager's first name does not match."

        assert len(data[0]["_team"]) == 2, "Manager's team should contain two employees."

        # Verify data structure and content for team members
        for prop in expected_attr_for_dev:
            assert prop in data[0]["_team"][0]
        assert data[0]["_team"][0]["_first_name"] == "Krasimir", "Developer's first name does not match."

        for prop in expected_attr_for_des:
            assert prop in data[0]["_team"][1]
        assert data[0]["_team"][1]["_first_name"] == "Gabriela", "Designer's first name does not match."

    def test_load_employees(self):
        dep = Department()
        temp_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data", "testing.json")

        dep.load_employees(filename=str(temp_file))

        assert len(dep.managers) == 1, "There should be one manager loaded from the list."
        for man in dep.managers:
            assert hasattr(man, "first_name"), "Manager missing first name."
            assert man.first_name == "Deya", "Incorrect values are loaded."
            assert hasattr(man, "last_name"), "Manager missing last name."
            assert hasattr(man, "base_salary"), "Manager missing base salary."
            assert hasattr(man, "experience"), "Manager missing experience."
            assert hasattr(man, "team"), "Manager missing team."
            for emp in man.team:
                assert hasattr(emp, "first_name"), "Employee missing first name."
                assert hasattr(emp, "last_name"), "Employee missing last name."
                assert hasattr(emp, "base_salary"), "Employee missing base salary."
                assert hasattr(emp, "experience"), "Employee missing experience."
                if isinstance(emp, Designer):
                    assert hasattr(emp, "eff_coeff")
                    assert emp.first_name == "Gabriela", "Incorrect values are loaded."

    def test_load_employees_handles_error(self, capsys):
        dep = Department()
        invalid_file = "non_existing_file.json"

        dep.load_employees(str(invalid_file))

        captured = capsys.readouterr()  # Capture the printed output

        assert captured.out == f"Error: The file {invalid_file} was not found.\n"
