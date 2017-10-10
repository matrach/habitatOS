import math
import datetime
from django.utils.translation import ugettext_lazy as _


"""
Based on http://jtauber.github.io/mars-clock/

Formulae from Allison, M., and M. McEwen 2000. <a href="http://pubs.giss.nasa.gov/abs/al05000n.html">A post-Pathfinder evaluation of aerocentric solar coordinates with improved timing recipes for Mars seasonal/diurnal climate studies.</a> <i>Planet. Space Sci.</i> <b>48</b>, 215-235. and <a href="http://www.giss.nasa.gov/tools/mars24/help/algorithm.html">Mars24 Algorithm and Worked Examples</a>
"""


class MartianStandardTime:
    NAME = 'Martian Standard Time'
    DATE_VERBOSE_NAME = _('Mars Sol Date')
    DATE_HELP_TEXT = _('example: 51099.420109, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time')
    TIME_VERBOSE_NAME = _('Coordinated Mars Time')
    TIME_HELP_TEXT = _('example: 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time')
    DATETIME_VERBOSE_NAME = _('Mars Standard Time')
    DATETIME_HELP_TEXT = _('example: 51099.420109 16:04:57, <a href="/api/v1/timezone/martian-standard-time/converter/" target="_blank">use converter</a> to calculate from Earth time')

    MILISECOND = 1000

    # Near Coincident Earth and Mars Times
    # An easy-to-remember benchmark for calibrating clocks is a date and time at which the "standard time" for both Mars and Earth was almost the same. When the time on Earth was 00:00:00 on Jan. 6, 2000 (UTC), it was just 21 Mars-seconds away from also being mean midnight at the Mars prime meridian.
    # The equivalent of the Julian Date for Mars is the Mars Sol Date.
    # At midnight on the 6th January 2000 (ΔtJ2000 = 4.5) it was midnight at the Martian prime meridian, so our starting point for Mars Sol Date is ΔtJ2000 − 4.5.
    J2000_MIDNIGHT_SYNCHRONIZATION = 4.5

    # The length of a Martian day and Earth (Julian) day differ by a ratio of 1.027491252 so we divide by that.
    MARS_DAY_LENGTH = 1.027491252

    # By convention, to keep the MSD positive going back to midday December 29th 1873, we add 44,796.
    ADD_BY_CONVENTION = 44796.0

    # There is a slight adjustment as the midnights weren't perfectly aligned. Allison, M., and M. McEwen 2000 has −0.00072 but the Mars24 site gives a more up-to-date −0.00096.
    # MSD = ([(ΔtJ2000 − 4.5) / 1.027491252] + 44,796.0 − 0.00096)
    J2000_MIDNIGHT_ADJUSTMENT = 0.00096

    @classmethod
    def get_time_dict(cls, from_datetime=None):
        if not from_datetime:
            from_datetime = datetime.datetime.utcnow()

        # Difference between TAI and UTC. This value should be
        # updated each time the IERS announces a leap second.
        tai_offset = 37

        miliseconds = from_datetime.timestamp() * cls.MILISECOND

        jd_ut = 2440587.5 + (miliseconds / 8.64E7)
        jd_tt = jd_ut + (tai_offset + 32.184) / 86400
        j2000 = jd_tt - 2451545.0
        date = (((j2000 - cls.J2000_MIDNIGHT_SYNCHRONIZATION) / cls.MARS_DAY_LENGTH) + cls.ADD_BY_CONVENTION - cls.J2000_MIDNIGHT_ADJUSTMENT)
        time = (24 * date) % 24

        x = time * 3600
        hours = math.floor(x / 3600)

        y = x % 3600
        minutes = math.floor(y / 60)
        seconds = round(y % 60)

        # By convention during Lunares martian missions we skip decimal part of date (which is time)
        only_date = int(date)

        return {
            'date': f'{only_date:,d}',
            'time': f'{hours:02d}:{minutes:02d}:{seconds:02d}',
            'datetime': f'{only_date:,d} {hours:02d}:{minutes:02d}:{seconds:02d}',
            'hour': f'{hours:02d}',
            'minute': f'{minutes:02d}',
            'second': f'{seconds:02d}',
            'full_date': f'{date:f}',
        }

    @classmethod
    def date(cls):
        """
        Mars Sol Date
        """
        mst = cls.get_time_dict()
        return mst['date']

    @classmethod
    def time(cls):
        """
        MTC - Coordinated Mars Time
        """
        mst = cls.get_time_dict()
        return mst['time']

    @classmethod
    def datetime(cls):
        mst = cls.get_time_dict()
        return mst['datetime']
