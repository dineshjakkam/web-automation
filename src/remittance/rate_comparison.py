from common import WALogger
from remittance.modules import (
    RemitlyRate,
    RiaRate,
    XoomRate,
    WesternUnionRate
)

logger = WALogger.get_logger()


class AllRates:
    """
    Fetch all rates and compare with previous rates
    """
    prev_remitly_rate = None
    prev_ria_rate = None
    prev_wu_rate = None
    prev_xoom_rate = None

    def __init__(self):
        self.remitly_rate = None
        self.ria_rate = None
        self.wu_rate = None
        self.xoom_rate = None

    def fetch_all_rates(self, tab):
        """
        Given the fetch rates form all sites
        :param tab: Selenium tab for web scraping
        :return:
        """
        self.remitly_rate = RemitlyRate(tab).get_rate()
        self.ria_rate = RiaRate(tab).get_rate()
        self.wu_rate = WesternUnionRate(tab).get_rate()
        self.xoom_rate = XoomRate(tab).get_rate()

    def check_if_values_changes(self):
        """
        Check if values changed from the previous cached values
        Update the cached values to previous values
        :return: True if changed False else
        """
        status = not (self.remitly_rate == AllRates.prev_remitly_rate and
                      self.ria_rate == AllRates.ria_rate and
                      self.xoom_rate == AllRates.xoom_rate and
                      self.wu_rate == AllRates.wu_rate)

        logger.debug("Status changed flag: {}".format(str(not status)))

        AllRates.prev_remitly_rate = self.remitly_rate
        AllRates.ria_rate = self.ria_rate
        AllRates.wu_rate = self.wu_rate
        AllRates.xoom_rate = self.xoom_rate

        return status
