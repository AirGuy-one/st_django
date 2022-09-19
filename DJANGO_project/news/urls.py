from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('test/', test),
    path('category/<int:category_id>', get_category, name='category_url'),
    path('add_news/', add_new_news, name='add_news_name'),
    path('add_category/', add_new_category, name='add_category_name'),
    path('settings/', settings_of_news, name='settings_url'),
    path('settings/delete_news/', delete_news_method, name='delete_news_name'),
    path('settings/delete_category/', delete_category_method, name='delete_category_name'),
]
