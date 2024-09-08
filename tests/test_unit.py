from BE.calculator_helper import CalculatorHelper
import pytest

class BaseSetupTeardown():

    def setup_method(self, method):
        # Arrange: Instantiate the CalculatorHelper object
        self.calculator = CalculatorHelper()
    
    def teardown_method(self, method):
        # Teardown: Clean up the object
        self.calculator = None

class TestCalculatorMethods(BaseSetupTeardown):

    @pytest.mark.parametrize("test_input_a, test_input_b ,expected", [(3, 5, 8), (7, 3 , 10), (33, 4, 37)])

    def test_addition(self, test_input_a, test_input_b, expected):
        # Arrange
        ### calculator = CalculatorHelper()
        # Action
        value = self.calculator.add(test_input_a, test_input_b)
        # Assert
        assert value == expected
        
    def test_subtraction(self):
        # Arrange
        ### calculator = CalculatorHelper()
        # Action
        value = self.calculator.subtract(3,1)
        # Assert
        assert value == 2, "Expected value result is 2"

    def test_multiplication(self):
        # Arrange
        ### calculator = CalculatorHelper()
        # Action
        value = self.calculator.multiply(3,2)
        # Assert
        assert value == 6, "Expected value result is 6"
        
    def test_multiplication(self):
        # Arrange
        ### calculator = CalculatorHelper()
        # Action
        value = self.calculator.multiply(-3,-1)
        # Assert
        assert value == 3, "Expected value result is 3"
        
    def test_division(self):
        # Arrange
        ### calculator = CalculatorHelper()
        # Action
        value = self.calculator.divide(4,2)
        # Assert
        assert value == 2, "Expected value result is 2"
        
    def test_division_by_zero(self):
        # Arrange
        ### calculator = CalculatorHelper()
        # Action
        with pytest.raises(ZeroDivisionError) as exinfo:
            value = self.calculator.divide(4,0)
        # Assert
        assert "division by zero" in str(exinfo.value), "Expected exception"

    
