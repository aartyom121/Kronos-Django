from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

from news.models import Articles


def superuser_check(user):
    return user.is_superuser


def index(request):

    news = Articles.objects.order_by('-date')
    data = {
        'title': 'Главная страница',
        'news': news,
    }
    return render(request, 'main/index.html', data)


@user_passes_test(superuser_check)
@login_required
def for_admin(request):
    return render(request, 'main/for_admin.html')


def about(request):
    return render(request, 'main/about.html')


def i(request):
    return render(request, 'main/i.html')