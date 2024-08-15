from django.urls import path
from . import views

urlpatterns = [
    path('', views.tests_home, name='tests_home'),
    path('create_question', views.create_question, name='create_question'),
    path('create_test', views.create_test, name='create_test'),
    path('<int:pk>', views.TestDetailView.as_view(), name="test-detail"),
    path('question/<int:pk>/update', views.QuestionsUpdateView.as_view(), name="questions-update"),
    path('question/<int:pk>/delete', views.QuestionsDeleteView.as_view(), name="questions-delete"),
    path('test/<int:pk>/update', views.TestsUpdateView.as_view(), name="tests-update"),
    path('test/<int:pk>/delete', views.TestsDeleteView.as_view(), name="tests-delete"),
    path('save-results/', views.save_results, name='save-results'),

]