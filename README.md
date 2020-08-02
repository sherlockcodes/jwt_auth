# JWT auth using Django

Django Rest API with JSON web token(JWT) authentication.

## Note
Since JWT authentication is stateless, I added another field in user model called jwt_secret to change JWT token while logout.
When user logs out, a new jwt_secret value will be generated for a user and old JWT token will be invalidated. 

## Usage

```bash
cd jwt_auth
```


Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```
Install all the packages from requirements.txt

```bash
pip3 install requirements.txt
```

Migrate

```bash
python3 manage.py migrate
```

Start the app
```bash
python3 manage.py runserver
```

Please refer jwt.postman_collection.json to play with API's.

 
## TODO's
need to host this solution. will do if required.
