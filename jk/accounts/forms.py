from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# from accounts.models import UserProfileSpecification
from django import forms
from django.core import validators
from accounts.models import Document


class UserCreateForm(UserCreationForm):
    """
    this class is inheriting from: UserCreationForm
    that's why you can use this fields like:
        - username
        - email
        - password1
        - password2
    plus playing with label names etc.
    """
    class Meta():
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'


# class UserProfileSpecificationForm(UserCreationForm):
#
#     class Meta():
#         model = UserProfileSpecification
#         fields = ('company', 'portfolio_site', 'profile_pic')


# class DocumentForm(forms.Form):
#     doc_file = forms.FileField(
#         label='File',
#     )
#
class DocumentForm(forms.ModelForm):

    class Meta():
        model = Document
        fields = ('doc_file', 'name', )

        # widgets = {
        #     'author': forms.TextInput(attrs={
        #         'class': 'textinputclass'
        #     }),
        #     'text': forms.Textarea(attrs={
        #         'class': 'editable medium-editor-textarea'
        #     })
        # }

'''
I want to place these two forms to on view man :))
'''


class FancyFormPzsBozpPo(forms.Form):

    custom_name = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'Define custom name'}))
    mandant_obchodne_meno = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'JK s.r.o'}))
    mandant_sidlo = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'Kosice Povazska 40/A'}))
    mandant_ICO = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'2222222222'}))
    mandant_DIC = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'11111111'}))
    mandant_IC_DPH = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'77777777'}))
    mandant_zapis = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'Kosice SUD 2'}))
    mandant_zastupenie = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'Katarina Szilagiyova'}))
    mandant_email = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'katka@gmail.com'}))
    mandant_telefon = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'0915 777 777'}))
    suma_pzs = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'550'}))
    suma_po = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'440'}))
    suma_bozp = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'480'}))
    datum = forms.CharField(max_length=256,  widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'14.11.2017'}))
    miesto = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class':'textinputclass', 'value':'Kosice'}))


# class SelectProcessForm(forms.Form):
#     my_docs = Document.objects.all()

