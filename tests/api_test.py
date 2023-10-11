import requests

data = {
    "currentAge":19,
    "retirementAge":60,
    "corpusGoal": 600000,
    "interestRate": 10
}

post_request = requests.post("http://127.0.0.1:5000/calculate_api", json = data)


print(post_request.json())
