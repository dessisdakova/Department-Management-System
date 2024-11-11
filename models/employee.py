class Employee:
    """Base class for employees"""
    def __init__(self, f_name: str, l_name: str, b_salary: float, exp: int):
        """(Constructor) Creates an object with given attributes"""
        if not f_name.isalpha():
            raise ValueError("First name must contains alphabetic characters only.")
        self._first_name = f_name

        if not l_name.isalpha():
            raise ValueError("Last name must contains alphabetic characters only.")
        self._last_name = l_name

        if not isinstance(b_salary, (int, float)):
            raise TypeError("Base salary must be a number.")
        if b_salary <= 0:
            raise ValueError("Base salary must be bigger than zero.")
        self._base_salary = b_salary

        if not isinstance(exp, int):
            raise TypeError("Experience must be an integer.")
        if exp < 0:
            raise ValueError("Experience must be a positive integer.")
        self._experience = exp

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
