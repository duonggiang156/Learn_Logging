import logging
import math

logger = logging.getLogger("math_utils")
logger.setLevel(logging.DEBUG)

def safe_sqrt(x):
    if x < 0:
        logger.warning(f"Giá trị âm: {x}, không thể tính căn bậc 2 thực.")
        return None
    logger.info(f"Tính căn bậc 2 của {x}")
    return math.sqrt(x)