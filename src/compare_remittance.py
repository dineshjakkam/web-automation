from models.remittance import RemitlyRate, XoomRate, WesternUnionRate, RiaRate
from models import Browser, GoogleSearch

browser = Browser()
tab = browser.open_new_tab(incognito=True, headless=True)
try:
    rate = RemitlyRate(tab)
    print("{} -> {}".format("Remitly", rate.get_rate()))

    rate = XoomRate(tab)
    print("{} -> {}".format("Xoom", rate.get_rate()))

    rate = RiaRate(tab)
    print("{} -> {}".format("Ria", rate.get_rate()))

    rate = WesternUnionRate(tab)
    print("{} -> {}".format("WesternUnion", rate.get_rate()))

    GoogleSearch(tab).search("USD to INR")
    element = tab.find_element_by_css_selector(".dDoNo.vk_bk.gsrt")
    print("{} -> {}".format("Current exchange rate", float(element.text[:5])))
except KeyboardInterrupt:
    pass
finally:
    browser.close_all_tabs()
