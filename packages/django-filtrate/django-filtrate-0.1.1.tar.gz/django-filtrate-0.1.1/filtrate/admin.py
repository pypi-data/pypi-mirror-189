from django import forms
from django.contrib import admin

from .models import Filter
from .registry import filter_registry


class FiltrateForm(forms.ModelForm):
    model = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Now you can get your choices based on that object id
        self.fields["model"].choices = [
            (f"{model._meta.app_label}.{model._meta.model_name}", cls_name)
            for cls_name, model in filter_registry.all()
        ]


@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    search_fields = ["name", "model"]
    list_display = ["name", "model", "is_active"]
    list_filter = ["is_active"]
    form = FiltrateForm

    # def formfield_for_choice_field(self, db_field, request, **kwargs):
    #     if db_field.name == "model":
    #         kwargs["choices"] = [
    #             (f"{model._meta.app_label}.{model._meta.model_name}", cls_name) for cls_name, model in filter_registry.all()
    #         ]
    #     return super().formfield_for_choice_field(db_field, request, **kwargs)
