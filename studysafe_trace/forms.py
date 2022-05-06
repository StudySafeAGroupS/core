from django import forms
class ContactForm(forms.Form):
   HKU_ID = forms.CharField(required=False)
   date_of_diagnosis = forms.CharField(max_length=1000)