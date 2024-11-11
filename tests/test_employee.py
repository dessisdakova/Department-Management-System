from models.employee import Employee
import pytest


class TestInitializing:
    def test_create_instance_with_complete_valid_data(self):
        employee = Employee("Ivan", "Stefanov", 1500, 5)

        assert employee is not None, "Object should not be None."
        assert isinstance(employee, Employee), "Object should be an instance of Employee"

    @pytest.mark.parametrize("first_name, last_name, base_salary, experience,", [
        ("Ivan2", "Stefanov", 1500, 5),  # Invalid data for first_name
        ("Ivan", "Stefanov!", 1500, 5),  # Invalid data for last_name
        ("Ivan", "Stefanov", 0, 5),  # Invalid data for base_salary
        ("Ivan", "Stefanov", 1500, -1)  # Invalid data for experience
    ])
    def test_create_instance_with_invalid_value(self, first_name, last_name, base_salary,experience):
        with pytest.raises(ValueError):
            Employee(first_name, last_name, base_salary, experience)

    @pytest.mark.parametrize("first_name, last_name, base_salary, experience,", [
        ("Ivan", "Stefanov", "1500", 5),  # Invalid type for base_salary
        ("Ivan", "Stefanov", 1500, 5.5)  # Invalid type for experience
    ])
    def test_create_instance_with_invalid_type_od_data(self, first_name, last_name, base_salary,experience):
        with pytest.raises(TypeError):
            Employee(first_name, last_name, base_salary, experience)


class TestCalculateSalaryFunction:
    @pytest.mark.parametrize("base, experience, expected", [
        (1500, 0, 1500),
        (1700, 2, 1700)
    ])
    def test_calculate_salary_experience_less_than_two_years(self, base, experience, expected):
        employee = Employee("Ivan", "Stefanov", base, experience)

        assert employee.calculate_salary() == expected, "Should return base salary"

    @pytest.mark.parametrize("base, experience, expected", [
        (2000, 3, 2200),
        (3000, 5, 3200)
    ])
    def test_calculate_salary_experience_more_than_two_less_than_five_years(self, base, experience, expected):
        employee = Employee("Ivan", "Stefanov", base, experience)

        assert employee.calculate_salary() == expected, "Should return base salary + 200"

    @pytest.mark.parametrize("base, experience, expected", [
        (5500, 6, 7100),
        (9000, 15, 11300)
    ])
    def test_calculate_salary_experience_more_than_five_years(self, base, experience, expected):
        employee = Employee("Ivan", "Stefanov", base, experience)

        assert employee.calculate_salary() == expected, "Should return base salary * 1.2 + 500"
