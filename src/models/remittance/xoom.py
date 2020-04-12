class XoomRate:

    def __init__(self, tab):
        self.tab = tab
        self.tab.get("https://www.xoom.com/india/send-money")

    def get_rate(self):
        elem = self.tab.find_element_by_class_name('js-exchange-rate')
        return float(elem.text[8:14])
