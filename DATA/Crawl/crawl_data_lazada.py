# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import time
# import random
# from datetime import datetime

# # Thiết lập đường dẫn tới ChromeDriver
# driver_path = r'D:\Code\PBL6_DuAnChuyenNganh\chromedriver-win64\chromedriver.exe' 
# chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# chrome_options = Options()
# chrome_options.add_argument("--disable-web-security")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--disable-dev-shm-usage")  # Giảm thiểu vấn đề liên quan đến bộ nhớ
# chrome_options.add_argument("--no-sandbox")  # Tắt sandbox để tránh một số lỗi trong môi trường Linux
# chrome_options.add_argument("--disable-software-rasterizer") 
# chrome_options.add_argument("--headless")
# # chrome_options.add_argument("--headless")  # Chạy Chrome mà không hiển thị giao diện

# chrome_options.binary_location = chrome_binary_path
# # Khởi tạo ChromeDriver
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service, options=chrome_options)


# # Hàm thu thập bình luận từ HTML sử dụng BeautifulSoup
# def extract_comments(soup):
#     mod_reviews=soup.find("div", class_="mod-reviews")
#     comments = mod_reviews.find_all("div", class_="item")
#     for comment in comments:
#         try:
#             item_content=comment.find("div", class_="item-content")
#             content = item_content.find("div", class_="content").get_text(strip=True)
#             print(f"Trang {page} - bình luận : ",content)
#             all_comments.append(content)
#         except AttributeError:
#             continue
        
# # Hàm tìm nút next và cuộn xuống vị trí đó  
# def find_nextbutton(driver):
#     driver.execute_script("window.scrollBy(0, 500);")
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, 400);")
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, -200);")
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, -100);")
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, 300);")
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, -200);")
#     time.sleep(0.5)
#     driver.execute_script("window.scrollBy(0, 200);")
#     next_button = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/button[2]'))
#     )
#     # Cuộn trang đến vị trí của nút "Next"
#     driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
#     time.sleep(random.uniform(4, 6))  # Đợi một chút để đảm bảo phần tử đã vào đúng vị trí
#     return next_button

# # URL sản phẩm Lazada
# product_url = "https://www.lazada.vn/products/mat-na-ngu-duong-moi-cang-mong-tay-te-bao-chet-laneige-lip-sleeping-mask-berry-20g-huong-qua-mong-i260515234-s365256627.html?scm=1007.17760.398138.0&pvid=ea1516c2-8611-4699-b778-0222d3ae4081&search=flashsale&spm=a2o4n.homepage.FlashSale.d_260515234&pdpBucketId=3"  # Thay bằng URL sản phẩm cụ thể

# page=1
# try:
#     # Mở trình duyệt và truy cập vào URL
#     driver.get(product_url)
    
    
#     # driver.get(product_url)
    
    
#     # #Tìm nút xem thêm bằng XPath mà bạn đã cung cấp
#     # xem_them = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_detail"]/div/div/div[2]/button'))
#     # )

#     # # Cuộn trang đến vị trí của nút xem thêm
#     # driver.execute_script("arguments[0].scrollIntoView(true);", xem_them)
#     # time.sleep(random.uniform(4, 7))  # Đợi một chút để đảm bảo phần tử đã vào đúng vị trí

#     # # Sử dụng JavaScript để click vào nút xem thêm
#     # driver.execute_script("arguments[0].click();", xem_them)
    
#     # Cuộn trang đến vị trí của nút "Next"
    
#      # Đợi một chút để đảm bảo phần tử đã vào đúng vị trí
#     # Chờ tải mục bình luận
    
#     # Tìm nút "Next" bằng XPath mà bạn đã cung cấp
#     next_button = find_nextbutton(driver)
    
#     # Tìm kiếm phần có các comment
#     WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]'))
#     )
    
#     all_comments = []  # Danh sách lưu trữ bình luận
    
#     # Lấy HTML trang đầu tiên
#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, "html.parser")
    
#     # Thu thập bình luận trang đầu tiên
#     extract_comments(soup)
    
#     # chuyển trang tiếp theo
#     driver.execute_script("arguments[0].click();", next_button)
    
#     # Lặp qua các trang tiếp theo
#     while page < 10:
#         current_url = driver.current_url
#         driver.get(current_url)
#         page+=1
#         print(f"Đã chuyển sang trang {page}")
#         try:
#             # Tìm nút "Next" bằng XPath mà bạn đã cung cấp
#             next_button = find_nextbutton(driver)
        
