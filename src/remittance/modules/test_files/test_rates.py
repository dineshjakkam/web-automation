from common import Browser
from remittance.modules import RemitlyRate

tab = Browser.open_new_tab(incognito=True, headless=True)
rate = RemitlyRate(tab).get_rate()
print("Remitly rate: {}".format(rate))

