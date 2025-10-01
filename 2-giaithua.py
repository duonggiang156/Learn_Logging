"""
    Mục tiêu: luyện tập format log với thời gian, mức log.

👉 Yêu cầu:

Viết chương trình tính giai thừa (factorial).

Cấu hình format="%(asctime)s - %(levelname)s - %(message)s".

Log lại từng bước tính giai thừa (DEBUG).

In log INFO khi có kết quả cuối.

👉 Kỳ vọng: log ra vừa có timestamp, vừa có mức log.
    
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    #datefmt="%Y-%m-%d  %H:%M:%S",
)

def factorial(n):
    logging.info(f"Tính giai thừa của {n}")
    result = 1
    for i in range(1,n+1):
        logging.debug(f"Nhân với {i}, hiện tại total = {result}")
        result *= i
    logging.info(f"Hoàn thành. Kết quả giai thừa của {n} là {result}")
    return result

factorial(5)



""" 
👉 Kết quả
2025-10-01  14:41:35 - INFO - Tính giai thừa của 5
2025-10-01  14:41:35 - DEBUG - Nhân với 1, hiện tại total = 1
2025-10-01  14:41:35 - DEBUG - Nhân với 2, hiện tại total = 1
2025-10-01  14:41:35 - DEBUG - Nhân với 3, hiện tại total = 2
2025-10-01  14:41:35 - DEBUG - Nhân với 4, hiện tại total = 6
2025-10-01  14:41:35 - DEBUG - Nhân với 5, hiện tại total = 24
2025-10-01  14:41:35 - INFO - Hoàn thành. Kết quả giai thừa của 5 là 120
"""