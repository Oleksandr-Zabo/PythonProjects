from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Crismastree, CrismasTreeLike

def winner_crismastree(request):
    trees = Crismastree.objects.all()
    winner = None
    if trees.exists():
        winner = max(trees, key=lambda t: t.likes_count())
    return render(request, 'crismastree_2026/winner.html', {
        'winner': winner
    })

def new_crismastree_list(request):
    new_list = Crismastree.objects.all().order_by('-created_at')
    return render(request, 'crismastree_2026/new_crismastree_list.html', {
        'new_list': new_list
    })

def cristmas_tree_details(request, id):
    crismastree = get_object_or_404(Crismastree, id=id)
    return render(request, 'crismastree_2026/cristmas_tree_details.html', {
        'crismastree': crismastree
    })

@login_required
def like_crismastree(request, id):
    tree = get_object_or_404(Crismastree, id=id)
    # створюємо лайк, якщо його ще немає
    CrismasTreeLike.objects.get_or_create(crismastree=tree, user=request.user)
    return redirect('new_crismastree_list')
