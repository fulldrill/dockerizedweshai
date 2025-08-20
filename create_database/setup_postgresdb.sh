#READ ME

##The script sets up PostgreSQL container running with a WESHAI DB.
##Creates superuser (role with full rights).
##Ability to connect with pgAdmin on your Mac.

#/Users/weshgawd/Documents/WESHDOCBUILD/create_database/docker-compose.yml

##Below script performs the creation of the PostgreSQL DB in docker container.
##It ensures the container is not already existing.

#/Users/weshgawd/Documents/WESHDOCBUILD/setup_postgresdb.sh

docker rm -f weshai_postgres 2>/dev/null
docker compose up -d

#Next step is to create admin user