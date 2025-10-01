""" 
Mục tiêu: ghi log ra file thay vì chỉ màn hình.

👉 Yêu cầu:

Viết chương trình đọc một danh sách số từ file numbers.txt.

Nếu file không tồn tại → log ERROR.

Nếu đọc thành công → log INFO số lượng phần tử đọc được.

Lưu toàn bộ log ra file app.log.

👉 Kiểm tra: mở app.log để thấy log được ghi.

"""
import logging
import os

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d  %H:%M:%S",
)


def read_numbers(file_path):
    if not os.path.exists(file_path):
        logging.error(f"Không tồn tại {file_path}")
        return []
    
    with open(file_path, "r") as f:
        numbers = [int(line.strip()) for line in f if line.strip()]
    logging.info(f"Co {len(numbers)} so o trong file {file_path}")
    return numbers


num = read_numbers("number.txt")




