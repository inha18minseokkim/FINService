from fastapi import FastAPI
from api import apartmentRouter
app = FastAPI()
app.include_router(apartmentRouter)

@app.get("/")
async def test():
    return "RealEstateSubscription 정상 작동중"