from django import forms

class MyForm(forms.Form):
    category = (
        ('Programming', 'Programming'),
        ('Misc', 'Misc'),
        ('Dark', 'Dark'),
        ('Pun', 'Pun'),
        ('Spooky', 'Spooky'),
        ('Christmas', 'Christmas'),
    )
    flags = (
        ('nsfw', 'nsfw'),
        ('religious', 'religious'),
        ('political', 'political'),
        ('racist', 'racist'),
        ('sexist', 'sexist'),
        ('explicit', 'explicit'),
    )
    types = (
        ('single', 'single'),
        ('twopart', 'twopart')
    )
    lang = (
        ('cs', 'cs - Czech'),
        ('de', 'de - German'),
        ('en', 'en - English' ),
        ('es', 'es - Spanish'),
        ('fr', 'fr - French'),
        ('pt', 'pt - Portuguese'),
        
    )

    keyword = forms.CharField(max_length=100, label='Keyword: ', required=False )
    start = forms.IntegerField(max_value=1000, label='Start', required=False, min_value=0, initial=0)
    end = forms.IntegerField(max_value=9999, label='End', required=False, min_value=100, initial=100)
    amount = forms.IntegerField(max_value=100,label='Amount of joke: ', required=False, min_value=1, initial=1)
    lang_select = forms.CharField(
        label="Select language: ",
        widget = forms.Select(choices=lang, ),
        initial= lang[2]
    )
    category_choice = forms.MultipleChoiceField(
        label='Category',
        choices=category,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    flags_choice = forms.MultipleChoiceField(
        label='Black List',
        choices=flags,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    types_choice = forms.MultipleChoiceField(
        label='Types',
        choices=types,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    field_order = ['category_choice','flags_choice', 'types_choice' ]