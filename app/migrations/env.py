import os
from logging import config

import dotenv
from alembic import context
import sqlalchemy

from app.models import Base

conf = context.config
dotenv.load_dotenv()

postgres_url = os.getenv("POSTGRES_URL", "postgres")
config.fileConfig(conf.config_file_name)
conf.set_main_option("sqlalchemy.url", postgres_url)
target_metadata = Base.metadata

def run_migrations_online():
    connectable = sqlalchemy.engine_from_config(
        conf.get_section(conf.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=sqlalchemy.pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()