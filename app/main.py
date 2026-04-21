from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.ask import router as ask_router

app = FastAPI()

app.include_router(upload_router)
app.include_router(ask_router)

@app.get("/")
def root():
    return {"message": "RAG API is running"}


# main entry point for the application. It sets up the FastAPI app and includes the routes for uploading files and asking questions.