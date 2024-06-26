import logging

class Log:

  @staticmethod
  def logGen():
    logging.basicConfig(filename=".\\Logs\\test.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger