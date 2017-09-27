class MartianStandardTime:
    NAME = 'Martian Standard Time'

    @classmethod
    def date(cls):
        return f'0000-00-00'

    @classmethod
    def time(cls):
        return '00:00'

    @classmethod
    def datetime(cls):
        return f'{self.date()} {self.time()}'
