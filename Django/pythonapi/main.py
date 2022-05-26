# To start the app use the command:
#   uvicorn <name of your main file>:<name of your FastAPI instance>
# Imported the library
from xmlrpc.client import FastMarshaller
from fastapi import FastAPI

# Created an instance of the FastAPI
app = FastAPI()

# Created the route(Path operations)


@app.get("/")  # Decorator(References the path when going through the url)
def root():  # Root function
    return {"message": "Hello World"}  # Returning the data
