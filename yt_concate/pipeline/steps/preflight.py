import logging

from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        logging.getLogger().info('in Preflight')
        utils.creat_dirs()
