import time
from pytz import timezone
from threading import Thread
import pandas as pd
import datetime
import logging

from models.remittance import RemitlyRate, XoomRate, WesternUnionRate, RiaRate
from models import Browser, GoogleSearch
from models.database import S3Bucket

remitly_prev_value = 0
xoom_prev_value = 0
ria_prev_value = 0
wu_prev_value = 0

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(filename='log/remittance.log')
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def remitly_value():
    try:
        global remitly_df, remitly_prev_value
        rate = RemitlyRate(tab).get_rate()
        if not rate == remitly_prev_value:
            remitly_prev_value = rate
            new_value = {'datetime': datetime.datetime.now(), 'value': rate}
            remitly_df = remitly_df.append(new_value, ignore_index=True)
            bucket.save_to_s3(file_name="remitly/"+str(datetime.datetime.now()) + ".csv", src_data=remitly_df)
            remitly_df = pd.DataFrame(columns=['datetime', 'value'])
        logger.debug("{} -> {}".format("Remitly", rate))
    except Exception as e:
        logger.debug("remitly error: {}".format(e))


def xoom_value():
    try:
        global xoom_prev_value, xoom_df
        rate = XoomRate(tab).get_rate()
        if not rate == xoom_prev_value:
            xoom_prev_value = rate
            new_value = {'datetime': datetime.datetime.now(), 'value': rate}
            xoom_df = xoom_df.append(new_value, ignore_index=True)
            bucket.save_to_s3(file_name="xoom/"+str(datetime.datetime.now()) + ".csv", src_data=xoom_df)
            xoom_df = pd.DataFrame(columns=['datetime', 'value'])
        logger.debug("{} -> {}".format("Xoom", rate))
    except Exception as e:
        logger.debug("xoom error: {}".format(e))


def ria_value():
    try:
        global ria_prev_value, ria_df
        rate = RiaRate(tab).get_rate()
        if rate is not None and not rate == ria_prev_value:
            ria_prev_value = rate
            new_value = {'datetime': datetime.datetime.now(), 'value': rate}
            ria_df = ria_df.append(new_value, ignore_index=True)
            bucket.save_to_s3(file_name="ria/"+str(datetime.datetime.now()) + ".csv", src_data=ria_df)
            ria_df = pd.DataFrame(columns=['datetime', 'value'])
        logger.debug("{} -> {}".format("Ria", rate))
    except Exception as e:
        logger.debug("ria error: {}".format(e))


def wu_value():
    try:
        global wu_prev_value, wu_df
        rate = WesternUnionRate(tab).get_rate()
        if not rate == wu_prev_value:
            wu_prev_value = rate
            new_value = {'datetime': datetime.datetime.now(), 'value': rate}
            wu_df = wu_df.append(new_value, ignore_index=True)
            bucket.save_to_s3(file_name="western_union/"+str(datetime.datetime.now()) + ".csv", src_data=wu_df)
            wu_df = pd.DataFrame(columns=['datetime', 'value'])
        logger.debug("{} -> {}".format("WesternUnion", rate))
    except Exception as e:
        logger.debug("wu error: {}".format(e))


def google_value():
    try:
        global exchange_df
        GoogleSearch(tab).search("USD to INR")
        element = tab.find_element_by_css_selector(".dDoNo.vk_bk.gsrt")
        new_value = {'datetime': datetime.datetime.now(), 'value': float(element.text[:5])}
        exchange_df = exchange_df.append(new_value, ignore_index=True)
        if exchange_df.size > 30:
            bucket.save_to_s3(file_name="exchange/"+str(datetime.datetime.now()) + ".csv", src_data=exchange_df)
            exchange_df = pd.DataFrame(columns=['datetime', 'value'])
        logger.debug("{} -> {}".format("Current exchange rate", float(element.text[:5])))
    except Exception as e:
        logger.debug("google error: {}".format(e))


def main():
    while True:
        threads = []
        try:
            remitly_thread = Thread(target=remitly_value)
            threads.append(remitly_thread)
            remitly_thread.daemon = True

            xoom_thread = Thread(target=xoom_value)
            threads.append(xoom_thread)
            xoom_thread.daemon = True

            ria_thread = Thread(target=ria_value)
            threads.append(ria_thread)
            ria_thread.daemon = True

            wu_thread = Thread(target=wu_value)
            threads.append(wu_thread)
            wu_thread.daemon = True

            conversion_thread = Thread(target=google_value)
            threads.append(conversion_thread)
            conversion_thread.daemon = True

            for thread in threads:
                thread.start()
                thread.join()

        except:
            return
        finally:
            time.sleep(180)


bucket = S3Bucket("com-remittance-data")

remitly_df = pd.DataFrame(columns=['datetime', 'value'])
xoom_df = pd.DataFrame(columns=['datetime', 'value'])
ria_df = pd.DataFrame(columns=['datetime', 'value'])
wu_df = pd.DataFrame(columns=['datetime', 'value'])
exchange_df = pd.DataFrame(columns=['datetime', 'value'])
tz = timezone('EST')
browser = Browser()
tab = browser.open_new_tab(incognito=True, headless=True)
main()
