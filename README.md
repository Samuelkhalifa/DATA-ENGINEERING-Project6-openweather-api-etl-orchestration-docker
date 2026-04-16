Project in the context of Data Engineering self-learning

<br>

## &#128295; Used tools
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-5BC0EB?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-000000?style=for-the-badge&logo=gnubash&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![phpMyAdmin](https://img.shields.io/badge/phpMyAdmin-6C78AF?style=for-the-badge&logo=phpmyadmin&logoColor=white)


<br>

## [Subject : Build a complete ETL-process by using containerization with Docker and Airflow orchestration, to serve openweather-API data]

<br>

## &#x1F4DD; Project graph

<br>

<p align="center";>
  <img width="978" height="269" alt="Capture d’écran 2026-04-16 à 17 22 27" 
  src="https://github.com/user-attachments/assets/f5626bff-ef9f-409e-b7cb-294fc918b15e" />
</p>

<br>

## &#127919; Project steps

<br>

  * Retrieve data from openweather-API.
  * Transform data with `Python`.
  * Set up docker with a docker-compose.yml file and configurate all necessary services (`MySQL`and a MySQL UI `phpmyadmin`, `airflow` and dashboard tool `metabase`).
  * Activate airflow dag to make data travel from API source to metabase, through a SQL database.

<br>

## &#128640; Project setup and activation

<br>

`Git clone` the project and get inside, to project root.
  ```bash
  git clone <repository-url> openweather-api-etl-orchestration-docker
  cd openweather-api-etl-orchestration-docker
  ```
<br>

Write into a `env.` file your personal API key.
  ```bash
  touch .env # (for Mac)
  ```
  ```dotenv
  MYSQL_USER=""
  MYSQL_PASSWORD=""
  MYSQL_ROOT_PASSWORD=""
  MYSQL_DB=""

  AIRFLOW_USER=""
  AIRFLOW_PASSWORD=""
  
  OPENWEATHER_API_KEY=""
  ```

<br>

Enable `docker` by running the `docker-compose` file, which will create all necessary services, volumes and networks.
  ```bash
  docker-compose up
  ```
<br>

Go to `localhost:8081` to manage your SQL database through `phpmyadmin`.

Go to `localhost:8080` to trigger your `Airflow` dag and start orchestrationg ETL process.

Go to `localhost:3000` to start using dashording tool `Metabase`
