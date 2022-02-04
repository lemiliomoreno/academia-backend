# Sample Flask App to interact with DynamoDB

## Setup

### Set environment variables

```bash
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=us-west-2
export FLASK_APP=flask_app
```

### Run application 

```bash
flask run
```

## Making API requests

### Get user

```python
import requests

response = requests.get("http://127.0.0.1:5000/users?email=lemiliomoreno@gmail.com")
response.json()
```

### Create user

```python
import requests

response = requests.post("http://127.0.0.1:5000/users", json={"email": "lemiliomoreno@gmail.com", "username": "luisemd", "password": "emilio"})
response.json()
```

### Login

```python
import requests

response = requests.post("http://127.0.0.1:5000/login", json={"email": "lemiliomoreno@gmail.com", "password": "emilio"})
response.json()
```
