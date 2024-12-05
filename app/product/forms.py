from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from product.models import Product


class CustomArrayWidget(forms.Textarea):
    def format_value(self, value):
        if (not value):
            return ''
        value = value.split(",")
        return '\n'.join(value)

    def value_from_datadict(self, data, files, name):
        raw_value = data.get(name)
        if raw_value:
            return [item.strip() for item in raw_value.split('\n') if item.strip()]
        return []


class ProductModelAdminForm(forms.ModelForm):
    poe_power_output = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    power_consumption = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    poe_power_budget = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    port = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    poe_injector_port = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    accessories = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    operation_mode = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    interface = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    package = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )
    ir_distance = SimpleArrayField(
        forms.CharField(max_length=255),
        widget=CustomArrayWidget,
        required=False,
        help_text="Enter each element on a new line.",
    )

    class Meta:
        model = Product
        fields = '__all__'
