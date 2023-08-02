from django.urls import path
from .views import index,get_all,get_by_index

urlpatterns = [
    path('',index),
    path('all/',get_all),
    path('<int:question_id>',get_by_index)
]