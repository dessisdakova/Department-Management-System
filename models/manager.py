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
        for new_member in employees:
            if not isinstance(new_member, (Developer, Designer)):
                raise TypeError("Only Designers and Developer can be added to team.")

            for team_member in self.team:
                if new_member.first_name == team_member.first_name \
                        and new_member.last_name == team_member.last_name \
                        and type(new_member).__name__ == type(team_member).__name__:
                    raise ValueError(f"{new_member.first_name} {new_member.last_name} "
                                     f"({type(new_member).__name__}) is already in this team.")
            self._team.append(new_member)

    def remove_employees_from_team(self, *employees: (Designer, Developer)):
        """Removes an employee from manager's team"""
        for member_to_remove in employees:
            if not isinstance(member_to_remove, (Developer, Designer)):
                raise TypeError("Only Designers and Developer can be added to team.")

            for team_member in self.team:
                if member_to_remove.first_name != team_member.first_name \
                        and member_to_remove.last_name != team_member.last_name \
                        and type(member_to_remove).__name__ != type(team_member).__name__:
                    raise ValueError(f"{member_to_remove.first_name} {member_to_remove.last_name} "
                                     f"({type(member_to_remove).__name__}) is not part of this team.")
                elif member_to_remove.first_name == team_member.first_name \
                        and member_to_remove.last_name == team_member.last_name \
                        and type(member_to_remove).__name__ == type(team_member).__name__:
                    self._team.remove(team_member)

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
