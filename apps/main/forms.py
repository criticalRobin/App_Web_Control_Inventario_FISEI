from django import forms
from .models import (
    Computer,
    Laboratory,
    Recommendation,
    Task,
    LabItem,
    ComputerItem,
)


# CREATION FORMS
class CreateLaboratoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["name"].widget.attrs["autofocus"] = True

    class Meta:
        model = Laboratory
        fields = "__all__"


class CreateComputerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["mouse"].widget.attrs["autofocus"] = True

    class Meta:
        model = Computer
        fields = "__all__"


class CreateProjectorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = LabItem
        fields = "__all__"


class CreateRecommendationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["description"].widget.attrs["autofocus"] = True

    class Meta:
        model = Recommendation
        fields = ["description", "user_id"]


class CreateTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["description"].widget.attrs["autofocus"] = True

    class Meta:
        model = Task
        fields = ["description", "user_id"]


class CreateRamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = ComputerItem
        fields = "__all__"