#             # Tìm kiếm phần có các comment
#             WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]'))
#             )
            
#             # Lấy HTML trang hiện tại
#             page_source = driver.page_source
#             soup = BeautifulSoup(page_source, "html.parser")
            
#             # Thu thập bình luận
#             extract_comments(soup)
            
#             # chuyển trang tiếp theo
#             driver.execute_script("arguments[0].click();", next_button)
            
#         except Exception as e:
#             page-=1
#             print(f"Bạn đang dừng lại ở trang {page}: hết trang hoặc gặp lỗi:", e)
#             break
    
#     # # Xử lý dữ liệu
#     # df = pd.DataFrame({"Comment": all_comments})
    
#     # # Lưu dữ liệu vào file CSV
#     # file_name = f"lazada_comments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
#     # df.to_csv(file_name, encoding="utf-8-sig", index=False)
#     # print(f"Dữ liệu đã được lưu vào file {file_name}")
# except Exception as e:
#     print("Lỗi ở trang 1 - tải lại: ",e)
#     driver.get(product_url)
# finally: 
# # Đóng trình duyệt
#     driver.quit()


#----------------------------------------------------------------------------------------------
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
chrome_options.add_argument("--disable-dev-shm-usage")  # Giảm thiểu vấn đề liên quan đến bộ nhớ
chrome_options.add_argument("--no-sandbox")  # Tắt sandbox để tránh một số lỗi trong môi trường Linux
chrome_options.add_argument("--disable-software-rasterizer")
# chrome_options.add_argument("--headless")  # Chạy Chrome mà không hiển thị giao diện
chrome_options.binary_location = chrome_binary_path

# Khởi tạo ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


# Hàm thu thập bình luận từ HTML sử dụng Selenium
def extract_comments(driver):
    time.sleep(2)
    try:
        reviews_section = driver.find_element(By.CLASS_NAME, "mod-reviews")
        comments = reviews_section.find_elements(By.CLASS_NAME, "item")
        for comment in comments:
            try:
                content = comment.find_element(By.CLASS_NAME, "content").text.strip()
                print(f"Trang {page} - bình luận: {content}")
                all_comments.append(content)
            except Exception as e:
                print("Lỗi khi thu thập bình luận:", e)
                continue
    except Exception as e:
        print("Không tìm thấy phần bình luận:", e)


# Hàm tìm nút next và cuộn xuống vị trí đó
def find_nextbutton(driver):
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, -100);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, -100);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, -100);")
    next_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/button[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    time.sleep(random.uniform(4, 6))  # Đợi một chút để đảm bảo phần tử đã vào đúng vị trí
    return next_button


# URL sản phẩm Lazada
product_url = "https://www.lazada.vn/products/mat-na-ngu-duong-moi-cang-mong-tay-te-bao-chet-laneige-lip-sleeping-mask-berry-20g-huong-qua-mong-i260515234-s365256627.html?scm=1007.17760.398138.0&pvid=ea1516c2-8611-4699-b778-0222d3ae4081&search=flashsale&spm=a2o4n.homepage.FlashSale.d_260515234&pdpBucketId=3"  # Thay bằng URL sản phẩm cụ thể

page = 1
try:
    # Mở trình duyệt và truy cập vào URL
    driver.get(product_url)

    all_comments = []  # Danh sách lưu trữ bình luận
    next_button = find_nextbutton(driver)
    # Thu thập bình luận trang đầu tiên
    extract_comments(driver)
    
    driver.execute_script("arguments[0].click();", next_button)
    # Lặp qua các trang tiếp theo
    while page < 10:
        try:
            # Tìm nút "Next" và chuyển trang
            next_button = find_nextbutton(driver)
            

            # Đợi trang mới tải xong
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]'))
            )

            # Thu thập bình luận trang hiện tại
            extract_comments(driver)
            
            driver.execute_script("arguments[0].click();", next_button)
            page += 1
            print(f"Đã chuyển sang trang {page}")
        except Exception as e:
            print(f"Bạn đang dừng lại ở trang {page}: hết trang hoặc gặp lỗi:", e)
            break

    # Xử lý dữ liệu
    df = pd.DataFrame({"Comment": all_comments})

    # Lưu dữ liệu vào file CSV
    file_name = f"lazada_comments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(file_name, encoding="utf-8-sig", index=False)
    print(f"Dữ liệu đã được lưu vào file {file_name}")
except Exception as e:
    print("Lỗi ở trang 1 - tải lại:", e)
    driver.get(product_url)
finally:
    # Đóng trình duyệt
    driver.quit()
