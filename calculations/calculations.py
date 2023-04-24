from .crops_list import CROP_DATA, LIVESTOCK_CHOICES, CROP_CHOICES, LIVESTOCK_DATA

def calculate_acres_required(people, daily_calories, daily_protein, acreage, crop_data, livestock_data, dry_season_length, wet_season_length):
    total_daily_calories = people * daily_calories
    total_daily_protein = people * daily_protein

    recommendation = {}

    total_season_length = dry_season_length + wet_season_length

    for crop in crop_data:
        crop_calories_per_acre = crop_data[crop]['calories_per_acre']
        crop_protein_per_acre = crop_data[crop]['protein_per_acre']
        crop_yield_factor = crop_data[crop]['yield_factor']

        # Adjust the crop yield factor based on the weather seasons
        crop_yield_factor = crop_yield_factor * (wet_season_length / total_season_length)

        crop_acres = acreage * crop_yield_factor
        crop_calories = crop_acres * crop_calories_per_acre
        crop_protein = crop_acres * crop_protein_per_acre

        print(f"{crop}: acres: {crop_acres}, calories: {crop_calories}, protein: {crop_protein}")  # Added print statement

        recommendation[crop] = {
            'acres': crop_acres,
            'calories': crop_calories,
            'protein': crop_protein,
        }

    for livestock in livestock_data:
        livestock_calories_per_animal = livestock_data[livestock]['calories_per_animal']
        livestock_protein_per_animal = livestock_data[livestock]['protein_per_animal']
        livestock_yield_factor = livestock_data[livestock]['yield_factor']

        livestock_acres = acreage * livestock_yield_factor
        livestock_calories = livestock_acres * livestock_calories_per_animal
        livestock_protein = livestock_acres * livestock_protein_per_animal

        print(f"{livestock}: acres: {livestock_acres}, calories: {livestock_calories}, protein: {livestock_protein}")  # Added print statement

        recommendation[livestock] = {
            'acres': livestock_acres,
            'calories': livestock_calories,
            'protein': livestock_protein,
        }

    return recommendation


def filter_selected_crops(crop_codes):
    selected_crops = []
    for crop_code in crop_codes:
        for crop_data in CROP_CHOICES:
            if crop_data[0] == crop_code:
                selected_crops.append(crop_data[1])
                break
    return selected_crops

def filter_selected_livestock(livestock_codes):
    selected_livestock = []
    for code, name in LIVESTOCK_CHOICES:
        if code in livestock_codes:
            selected_livestock.append(name)
    return selected_livestock
