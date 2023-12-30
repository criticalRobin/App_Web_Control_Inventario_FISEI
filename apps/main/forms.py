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
    Security_camera,
    Air_Conditioner,
    Regulator_voltage,
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
        model = Projector
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
        fields = ["description", "computer_id", "user_id"]


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


class CreateMonitorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["model"].widget.attrs["autofocus"] = True

    class Meta:
        model = Monitor
        fields = "__all__"


class CreateCpuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = Cpu
        fields = "__all__"


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
        model = Ram
        fields = "__all__"


class CreateDiskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = Disk
        fields = "__all__"


class CreateProcessorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = Processor
        fields = "__all__"


class CreateSecurityCameraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = Security_camera
        fields = "__all__"


class CreateRegulatorVoltageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = Regulator_voltage
        fields = "__all__"


class CreateAirConditionerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["brand"].widget.attrs["autofocus"] = True

    class Meta:
        model = Air_Conditioner
        fields = "__all__"
