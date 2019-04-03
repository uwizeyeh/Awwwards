from django import forms
from .models import Project,Profile,Votes

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile','posted_on'] 


class VotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user','posted_on','project']               