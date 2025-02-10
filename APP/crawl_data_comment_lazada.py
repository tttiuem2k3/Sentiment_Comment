from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random
from datetime import datetime

# Thiết lập đường dẫn tới ChromeDriver
driver_path = r'D:\Code\Library\chromedriver-win64\chromedriver.exe'
chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

chrome_options = Options()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-dev-shm-usage")  # Giảm thiểu vấn đề liên quan đến bộ nhớ
chrome_options.add_argument("--no-sandbox")  # Tắt sandbox để tránh một số lỗi trong môi trường Linux
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.binary_location = chrome_binary_path
# chrome_options2 = Options()
# chrome_options2.add_argument("--disable-web-security")
# chrome_options2.add_argument("--disable-gpu")
# chrome_options2.add_argument("--disable-features=IsolateOrigins,site-per-process")
# chrome_options2.add_argument("--ignore-certificate-errors")
# chrome_options2.add_argument("--disable-dev-shm-usage")  # Giảm thiểu vấn đề liên quan đến bộ nhớ
# chrome_options2.add_argument("--no-sandbox")  # Tắt sandbox để tránh một số lỗi trong môi trường Linux
# chrome_options2.add_argument("--disable-software-rasterizer")
# chrome_options2.add_argument("--headless")  # Chạy Chrome mà không hiển thị giao diện
# chrome_options2.binary_location = chrome_binary_path

# Hàm thu thập bình luận từ HTML sử dụng Selenium
def extract_comments(driver, page,all_comments):
    time.sleep(1)
    try:
        reviews_section = driver.find_element(By.CLASS_NAME, "mod-reviews")
        comments = reviews_section.find_elements(By.CLASS_NAME, "item")
        for comment in comments:
            try:
                content = comment.find_element(By.CLASS_NAME, "content").text.strip()
                if not content:
                    continue
                print(f"Trang {page} - bình luận: {content}")
                all_comments.append(content)
            except Exception as e:
                print("Lỗi khi thu thập bình luận:", e)
                continue
    except Exception as e:
        print("Không tìm thấy phần bình luận:", e)

# Hàm thu thập bình luận từ HTML sử dụng Selenium
def extract_product_info(driver):
    product_info = {"title": None, "image_url": None}
    try:
        # Trích xuất tiêu đề
        title_element = driver.find_element(By.CLASS_NAME, "pdp-mod-product-badge-title")
        product_info["title"] = title_element.text.strip()

        # Trích xuất liên kết ảnh
        img_element = driver.find_element(By.CSS_SELECTOR, "img.pdp-mod-common-image.gallery-preview-panel__image")
        product_info["image_url"] = img_element.get_attribute("src")

    except Exception as e:
        print("Không thể thu thập thông tin sản phẩm:", e)
        product_info=None
    
    return product_info

# Hàm tìm nút next và cuộn xuống vị trí đó
def find_nextbutton(driver):
    # driver.execute_script("window.scrollBy(0, 300);")
    # time.sleep(0.2)
    # driver.execute_script("window.scrollBy(0, 400);")
    # time.sleep(0.2)
    # driver.execute_script("window.scrollBy(0, -100);")
    # time.sleep(0.2)
    # driver.execute_script("window.scrollBy(0, 300);")
    # time.sleep(0.2)
    # driver.execute_script("window.scrollBy(0, -100);")
    # time.sleep(0.2)
    # driver.execute_script("window.scrollBy(0, 400);")
    # time.sleep(0.2)
    # driver.execute_script("window.scrollBy(0, -100);")
    next_button = WebDriverWait(driver, 155).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/button[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    time.sleep(random.uniform(1, 2))  # Đợi một chút để đảm bảo phần tử đã vào đúng vị trí
    return next_button



def craw_list_comment(product_url):
    # Khởi tạo ChromeDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    page = 1
    all_comments = []
    try:
        # Mở trình duyệt và truy cập vào URL
        driver.get(product_url)
        # Danh sách lưu trữ bình luận
        next_button = find_nextbutton(driver)
        # Thu thập tiêu đề của sản phẩm
        product_info = extract_product_info(driver)
        # Thu thập bình luận trang đầu tiên
        extract_comments(driver,page,all_comments)
        
        driver.execute_script("arguments[0].click();", next_button)
        # Lặp qua các trang tiếp theo
        while page < 6:
            try:
                # Tìm nút "Next" và chuyển trang
                next_button = find_nextbutton(driver)
                
                # Đợi trang mới tải xong
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]'))
                )

                # Thu thập bình luận trang hiện tại
                extract_comments(driver,page,all_comments)
                
                driver.execute_script("arguments[0].click();", next_button)
                page += 1
                print(f"Đã chuyển sang trang {page}")
            except Exception as e:
                print(f"Bạn đang dừng lại ở trang {page}: hết trang hoặc gặp lỗi:", e)
                break

    except Exception as e:
        print("Lỗi ở tải bình luận", e)
        product_info=None
        all_comments=None
        driver.quit()
        return product_info,all_comments
    finally:
        # Đóng trình duyệt
        driver.quit()
    return product_info,all_comments
