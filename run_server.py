import uvicorn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

uvicorn.run(
    "app:app",
    host="0.0.0.0",
    port=8000,
    reload=False
)
