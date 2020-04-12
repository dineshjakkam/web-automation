import time


class WesternUnionRate:

    def __init__(self, tab):
        self.tab = tab
        self.tab.get("https://www.compareremit.com/money-transfer-companies/western-union/")

    def get_rate(self):
        elements = self.tab.find_elements_by_class_name("col-sm-4.exchange-rate-1.none_border")
        for element in elements:
            if "IND" in element.text:
                return float(element.text[10:15])


