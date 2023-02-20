FROM mysql:latest

# Set MySQL root password
ENV MYSQL_ROOT_PASSWORD rlaalstjr99!

# Create a directory on the host machine to store the MySQL data
RUN mkdir -p /var/lib/mysql

# Set the owner of the directory to the user that runs the MySQL process inside the container
RUN chown -R mysql:mysql /var/lib/mysql

# Copy initialization SQL script to container
COPY create_database.sql /docker-entrypoint-initdb.d/

# Mount the directory on the host machine to the container's /var/lib/mysql directory
VOLUME /var/lib/mysql



# Expose the container's port 3306 to the host machine's port 3306
EXPOSE 3306