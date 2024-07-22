from django.urls import path
from .views import TreeView, DepartmentDetailView

urlpatterns = [
    path('', TreeView.as_view(), name='tree'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
]
