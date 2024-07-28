import requests

token = "4f28c75b86a790a5885b30b29be830984597f613"

# set the Authorization header with the token
headers = {
    "Authorization": f"Token {token}",
    "Content-Type": "application/json"
}

# make the POST request
response = requests.post("http://127.0.0.1:8000/api/posts/", headers=headers, json={"title": "New post", "content": "This is a new post"})
# response = requests.get('http://127.0.0.1:8000/api/posts/', headers=headers)
print(response.json())