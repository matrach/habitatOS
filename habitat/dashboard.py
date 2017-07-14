from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import Dashboard
from grappelli.dashboard import modules


class IndexDashboard(Dashboard):
    def init_with_context(self, context):

        self.children.append(modules.ModelList(
            title=_('Sensors'),
            column=1,
            collapsible=False,
            models=[
                'habitat.building.sensors.*',
            ]))

        self.children.append(modules.ModelList(
            title=_('Experiments'),
            column=1,
            collapsible=False,
            models=[
                'habitat.experiments.biolab.*',
            ]))

        self.children.append(modules.ModelList(
            title=_('Food'),
            column=1,
            collapsible=False,
            models=[
                'habitat.systems.food.*',
            ]))

        self.children.append(modules.ModelList(
            title=_('Systems'),
            column=1,
            collapsible=False,
            models=[
                'habitat.systems.inventory.*',
            ]))

        self.children.append(modules.ModelList(
            title=_('Communication'),
            column=1,
            collapsible=False,
            models=[
                'habitat.systems.communication.*',
                'habitat.systems.reporting.*',
            ]))

        self.children.append(modules.ModelList(
            title=_('Science'),
            column=1,
            collapsible=False,
            models=[
                'habitat.science.education.*',
                'habitat.science.psychology.*',
            ]))

        self.children.append(modules.ModelList(
            title=_('Medical'),
            column=1,
            collapsible=False,
            models=[
                'habitat.science.medicine.*',
            ]))

        self.children.append(modules.LinkList(
            title=_('Shortcuts'),
            collapsible=False,
            column=3,
            children=[
                {'title': _('Calendar'), 'url': 'javascript:alert("not yet connected")'},
                {'title': _('Chat'), 'url': 'javascript:alert("not yet connected")'},
                {'title': _('Documentation'), 'url': 'javascript:alert("not yet connected")'},
                {'title': _('Issue Tracker'), 'url': 'javascript:alert("not yet connected")'}]))

        if context['user'].has_perm('admin.add_user'):
            self.children.append(modules.ModelList(
                title=_('Administration'),
                column=3,
                collapsible=False,
                models=['django.contrib.*'],
                css_classes=['grp-closed']))

        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5,
            collapsible=True,
            column=3,
            css_classes=['grp-closed']))
