# -*- coding: UTF-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from register.models import User


class UserForm(forms.ModelForm):
    salutation = forms.ChoiceField(choices=(("Mr.", "Mr."), ("Mrs.", "Mrs."), ("Ms.", "Ms."), ("Dr.", "Dr."),
                                            ("Prof.", "Prof."), ("Sir", "Sir"), ("Lady", "Lady"), ("Lord", "Lord")),
                                   required=True)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)
    organisation = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=40, required=True)
    postcode = forms.CharField(max_length=10, required=True)
    country = forms.CharField(max_length=60, required=True)
    telephone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=60, required=True)
    fee_normal = forms.BooleanField(label="I wish to register for the conference at the normal price of £420",
                                    required=False)
    fee_student = forms.BooleanField(label="I wish to register for the conference at the reduced price of £300"
                                           "(bona fide students only)", required=False)
    fee_one_day = forms.BooleanField(label="I wish to register for a one day pass to the conference for £250",
                                     required=False)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('/register/', 'Submit Registration', css_class='btn-primary'))

    class Meta:
        model = User
        fields = ('salutation', 'first_name', 'last_name', 'organisation', 'address', 'city', 'postcode', 'country',
                  'telephone', 'email', 'fee_normal', 'fee_student', 'fee_one_day')
