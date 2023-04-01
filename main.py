import sys

from cron_parser import CronParser


def main(args):
    cron_parser = CronParser()
    cron_parser.parse_cron(args[1])


if __name__ == '__main__':
    main(args=sys.argv)
