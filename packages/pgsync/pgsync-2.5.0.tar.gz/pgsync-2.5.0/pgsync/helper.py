"""PGSync helpers."""
import logging
import os
from typing import Optional

import sqlalchemy as sa

from .base import database_exists, drop_database
from .sync import Sync
from .utils import config_loader, get_config

logger = logging.getLogger(__name__)


def teardown(
    drop_db: bool = True,
    truncate_db: bool = True,
    delete_redis: bool = True,
    drop_index: bool = True,
    delete_checkpoint: bool = True,
    config: Optional[str] = None,
    validate: bool = False,
) -> None:
    """Teardown helper."""
    config: str = get_config(config)

    for document in config_loader(config):

        if not database_exists(document["database"]):
            logger.warning(f'Database {document["database"]} does not exist')
            continue

        sync: Sync = Sync(document, validate=validate)
        if truncate_db:
            try:
                sync.truncate_schemas()
                sync.engine.connect().close()
                sync.engine.dispose()
            except sa.exc.OperationalError as e:
                logger.warning(
                    f'Database "{sync.database}" does not exist: {e}'
                )
        if drop_db:
            drop_database(sync.database)
        if drop_index:
            sync.search_client.teardown(sync.index)
        if delete_redis:
            sync.redis.delete()
        if delete_checkpoint:
            try:
                os.unlink(sync._checkpoint_file)
            except (OSError, FileNotFoundError):
                pass
