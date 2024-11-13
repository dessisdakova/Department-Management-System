from .employee import Employee


class Designer(Employee):
    """Derived class from Employee class for designers"""
    def __init__(self, f_name: str, l_name: str, b_salary: int, exp: int, coefficient: float):
        """(Constructor) Creates an object by calling parent constructor and adding additional field"""
        super().__init__(f_name, l_name, b_salary, exp)
        self._eff_coeff = self.validate_efficiency_coefficient(coefficient)

    @staticmethod
    def validate_efficiency_coefficient(coefficient: float) -> float:
        if not isinstance(coefficient, float):
            raise TypeError("Efficiency coefficient must be a float number.")
        if not 0.0 <= coefficient <= 1.0:
            raise ValueError("Efficiency coefficient must be between 0.0 and 1.0")
        return coefficient

    @property
    def eff_coeff(self):
        """Returns the efficiency coefficient of a designer"""
        return self._eff_coeff

    @eff_coeff.setter
    def eff_coeff(self, new_value):
        """Changes the efficiency coefficient of a designer"""
        self._eff_coeff = new_value

    def __str__(self):
        """Returns a descriptive string representation for each designer.
        Calls parent method and adds additional information"""
        base_str = super().__str__()
        return f"{base_str} They have an efficiency coefficient of {self._eff_coeff}."

    def calculate_salary(self):
        """Calculates salary with additional conditions for designer and returns value"""
        counted_salary = super().calculate_salary()
        bonus = counted_salary * self._eff_coeff
        return counted_salary + bonus
