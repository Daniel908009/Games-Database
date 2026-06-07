from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, ProfileUpdateForm, RegisterForm, ReviewForm, SearchForm
from .models import Game, Review, Studio, UserProfile


def home(request):
    query = request.GET.get('q', '').strip()
    games = Game.objects.select_related('genre', 'studio').prefetch_related('platforms').order_by('title')
    if query:
        games = games.filter(Q(title__icontains=query) | Q(studio__name__icontains=query) | Q(genre__name__icontains=query))
    return render(request, 'home.html', {
        'games': games,
        'search_form': SearchForm(initial={'q': query}),
        'query': query,
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('games:profile')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('games:profile')
    else:
        form = LoginForm(request)

    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user)
            messages.success(request, 'Account created. You can now log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('games:profile')
    else:
        form = ProfileUpdateForm(instance=profile, user=request.user)

    return render(request, 'registration/profile.html', {
        'profile': profile,
        'form': form,
        'user_reviews': request.user.reviews.select_related('game').order_by('-created_at'),
    })


def user_profile(request, username):
    profile = get_object_or_404(UserProfile.objects.select_related('user'), user__username=username)
    reviews = Review.objects.filter(author=profile.user).select_related('game', 'game__studio').order_by('-created_at')
    return render(request, 'profile_detail.html', {'profile': profile, 'reviews': reviews})


def game_detail(request, pk):
    game = get_object_or_404(
        Game.objects.select_related('genre', 'studio').prefetch_related('platforms', 'reviews__author__profile'),
        pk=pk,
    )
    reviews = game.reviews.select_related('author', 'author__profile').order_by('-created_at')
    review_form = ReviewForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.game = game
            review.save()
            messages.success(request, 'Your review has been posted.')
            return redirect('games:game_detail', pk=game.pk)

    return render(request, 'game_detail.html', {
        'game': game,
        'reviews': reviews,
        'review_form': review_form,
    })


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review.objects.select_related('game', 'author'), pk=pk)

    if request.method != 'POST':
        return redirect('games:game_detail', pk=review.game.pk)

    if not (request.user.is_superuser or review.author_id == request.user.id):
        messages.error(request, 'You can only delete your own reviews.')
        next_url = request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('games:game_detail', pk=review.game.pk)

    game_pk = review.game.pk
    review.delete()
    messages.success(request, 'Review deleted successfully.')

    next_url = request.POST.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('games:game_detail', pk=game_pk)


def studios(request):
    query = request.GET.get('q', '').strip()
    studios = Studio.objects.prefetch_related('game_set').order_by('name')
    if query:
        studios = studios.filter(Q(name__icontains=query) | Q(country__icontains=query))
    return render(request, 'studio_list.html', {
        'studios': studios,
        'search_form': SearchForm(initial={'q': query}),
        'query': query,
    })


def studio_detail(request, pk):
    studio = get_object_or_404(Studio.objects.prefetch_related('game_set__genre', 'game_set__platforms'), pk=pk)
    games = studio.game_set.all().order_by('title')
    return render(request, 'studio_detail.html', {'studio': studio, 'games': games})


def search(request):
    form = SearchForm(request.GET or None)
    query = ''
    games = []
    studios = []
    users = []

    if form.is_valid():
        query = form.cleaned_data['q'].strip()
        if query:
            games = Game.objects.select_related('genre', 'studio').filter(
                Q(title__icontains=query) | Q(studio__name__icontains=query) | Q(genre__name__icontains=query)
            ).order_by('title')
            studios = Studio.objects.filter(Q(name__icontains=query) | Q(country__icontains=query)).order_by('name')
            users = UserProfile.objects.select_related('user').filter(
                Q(user__username__icontains=query)
                | Q(display_name__icontains=query)
                | Q(public_handle__icontains=query)
            ).order_by('display_name')

    return render(request, 'search_results.html', {
        'form': form,
        'query': query,
        'games': games,
        'studios': studios,
        'users': users,
    })
