from locust import HttpUser, task, between
import json
import random

class CalculatorUser(HttpUser):

    wait_time = between(2,4)

    def on_start(self):
        pass

    @task
    def add(self):
        data = [[-15, -45, -60], [-10, 20, 10], [50000, 100000, 150000], [10000000, 1000000, 11000000]]
        data_to_use = random.choice(data)
        add = {
            "operation": "add",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Result was {response_data['result']}")

    @task
    def subtract(self):
        data = [[-15, -45, 30], [-10, 20, -30], [100, 1000, -900], [1000, 100, 900]]
        data_to_use = random.choice(data)
        body = {
            "operation": "subtract",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=body) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Result was {response_data['result']}")

    @task
    def multiply(self):
        data = [[10, 10, 100], [5, 5, 25], [-10, 2, -20], [1000, 1000, 1000000]]
        data_to_use = random.choice(data)
        body = {
            "operation": "multiply",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=body) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Result was {response_data['result']}")            

    @task(10)
    def divide(self):
        data = [[25, 5, 5], [-100, 20, -5], [50000, 10, 10000], [100, 4, 25]]
        data_to_use = random.choice(data)
        body = {
            "operation": "divide",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=body) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Result was {response_data['result']}")
                
if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
