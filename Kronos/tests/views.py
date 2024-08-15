from random import shuffle

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator

from .models import Test, Question, Results
from .forms import QuestionsForm, TestsForm
from django.core.paginator import Paginator
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q
from django.db import IntegrityError


def tests_home(request):
    tests = Test.objects.all()
    return render(request, 'tests/tests_home.html', {'tests': tests})


def superuser_check(user):
    return user.is_superuser


class TestDetailView(DetailView):
    model = Test
    template_name = 'tests/tests_datails_view.html'
    context_object_name = 'test'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = self.get_object()
        questions = test.question_set.all()
        for question in questions:
            answers = [question.cor_ans, question.uncor_ans1, question.uncor_ans2, question.uncor_ans3]
            shuffle(answers)
            question.answers = answers
        context['questions'] = questions
        return context


#
#
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class QuestionsUpdateView(UpdateView):
    model = Question
    template_name = 'tests/questions-update.html'
    form_class = QuestionsForm

    success_url = '/tests/'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class QuestionsDeleteView(DeleteView):
    model = Question
    template_name = 'tests/questions-delete.html'

    success_url = '/tests/'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class TestsUpdateView(UpdateView):
    model = Test
    template_name = 'tests/tests-update.html'
    form_class = TestsForm


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(superuser_check), name='dispatch')
class TestsDeleteView(DeleteView):
    model = Test
    template_name = 'tests/tests-delete.html'

    success_url = '/tests/'


@user_passes_test(superuser_check)
@login_required
def create_question(request):
    error = ''
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tests_home')
        else:
            error = 'Форма заполнена неверно'

    form = QuestionsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tests/create_question.html', data)


@user_passes_test(superuser_check)
@login_required
def create_test(request):
    error = ''
    if request.method == 'POST':
        form = TestsForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.created_by = request.user
            test.save()
            return redirect('tests_home')
        else:
            error = 'Форма заполнена неверно'

    form = TestsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tests/create_test.html', data)


def get_question_by_id(question_id):
    try:
        question = Question.objects.get(id=question_id)
        return question
    except Question.DoesNotExist:
        return None


def save_results(request):
    if request.method == 'POST':
        user = request.user
        test_name = None

        results = Results(user=user, test_name=test_name)

        # print(request.POST)
        ans = list(request.POST.items())
        test_name = get_question_by_id(ans[2][0]).test_number
        # print(test_name)
        cor_ans = Question.objects.filter(test_number=test_name).values_list('cor_ans', flat=True)
        # print("test_name", test_name, "cor_ans", cor_ans)
        q_numb = 1
        cor_ans_pointer = 0

        for question in request.POST:
            if question.isdigit():
                selected_answer = request.POST.get(question)
                print(selected_answer)
                print(cor_ans[cor_ans_pointer])
                if selected_answer == cor_ans[cor_ans_pointer]:
                    setattr(results, f'res{q_numb}', 1)
                else:
                    setattr(results, f'res{q_numb}', 0)
                setattr(results, f'ans{q_numb}', selected_answer)
                if not test_name:
                    test_name = get_question_by_id(question).test_number
                    print(test_name)
                q_numb += 1
                cor_ans_pointer += 1

        results.test_name = test_name
        results.save()

        return redirect('UserProfile')

    return redirect('tests_home')

# class search(ListView):
#
#     template_name = 'players/players_home.html'
#     context_object_name = 'players'
#     paginate_by = 2
#
#     # def get_queryset(self):
#     #     return Players.objects.filter(name__icontains=self.request.GET.get('q'))
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             return Players.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
#         else:
#             return Players.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['q'] = self.request.GET.get('q')
#         return context
