from remittance import AmountRange, TransferType
from common import WALogger

logger = WALogger.get_logger()


class RemitlyRate:
    """
    Fetches remitly rate
    """
    _previous_rate = None

    def __init__(self, tab):
        logger.debug("Fetching remitly rate")
        self.tab = tab
        self.tab.get("https://www.remitly.com/us/en/india")

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
        Fetch remitly economy rate
        :return: float rate value
        """
        element = self.tab.find_elements_by_class_name('f1smo2ix')[2]
        rate = element.text[1:]
        if rate is None:
            raise
        self.economy_rate[AmountRange.v_0_to_499.value] = rate
        self.economy_rate[AmountRange.v_500_to_999.value] = rate
        self.economy_rate[AmountRange.v_1000_to_1999.value] = rate
        self.economy_rate[AmountRange.v_above_2000.value] = rate

    def fetch_express_rate(self):
        """
        Fetch remitly express rate
        :return:
        """
        element = self.tab.find_elements_by_class_name('f1smo2ix')[0]
        rate = element.text[1:]
        if not rate:
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
            RemitlyRate._previous_rate = self.return_value
            return self.return_value
        except Exception as e:
            RemitlyRate._previous_rate
            logger.error("Exception in remitly fetch: {}".format(e))

