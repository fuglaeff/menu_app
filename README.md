# menu_app
 Project for hh.ru job vacancy

## Схема работы с базой данных:
 Предположим, что у нас N меню, тогда:
 1. Делаем 1 запрос, чтобы получить все имеющиеся меню (slug'и для template tag);
 2. Делаем N запросов, чтобы их заполнить.

## Проблема
 Для несуществующего id элемента меню, выводим первый уровень вложения для всех меню.
 В идеале хотелось бы бросать исключение в такой ситуации.