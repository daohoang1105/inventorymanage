from django.forms import ModelForm
from .models import SparePartOutRequest, User, AllSparePart, SparePartOutRecord
from django.contrib.auth.forms import UserCreationForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username','email', 'password1','password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username','email', 'bio']


class ManageForm(forms.ModelForm):
    class Meta:
        model = AllSparePart
        fields = '__all__'
        widgets = {
            'partCode': forms.TextInput(attrs={'class': 'form-control'}),
            'goodStatus': forms.Select(attrs={'class': 'form-control'}, choices=AllSparePart.Status.choices),
            'sparePartType': forms.Select(attrs={'class': 'form-control'}, choices=AllSparePart.SpareType.choices),
            'csceHWMO': forms.Select(attrs={'class': 'form-control'}, choices=AllSparePart.CSCEHWMO.choices),
            'warehouse': forms.Select(attrs={'class': 'form-control'}, choices=AllSparePart.WAREHOUSE.choices),
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'productDescription' : forms.TextInput(attrs={'class': 'form-control'}),
            'deliverDate' : forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'sender' : forms.TextInput(attrs={'class': 'form-control'}),
            'batch' : forms.TextInput(attrs={'class': 'form-control'}),
            'transitWay' : forms.TextInput(attrs={'class': 'form-control'}),
            'invoice' : forms.TextInput(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control','rows':'3'}),
            'actualQTY' : forms.NumberInput(attrs={'class': 'form-control'}),
            'remainQTY' : forms.NumberInput(attrs={'class': 'form-control'}),
            'consumQTY' : forms.NumberInput(attrs={'class': 'form-control'}),
            'user' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ManageFormOuT(forms.ModelForm):
    class Meta:
        model = SparePartOutRecord
        fields = ['outgsp']
        widgets = {
            'outgsp': forms.TextInput(attrs={'class': 'form-control'}),
        }