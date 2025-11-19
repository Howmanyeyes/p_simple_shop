import os

import dotenv

from app.models import Base

dotenv.load_dotenv()
postgres_user = os.getenv("POSTGRES_USER", "postgres")
