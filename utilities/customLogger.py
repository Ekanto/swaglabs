import logging

class LogGen:
    @staticmethod
    def loggen():
        logger  = logging.getLogger("Test Login")
        fileHandler  = logging.FileHandler('.\\Logs\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger