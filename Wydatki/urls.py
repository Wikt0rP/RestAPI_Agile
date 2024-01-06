from django.contrib import admin
from django.urls import path
from Wydatki import views

urlpatterns = \
    [
        path('expense/create/', views.CreateExpense.as_view()),
        path('expense/list/', views.ExpenseList.as_view()),
        path('expense/delete/', views.DeleteExpense.as_view()),
    ]
