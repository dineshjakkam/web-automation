import time

from remittance import AmountRange, TransferType
from common import WALogger

logger = WALogger.get_logger()


class RiaRate:
    """
    Fetches Ria rate
    """
    _previous_rate = None

    def __init__(self, tab):
        """
        Instantiate Ria class object
        :param tab: Browser tab with selenium and chrome driver
        """
        logger.debug("Fetching ria rate")
        self.tab = tab
        self.tab.get("https://www.riamoneytransfer.com/us/en/send-money-to-india")
        self.raw_rate = None

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

    def fetch_raw_rate(self):
        """
        Fetch ria raw rate
        :return: return raw rate without fee
        """
        retries = 100
        while True and retries:
            time.sleep(0.1)
            try:
                elem = self.tab.find_elements_by_class_name('sc-fUdGnz.eVINwC')[0]
                if not elem:
                    elem.text[-9:-4]
                else:
                    self.raw_rate = float(elem.text[-9:-4])
                    break
            except (IndexError, ValueError):
                retries -= 1
                pass

    def fetch_economy_rate(self):
        """
        Fetch ria economy rate
        :return: float rate value
        """
        if self.raw_rate is None:
            self.fetch_raw_rate()

        rate = '{0:.{1}f}'.format((1000 * self.raw_rate) / 1001, 2)
        if rate is None:
            raise

        self.economy_rate[AmountRange.v_0_to_499.value] = rate
        self.economy_rate[AmountRange.v_500_to_999.value] = rate
        self.economy_rate[AmountRange.v_1000_to_1999.value] = rate
        self.economy_rate[AmountRange.v_above_2000.value] = rate

    def fetch_express_rate(self):
        """
        Fetch ria express rate
        :return:
        """
        if self.raw_rate is None:
            self.fetch_raw_rate()

        rate = '{0:.{1}f}'.format((1000 * self.raw_rate) / 1001, 2)
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
            RiaRate._previous_rate = self.return_value
            return self.return_value
        except Exception as e:
            return RiaRate._previous_rate
            logger.error("Exception in ria fetch: {}".format(e))

