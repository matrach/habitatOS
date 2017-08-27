from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import Dashboard
from grappelli.dashboard import modules


class IndexDashboard(Dashboard):

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
        self.children.append(modules.LinkList(
            title=_('Shortcuts'),
            collapsible=False,
            column=3,
            children=[
                {'title': _('Subjective Time Perception'), 'url': 'http://stpa.astrotech.io'},
                {'title': _('Lunar Clock'), 'url': 'http://lunarclock.org/'},
                {'title': _('Schedule'), 'url': 'http://mariusz-slonina.pl/le-1-control/'},
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

        if context['user'].has_perm('admin.add_user'):
            self.children.append(modules.ModelList(
                title=_('Administration'),
                column=3,
                collapsible=False,
                models=['django.contrib.*'],
                css_classes=['grp-closed']))

        """
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5,
            collapsible=True,
            column=3,
            css_classes=['grp-closed']))
        """
