import logging

import inngest

logger = logging.getLogger(__name__)

# Create an Inngest client
inngest_client = inngest.Inngest(
    app_id="edemy",
    logger=logger,
)
