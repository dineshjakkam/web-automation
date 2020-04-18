"""
Run this on interpreter to run this test
The test file run roots from src
sudo PYTHONPATH=. ~/.pyenv/versions/3.7.0/envs/myproject/bin/python3.7 remittance/modules/test_files/test_rates.py
"""

from common import Browser
from remittance.modules import RemitlyRate, RiaRate, XoomRate, WesternUnionRate

tab = Browser.open_new_tab(incognito=True, headless=True)

rate = RemitlyRate(tab).get_rate()
print("Remitly rate: {}".format(rate))

rate = RiaRate(tab).get_rate()
print("Ria rate: {}".format(rate))

rate = XoomRate(tab).get_rate()
print("Xoom rate: {}".format(rate))

rate = WesternUnionRate(tab).get_rate()
print("WU rate: {}".format(rate))

