from collections import defaultdict
from typing import Any

from django import template

from menu_items.models import MenuItem

register = template.Library()


@register.filter(name='get')
def get(value: dict[str, Any], arg: str) -> Any:
    return value.get(arg, [])


@register.inclusion_tag('menu_tree.html', takes_context=True)
def draw_menu(context, menu_slug):
    menu_item_id = context.get('menu_item_id')
    if menu_item_id is None:
        menu_items = MenuItem.objects.filter(parent_id=menu_item_id, menu=menu_slug).all()
    else:
        menu_items = MenuItem.objects.raw(
            '''
            WITH RECURSIVE menu_item_ids AS (
                SELECT mi.id
                    FROM menu_items_menuitem AS mi
                    WHERE mi.id = %s AND mi.menu_id = %s
                UNION ALL
                SELECT mi2.id
                    FROM menu_items_menuitem AS mi1
                    JOIN menu_item_ids AS mii ON mii.id = mi1.id
                    JOIN menu_items_menuitem AS mi2 ON mi1.parent_id = mi2.id
            )
            SELECT DISTINCT mi.*, mi.parent_id AS parent_id
                FROM menu_items_menuitem AS mi
                LEFT JOIN menu_item_ids AS mii ON mi.parent_id = mii.id
                WHERE mi.parent_id IS NULL AND mi.menu_id = %s OR mii.id IS NOT NULL
            ''',
            (menu_item_id, menu_slug, menu_slug)
        )

    menu_tree_dict = defaultdict(list)
    for item in menu_items:
        if getattr(item, 'parent_id', None) is None:
            parent_id = -1
        else:
            parent_id = item.parent_id

        menu_tree_dict[parent_id].append(item)

    return {
        'menu_tree_dict': menu_tree_dict,
        'selected_item_id': menu_item_id,
        'parent': -1,
    }
