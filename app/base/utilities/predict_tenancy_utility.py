from ..models import Tenancy
import joblib
from pathlib import Path
import pandas as pd

def load_model():
    model_path = Path(__file__).parent.parent.parent.parent / 'stacked_housing_model.joblib'
    return joblib.load(model_path)

def predict_tenancy_scores(profile_data):
    # Define features list matching the training data
    features = [
        'Age', 'Adults', 'Children', 'Rent', 'IsStudent',
        'Distance_to_New_Tenancy', 'Total_Rooms', 'Area_m2',
        'Hospital_distance', 'Gym_distance', 'School_distance',
        'Supermarket_distance', 'Distance_to_University'
    ]
    
    # Get all tenancies
    tenancies_queryset = Tenancy.objects.all()
    
    # Load model
    model = load_model()
    recommendations = []

    for tenancy in tenancies_queryset:
        # Prepare a feature row (profile_data merged with tenancy fields)
        feature_row = {
            "Age": profile_data.get("age"),
            "Adults": profile_data.get("number_of_adults"),
            "Children": profile_data.get("number_of_children"),
            "IsStudent": profile_data.get("is_student"),
            "Distance_to_New_Tenancy": 0.00, # to be calculated on the go
            "Rent": tenancy.rent_amount,  # from tenancy table
            "Total_Rooms": tenancy.total_rooms,
            "Area_m2": tenancy.size,
            "Hospital_distance": tenancy.hospital_distance,
            "Gym_distance": tenancy.gym_distance,
            "School_distance": tenancy.school_distance,
            "Supermarket_distance": tenancy.supermarket_distance,
            "Distance_to_University": tenancy.distance_to_university,
        }

        # Convert to DataFrame since model expects tabular format
        X_input = pd.DataFrame([feature_row], columns=features)

        # Predict score
        score = model.predict(X_input)[0]

        # Append recommendation entry
        recommendations.append({
            "title": tenancy.title,  # assuming you have a `title` field in Tenancy
            "description": tenancy.description,  # assuming `description`
            "price": f"DKK {tenancy.rent}/month",
            "address": tenancy.address,  # assuming `address`
            "rooms": f"{tenancy.total_rooms} rooms",
            "size": f"{tenancy.area_m2} sq meters",
            "recommendation": f"{min(100, max(0, round(score * 100)))}% relevant to your profile",
        })

    # Sort recommendations by score (descending)
    recommendations = sorted(recommendations, key=lambda x: int(x["recommendation"].replace("% relevant to your profile", "")), reverse=True)
    
    return recommendations