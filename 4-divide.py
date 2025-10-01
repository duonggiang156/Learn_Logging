""" 
Mục tiêu: log lỗi và traceback.

👉 Yêu cầu:

Viết hàm chia divide(a, b).

Nếu chia cho 0, thay vì print("Error"), hãy logger.error(..., exc_info=True).

Gọi thử divide(10,0) và xem log ra sao.

👉 Kỳ vọng: log sẽ ghi cả traceback (giúp debug nhanh).
"""
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d  %H:%M:%S",
    )

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Không thể chia cho 0", exc_info=True)
        return None
    
print(divide(10,0))