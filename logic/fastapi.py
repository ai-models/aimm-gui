from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#
# class api_server:
#     @staticmethod
#     def get_models():
#
#         return data
