import os
from dotenv import load_dotenv

load_dotenv()  # won't work without this for some reason

MXBAI_API_KEY = os.getenv("MXBAI_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
