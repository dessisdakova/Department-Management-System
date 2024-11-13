class Employee:
    """Base class for employees"""
    def __init__(self, f_name: str, l_name: str, b_salary: float, exp: int):
        """(Constructor) Creates an object with given attributes"""
        self._first_name = self.validate_name(f_name, "First name")
        self._last_name = self.validate_name(l_name, "Last name")
        self._base_salary = self.validate_base_salary(b_salary)
        self._experience = self.validate_experience(exp)

    @staticmethod
    def validate_name(name: str, attribute: str) -> str:
        if not name.isalpha():
            raise ValueError(f"{attribute} must contains alphabetic characters only.")
        return name

    @staticmethod
    def validate_base_salary(salary: float) -> float:
        if not isinstance(salary, (int, float)):
            raise TypeError("Base salary must be a number.")
        if salary <= 0:
            raise ValueError("Base salary must be bigger than zero.")
        return salary

    @staticmethod
    def validate_experience(experience: int) -> int:
        if not isinstance(experience, int):
            raise TypeError("Experience must be an integer.")
        if experience < 0:
            raise ValueError("Experience must be a positive integer.")
        return experience

    @property
    def first_name(self):
        """Returns the first name of an employee"""
        return self._first_name

    @property
    def last_name(self):
        """Returns the last name of an employee"""
        return self._last_name

    @property
    def base_salary(self):
        """Returns the salary of an employee"""
        return self._base_salary

    @base_salary.setter
    def base_salary(self, new_value):
        """Changes the salary of an employee"""
        self._base_salary = new_value

    @property
    def experience(self):
        """Returns the experience of an employee"""
        return self._experience

    @experience.setter
    def experience(self, new_value):
        """Changes the experience of an employee"""
        self._experience = new_value

    def __str__(self):
        """Returns a descriptive string representation for each employee"""
        return f"{self._first_name} {self._last_name} is a {type(self).__name__} " \
               f"with base salary of €{self._base_salary} and {self._experience} years of experience."

    def calculate_salary(self):
        """Calculates salary on given conditions and returns value"""
        if self._experience <= 2:
            return self._base_salary
        elif 2 < self._experience <= 5:
            return self._base_salary + 200
        elif self._experience > 5:
            return self._base_salary * 1.2 + 500
