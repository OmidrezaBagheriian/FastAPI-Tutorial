from fastapi import FastAPI

app = FastAPI()

@app.get("/weblogs/")
async def weblogs(number_page:int):
    return {"message": f'Weblog is page {number_page}'}

