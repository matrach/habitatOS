from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import Dashboard
from grappelli.dashboard import modules


class IndexDashboard(Dashboard):
    def init_with_context(self, context):

        self.children.append(modules.ModelList(
            title=_('Education'),
            column=1,
            collapsible=False,
            models=['habitat.education.*']))

        self.children.append(modules.ModelList(
            title=_('Environment'),
            column=1,
            collapsible=False,
            models=['habitat.environment.*']))

        self.children.append(modules.ModelList(
            title=_('Greenhouse'),
            column=1,
            collapsible=False,
            models=['habitat.greenhouse.*']))

        self.children.append(modules.ModelList(
            title=_('Inventory'),
            column=1,
            collapsible=False,
            models=['habitat.inventory.*']))

        self.children.append(modules.ModelList(
            title=_('Medicine'),
            column=1,
            collapsible=False,
            models=['habitat.medicine.*']))

        self.children.append(modules.ModelList(
            title=_('Notepad'),
            column=1,
            collapsible=False,
            models=['habitat.notepad.*']))

        self.children.append(modules.ModelList(
            title=_('Psychology'),
            column=1,
            collapsible=False,
            models=['habitat.psychology.*']))

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

