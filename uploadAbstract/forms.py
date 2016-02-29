from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from uploadAbstract.models import SubmittedAbstract


class UserForm(forms.ModelForm):
    salutation = forms.ChoiceField(choices=(("Mr.", "Mr."), ("Mrs.", "Mrs."), ("Ms.", "Ms."), ("Dr.", "Dr."),
                                            ("Prof.", "Prof."), ("Sir", "Sir"), ("Lady", "Lady"), ("Lord", "Lord")),
                                   required=True)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(max_length=60, required=True)
    paper_title = forms.CharField(max_length=60, required=True)
    abstract = forms.CharField(max_length=2000, required=True, widget=forms.Textarea)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('/uploadAbstract/', 'Upload Abstract', css_class='btn-primary'))

    class Meta:
        model = SubmittedAbstract
        fields = ('salutation', 'first_name', 'last_name', 'email', 'paper_title', 'abstract')
