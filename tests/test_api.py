import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse

class TestCalculatorAPI():

    def test_calculate_add(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "add",
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(url, json=payload)

    def test_gen_addition(self):
        client = Client(base_url = "http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1, operand2=5))
        assert isinstance(response, ResultResponse)
        assert response.result == 6

    def test_gen_subtraction(self):
        client = Client(base_url = "http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.SUBTRACT, operand1=33, operand2=13))
        assert isinstance(response, ResultResponse)
        assert response.result == 20

    def test_gen_multiply(self):
        client = Client(base_url = "http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.MULTIPLY, operand1=10, operand2=10))
        assert isinstance(response, ResultResponse)
        assert response.result == 100

    def test_gen_divide(self):
        client = Client(base_url = "http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.DIVIDE, operand1=15, operand2=3))
        assert isinstance(response, ResultResponse)
        assert response.result == 5