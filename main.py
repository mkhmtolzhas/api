from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pages.router import router

app = FastAPI()
app.mount("/static", StaticFiles(directory="/fastapi_app/static"), name="static")


app.include_router(router)
