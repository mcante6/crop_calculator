# crops_list.py

CROP_CHOICES = [
    ('sorghum', 'Sorghum'),
    ('millet', 'Millet'),
    ('finger_millet', 'Finger Millet'),
    ('maize', 'Maize'),
    ('pigeon_peas', 'Pigeon Peas'),
    ('soy_beans', 'Soy Beans'),
    ('bambara_beans', 'Bambara Beans'),
    ('rice', 'Rice'),
    ('groundnuts', 'Groundnuts'),
    ('kale', 'Kale'),
    ('cabbage', 'Cabbage'),
    ('jute_mallow', 'Jute Mallow'),
    ('pumpkin', 'Pumpkin'),
    ('sweet_potato', 'Sweet Potato'),
    ('irish_potato', 'Irish Potato'),
    ('banana', 'Banana'),
    ('plantain', 'Plantain'),
    ('okra', 'Okra'),
    ('eggplant', 'Eggplant'),
]

CROP_DATA = {
    'sorghum': {'calories_per_acre': 2400000, 'protein_per_acre': 70000, 'yield_factor': 1.0},
    'millet': {'calories_per_acre': 2250000, 'protein_per_acre': 66000, 'yield_factor': 1.1},
    'finger_millet': {'calories_per_acre': 2300000, 'protein_per_acre': 68000, 'yield_factor': 1.2},
    'maize': {'calories_per_acre': 2700000, 'protein_per_acre': 79000, 'yield_factor': 1.3},
    'pigeon_peas': {'calories_per_acre': 1500000, 'protein_per_acre': 90000, 'yield_factor': 0.9},
    'soy_beans': {'calories_per_acre': 1600000, 'protein_per_acre': 100000, 'yield_factor': 1.5},
    'bambara_beans': {'calories_per_acre': 1300000, 'protein_per_acre': 60000, 'yield_factor': 0.8},
    'rice': {'calories_per_acre': 2800000, 'protein_per_acre': 82000, 'yield_factor': 1.6},
    'groundnuts': {'calories_per_acre': 1700000, 'protein_per_acre': 93000, 'yield_factor': 1.7},
    'kale': {'calories_per_acre': 900000, 'protein_per_acre': 47000, 'yield_factor': 0.6},
    'cabbage': {'calories_per_acre': 800000, 'protein_per_acre': 43000, 'yield_factor': 0.5},
    'jute_mallow': {'calories_per_acre': 750000, 'protein_per_acre': 39000, 'yield_factor': 0.4},
    'pumpkin': {'calories_per_acre': 1100000, 'protein_per_acre': 58000, 'yield_factor': 0.7},
    'sweet_potato': {'calories_per_acre': 2000000, 'protein_per_acre': 74000, 'yield_factor': 1.4},
    'irish_potato': {'calories_per_acre': 2200000, 'protein_per_acre': 76000, 'yield_factor': 1.8},
    'banana': {'calories_per_acre': 2600000, 'protein_per_acre': 77000, 'yield_factor': 2.0},
    'plantain': {'calories_per_acre': 2500000, 'protein_per_acre': 75000, 'yield_factor': 1.9},
    'okra': {'calories_per_acre': 600000, 'protein_per_acre': 32000, 'yield_factor': 0.3},
    'eggplant': {'calories_per_acre': 555000, 'protein_per_acre': 15000, 'yield_factor': 0.2},
}


LIVESTOCK_CHOICES = [
    ('none', 'None'),
    ('chickens', 'Chickens'),
    ('goats', 'Goats'),
    ('cows', 'Cows'),
    ('sheep', 'Sheep'),
    ('pigs', 'Pigs'),
]

LIVESTOCK_DATA = {
    'none': {'calories_per_animal': 0, 'protein_per_animal': 0, 'yield_factor': 0},
    'chickens': {'calories_per_animal': 11000, 'protein_per_animal': 220, 'yield_factor': 0.1},
    'goats': {'calories_per_animal': 60000, 'protein_per_animal': 1800, 'yield_factor': 0.05},
    'cows': {'calories_per_animal': 200000, 'protein_per_animal': 5000, 'yield_factor': 0.02},
    'sheep': {'calories_per_animal': 45000, 'protein_per_animal': 1350, 'yield_factor': 0.03},
    'pigs': {'calories_per_animal': 120000, 'protein_per_animal': 3000, 'yield_factor': 0.04},
}