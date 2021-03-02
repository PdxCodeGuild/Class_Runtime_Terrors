import itertools
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.safestring import mark_safe
from potty_spotter.core.utils import get_local_time
from potty_spotter.apps.object import models as models_object
from django.urls import reverse


class BaseTable(tables.Table):
    no = tables.Column(
        empty_values=(), orderable=False,
        attrs={"th": {"width": "3%", "class": "text-center"}, "td": {
            "class": "text-center align-middle"}, }
    )

    class Meta:
        attrs = {
            'class': 'table table-bordered table-striped table-hover table-sm bg-white',
            'id': 'table',
            'th': {'class': 'text-center align-middle'},
            'td': {'class': 'text-left align-middle'},
        }
        empty_text = 'No records available.'

    def __init__(self, *args, **kwargs):
        super(BaseTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_no(self):
        return '{}.'.format(next(self.counter) + 1)


class RestroomTable(BaseTable):
    actions = tables.TemplateColumn(
        verbose_name='',
        orderable=False,
        template_name='member/object/restroom/includes/table_actions.html',
        attrs={
            'th': {'class': 'w-10 text-center'},
            'td': {'class': 'text-center align-middle'},
        },
    )

    status = tables.TemplateColumn(
        template_name="member/object/restroom/includes/table_status.html",
        attrs={'td': {'class': 'w-10 text-center'}}
    )

    restroom_id = tables.Column(
        "Restroom ID", attrs={'td': {'class': 'text-center align-middle W-15'}}
    )

    class Meta(BaseTable.Meta):
        model = models_object.Restroom
        fields = (
            'no',
            'restroom_id',
            'status',
            'name',
            'latitude',
            'longitude',
            'actions'
        )
