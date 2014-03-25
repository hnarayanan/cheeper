# Restful endpoints for Cheeper

| Method   | Slug               | Description                           | Who's allowed           |
|----------|--------------------|---------------------------------------|-------------------------|
| `POST`   | `/auth-token/`     | Creates and returns auth. token       | Anyone                  |
| `DELETE` | `/auth-token/`     | Invalidates auth. token               | Valid token             |
|          |                    |                                       |                         |
| `GET`    | `/users/`          | Retrieves list of all users           | Anyone                  |
| `POST`   | `/users/`          | Creates new user                      | Anyone                  |
| `GET`    | `/users/:user-id/` | Retrieves details of a specific user  | Anyone                  |
| `PATCH`  | `/users/:user-id/` | Updates details of a specific user    | Valid token as :user-id |
| `DELETE` | `/users/:user-id/` | Deletes a specific user               | Valid token as :user-id |
