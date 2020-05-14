from remittance import AmountRange, TransferType
from common import WALogger

logger = WALogger.get_logger()


class WesternUnionRate:
    """
    Fetches Western Union rate
    """
    _previous_rate = None

    def __init__(self, tab):
        """
        Instantiate WU class object
        :param tab: Browser tab with selenium and chrome driver
        """
        logger.debug("Fetching xoom rate")
        self.tab = tab
        self.tab.get("https://www.compareremit.com/money-transfer-companies/western-union/")

        self.express_rate = {
            AmountRange.v_0_to_499.value: None,
            AmountRange.v_500_to_999.value: None,
            AmountRange.v_1000_to_1999.value: None,
            AmountRange.v_above_2000.value: None
        }

        self.economy_rate = {
            AmountRange.v_0_to_499.value: None,
            AmountRange.v_500_to_999.value: None,
            AmountRange.v_1000_to_1999.value: None,
            AmountRange.v_above_2000.value: None
        }

        self.return_value = {TransferType.bank_account.value: self.economy_rate,
                             TransferType.debit_card.value: self.express_rate}

    def fetch_economy_rate(self):
        """
        Fetch WU economy rate
        :return: float rate value
        """
        elements = self.tab.find_elements_by_css_selector(".col-sm-4.exchange-rate-1.none_border")
        for element in elements:
            if "IND" in element.text and "USA" in element.text:
                rate = element.text[10:15]
        if rate is None:
            raise
        self.economy_rate[AmountRange.v_0_to_499.value] = rate
        self.economy_rate[AmountRange.v_500_to_999.value] = rate
        self.economy_rate[AmountRange.v_1000_to_1999.value] = rate
        self.economy_rate[AmountRange.v_above_2000.value] = rate

    def fetch_express_rate(self):
        """
        Fetch WU express rate
        :return:
        """
        elements = self.tab.find_elements_by_css_selector(".col-sm-4.exchange-rate-1.none_border")
        for element in elements:
            if "IND" in element.text and "USA" in element.text:
                rate = element.text[10:15]
        if rate is None:
            raise
        self.express_rate[AmountRange.v_0_to_499.value] = rate
        self.express_rate[AmountRange.v_500_to_999.value] = rate
        self.express_rate[AmountRange.v_1000_to_1999.value] = rate
        self.express_rate[AmountRange.v_above_2000.value] = rate

    def get_rate(self):
        """
        Fetch rate and makes dictionary with amount range and transfer type
        :return: Dictionary of rate values
        """
        try:
            self.fetch_economy_rate()
            self.fetch_express_rate()
            WesternUnionRate._previous_rate = self.return_value
            return self.return_value
        except Exception as e:
            return WesternUnionRate._previous_rate
            logger.error("Exception in WU fetch: {}".format(e))



