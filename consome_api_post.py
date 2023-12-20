import requests

post_data = [{
                "0":5,
                "1":8,
                "2":15
            }]

#url = ' http://127.0.0.1:5000/square/'

url = ' http://localhost:5000/square/'

response = requests.post(url, json=post_data)
print(response.text)