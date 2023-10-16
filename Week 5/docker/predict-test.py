import requests


url = 'http://localhost:9696/predict'

customer = {
    "job": "retired", 
    "duration": 445, 
    "poutcome": "success"
}

response = requests.post(url, json=customer).json()
print(response)

print('Credit score for customer:', response['credit_score_probability'])
