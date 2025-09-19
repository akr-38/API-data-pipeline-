ok this is the code for the python script that store the api data from the url :"https://api.restful-api.dev/objects"
into the postgres docker container 
for working with the postgres docker container:
step 1: docker pull the local image from the dockerhub website, command is: docker pull postgres
step 2: create a volume for data persistance: docker volume create pg-data
step 3: run the postgres image along with the volume: docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5431:5432 -v pg-data:/var/lib/postgresql/data -d postgres
step 4: in the .env file the set the DB_HOST as DB_HOST = "192.168.1.4" which will be the local ip address of your machine, if you set it to localhost it will point to the port inside the container which we don not want.
step 5: now just enter the command: dokcer compose up to run the python script inside a container.

and check in the postgres container to verify, you can do that using either psql inside the postgres container or you can just register the new connection in the pgadmin of you local machine, if you have that downloaded!
