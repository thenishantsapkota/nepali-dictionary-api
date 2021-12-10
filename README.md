
# Nepali Dictionary API

A Nepali dictionary api created using Fast API and inspired from https://github.com/nirooj56/Nepdict.
You can say this is just the API version of that project.



## Documentation

### Setting up the project locally.


#### Prequisities

- `make` makes the process automated. Make sure, `make` is installed.
- `docker-compose` and `docker` are used to bake the images and run in isolation. This also helps you from not requiring psql, pgadmin installed in your machine.

#### Steps

1. Clone the repository.
2. Make sure to override `.env` file to add your own variables.
    ```shell
      cp .env.local .env
      $EDITOR .env
    ```

2. Run the project using the following command.
    ```shell
    make dev
    ```

3. If you're running for the first time, you may want to run migrations with the command.
    ```shell
      make migrate
    ```

4. If you want to seed the database using the currently provided data, run the following command.
    ```shell
      make seed-db
    ```

5. The development service will be live: http://localhost:8000

6. PGAdmin will be available on: http://localhost:5000
    ```
