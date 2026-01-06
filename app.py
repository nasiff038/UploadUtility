from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from pathlib import Path
import shutil

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <head>
            <style>
                body {
                    font-family: 'Courier New', Courier, monospace;
                }
                h3, text, input, button {
                    font-family: inherit; /* Inherit monospace from body */
                }
            </style>
        </head>

        <body>
            <h3>Upload your zip</h3>
            <text>Please use your ID as the name, e.g.: 2102XXX.zip</text>
            <br></br>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <button type="submit">Upload</button>
            </form>
        </body>
    </html>
    """


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    dest = UPLOAD_DIR / file.filename
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"STATUS": "UPLOAD SUCCESSFUL", "FILENAME": file.filename}
