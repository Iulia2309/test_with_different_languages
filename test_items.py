#import time

def test_is_there_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
        
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "button is not exist"
           
