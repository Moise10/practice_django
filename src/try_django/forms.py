from django import forms


class Contact_form(forms.Form):
  full_name = forms.CharField()
  email = forms.EmailField()
  content = forms.CharField(widget=forms.Textarea)
  
  def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get('email')
    return email