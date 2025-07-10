from fastapi import FastAPI
from app.routers import hotcommands, spaces

app = FastAPI()
app.include_router(hotcommands.router)
app.include_router(spaces.router)
