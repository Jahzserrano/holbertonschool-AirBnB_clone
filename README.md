# Airbnb Clone

## Command-Line Interface

The `console.py` script provides a command-line interface with the following commands:

- `create`: Create a new instance of a specified class.
- `show`: Display the string representation of an instance.
- `destroy`: Delete an instance.
- `all`: Display the string representation of all instances of a class.
- `update`: Update an instance's attribute.

Supported classes include:
- `BaseModel`
- `User`
- `State`
- `City`
- `Amenity`
- `Place`
- `Review`

## Models

### BaseModel

The base model class with common attributes:

- `id`: Unique identifier (UUID).
- `created_at`: Creation timestamp.
- `updated_at`: Last update timestamp.

### User

Public class attributes:

- `email`: Empty string.
- `password`: Empty string.
- `first_name`: Empty string.
- `last_name`: Empty string.

### State

Public class attributes:

- `name`: Empty string.

### City

Public class attributes:

- `state_id`: Empty string.
- `name`: Empty string.

### Amenity

Public class attributes:

- `name`: Empty string.

### Place

Public class attributes:

- `city_id`: Empty string.
- `user_id`: Empty string.
- `name`: Empty string.
- `description`: Empty string.
- `number_rooms`: Integer (default: 0).
- `number_bathrooms`: Integer (default: 0).
- `max_guest`: Integer (default: 0).
- `price_by_night`: Integer (default: 0).
- `latitude`: Float (default: 0.0).
- `longitude`: Float (default: 0.0).
- `amenity_ids`: List of strings (default: []).

### Review

Public class attributes:

- `place_id`: Empty string.
- `user_id`: Empty string.
- `text`: Empty string.

## File Storage

The project includes a file storage system using the `FileStorage` class.


## Usage
Run the console application:

./console.py

Contributing
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Authors
Leomar Rodriguez Gonzalez <leomar.rodriguez1@upr.edu>
Jahaziel A Serrano <serranojahaziel2@gmail.com>
