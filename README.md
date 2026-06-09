# Event Registration System

## Description
A Django REST Framework API for managing event registrations.

## Features
- Create events
- View all events
- Store event details in SQLite database
- REST API using Django REST Framework

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite

## API Endpoint

GET /events/
Returns all events.

POST /events/
Creates a new event.

Example JSON:

{
    "name": "CodeAlpha Workshop",
    "description": "Python Django REST API Workshop",
    "date": "2026-06-15",
    "location": "Kolkata"
}