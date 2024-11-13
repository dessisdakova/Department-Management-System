from models import *
import pytest
import re


class TestInitializing:
    def test_create_instance_without_team(self):
        test_manager = Manager("Ivan", "Stefanov", 5000, 5)

        assert test_manager.team is not None, "List for team should be created."
        assert len(test_manager.team) == 0, "Created team list should be empty."

    def test_create_instance_with_team(self):
        team = [
            Developer("Krasimir", "Zoykov", 1500, 0),
            Designer("Gabriela", "Stoeva", 1500, 1, 0.99)
        ]
        test_manager = Manager("Ivan", "Stefanov", 5000, 5, team)

        assert test_manager.team is not None, "Manager's team list should not be None when a team is passed."
        assert len(test_manager.team) == len(team), \
            "Manager's team should have the same number of members as the passed team."

        for index, member in enumerate(test_manager.team):
            assert member.first_name == team[index].first_name, \
                f"Team member at index {index} has an incorrect first name."
            assert member.last_name == team[index].last_name, \
                f"Team member at index {index} has an incorrect last name."
            assert member.base_salary == team[index].base_salary, \
                f"Team member at index {index} has an incorrect base salary."
            assert member.experience == team[index].experience, \
                f"Team member at index {index} has an incorrect experience."


class TestAddEmployeeToTeamFunction:
    def test_adding_employees_with_valid_data(self):
        dev = Developer("Krasimir", "Zoykov", 1500, 0)
        des = Designer("Gabriela", "Stoeva", 1500, 1, 0.99)
        man = Manager("Ivan", "Stefanov", 5000, 5)

        man.add_employees_to_team(dev, des)

        assert len(man.team) == 2, "Employees should be added to team."

    def test_adding_employee_with_invalid_type(self):
        des = ("Gabriela", "Stoeva", 1500, 1, 0.99)
        man = Manager("Ivan", "Stefanov", 5000, 5)

        with pytest.raises(TypeError, match="Only Designers and Developer can be added to team."):
            man.add_employees_to_team(des)

    def test_adding_employee_that_exists_in_list(self):
        des = Designer("Gabriela", "Stoeva", 1500, 1, 0.99)
        man = Manager("Ivan", "Stefanov", 5000, 5)
        man.add_employees_to_team(des)

        with pytest.raises(ValueError, match=re.escape(f"{des.first_name} {des.last_name} "
                                                       f"({type(des).__name__}) is already in this team.")):
            man.add_employees_to_team(Designer("Gabriela", "Stoeva", 1500, 1, 0.99))


class TestRemoveEmployeeToTeamFunction:
    def test_removing_employee_with_valid_data(self):
        team = [
            Developer("Krasimir", "Zoykov", 1500, 0),
            Designer("Gabriela", "Stoeva", 1500, 1, 0.99)
        ]
        man = Manager("Ivan", "Stefanov", 5000, 5, team)

        man.remove_employees_from_team(Developer("Krasimir", "Zoykov", 1500, 0))

        assert len(man.team) == 1, "Employees should be removed from team."
        assert man.team[0].first_name == "Gabriela", "Correct employee should be removed from team."

    def test_removing_employee_with_invalid_type(self):
        des = ("Gabriela", "Stoeva", 1500, 1, 0.99)
        man = Manager("Ivan", "Stefanov", 5000, 5)

        with pytest.raises(TypeError, match="Only Designers and Developer can be added to team."):
            man.remove_employees_from_team(des)

    def test_removing_employee_that_is_not_in_team(self):
        dev = Developer("Mihail", "Atanasov", 4000, 3)
        team = [
            Developer("Krasimir", "Zoykov", 1500, 0),
            Designer("Gabriela", "Stoeva", 1500, 1, 0.99)
        ]
        man = Manager("Ivan", "Stefanov", 5000, 5, team)

        with pytest.raises(ValueError, match=re.escape(f"{dev.first_name} {dev.last_name} "
                                                       f"({type(dev).__name__}) is not part of this team.")):
            man.remove_employees_from_team(dev)


class TestCalculateSalaryFunction:
    @pytest.mark.parametrize("team_size, expected_bonus", [
        (0, 0),
        (5, 0),
        (6, 200),
        (10, 200),
        (11, 300),
        (20, 300)
    ])
    def test_calculate_salary_based_on_team_members(self, team_size, expected_bonus):
        team = [Designer("Test", "Data", 1500, 1, 0.99) for _ in range(team_size)]
        test_manager = Manager("Ivan", "Stefanov", 5000, 5, team)

        assert len(test_manager.team) == team_size, "Team size does not match."
        assert test_manager.calculate_salary() == 5200 + expected_bonus, \
            f"Expected bonus for {team_size} team members is not calculated correctly."

    @pytest.mark.parametrize("team_size, devs, expected_bonus", [
        (2, 1, 0),
        (3, 2, 520),
        (2, 2, 520)
    ])
    def test_calculate_salary_based_on_developers_in_team(self, team_size, devs, expected_bonus):
        designers = team_size - devs

        team = [Developer("Dev", f"Dev", 1500, 1) for _ in range(devs)] + \
               [Designer("Des", f"Des", 1500, 1, 0.99) for _ in range(designers)]

        test_manager = Manager("Ivan", "Stefanov", 5000, 5, team)
        assert len(test_manager.team) == len(team), "Team size does not match."
        assert test_manager.calculate_salary() == 5200 + expected_bonus, \
            f"Expected bonus for {designers} designers and {devs} developers is not calculated correctly."
