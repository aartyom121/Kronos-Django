from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def superuser_check(user):
    return user.is_superuser


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_datails_view.html'
    context_object_name = 'article'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/news-update.html'
    form_class = ArticlesForm


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


@user_passes_test(superuser_check)
@login_required
def create_news(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            article.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create_news.html', data)