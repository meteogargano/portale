from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")
app.mount("/lib", StaticFiles(directory="node_modules"), name="node_modules")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(
        request=request, name="homepage.html",
        context={"current_year": "2023"}
    )
