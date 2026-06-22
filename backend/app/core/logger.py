import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO
)

logger = logging.getLogger(__name__)