from typing import Sequence

from django.contrib import admin
from django.http import HttpRequest

from .filters import FiltrateFilter
from .registry import filter_registry


class FiltrateMixin(admin.ModelAdmin):
    custom_lookups = None

    def __init__(self, model, admin_site, *args, **kwargs):
        self.custom_lookups = None

        super().__init__(model, admin_site, *args, **kwargs)

        filter_registry.register(model)

    def get_list_filter(self, request: HttpRequest) -> Sequence[str]:
        list_filter = super().get_list_filter(request)

        if list_filter is None:
            list_filter = []
        elif isinstance(list_filter, tuple):
            list_filter = list(list_filter)

        list_filter.insert(0, FiltrateFilter)

        return list_filter
