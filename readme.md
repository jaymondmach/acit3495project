# ACIT3495 Project Documentation

## Overview

The ACIT3495 project is a web application designed to manage and analyze data efficiently. It leverages a microservices architecture, utilizing multiple databases and services to provide a robust and scalable solution.

## Architecture

The application is composed of several interconnected services, each responsible for specific functionalities:

- **Authentication Service (`auth`)**: Manages user authentication and authorization.
- **Data Entry Service (`enter_data`)**: Handles the input and validation of data entries.
- **Analytics Service (`analytics`)**: Performs data analysis and generates reports.
- **Results Service (`results`)**: Displays the outcomes of data analysis to users.

These services communicate with each other through defined APIs and are orchestrated using Docker Compose.

## Databases

The project employs two types of databases:

- **MySQL Database (`mysql_db`)**: Stores structured relational data.
- **MongoDB Database (`mongo_db`)**: Stores unstructured or semi-structured data in a flexible, JSON-like format.

Each service interacts with the appropriate database as required.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/jaymondmach/acit3495project.git
   cd acit3495project
   ```

2. **Build and Start Services**:

   Use Docker Compose to build and start all services:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images for each service and start the containers.

3. **Accessing the Application**:

   Once all services are running, the application can be accessed at `http://localhost:8000` (or the configured port).

## Directory Structure

The repository is organized as follows:

```
acit3495project/
├── analytics/
├── auth/
├── enter_data/
├── mongo_db/
├── mysql_db/
├── results/
└── docker-compose.yml
```

- **`analytics/`**: Contains the Analytics Service code.
- **`auth/`**: Contains the Authentication Service code.
- **`enter_data/`**: Contains the Data Entry Service code.
- **`mongo_db/`**: Configuration and data for MongoDB.
- **`mysql_db/`**: Configuration and data for MySQL.
- **`results/`**: Contains the Results Service code.
- **`docker-compose.yml`**: Defines the Docker services and their configurations.

## Technologies Used

- **Backend**: Python
- **Frontend**: JavaScript
- **Databases**: MySQL, MongoDB
- **Containerization**: Docker, Docker Compose
