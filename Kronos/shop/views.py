from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from .models import Product, Category
from .forms import ProductsForm
from django.core.paginator import Paginator
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q


def superuser_check(user):
    return user.is_superuser


def shop_home(request):
    product = Product.objects.all()
    paginator = Paginator(product, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/shop_home.html', {'page_obj': page_obj, 'product': product})


class ShopDetailView(DetailView):
    model = Product
    template_name = 'shop/products_datails_view.html'
    context_object_name = 'products'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class ShopUpdateView(UpdateView):
    model = Product
    template_name = 'shop/products-update.html'
    form_class = ProductsForm


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class ShopDeleteView(DeleteView):
    model = Product
    template_name = 'shop/products-delete.html'

    success_url = '/shop/'


@user_passes_test(superuser_check)
@login_required
def create_products(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop_home')
        else:
            error = 'Форма заполнена неверно'

    form = ProductsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'shop/create_products.html', data)


class search(ListView):

    template_name = 'shop/shop_home.html'
    context_object_name = 'shop'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(Q(name__icontains=query) | Q(category__cat__icontains=query))
        else:
            return Product.objects.all()
        # return Product.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

