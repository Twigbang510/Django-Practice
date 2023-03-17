from django import forms

class MyForm(forms.Form):
    param1 = forms.CharField(label='Parameter 1', max_length=100)
    param2 = forms.CharField(label='Parameter 2', max_length=100)
    checkbox_choices = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )
    checkbox_field = forms.MultipleChoiceField(
        label='Checkbox Field',
        choices=checkbox_choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )