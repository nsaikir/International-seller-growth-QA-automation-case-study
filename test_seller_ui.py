from selenium import webdriver

def test_seller_registration_form():
    driver = webdriver.Chrome()
    driver.get("https://web.example.com/register")
    assert "Seller Registration" in driver.title
    driver.quit()
