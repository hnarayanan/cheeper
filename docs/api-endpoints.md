# Restful endpoints for Cheeper

| Method   | Slug                 | Description                           | Who's allowed                      |
|----------|----------------------|---------------------------------------|------------------------------------|
| `POST`   | `/auth-token/`       | Creates and returns an auth. token    | Valid login credentials            |
| `DELETE` | `/auth-token/`       | Invalidates request's auth. token     | Valid token                        |
| `GET`    | `/users/`            | Retrieves the list of all users       | Anyone                             |
| `POST`   | `/users/`            | Creates a new user                    | Anyone                             |
| `GET`    | `/users/:user-id/`   | Retrieves details of a specific user  | Anyone                             |
| `PATCH`  | `/users/:user-id/`   | Updates details of a specific user    | Valid token as :user-id            |
| `DELETE` | `/users/:user-id/`   | Deletes a specific user               | Valid token as :user-id            |
| `GET`    | `/cheeps/`           | Retrieves the list of all cheeps      | Anyone                             |
| `POST`   | `/cheeps/`           | Creates a new cheep                   | Valid token                        |
| `GET`    | `/cheeps/:cheep-id/` | Retrieves details of a specific cheep | Anyone                             |
| `PATCH`  | `/cheeps/:cheep-id/` | Updates details of a specific cheep   | Valid token as author of :cheep-id |
| `DELETE` | `/cheeps/:cheep-id/` | Deletes a specific cheep              | Valid token as author of :cheep-id |
