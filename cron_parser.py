import configparser
from utils import *


class CronParser:
    def __init__(self, config_file_path = "cron_parser.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)
        self.components = self.config['DEFAULT']['cron_string_component'].split(', ')
        self.ranges = self.config['DEFAULT']

    def get_range(self, cur_period, range_string='*'):
        if '*' in range_string:
            return int(self.ranges[cur_period + '_start']), int(self.ranges[cur_period + '_end'])
        return (int(number) for number in range_string.split('-'))

    def process_asterisk(self, cur_period):
        start, end = self.get_range(cur_period)
        return list(range(start, end + 1))

    def process_slash(self, item, cur_period):
        range_string, step = item.split('/')
        step = int(step)
        start, end = self.get_range(cur_period, range_string)
        return list(range(start, end + 1, step))

    def get_values(self, item, cur_period):
        if ',' in item:
            return process_comma(item)
        if '/' in item:
            return self.process_slash(item, cur_period)
        if '-' in item:
            return process_hyphen(item)
        if '*' in item:
            return self.process_asterisk(cur_period)
        return [int(item)]

    def parse_cron(self, cron_string):
        cron_string = cron_string.split(' ')

        for cur_component, item in zip(self.components, cron_string):
            values = item
            if cur_component != 'command':
                values_list = self.get_values(item, cur_component)
                values = get_stringified_values(values_list)

            print_string(cur_component, values)


def process_comma(item):
    return [int(number) for number in item.split(',')]


def process_hyphen(item):
    start, end = [int(number) for number in item.split('-')]
    return [number for number in range(start, end + 1)]
