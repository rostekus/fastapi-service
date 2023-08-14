# FastAPI Model Relevance Service

This repository contains a REST service implemented in Python using FastAPI that allows for training and querying a model for object relevance.

## Getting Started
1. Clone this repository: `git clone https://github.com/rostekus/fastapi-service/`
2. Install project dependencies: `pip install -r requirements.txt`
3. Install development dependencies: `pip install -r requirements_dev.txt` (for running tests)
4. Run the FastAPI application: `uvicorn app.main:app --host 0.0.0.0 --port 80`

#### Docker 
You can also use docker 
```bash
docker build -t fastapi-service .
```
and then run
```bash
docker run -p 80:80
```
Check whether service started correctly:
```bash
curl localhost:80/health
```

## Endpoints

**/model/train**: Train the model using the calculated representativeness values and saved model to Database. If there is training, endpoint will return info when training has started.

**/model/predict**: Query the trained model to predict the representativeness of new data

**/model**: Get all saved models id

**/health**: Check weather service works correctly

For more information run service and have a look on OpenAPI docs:
```bash
http://localhost/docs
```
![screencapture-localhost-docs-2023-08-14-18_57_09](https://github.com/rostekus/fastapi-service/assets/34031791/366066c2-79ed-4a43-8e8c-f90f40454b74)

## Project Structure - Three-Layer Architecture

This project follows a three-layer architecture, which separates the application into distinct layers for improved modularity and maintainability. The three layers are:

1. Presentation Layer (app/app/routers and app/app/schemas):
   This layer handles user interactions, input validation, and presentation logic. It consists of routers and schemas.
```
   ├── app
   │   ├── app
   │   │   ├── routers
   │   │   │   ├── __init__.py
   │   │   │   └── model.py
   │   │   ├── schemas
   │   │   │   ├── __init__.py
   │   │   │   └── model.py
```
   - Routers (app/app/routers): Contains the API route definitions that handle incoming requests. These routers validate input, interact with the services layer, and return appropriate responses.

   - Schemas (app/app/schemas): Defines the data models and validation schemas for incoming and outgoing data. These schemas ensure the data's integrity and provide a consistent structure for communication between layers.

2. Business Logic Layer (app/app/services and app/app/relevance):
   This layer contains the core business logic and orchestrates the application's functionality. It consists of services and specific business logic modules.
```
   ├── app
   │   ├── app
   │   │   ├── relevance
   │   │   │   ├── api.py
   │   │   │   ├── __init__.py
   │   │   │   └── model.py
   │   │   ├── services
   │   │   │   ├── base.py
   │   │   │   ├── __init__.py
   │   │   │   └── model.py
```
   - Services (app/app/services): Encapsulates the core business logic and interacts with data repositories and external services if needed. It abstracts away implementation details and provides a clean interface to the presentation layer.

   - Specific Business Logic Modules (app/app/relevance): Contains modules related to specific business logic, such as relevance calculations. These modules may include APIs, models, and other components necessary for the specific domain.

3. Data Access Layer (app/app/repository):
   This layer is responsible for handling data storage and retrieval. It abstracts the interaction with data sources, such as databases, APIs, or in-memory storage.
```
   ├── app
   │   ├── app
   │   │   ├── repository
   │   │   │   ├── api.py
   │   │   │   ├── __init__.py
   │   │   │   └── inmemorydb.py
```
   - Data Repositories (app/app/repository): Provides an interface to access and manipulate data sources. This layer ensures that the rest of the application can work with data without directly interacting with the storage mechanisms.

By following the three-layer architecture, this project achieves better separation of concerns, making it easier to maintain, extend, and test different components independently.
