# API Demo

A simple REST API built with Python + Flask to understand basic API concepts.

## Concepts Covered
- **GET** – Read data
- **POST** – Create data
- **PUT** – Update data
- **DELETE** – Remove data

## Setup & Run

```bash
pip install -r requirements.txt
python app.py
```

Server runs at: `http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint         | Description        |
|--------|------------------|--------------------|
| GET    | /items           | Get all items      |
| GET    | /items/<id>      | Get item by ID     |
| POST   | /items           | Create a new item  |
| PUT    | /items/<id>      | Update an item     |
| DELETE | /items/<id>      | Delete an item     |

## Example Requests

**GET all items**
```
GET http://127.0.0.1:5000/items
```

**POST - Create item**
```json
POST http://127.0.0.1:5000/items
Content-Type: application/json

{ "name": "Mango", "price": 2.0 }
```

**PUT - Update item**
```json
PUT http://127.0.0.1:5000/items/1
Content-Type: application/json

{ "price": 3.0 }
```

**DELETE - Remove item**
```
DELETE http://127.0.0.1:5000/items/1
```
