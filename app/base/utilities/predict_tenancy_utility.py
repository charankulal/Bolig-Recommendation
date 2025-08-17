from base.utilities.distance_calc_utility import haversine
import joblib
from pathlib import Path
import pandas as pd
import numpy as np

def load_model():
    model_path = Path(__file__).parent.parent.parent.parent / 'stacked_housing_model.joblib'
    return joblib.load(model_path)

def predict_tenancy_scores(profile_data, all_tenancies):
    all_tenancies = list(all_tenancies.values())
    
    if profile_data is None or not all_tenancies:
        return []
    
    is_student = profile_data.get("is_student") == "on"
    
    if is_student:
        university_lat = float(profile_data.get("university_latitude"))
        university_lon = float(profile_data.get("university_longitude"))
    
            
    current_lat = float(profile_data.get("address_latitude"))
    current_lon = float(profile_data.get("address_longitude"))
    
    features = [
        'Age', 'Adults', 'Children', 'Rent', 'IsStudent',
        'Distance_to_New_Tenancy', 'Total_Rooms', 'Area_m2',
        'Hospital_distance', 'Gym_distance', 'School_distance',
        'Supermarket_distance', 'Distance_to_University'
    ]
    
    # Load model
    model = load_model()
    recommendations = []

    for tenancy in all_tenancies:

        for key, value in tenancy.items():
            if isinstance(value, set):
                print(f"Found set in tenancy field {key}: {value}")
                tenancy[key] = list(value) 
        
        feature_row = {
            "Age": int(profile_data.get("age", 0)) or 0,
            "Adults": int(profile_data.get("number_of_adults", 0)) or 0,
            "Children": int(profile_data.get("number_of_children", 0)) or 0,
            "IsStudent": is_student,
            "Distance_to_New_Tenancy": haversine(current_lat, current_lon, float(tenancy.get("latitude")), float(tenancy.get("longitude"))) or np.nan,
            "Rent": float(tenancy.get("rent_amount", 0)) or 0,
            "Total_Rooms": int(tenancy.get("total_rooms", 0)) or 0,
            "Area_m2": float(tenancy.get("size", 0)) or 0,
            "Hospital_distance": round(float(tenancy.get("hospital_distance", 0)), 2) or 0,
            "Gym_distance": round(float(tenancy.get("gym_distance", 0)), 2) or 0,
            "School_distance": round(float(tenancy.get("school_distance", 0)), 2) or 0,
            "Supermarket_distance": round(float(tenancy.get("supermarket_distance", 0)), 2) or 0,
            "Distance_to_University": haversine(university_lat, university_lon, float(tenancy.get("latitude")), float(tenancy.get("longitude"))) if is_student else np.nan,
        }
        

        X_input = pd.DataFrame([feature_row], columns=features)
        score = model.predict(X_input)[0]
        
        recommendation = {
            "title": str(tenancy.get("name", "")), 
            "description": str(tenancy.get("description", "")),
            "price": f"DKK {tenancy.get('rent_amount', 0)}/month",
            "address": str(tenancy.get("address", "")),
            "rooms": f"{tenancy.get('total_rooms', 0)} rooms",
            "size": f"{tenancy.get('size', 0)} sq meters",
            "recommendation": min(100, max(0, round(score * 100))),
            "distace_to_new_tenancy": round(tenancy.get("distance_to_new_tenancy", 0), 2),
            "Hospital_distance": round(float(tenancy.get("hospital_distance", 0)), 2) or 0,
            "Gym_distance": round(float(tenancy.get("gym_distance", 0)), 2) or 0,
            "School_distance": round(float(tenancy.get("school_distance", 0)), 2) or 0,
            "Supermarket_distance": round(float(tenancy.get("supermarket_distance", 0)), 2) or 0,
            "Distance_to_University": round(float(tenancy.get("distance_to_university", 0)), 2) if tenancy.get("distance_to_university") is not None else 'N/A',
        }
        recommendations.append(recommendation)

    recommendations = sorted(
        recommendations,
        key=lambda x: x["recommendation"],
        reverse=True
    )
    
    return recommendations