import uvicorn
from fastapi import FastAPI

class ApiHandler:
    @staticmethod
    def start_api():
        print('a')
        app_api = FastAPI()
        @app_api.get("/")
        async def root():
            return {"message": "Hello World"}
        print(__name__)
        if __name__ == "logic.api":
            print('naop')
            uvicorn.run("api:app_api",host='127.0.0.1', port=4557, reload=True, workers=3)
