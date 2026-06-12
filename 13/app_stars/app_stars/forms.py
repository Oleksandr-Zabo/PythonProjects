from django import forms

#1
class FeedbackForm(forms.Form):
    nickname = forms.CharField(label="Нік", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    stars = forms.ChoiceField(
        label="Кількість зірочок",
        choices=[(i, str(i)) for i in range(1, 6)],
        required=True
    )
    experience = forms.CharField(
        label="Опис досвіду",
        widget=forms.Textarea,
        required=True,
        min_length=10
    )

#2

class BookReviewForm(forms.Form):
    nickname = forms.CharField(label="Нік", max_length=50, required=True)
    rating = forms.IntegerField(
        label="Ваш рейтинг книги (0–100)",
        min_value=0,
        max_value=100,
        required=True
    )
    review = forms.CharField(
        label="Рецензія",
        widget=forms.Textarea,
        required=True,
        min_length=20
    )
    contains_spoilers = forms.BooleanField(
        label="Містить спойлери?",
        required=False
    )

#3

class PersonSearchForm(forms.Form):
    full_name = forms.CharField(label="ПІБ", max_length=100, required=True)
    city = forms.CharField(label="Місто", max_length=100, required=True)
