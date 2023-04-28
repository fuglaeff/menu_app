from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

from .models import Menu


class MenuItemsPageView(View):
    def get(self, request: HttpRequest, menu_item_id: str | None = None) -> HttpResponse:
        """
        Render page with tree menu structure.
        """
        if menu_item_id is not None:
            menu_item_id = int(menu_item_id)

        menus = Menu.objects.all()
        context = {
            'menu_item_id': menu_item_id,
            'menus': menus,
        }
        return render(request, 'menu_page.html', context)
