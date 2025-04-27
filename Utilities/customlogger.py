import logging
import os

class logGen():
    @staticmethod
    def logger():
        filepath = os.path.join(os.path.dirname(__file__), '..', 'Logs', 'automation.log')
        logging.basicConfig(filename=filepath,
                            format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG, force=True)

        logger= logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger