FROM python:3.12-slim
COPY calculator.py calculator_helper.py calculator_rest_service.py logger.py models.py requirements.txt __pycache__ /
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "calculator.py" ]