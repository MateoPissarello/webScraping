from fastapi import FastAPI
import uvicorn
from web_scraping_classcentral import get_data

app = FastAPI()


@app.get("/class_central")
async def class_central():
    data = get_data()
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
