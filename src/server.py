from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from src.routes import api
from src.services.rag_service import initialize_chain

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--- Server starting up ---")
    initialize_chain()
    yield
    print("--- Server shutting down ---")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Docu-Mentor API is running!"}