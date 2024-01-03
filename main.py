from fastapi_offline import FastAPIOffline
from config.config import motorcon
from models import models
from routes.routes import taller
from fastapi.responses import RedirectResponse
models.crearbd.metadata.create_all(bind=motorcon)

app = FastAPIOffline()
app.include_router(taller)

@app.get('/')
def index():
    return RedirectResponse('/docs')
