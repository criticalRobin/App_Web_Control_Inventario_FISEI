from django import forms
from .models import (
    Computer,
    Laboratory,
    Projector,
    Recommendation,
    Cpu,
    Monitor,
    Task,
    Processor,
    Disk,
    Ram,
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
