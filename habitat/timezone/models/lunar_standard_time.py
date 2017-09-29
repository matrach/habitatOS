import datetime
from django.utils.translation import ugettext_lazy as _


class LunarStandardTime:
    NAME = 'Lunar Standard Time'
    DATE_VERBOSE_NAME = _('Lunar Date')
    DATE_HELP_TEXT = _('example: 50-09-12')
    TIME_VERBOSE_NAME = _('Coordinated Lunar Time')
    TIME_HELP_TEXT = _('example: 16:04:57')
    DATETIME_VERBOSE_NAME = _('Lunar Standard Time')
    DATETIME_HELP_TEXT = _('example: 50-09-03 ∇ 09:51:25')

    MINUTE = 60
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    MONTH = 30 * DAY
    YEAR = 12 * MONTH

    TIMESTAMP_NOW = 1506515436
    ADJUSTMENT = 1520674461
    TIMESTAMP_FIRST_STEP = 14159025
    SECONDS_LENGTH = 0.9843529666671
    MONTH_NAMES = {
        1: 'Armstrong',
        2: 'Aldrin',
        3: 'Conrad',
        4: 'Bean',
        5: 'Shepard',
        6: 'Mitchel',
        7: 'Scott',
        8: 'Irwin',
        9: 'Young',
        10: 'Duke',
        11: 'Cernan',
        12: 'Schmitt',
    }

    @classmethod
    def month_name(cls, number):
        return cls.MONTH_NAMES[number]

    @classmethod
    def get_time_dict(cls, time_shift=0):

        now = datetime.datetime.now().timestamp()
        s = (now + cls.ADJUSTMENT - cls.TIMESTAMP_NOW) / cls.SECONDS_LENGTH - time_shift

        year = int(s / cls.YEAR) | 0
        s -= cls.YEAR * year
        if time_shift <= 0:
            year += 1

        month = int(s / cls.MONTH) | 0
        s -= cls.MONTH * month
        if time_shift <= 0:
            month += 1

        day = int(s / cls.DAY) | 0
        s -= cls.DAY * day
        if time_shift <= 0:
            day += 1

        hour = int(s / cls.HOUR) | 0
        s -= cls.HOUR * hour

        minute = int(s / cls.MINUTE) | 0
        s -= cls.MINUTE * minute

        second = int(s / 1) | 0

        return {
            'year': f'{year:02d}',
            'month': f'{month:02d}',
            'day': f'{day:02d}',
            'hour': f'{hour:02d}',
            'minute': f'{minute:02d}',
            'second': f'{second:02d}',
            'date': f'{year:02d}-{month:02d}-{day:02d}',
            'time': f'{hour:02d}:{minute:02d}:{second:02d}',
            'datetime': f'{year:02d}-{month:02d}-{day:02d} ∇ {hour:02d}:{minute:02d}:{second:02d}',
            'separator': '∇',
            'name': cls.month_name(month),
        }

    @classmethod
    def date(cls):
        lst = cls.get_time_dict()
        return lst['date']

    @classmethod
    def time(cls):
        lst = cls.get_time_dict()
        return lst['time']

    @classmethod
    def datetime(cls):
        lst = cls.get_time_dict()
        return lst['datetime']
