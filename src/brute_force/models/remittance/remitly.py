class RemitlyRate:

    def __init__(self, tab):
        self.tab = tab
        self.tab.get("https://www.remitly.com/us/en/india")

    def get_rate(self):
        elem = self.tab.find_elements_by_class_name('f1smo2ix')[2]
        return float(elem.text[1:])
