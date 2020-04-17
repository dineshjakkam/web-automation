class RiaRate:

    def __init__(self, tab):
        self.tab = tab
        self.tab.get("https://www.riamoneytransfer.com/us/en/send-money-to-india")

    def get_rate(self):
        retries = 1000
        while True and retries:
            try:
                elem = self.tab.find_elements_by_css_selector(".sc-giOsra.bxRkOK")[0]
                if len(elem.text[15:]) == 10:
                    raise ValueError
                else:
                    return float(elem.text[26:30])
            except (IndexError, ValueError):
                retries -= 1
                pass
