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
        widgets = {
            'description': forms.Textarea(attrs={'rows':5, 'cols':30}),
        }


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


class CreateLabItemForm(forms.ModelForm):
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
        widgets = {
            'description': forms.Textarea(attrs={'rows':5, 'cols':30}),
        }


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
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows':2, 'cols':30}),
        }


class StudentRecommendationForm(forms.ModelForm):
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
        fields = ["name", "description"]

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
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows':2, 'cols':30}),
        }


class CreateComputerItem(forms.ModelForm):
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
        widgets = {
            'description': forms.Textarea(attrs={'rows':5, 'cols':30}),
        }

class UpdateLaboratoryForm(CreateLaboratoryForm):
    class Meta:
        model = Laboratory
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows':5, 'cols':30}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        

class UpdateComputerForm(CreateComputerForm):
    class Meta:
        model = Computer
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].disabled = True

class UpdateLabItemForm(CreateLabItemForm):
    class Meta:
        model = LabItem
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows':5, 'cols':30}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].disabled = True

class UpdateRecommendationForm(CreateRecommendationForm):
    class Meta:
        model = Recommendation
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows':2, 'cols':30}),
        }

class UpdateTaskForm(CreateTaskForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows':2, 'cols':30}),
        }

class UpdateComputerItemForm(CreateComputerItem):
    class Meta:
        model = ComputerItem
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows':5, 'cols':30}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].disabled = True