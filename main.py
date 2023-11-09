import uvicorn
from views.files import files_router
from fastapi import FastAPI, APIRouter

app = FastAPI()
api_router = APIRouter()

api_router.include_router(files_router, prefix="", tags=["Files"])
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8888)
