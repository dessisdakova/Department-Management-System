from models.designer import Designer
import pytest


class TestInitializing:
    def test_create_instance_with_complete_valid_data(self):
        designer = Designer("Ivan", "Stefanov", 1500, 5, 0.95)

        assert designer is not None, "Object should not be None."
        assert isinstance(designer, Designer), "Object should be an instance of Designer"

    @pytest.mark.parametrize("invalid_coeff", [-0.1, 1.1, 2.0])
    def test_designer_efficiency_coefficient_out_of_bounds(self, invalid_coeff):
        with pytest.raises(ValueError, match="Efficiency coefficient must be between 0.0 and 1.0"):
            Designer("Ivan", "Stefanov", 1500, 5, invalid_coeff)

    @pytest.mark.parametrize("coeff", [-1, 2, 3])
    def test_create_instance_with_invalid_data_for_eff_coeff(self, coeff):
        with pytest.raises(TypeError, match="Efficiency coefficient must be a float number."):
            Designer("Ivan", "Stefanov", 1500, 5, coeff)


class TestCalculateSalaryFunction:
    @pytest.mark.parametrize("eff_coeff, expected", [
        (0.9, 1350),
        (0.78, 1170)
    ])
    def test_calculate_salary(self, eff_coeff, expected):
        designer = Designer("Ivan", "Stefanov", 1500, 1, eff_coeff)

        assert designer.calculate_salary() == designer.base_salary + expected, \
            "Should return salary multiplied by eff_coeff"
