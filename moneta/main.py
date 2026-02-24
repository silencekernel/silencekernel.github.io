#     __  ___                 __       
#    /  |/  /___  ____  ___  / /_____ _
#   / /|_/ / __ \/ __ \/ _ \/ __/ __ `/
#  / /  / / /_/ / / / /  __/ /_/ /_/ / 
# /_/  /_/\____/_/ /_/\___/\__/\__,_/  
# Moneta (v1.0)
# Intelligent Iranian Banknote Recognition System
# Moneta project team: Amirmohammad Piri
import cv2
import math
import numpy as np
# Configuration variables:
samples_folder = 'samples/'  # Relative or absolute address of the 6 Sample Money folder
image_path = 'test.jpg'  # Relative or absolute address of the test image
money_types = {
    'sample500irt.jpg': {'value': 500},
    'sample1000irt.jpg': {'value': 1000},
    'sample1000irtv2.jpg': {'value': 1000},
    'sample2000irt.jpg': {'value': 2000},
    'sample5000irt.jpg': {'value': 5000},
    'sample10000irt.jpg': {'value': 10000},
}
def find_dominant_color(image_path):
    img = cv2.imread(image_path)
    avg_color = np.mean(img, axis=(0, 1))
    return tuple(avg_color.astype(int))
def color_distance(color1, color2):
    b1, g1, r1 = color1
    b2, g2, r2 = color2
    diff_b = b1 - b2
    diff_g = g1 - g2
    diff_r = r1 - r2
    distance = math.sqrt(diff_b**2 + diff_g**2 + diff_r**2)
    return distance
this_dominant_color = find_dominant_color(image_path)
for image, money in money_types.items():
    dominant_color = find_dominant_color(samples_folder + image)
    distance = color_distance(dominant_color, this_dominant_color)
    money['difference'] = distance
closest_money = min(money_types.items(), key=lambda x: x[1]['difference'])
closest_value = closest_money[1]['value']
print(f'{closest_value} Tomans!')
# Proprietary and Confidential: Unauthorized copying, distribution, or modification strictly prohibited.
# Copyright (c) 2026 Moneta Project
# All rights reserved.
