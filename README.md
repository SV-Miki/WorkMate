# Workmate: Анализ рейтинга брендов

Консольное приложение на Python для анализа CSV-файлов с рейтингами товаров.  
Скрипт формирует отчёт `average-rating`, показывающий средний рейтинг бренда, отсортированный по убыванию.

---

## Структура проекта

```
Workmate_rating/
├──workmate_rating/
│    ├── examples/
│    │   ├── products1.csv
│    │   └── products2.csv
│    ├── tests/
│    │   ├── test_average_rating.py
│    │   ├── test_loader.py
│    │   └── test_main.py
│    ├── workmate_rating/
│    │   ├── reports/
│    │   │   ├── __init__.py
│    │   │   ├── average_rating.py
│    │   │   └── base.py
│    │   ├── __init__.py
│    │   ├── loader.py
     ├── __init__.py
│    └── main.py
├── .gitignore
├── README.md
└── requirements.txt
```

⸻

Примеры CSV-файлов

***examples/products1.csv***

```
name	brand	price	rating
iphone 15 pro	apple	999	4.9
galaxy s23 ultra	samsung	1199	4.8
redmi note 12	xiaomi	199	4.6
iphone 14	apple	799	4.7
galaxy a54	samsung	349	4.2
```

***examples/products2.csv***

```
name	brand	price	rating
poco x5 pro	xiaomi	299	4.4
iphone se	apple	429	4.1
galaxy z flip 5	samsung	999	4.6
redmi 10c	xiaomi	149	4.1
iphone 13 mini	apple	599	4.5
```

⸻

## Запуск скрипта и результаты

### Обработка двух файлов одновременно

```commandline
python -m workmate_rating.main --files workmate_rating/examples/products1.csv workmate_rating/examples/products2.csv --report average-rating
```
Результат:

|    | brand   |   rating |
|----|---------|----------|
|  1 | apple   |     4.55 |
|  2 | samsung |     4.53 |
|  3 | xiaomi  |     4.37 |


⸻

### Обработка одного файла - products1

```commandline
python -m workmate_rating.main --files workmate_rating/examples/products1.csv --report average-rating
```


Результат:

|    | brand   | rating |
|----|---------|--------|
|  1 | apple   | 4.8    |
|  2 | samsung | 4.6    |
|  3 | xiaomi  | 4.5    |

⸻

### Ошибка: отсутствующий файл

```commandline
python -m  workmate_rating.main --files workmate_rating/examples/non_existent.csv  --report average-rating
```

Результат:

`Ошибка: Файл не найден по пути 'workmate_rating/examples/non_existent.csv'`

⸻
### Ошибка: неизвестный отчет

```commandline
python -m  workmate_rating.main --files workmate_rating/examples/products2.csv  --report average-potke 
```

Результат:

`Неизвестный отчет: average-potke
 Доступные отчеты: average-rating
`

⸻
## Тестирование
`python -m pytest -v`
`python -m pytest --cov=workmate_rating`

⸻
## Расширение функционала

Чтобы создать новый отчет, например, `average-price`:
1.  Создайте файл `workmate_rating/reports/average_price.py`.
2.  В нем создайте класс `AveragePriceReport`, унаследовав его от `base.Report`.
3.  Задайте `name = "average-price"` и реализуйте метод `generate()`, который будет вычислять среднюю цену по брендам.
4.  Зарегистрируйте новый отчет в `workmate_rating/reports/__init__.py`, добавив его в словарь `REPORTS`.

После этого новый отчет можно запускать через main.py так же, как и average-rating.
