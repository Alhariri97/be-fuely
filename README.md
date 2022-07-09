Hello and welcome to the Fuely app backend code.. This bakkend framework uses python fastapi and mongo database Here is a guide to installing and running the backend:

1. Clone this repo into your preferred location

2. Sign up for an account to mongodb, install and run mongodb: [https://www.mongodb.com/cloud/atlas/lp/try2?https%3A%2F%2Fwww.mongodb.com%2Fcloud%2Fatlas%2Flp%2Ftry2-aterms=&adgroup=115749705303]

3. This app uses a google api key: Sign up for a free subscription to googlemaps platform to get one: [https://developers.google.com/maps]

4. Ensure that you have python 3.10 or above with pip 22.1.2

5. install venv: 

```sudo apt-get -y install virtualenv```

6. cd to be-fuely via the terminal. Make the virtual environment with the following command: 

```python3 -m venv petrol```

7. Activate the virtual envronment: 

```source petrol/bin/activate```

8. Install the required dependencies: 

```pip install -r requirements.txt```

9. Create a local database on mongo

10. In the projects root, make a .env file that contains the following code: 

```googleAPIKey=<yourapiykeyhere>```
```PersonalDBConnection= mongodb+srv://<mongousernamehere>:<mongodbpasswordhere>@cluster0.lek7zey.mongodb.net/?retryWrites=true&w=majority```

11. You can now run tests on the backend with the following command: 

```pytest -n auto```
