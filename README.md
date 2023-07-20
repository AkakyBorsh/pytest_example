# pytest
> docker build -t pytest_example .
docker run -d pytest_example sleep infinity

# allure server 
> docker run -p 8080:8080 kochetkovma/allure-server:latest

# postgres  
> docker run --name habr-pg-13.3 -p 5432:5432 -e POSTGRES_USER=habrpguser -e POSTGRES_PASSWORD=pgpwd4habr -e POSTGRES_DB=habrdb -d postgres:13.3

> docker run --name habr-pg-13.3 -p 5432:5432 -e POSTGRES_USER=habrpguser -e POSTGRES_PASSWORD=pgpwd4habr -e POSTGRES_DB=habrdb -d -v "/absolute/path/to/directory-with-init-scripts":/docker-entrypoint-initdb.d postgres:13.3

> docker run --name habr-pg-13.3 -p 5432:5432 -e POSTGRES_USER=habrpguser -e POSTGRES_PASSWORD=pgpwd4habr -e POSTGRES_DB=habrdb -d -v "/Users/ivahrusev/src/useful-sql-scripts/running_pg_in_docker/2. Init Database":/docker-entrypoint-initdb.d postgres:13.3

# postgres with data set 
> docker run -d --name pg-ds-dellstore -p 5432:5432 -e POSTGRES_USER=habrpguser -e POSTGRES_PASSWORD=pgpwd4habr aa8y/postgres-dataset:dellstore
