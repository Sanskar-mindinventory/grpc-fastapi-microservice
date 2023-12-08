import uvicorn
from config.config import get_current_server_config as settings

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)

