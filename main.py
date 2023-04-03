from selenium import webdriver

chrome_driver_path = r"C:\Users\Manu\Desktop\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.udemy.com/?utm_source=adwords-brand&utm_medium=udemyads&utm_campaign=Brand-Udemy_la.EN_cc.ROW"
           "&utm_term=_._ag_80315195513_._ad_535757779892_._de_c_._dm__._pl__._ti_kwd-296956216253_._li_9076844_"
           "._pd__._&utm_term=_._pd__._kw_udemy_._&matchtype=b&gclid"
           "=EAIaIQobChMIxLek_u79_QIVdpBoCR1YKwBqEAAYASAAEgJ5v_D_BwE")

x = driver.find_element(by="css_selector", value="q")

driver.quit()
