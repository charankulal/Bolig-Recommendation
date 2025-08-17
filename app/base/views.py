from django.http import JsonResponse
from django.shortcuts import render
from .forms import MyProfileForm
from .utilities.predict_tenancy_utility import predict_tenancy_scores
from django.views.decorators.csrf import csrf_exempt
from .models import Tenancy
import json
from .assets.data import addresses, universities
from .assets.profile_data import myprofiledata

def home(request):
    return render(request, "base/home.html")

def recommend_page(request):
    if request.method == 'POST':
        form = MyProfileForm(request.POST)
        if form.is_valid():
            return render(request, 'base/recommend.html', {'form': form, 'success': True})
    else:
        form = MyProfileForm()
    
    return render(request, 'base/recommend.html', {
        'form': form,
        'addresses': addresses,
        'universities': universities,
        'myprofiledata': myprofiledata,
    })

@csrf_exempt
def recommendations(request):
    if request.method == 'POST':
        inserted_tenancy_count = update_database()
        profile_data = request.POST
        all_tenancies = Tenancy.objects.all()
        try:
            tenancies = predict_tenancy_scores(profile_data, all_tenancies)

            for tenancy in tenancies:
                for key, value in tenancy.items():
                    if isinstance(value, set):
                        tenancy[key] = list(value)
            return JsonResponse({
                "tenancies": tenancies,
                "count_of_tenancies": inserted_tenancy_count
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)

def update_database():
    total_deleted, _ = Tenancy.objects.all().delete()

    with open("../tenancy_data_preparation/tenancies_with_distances.json", "r", encoding="utf-8") as f:
        data = json.load(f)


    tenancies_to_create = []
    for item in data:
        tenancies_to_create.append(
            Tenancy(
                name=item["name"],
                description=item.get("description", ""),
                rent_amount=item.get("rent"),
                size=item.get("size_sqm"),
                total_rooms=item.get("rooms"),
                address=item.get("address", ""),
                hospital_distance=item.get("distance_to_hospital"),
                gym_distance=item.get("distance_to_gym"),
                school_distance=item.get("distance_to_school"),
                supermarket_distance=item.get("distance_to_supermarket"),
                latitude=item.get("latitude"),
                longitude=item.get("longitude"),
            )
        )

    Tenancy.objects.bulk_create(tenancies_to_create)
    return len(tenancies_to_create)