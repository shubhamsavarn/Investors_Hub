from django import forms
  
# create a ModelForm
class SignUpForm(forms.Form):
    # specify the name of model to use
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))