import datetime
from django.conf import settings
from django.utils.module_loading import import_string


def get_timezone():
    timezone = settings.HABITATOS['TIME_ZONE']
    cls = import_string(timezone)
    return cls


class LunarStandardTime:
    OFFSET_DAYS = 27
    OFFSET_HOURS = 10
    OFFSET_MINUTES = 50

    @staticmethod
    def date():
        begin = datetime.date(1969, 7, 21)
        today = datetime.date.today()
        year = int((today - begin).days / 365 + 2)
        date = today - datetime.timedelta(days=LunarStandardTime.OFFSET_DAYS)
        return f'{year}-{date.month:02}-{date.day:02}'

    @staticmethod
    def time():
        OFFSET = '11'
        # http://lunarclock.org/service/lst-for-iframe.php
        today = datetime.datetime.now()
        now = today - datetime.timedelta(hours=LunarStandardTime.OFFSET_HOURS, minutes=LunarStandardTime.OFFSET_MINUTES)
        return f'{now:%H:%M}'

    @staticmethod
    def datetime():
        return f'{self.date()} ∇ {self.time()}'


class MartianStandardTime:

    @staticmethod
    def date():
        return f'0000-00-00'

    @staticmethod
    def time():
        # http://lunarclock.org/service/lst-for-iframe.php
        return '00:00'

    @staticmethod
    def datetime():
        return f'{self.date()} {self.time()}'


