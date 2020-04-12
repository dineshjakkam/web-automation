import time


class WesternUnionRate:

    def __init__(self, tab):
        self.tab = tab
        self.tab.get("https://www.compareremit.com/money-transfer-companies/western-union/")

    def get_rate(self):
        elements = self.tab.find_element_by_css_selector(".col-sm-4.exchange-rate-1.none_border")
        for element in elements:
            if "IND" in element.text:
                return float(element.text[10:15])


