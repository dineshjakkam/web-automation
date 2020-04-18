from common import Browser, WALogger
from remittance import AllRates

logger = WALogger.get_logger()


def main():
    """
    TO run this file sourcing root as src
    sudo PYTHONPATH=. ~/.pyenv/versions/3.7.0/envs/myproject/bin/python3.7 remittance/main.py
    :return:
    """
    tab = Browser.open_new_tab(incognito=True, headless=True)
    all_rates = AllRates()
    all_rates.fetch_all_rates(tab)
    status = all_rates.check_if_values_changes()
    if status:



if __name__ == '__main__':
    main()
