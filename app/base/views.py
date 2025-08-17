from django.http import JsonResponse
from django.shortcuts import render
from .forms import MyProfileForm
from .utilities.maps_utility import get_address_suggestions
from .utilities.predict_tenancy_utility import predict_tenancy_scores
from django.views.decorators.csrf import csrf_exempt

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
        'form': form
    })

def address_autocomplete(request):
    query = request.GET.get('query', '')
    country_code = request.GET.get('country_code', 'dk')
    suggestions = get_address_suggestions(query, country_code=country_code)
    return JsonResponse({'suggestions': suggestions})

@csrf_exempt
def recommendations(request):
    if request.method == 'POST':
        data = request.POST
        try:
            tenancies = predict_tenancy_scores(data)
            return JsonResponse({"tenancies": tenancies})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)