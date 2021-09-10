# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите библиотеки

```bash
$ pip3 install -r requirements.txt
```

- Запустите сайт командой 

```bash
$ python3 main.py
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000). 

- На сайте буду отображены данные тестового каталога из файла `file_sample.xlsx`

## Как подставить свои данные

- Создайте Excel таблицу по образу и подобию `file_sample.xlsx`. При этом группировка товаров будет осуществлена по первому столбцу, для тестового каталога - это "Категория". Названия столбцов из образца менять нельзя.
- Измените значение константы `WINE_FILENAME` в модуле `main.py`, чтобы чтение данных было из вашего каталога. Сохраните файл `main.py` после изменения.
- Измените значение константы `FOUNDATION_YEAR` (дата основания компании), чтобы на главной странице корректно отображался возраст компании. Сохраните файл `main.py` после изменения.


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
