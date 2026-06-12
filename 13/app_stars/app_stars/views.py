from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import FeedbackForm
from .forms import BookReviewForm
from .forms import PersonSearchForm

def home_view(request):
    return render(request, "app_stars/home.html")

#1
def feedback_view(request):
    formatted_data = None
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            formatted_data = {
                "nickname": data["nickname"],
                "email": data["email"],
                "stars": data["stars"],
                "experience": data["experience"]
            }
    else:
        form = FeedbackForm()

    return render(request, "app_stars/feedback.html", {
        "form": form,
        "formatted_data": formatted_data
    })#1

#2



def book_review_view(request):
    formatted_data = None
    if request.method == "POST":
        form = BookReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            formatted_data = {
                "nickname": data["nickname"],
                "rating": data["rating"],
                "review": data["review"],
                "contains_spoilers": data["contains_spoilers"]
            }
    else:
        form = BookReviewForm()

    return render(request, "app_stars/book_review.html", {
        "form": form,
        "formatted_data": formatted_data
    })

#3


# Для прикладу використаємо список словників як "базу даних"
PEOPLE = [
    {"name": f"Person {i}", "city": "Vinnytsia", "info": f"Info about Person {i}"}
    for i in range(1, 51)
]

def person_search_view(request):
    results = []
    formatted_data = None

    if request.method == "POST":
        form = PersonSearchForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            city = form.cleaned_data["city"]

            # Фільтрація даних
            results = [p for p in PEOPLE if city.lower() in p["city"].lower()]

            # Пагінація (по 10 елементів)
            paginator = Paginator(results, 10)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

            formatted_data = page_obj
    else:
        form = PersonSearchForm()

    return render(request, "app_stars/person_search.html", {
        "form": form,
        "formatted_data": formatted_data
    })