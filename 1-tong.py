"""
Mục tiêu: làm quen với logging.basicConfig, phân biệt INFO và DEBUG.

👉 Yêu cầu:

Viết chương trình tính tổng từ 1 → N.

Dùng logger.info để thông báo khi bắt đầu và kết thúc chương trình.

Dùng logger.debug để log giá trị biến trong vòng lặp.

Chạy với level=logging.INFO và quan sát, sau đó đổi sang DEBUG xem khác biệt.

""" 
# ======================================================================#
import logging

# Cấu hình log
logging.basicConfig(
    level=logging.DEBUG
)


def sum_n(n):
    logging.info(f"Bắt đầu tính tổng từ 1 đến {n}")
    total = 0
    for i in range(1,n+1):
        logging.debug(f"Đang cộng i = {i}")
        total += i
        logging.debug(f"Total = {total}")
    logging.info(f"Kết thúc. Kết quả: {total}")
    return total


sum_n(6)





""" 
👉 Kết quả
INFO:root:Bắt đầu tính tổng từ 1 đến 6
DEBUG:root:Đang cộng i = 1
DEBUG:root:Total = 1
DEBUG:root:Đang cộng i = 2
DEBUG:root:Total = 3
DEBUG:root:Đang cộng i = 3
DEBUG:root:Total = 6
DEBUG:root:Đang cộng i = 4
DEBUG:root:Total = 10
DEBUG:root:Đang cộng i = 5
DEBUG:root:Total = 15
DEBUG:root:Đang cộng i = 6
DEBUG:root:Total = 21
INFO:root:Kết thúc. Kết quả: 21

"""