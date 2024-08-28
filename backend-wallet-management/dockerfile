FROM python:3.11-slim

WORKDIR /backend-wallet-management

COPY requirements.txt /backend-wallet-management/
RUN pip3 install -r /backend-wallet-management/requirements.txt
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8007"]

