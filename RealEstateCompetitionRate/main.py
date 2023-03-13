from fastapi import FastAPI
from loguru import logger
from apartment.api import apartmentRouter

app = FastAPI()
app.include_router(apartmentRouter)


@app.get("/")
async def test():
    return "RealEstateSubscription 정상 작동중"

