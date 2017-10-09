from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import Dashboard
from grappelli.dashboard import modules


class AdminDashboard(Dashboard):

    def init_with_context(self, context):

        # Column 1
        self.children.append(modules.ModelList(
            title=_('Questionaries - Visible only to you'),
            column=1,
            collapsible=False,
            models=[
                'habitat.reporting.models.mood.Mood',
                'habitat.reporting.models.sociodynamics.SociodynamicReport',
                'habitat.reporting.models.sleep.Sleep']))

        self.children.append(modules.ModelList(
            title=_('Health - Visible only to you'),
            column=1,
            collapsible=False,
            models=[
                'habitat.health.models.blood_pressure.BloodPressure',
                'habitat.health.models.urine.Urine',
                'habitat.health.models.temperature.Temperature',
                'habitat.health.models.weight.Weight']))

        # Column 2
        self.children.append(modules.ModelList(
            title=_('Reporting - Visible to anyone'),
            column=2,
            collapsible=False,
            models=[
                'habitat.reporting.models.daily.Daily',
                'habitat.reporting.models.repair.Repair',
                'habitat.reporting.models.incident.Incident',
                'habitat.reporting.models.waste.Waste',
                'habitat.communication.models.diary.DiaryEntry',
                'habitat.extravehicular.models.activity.Activity']))

        self.children.append(modules.ModelList(
            title=_('Water - Visible to anyone'),
            column=2,
            collapsible=False,
            models=[
                'habitat.water.models.technical.TechnicalWater',
                'habitat.water.models.drinking.DrinkingWater',
                'habitat.water.models.green.GreenWater']))

        # Column 3
        if context['user'].has_perm('admin.add_user'):
            self.children.append(modules.ModelList(
                title=_('Administration'),
                column=3,
                collapsible=True,
                models=['django.contrib.*'],
                css_classes=['grp-closed']))

        self.children.append(modules.LinkList(
            title=_('Shortcuts'),
            collapsible=False,
            column=3,
            children=[
                {'title': _('Schedule'), 'url': '/api/v1/dashboard/schedule/'},
                {'title': _('Martian Clock Converter'), 'url': '/api/v1/timezone/martian-standard-time/converter/'},
                {'title': _('Subjective Time Perception'), 'url': 'http://time.astrotech.io'},
            ]))

        self.children.append(modules.ModelList(
            title=_('Sensors'),
            column=3,
            collapsible=False,
            models=[
                'habitat.sensors.models.zwave_sensor.ZWaveSensor']))
