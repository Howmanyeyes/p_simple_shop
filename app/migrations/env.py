import os

import dotenv

from app.models import Base

dotenv.load_dotenv()
name = os.getenv("POSTGRES_USER", "KYS")

