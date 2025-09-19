API Data Pipeline with Postgres and Docker

This project fetches product data from the API : https://api.restful-api.dev/objects

and stores it into a Postgres database running inside a Docker container.

Steps to Run
1. Pull the Postgres image
docker pull postgres

2. Create a Docker volume for data persistence
docker volume create pg-data

3. Run the Postgres container with volume attached
docker run --name some-postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5431:5432 \
  -v pg-data:/var/lib/postgresql/data \
  -d postgres


-p 5431:5432 → maps local port 5431 to Postgres container’s 5432

-v pg-data:/var/lib/postgresql/data → ensures DB data persists even if the container stops

4. Configure environment variables

Create a .env file in the project root:

DB_HOST=<local ip not localhost>   # local IP of your machine
DB_PORT=<port_no>
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=mysecretpassword


⚠️ Note: Do not use localhost as DB_HOST.
Inside a Docker container, localhost refers to the container itself, not your machine.

5. Run the Python script in a container

Use Docker Compose to start the pipeline container:

docker compose up


This will:

Build and run the Python script inside a container

Fetch API data

Insert data into the Postgres container

🔍 Verify Data

You can check the inserted data in two ways:

Using psql inside the Postgres container

docker exec -it some-postgres psql -U postgres -d postgres
\dt          # list tables
SELECT * FROM products;


Using pgAdmin (GUI Tool)

Add a new connection in pgAdmin with:

Host: 192.168.1.4

Port: 5431

Username: postgres

Password: mysecretpassword



 Now you can fetch live API data and store it in a Dockerized Postgres DB!
