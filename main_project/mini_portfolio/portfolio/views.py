from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import markdown
from django.utils.safestring import mark_safe

from .models import Project, DeleteRequest
from .forms import ProjectForm
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import UserProfile


'''Домашня сторінка'''
def home_view(request):
    return render(request, "portfolio/home.html")


'''Реєстрація'''
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("project_list")
    else:
        form = UserCreationForm()
    return render(request, "portfolio/register.html", {"form": form})


'''Вхід'''
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("project_list")
    else:
        form = AuthenticationForm()
    return render(request, "portfolio/login.html", {"form": form})


'''Вихід'''
def logout_view(request):
    logout(request)
    return redirect("login")


'''Список проєктів з пагінацією'''
def project_list(request):
    projects = Project.objects.all().order_by("-created_at")
    paginator = Paginator(projects, 3)  # 3 карток на сторінку
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "portfolio/project_list.html", {"page_obj": page_obj})


'''Додати проєкт (тільки авторизованим)'''
@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user

            if form.cleaned_data["description_source"] == "markdown" and request.FILES.get("markdown_file"):
                md_file = request.FILES["markdown_file"]
                content = md_file.read().decode("utf-8")
                # беремо увесь текст як опис
                project.description = content.strip()

            project.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "portfolio/add_project.html", {"form": form})





'''Перегляд картки проєкту'''
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.description:
        project.description_html = mark_safe(
            markdown.markdown(project.description, extensions=["fenced_code", "tables"])
        )
    else:
        project.description_html = None

    return render(request, "portfolio/project_detail.html", {"project": project})



'''Запит на видалення'''
@login_required
def delete_request_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        reason = request.POST.get("reason")
        DeleteRequest.objects.create(project=project, user=request.user, reason=reason)
        return redirect("project_list")
    return render(request, "portfolio/delete_request.html", {"project": project})


'''Telegram з'єднання'''
@csrf_exempt
def connect_telegram(request):
    if request.method == "POST":
        data = json.loads(request.body)
        telegram_id = data.get("telegram_id")
        username = data.get("username")

        try:
            user = User.objects.get(username=username)
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.telegram_id = telegram_id
            profile.save()
            return JsonResponse({"status": "ok"})
        except User.DoesNotExist:
            return JsonResponse({"status": "error", "message": "User not found"})
    return render(request, "portfolio/connect_telegram.html")


'''API: Отримати проєкти користувача'''
@csrf_exempt
def api_user_projects(request, username):
    try:
        user = User.objects.get(username=username)
        projects = Project.objects.filter(author=user).order_by("-created_at")
        projects_data = [
            {
                "title": project.title,
                "description": project.description,
                "link": project.link,
                "created_at": project.created_at.strftime("%Y-%m-%d %H:%M")
            }
            for project in projects
        ]
        return JsonResponse(projects_data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


'''API: Отримати запити на видалення'''
@csrf_exempt
def api_delete_requests(request):
    requests_data = DeleteRequest.objects.filter(status="pending").order_by("-created_at")
    requests_list = [
        {
            "project_title": req.project.title,
            "user_username": req.user.username,
            "reason": req.reason,
            "created_at": req.created_at.strftime("%Y-%m-%d %H:%M")
        }
        for req in requests_data
    ]
    return JsonResponse(requests_list, safe=False)
