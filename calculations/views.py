from django.shortcuts import render, redirect
from .form import CropCalculatorForm
from .crops_list import CROP_DATA, LIVESTOCK_DATA
from .calculations import calculate_acres_required, filter_selected_crops, filter_selected_livestock

def crop_calculator(request):
    if request.method == 'POST':
        form = CropCalculatorForm(request.POST)
        if form.is_valid():
            num_people = form.cleaned_data['num_people']
            acreage = form.cleaned_data['acreage']
            calories_per_day = form.cleaned_data['calories_per_day']
            protein_diet_per_person = form.cleaned_data['protein_diet_per_person']
            dry_season_length = form.cleaned_data['dry_season_length']
            wet_season_length = form.cleaned_data['wet_season_length']
            livestock = form.cleaned_data.get('livestock', [])
            crops = form.cleaned_data.get('crops', [])

            selected_crops = filter_selected_crops(crops)
            selected_livestock = filter_selected_livestock(livestock)

            # calculate acres required for each crop and livestock
            results = calculate_acres_required(
                num_people,
                calories_per_day,
                protein_diet_per_person,
                acreage,
                CROP_DATA,
                LIVESTOCK_DATA,
                dry_season_length,
                wet_season_length
            )
            
            print(results) # Added print statement

            return render(request, 'calculations/results.html', {
                'selected_crops': selected_crops,
                'selected_livestock': selected_livestock,
                'results': results,
            })
    else:
        form = CropCalculatorForm()

    return render(request, 'calculations/crop_calculator.html', {'form': form})

def results(request):
    results = request.session.get('results', {})
    print("Results retrieved from session:", results)
    selected_crops = request.session.get('selected_crops', [])
    selected_livestock = request.session.get('selected_livestock', [])
    print("Selected crops:", selected_crops)  # Added print statement
    print("Selected livestock:", selected_livestock)  # Added print statement
    return render(request, 'calculations/results.html', {'results': results, 'selected_crops': selected_crops, 'selected_livestock': selected_livestock})
