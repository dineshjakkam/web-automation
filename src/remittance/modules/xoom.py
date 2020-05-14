from remittance import AmountRange, TransferType
from common import WALogger

logger = WALogger.get_logger()


class XoomRate:
    """
    Fetches xoom rate
    """
    _previous_rate = None

    def __init__(self, tab):
        """
        Instantiate xoom class object
        :param tab: Browser tab with selenium and chrome driver
        """
        logger.debug("Fetching xoom rate")
        self.tab = tab

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

    def fetch_high_amount_rate(self):
        """
        Fetch xoom economy rate
        :return: float rate value
        """
        self.tab.get("https://www.xoom.com/india/send-money")
        element = self.tab.find_element_by_class_name('js-exchange-rate')
        rate = element.text[8:14]
        if rate is None:
            raise
        self.express_rate[AmountRange.v_1000_to_1999.value] = rate
        self.express_rate[AmountRange.v_above_2000.value] = rate
        self.economy_rate[AmountRange.v_1000_to_1999.value] = rate
        self.economy_rate[AmountRange.v_above_2000.value] = rate

    def fetch_low_amount_rate(self):
        """
        Fetch xoom express rate
        :return:
        """
        self.tab.get("https://www.remitly.com/us/en/india")
        element = self.tab.find_elements_by_class_name('fa2he18')[0]
        rate = element.text[1:]
        if rate is None:
            raise
        self.express_rate[AmountRange.v_0_to_499.value] = rate
        self.express_rate[AmountRange.v_500_to_999.value] = rate
        self.economy_rate[AmountRange.v_0_to_499.value] = rate
        self.economy_rate[AmountRange.v_500_to_999.value] = rate

    def get_rate(self):
        """
        Fetch rate and makes dictionary with amount range and transfer type
        :return: Dictionary of rate values
        """
        try:
            self.fetch_high_amount_rate()
            self.fetch_low_amount_rate()
            XoomRate._previous_rate = self.return_value
            return self.return_value
        except Exception as e:
            return XoomRate._previous_rate
            logger.error("Exception in xoom fetch: {}".format(e))
