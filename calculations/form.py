from django import forms
from .crops_list import CROP_CHOICES, LIVESTOCK_CHOICES

class CropCalculatorForm(forms.Form):
    num_people = forms.IntegerField(label='Number of people', min_value=1, initial=500)
    acreage = forms.FloatField(label='Acreage', min_value=0.1, initial=5)
    calories_per_day = forms.IntegerField(label='Calories per day', initial=2000, min_value=0, required=True)
    protein_diet_per_person = forms.IntegerField(label='Protein per day(g/day)', min_value=10, initial=50)
    dry_season_length = forms.IntegerField(label='Dry season length (months)', initial=5, min_value=0, max_value=12)
    wet_season_length = forms.IntegerField(label='Wet season length (months)', initial=5, min_value=0, max_value=12)


    livestock = forms.MultipleChoiceField(
        label='Livestock',
        choices=LIVESTOCK_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    crops = forms.MultipleChoiceField(
        label='Crops',
        choices=CROP_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
