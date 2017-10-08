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
                'habitat.reporting.*.*']))

        self.children.append(modules.ModelList(
            title=_('Experiments'),
            column=1,
            collapsible=False,
            models=[
                'habitat.experiments.*.*']))

        self.children.append(modules.ModelList(
            title=_('Extra-Vehicular Activity'),
            column=1,
            collapsible=False,
            models=[
                'habitat.extravehicular.*.*']))

        self.children.append(modules.ModelList(
            title=_('Laboratory'),
            column=1,
            collapsible=False,
            models=[
                'habitat.biolab.*']))

        self.children.append(modules.ModelList(
            title=_('Health'),
            column=1,
            collapsible=False,
            models=[
                'habitat.health.*']))

        # Column 2
        self.children.append(modules.ModelList(
            title=_('Water'),
            column=2,
            collapsible=False,
            models=[
                'habitat.water.*']))

        self.children.append(modules.ModelList(
            title=_('Communication'),
            column=2,
            collapsible=False,
            models=[
                'habitat.communication.*']))

        self.children.append(modules.ModelList(
            title=_('Food'),
            column=2,
            collapsible=False,
            models=[
                'habitat.food.*']))

        self.children.append(modules.ModelList(
            title=_('Systems'),
            column=2,
            collapsible=False,
            models=[
                'habitat.inventory.*']))

        # Column 3
        if context['user'].has_perm('admin.add_user'):
            self.children.append(modules.ModelList(
                title=_('Administration'),
                column=3,
                collapsible=True,
                models=['django.contrib.*'],
                css_classes=['grp-open']))

            self.children.append(modules.ModelList(
                title=_('API OAuth'),
                column=3,
                collapsible=True,
                models=['oauth2_provider.models.*'],
                css_classes=['grp-open']))

        self.children.append(modules.LinkList(
            title=_('Shortcuts'),
            collapsible=False,
            column=3,
            children=[
                {'title': _('Subjective Time Perception'), 'url': 'http://time.astrotech.io'},
                {'title': _('Martian Clock Clock'), 'url': 'http://icares1.habitatos.space/api/v1/dashboard/schedule/'},
            ]))

        self.children.append(modules.ModelList(
            title=_('Sensors'),
            column=3,
            collapsible=False,
            models=[
                'habitat.sensors.*']))

        self.children.append(modules.ModelList(
            title=_('Building'),
            column=3,
            collapsible=False,
            models=[
                'habitat.building.*',
                'habitat.light']))
