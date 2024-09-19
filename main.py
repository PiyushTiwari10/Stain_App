import uvicorn
import logging
from src.app import app

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Server is running!")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
