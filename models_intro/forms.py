from django import forms
from models_intro.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name':'Student Name',
            'roll': 'Student Roll',
        },
        widgets= {
            'name':forms.TextInput(attrs={'class':'input input-bordered w-full'}),
            'roll':forms.NumberInput(attrs={'class':'input input-bordered w-full'}),
            'f_name':forms.TextInput(attrs={'class':'input input-bordered w-full'}),
            'address':forms.TextInput(attrs={'class':'input input-bordered w-full'})
        }
        help_texts={
            
        }
        error_messages={
            
        }
    