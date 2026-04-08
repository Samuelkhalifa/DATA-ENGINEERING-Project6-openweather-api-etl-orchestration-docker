from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import mysql.connector
import os



API_KEY = os.getenv("OPENWEATHER_API_KEY")


UK_CITIES = [
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904},
    {"name": "Manchester", "lat": 53.4808, "lon": -2.2426},
    {"name": "Glasgow", "lat": 55.8642, "lon": -4.2518},
    {"name": "Liverpool", "lat": 53.4084, "lon": -2.9916},
    {"name": "Leeds", "lat": 53.8008, "lon": -1.5491},
    {"name": "Sheffield", "lat": 53.3811, "lon": -1.4701},
    {"name": "Bristol", "lat": 51.4545, "lon": -2.5879},
    {"name": "Newcastle", "lat": 54.9784, "lon": -1.6174},
    {"name": "Nottingham", "lat": 52.9548, "lon": -1.1581}
]



def fetch_weather(lat, lon, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = {
        "city": city_name,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "date": datetime.utcnow().date()
    }
    return weather



def store_weather():

    import logging

    conn = mysql.connector.connect(
        host="mysql", 
        database= os.getenv("MYSQL_DB"),
        user= os.getenv("MYSQL_USER"),
        password= os.getenv("MYSQL_PASSWORD")
    )
    
    cur = conn.cursor()
   

    for city in UK_CITIES:
        #try:
            
            weather = fetch_weather(city["lat"], city["lon"], city["name"])
            logging.info(f"Fetched weather for {city['name']}: {weather}")

            
            insert_query = """
            INSERT INTO weather (city, temperature, humidity, weather_description, date)
            VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(insert_query, (
                weather["city"],
                weather["temperature"],
                weather["humidity"],
                weather["description"],
                weather["date"]
            ))

        #    logging.info(f"Inserted weather for {city['name']} successfully.")
        #except Exception as e:
        #    logging.error(f"Error with {city['name']}: {e}")



    conn.commit()
    cur.close()
    conn.close()



default_args = {
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="weather_etl",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
) as dag:
    
    store_weather_task = PythonOperator(
        task_id="store_weather",
        python_callable=store_weather
    )

    store_weather_task
