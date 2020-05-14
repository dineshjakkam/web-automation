from common import WALogger

logger = WALogger.get_logger()

logger.debug("Testing non persisted logs")
logger.error("testing persisted logs")
