import logging
import os


class LogGeneration:

    @staticmethod
    def loggen():
        log = os.getcwd()
        log_dir = log.replace('testCases', 'logs')
        logging.basicConfig(filename=log_dir+"/automation.log",
                            filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
