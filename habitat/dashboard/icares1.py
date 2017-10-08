from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import Dashboard
from grappelli.dashboard import modules


class AdminDashboard(Dashboard):

    def init_with_context(self, context):

        # Column 1
        self.children.append(modules.ModelList(
            title=_('Reporting'),
            column=1,
            collapsible=False,
            models=[
                'habitat.reporting.models.daily.Daily',
                'habitat.reporting.models.repair.Repair',
                'habitat.reporting.models.incident.Incident',
                'habitat.reporting.models.waste.Waste',
                'habitat.water.models.drinking.Drinking',
                'habitat.water.models.green.Green',
                'habitat.water.models.technical.Technical',
                'habitat.communication.models.diary.DiaryEntry',
                'habitat.extravehicular.models.activity.Activity']))

        self.children.append(modules.ModelList(
            title=_('Questionaries'),
            column=1,
            collapsible=False,
            models=[
                'habitat.reporting.models.mood.Mood',
                'habitat.reporting.models.sociodynamics.SociodynamicReport',
                'habitat.reporting.models.sleep.Sleep']))

        self.children.append(modules.ModelList(
            title=_('Health'),
            column=1,
            collapsible=False,
            models=[
                'habitat.health.models.blood_pressure.BloodPressure',
                'habitat.health.models.urine.Urine',
                'habitat.health.models.temperature.Temperature',
                'habitat.health.models.weight.Weight']))

        # Column 2

        self.children.append(modules.LinkList(
            title=_('Shortcuts'),
            collapsible=False,
            column=2,
            children=[
                {'title': _('Schedule'), 'url': '/api/v1/dashboard/schedule/'},
                {'title': _('Subjective Time Perception'), 'url': 'http://time.astrotech.io'},
                # {'title': _('Martian Clock Clock'), 'url': '/api/v1/dashboard/clock/'},
            ]))

        self.children.append(modules.ModelList(
            title=_('Sensors'),
            column=2,
            collapsible=False,
            models=[
                'habitat.sensors.models.zwave_sensor.ZWaveSensor']))

        # Column 3
        if context['user'].has_perm('admin.add_user'):
            self.children.append(modules.ModelList(
                title=_('Administration'),
                column=3,
                collapsible=True,
                models=['django.contrib.*'],
                css_classes=['grp-closed']))