from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    # 使用 Service 指定 WebDriver 路径
    service = Service('/Users/panen/Documents/GitRepo/AutomaticTest/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=service)
    
    # 访问百度首页
    driver.get("https://www.baidu.com/")
    
    # 找到搜索框并输入查询内容
    search_box = driver.find_element("id", "kw")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))  # 等待搜索结果加载
    )

    # 验证页面标题
    assert "Python" in driver.title, f"Expected 'Python' in title, but got {driver.title}"

    # 或者通过检查页面的搜索结果来验证
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert any("Python" in result.text for result in results), "No result contains the keyword 'Python'"

    driver.quit()
