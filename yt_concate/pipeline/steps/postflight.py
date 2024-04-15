import logging

from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        logging.getLogger().info('in Postflight')
