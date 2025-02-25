import requests


class PaymentGateway:
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, order_id, amount):
        response = requests.post(
            "https://payment.example.com/charge",
            json={
                "order_id": order_id,
                "amount": amount,
                "api_key": self.api_key,
            },
        )
        return response.json()
