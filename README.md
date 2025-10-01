### 1. OVERVIEW
Mục đích: giúp bạn hiểu "bên trong code" đang xảy ra gì khi chạy thực tế.

Nguyên tắc (đang xếp theo level):
+ DEBUG: thông tin cực chi tiết (data, input, intermediate results).
+ INFO: tiến trình chính (start/finish của một bước quan trọng).
+ WARNING: có gì bất thường nhưng chưa hỏng.
+ ERROR: có lỗi, nhưng chương trình còn sống.
+ CRITICAL: chương trình sập.

### 2. Cách dùng loogging cơ bản
```
import logging

# Cấu hình cơ bản
logging.basicConfig(level=logging.INFO)

logging.debug("Đây là log DEBUG")   # chi tiết nhỏ, thường ẩn đi
logging.info("Chương trình bắt đầu")  # thông tin chính
logging.warning("Cẩn thận! Sắp có vấn đề")
logging.error("Có lỗi xảy ra rồi")
logging.critical("Lỗi cực nghiêm trọng, chương trình sập")
```

👉 Output mặc định (với level=INFO):
```
INFO:root:Chương trình bắt đầu
WARNING:root:Cẩn thận! Sắp có vấn đề
ERROR:root:Có lỗi xảy ra rồi
CRITICAL:root:Lỗi cực nghiêm trọng, chương trình sập
```

(DEBUG không hiện vì level=INFO bỏ qua DEBUG).

### 3. Tùy chỉnh format log
```
import logging

logging.basicConfig(
    level=logging.DEBUG,   # Cho hiện tất cả log
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Chạy tới đây rồi")
logging.debug("Xem biến x=42")
```
👉 Output:
```
2025-10-01 12:30:15 - INFO - Chạy tới đây rồi
2025-10-01 12:30:15 - DEBUG - Xem biến x=42
```

### 4. Ghi log ra file
```
import logging

logging.basicConfig(
    filename="app.log",    # ghi ra file app.log
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Ứng dụng bắt đầu chạy")
logging.error("Không kết nối được database")
```

👉 Sau khi chạy, mở app.log sẽ thấy log được lưu lại.

### 5. Tạo logger riêng cho module
Thay vì dùng logging.info(...) trực tiếp, bạn nên tạo logger riêng:
```
import logging

logger = logging.getLogger(__name__)  # tên logger = tên file python

logger.setLevel(logging.DEBUG)

logger.info("Logger riêng hoạt động")
logger.debug("Chi tiết debug ở đây")

```
👉 Dùng logger riêng giúp bạn:
Phân biệt log của từng file/module.
Tắt/bật log cho từng phần code khi dự án lớn.

### 6. Một số cách dùng thông dụng
## a, Log trong hàm
```
def divide(a, b):
    logger = logging.getLogger(__name__)
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Không thể chia cho 0", exc_info=True)  # log cả traceback
```
## b, Log cảnh báo
```
if not data:
    logger.warning("Dữ liệu trống!")
```
## c, Log debug biến
```
x = 10
logger.debug(f"Giá trị x = {x}")
```