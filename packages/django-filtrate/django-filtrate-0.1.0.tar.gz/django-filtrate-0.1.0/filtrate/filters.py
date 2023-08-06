from django.contrib.admin import SimpleListFilter

from .models import Filter


class FiltrateFilter(SimpleListFilter):
    title = "custom filters"
    parameter_name = "filtrate"

    def __init__(self, request, params, model, model_admin, *args, **kwargs):
        self.custom_filters = {f.name: f for f in Filter.filters_for_model(model)}

        super().__init__(request, params, model, model_admin, *args, **kwargs)

    def lookups(self, request, model_admin) -> tuple:
        """Add custom filter to allow custom log filtering"""
        # return (("backoffice_payments", "Backoffice User Payments"),)
        filters = []
        for filter_name in self.custom_filters.keys():
            filters.append((str(filter_name), filter_name))
        return tuple(filters)

    def queryset(self, request, queryset):
        if self.value() in self.custom_filters:
            return queryset.filter(**self.custom_filters[self.value()].filters)

        return queryset
