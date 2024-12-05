# industry-4-0-backend
the backend part of the laptop recommendation system developed for the Industry 4.0 course

# usage

in order to serve the application backend, one has to perform the following steps:

1. install all the project dependencies from requirements.txt using the below command:
```
  pip install -r requirements.txt
```
2. switch to the *application* directory using the below command:
```
  cd industry-4-0-backend/application 
```
3. serve the backend by executing the **app.py** script.

thereafter, one will be able to send requests to the */get_recommendations* endpoint of the API. 
example request:
```
curl --location 'http://127.0.0.0:8000/get_recommendations' \
--header 'Content-Type: application/json' \
--data '{
    "laptop_description": "a laptop for office tasks",
    "laptop_brands": [
        "HP",
        "Acer",
        "MSI"
    ],
    "laptop_price_range": [1000, 2000]
}'
```
where host, port can be configured in the app.py file. 
