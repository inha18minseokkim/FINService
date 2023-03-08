from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def test():
    return "RealEstateSubscription 정상 작동중"