# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger



import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # Create console handler and set level to info
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # Create formatter
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # Add formatter to ch
        ch.setFormatter(formatter)
        # Add ch to logger
        logger.addHandler(ch)
        return logger
