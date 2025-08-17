
# Bolig Recommendation System

This project is a Django-based web application for recommending housing tenancies based on user profiles and a trained machine learning model.

## Features
- User profile form for personalized recommendations
- Tenancy recommendation cards
- Machine learning model for tenancy prediction
- Data preparation and training notebooks

## Prerequisites
- Python 3.10+
- pip
- (Recommended) Virtual environment (venv)

## Setup Instructions

### 1. Clone the Repository
```powershell
git clone https://github.com/charankulal/Bolig-Recommendation.git
cd Bolig-Recommendation
```

### 2. Create and Activate Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install main requirements:
```powershell
pip install -r requirements.txt
```

### 4. Database Migration
Navigate to the `app` directory and run migrations:
```powershell
cd app
python manage.py migrate
```

### 5. Run the Development Server
```powershell
python manage.py runserver
```
Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Data Preparation & Model Training
- Data preparation scripts and notebooks are in `tenancy_data_preparation/` and `model_training/`.
- To retrain the model, use the Jupyter notebooks in `model_training/` and save the model as `stacked_housing_model.joblib` in the project root.

## Project Structure
- `app/` - Main Django project and app code
- `tenancy_data_preparation/` - Data scripts and JSON files
- `model_training/` - Jupyter notebooks and training data
- `stacked_housing_model.joblib` - Trained ML model

## Troubleshooting
- If you encounter missing packages, ensure all requirements are installed.
- For database issues, delete `db.sqlite3` and rerun migrations.

## License
MIT

## Contact
For questions, contact the maintainers
