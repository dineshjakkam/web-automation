from remittance import AmountRange, TransferType
from common import WALogger

logger = WALogger.get_logger()


class RemitlyRate:
    """
    Fetches remitly rate
    """

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
        self.economy_rate[AmountRange.v_0_to_499.value] = rate
        self.economy_rate[AmountRange.v_500_to_999.value] = rate
        self.economy_rate[AmountRange.v_1000_to_1999.value] = rate
        self.economy_rate[AmountRange.v_above_2000.value] = rate

    @staticmethod
    def _calculate_considering_fee(value, fee=3.99):
        """
        Return exact transfer rate by calculating fee
        :param value: Current exchange rate
        :param fee: remitly transfer fee
        :return: calculated exchange fee
        """
        return (999 * value) / (999 + fee)

    def fetch_express_rate(self):
        """
        Fetch remitly express rate
        :return:
        """
        element = self.tab.find_elements_by_class_name('f1smo2ix')[0]
        raw_rate = float(element.text[1:])
        rate_with_fee = self.__class__._calculate_considering_fee(raw_rate)
        self.express_rate[AmountRange.v_0_to_499.value] = '{0:.{1}f}'.format(rate_with_fee, 2)
        self.express_rate[AmountRange.v_500_to_999.value] = '{0:.{1}f}'.format(rate_with_fee, 2)
        self.express_rate[AmountRange.v_1000_to_1999.value] = str(raw_rate)
        self.express_rate[AmountRange.v_above_2000.value] = str(raw_rate)

    def get_rate(self):
        """
        Fetch rate and makes dictionary with amount range and transfer type
        :return: Dictionary of rate values
        """
        try:
            self.fetch_economy_rate()
            self.fetch_express_rate()
            return self.return_value
        except Exception as e:
            logger.error("Exception in remitly fetch: {}".format(e))

