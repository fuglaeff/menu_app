from django.urls import re_path

from .views import MenuItemsPageView

app_name = 'menu_items'

urlpatterns = [
    re_path(r'^(?P<menu_item_id>[0-9]+)?$', MenuItemsPageView.as_view(), name='menu_item'),
]
