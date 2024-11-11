from .employee import Employee
from .designer import Designer
from .developer import Developer
from typing import List, Union


class Manager(Employee):
    """Derived class from Employee class for managers"""
    def __init__(self, f_name: str, l_name: str, b_salary: int, exp: int,
                 team: List[Union[Developer, Designer]] = None):
        """(Constructor) Creates an object by calling parent constructor and adding optional field"""
        super().__init__(f_name, l_name, b_salary, exp)
        self._team = team if team is not None else []

    @property
    def team(self):
        """Returns manager's team"""
        return self._team

    def add_employees_to_team(self, *employees: (Designer, Developer)):
        """Adds an employee to manager's team"""
        for employee in employees:
            if not isinstance(employee, (Developer, Designer)):
                raise TypeError("Only Designers and Developer can be added to team.")

            if employee in self._team:
                raise ValueError(f"{employee.first_name} {employee.last_name} "
                                 f"({type(employee).__name__}) is already in this team.")
            self._team.append(employee)

    def remove_employees_from_team(self, *employees: (Designer, Developer)):
        """Removes an employee from manager's team"""
        for employee in employees:
            if employee not in self._team:
                raise ValueError(f"{employee.first_name} {employee.last_name} "
                                 f"({type(employee).__name__}) is not part of this team.")
            self._team.remove(employee)

    def __str__(self):
        """Returns a descriptive string representation for each manager.
        Calls parent method and adds additional information"""
        base_str = super().__str__()
        return f"{base_str} They manage a team of {len(self.team)} employees."

    def calculate_salary(self):
        """Calculates salary with additional conditions for manager and returns value"""
        counted_salary = super().calculate_salary()
        team_size_bonus = 200 if 5 < len(self.team) <= 10 else 300 if len(self.team) > 10 else 0
        devs_in_team = len([employee for employee in self._team if isinstance(employee, Developer)])
        dev_ratio_bonus = counted_salary * 0.1 if len(self.team) / 2 < devs_in_team else 0
        return counted_salary + team_size_bonus + dev_ratio_bonus
