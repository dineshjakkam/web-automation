import os
import logging

from logging.handlers import RotatingFileHandler

from common.utils import touch, ROOT_DIRECTORY

LOGS_DIRECTORY = ROOT_DIRECTORY+'/logs'

if not os.path.exists(LOGS_DIRECTORY):
    os.mkdir(LOGS_DIRECTORY)


class WALogger:
    """Logging module that can persist logs"""

    non_persisted_logs_path = "/tmp/wa.log"
    persisted_logs_path = LOGS_DIRECTORY+"/wa.log"

    @staticmethod
    def init_logger():
        """
        Init both persisted and non persisted logs
        :return:
        """
        logger = logging.getLogger('webAutomation')
        logger.setLevel(logging.DEBUG)

        non_persisted_logs_handler = WALogger.get_file_handler(
            logfile_location=WALogger.non_persisted_logs_path,
            max_bytes=(1024 * 1024 * 15),  # max fs size is 64MB
            backup_count=1)
        non_persisted_logs_handler.setLevel(logging.DEBUG)
        logger.addHandler(non_persisted_logs_handler)

        persisted_logs_handler = WALogger.get_file_handler(
            logfile_location=WALogger.persisted_logs_path,
            max_bytes=(1024 * 1024 * 2),  # max fs size is 64MB
            backup_count=1)
        persisted_logs_handler.setLevel(logging.ERROR)
        logger.addHandler(persisted_logs_handler)

        WALogger.set_logger(logger)

    @classmethod
    def get_file_handler(cls, logfile_location, max_bytes, backup_count):
        """
        A rotating file handler that defines the logs structure
        :param logfile_location:
        :param max_bytes:
        :param backup_count:
        :return:
        """
        try:
            if not os.path.exists(logfile_location):
                touch(logfile_location)
            file_handler = RotatingFileHandler(
                logfile_location,
                maxBytes=max_bytes,
                backupCount=backup_count)
            file_formatter = logging.Formatter(
                '%(filename)s: %(asctime)s %(levelname)s: %(message)s',
                datefmt='%b %d %H:%M:%S')
            file_handler.setFormatter(file_formatter)
            return file_handler
        except IOError as e:
            print(e)

    @staticmethod
    def set_logger(logger):
        WALogger.__logger = logger

    @staticmethod
    def get_logger():
        """
        returns logger
        :return:
        """
        WALogger.init_logger()
        return WALogger.__logger
