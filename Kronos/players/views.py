from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from .models import Players
from .forms import PlayersForm
from django.core.paginator import Paginator
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q

# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.
#
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "list.html", {"page_obj": page_obj})


def superuser_check(user):
    return user.is_superuser


def players_home(request):
    players = Players.objects.all()
    paginator = Paginator(players, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'players/players_home.html', {'page_obj': page_obj, 'players': players})


class PlayersDetailView(DetailView):
    model = Players
    template_name = 'players/players_datails_view.html'
    context_object_name = 'players'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class PlayersUpdateView(UpdateView):
    model = Players
    template_name = 'players/players-update.html'
    form_class = PlayersForm


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class PlayersDeleteView(DeleteView):
    model = Players
    template_name = 'players/players-delete.html'

    success_url = '/players/'


@user_passes_test(superuser_check)
@login_required
def create_players(request):
    error = ''
    if request.method == 'POST':
        form = PlayersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('players_home')
        else:
            error = 'Форма заполнена неверно'

    form = PlayersForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'players/create_players.html', data)


class search(ListView):

    template_name = 'players/players_home.html'
    context_object_name = 'players'
    paginate_by = 2

    # def get_queryset(self):
    #     return Players.objects.filter(name__icontains=self.request.GET.get('q'))
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Players.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
        else:
            return Players.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context