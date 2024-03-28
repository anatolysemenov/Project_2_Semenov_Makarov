## Модуль для конвертации марсианских дней в земные
Проект выполнен по набору данных ["Nine Martian Years of polar caps observations by SPICAM-IR" (Data Set S1)](https://zenodo.org/records/7082889).


Реализована функция для вычисления даты на Земле с помощью данных о положении Марса из таблицы *(Марсианский год, гелиоцентрическая долгота ls)*.

Воспроизводена работа данного конвертера:
[Mars Date (Year and Solar Longitude) to Earth Date Conversion](https://www-mars.lmd.jussieu.fr/mars/time/mars_date_to_earth_date.html)

---

### Установка и работа с модулем
Для работы с модулем скачайте файл `sol_converter.py`. Установка дополнительных зависимостей не требуется.

Функция `get_earth_date` принимает 2 значения из таблицы `spicam_obs.csv`: **ls** (float) и **martian_year** (int). Таблица скачивается с [сайта с набором данных](https://zenodo.org/records/7082889).

Файл `test_module.ipynb` демонстрирует работу модуля. Взаимодействие с таблицей происходит через библиотеку **Pandas**.

---

### Изученные материалы по теме:
- ["Solar longtitude"](https://en.wikipedia.org/wiki/Solar_longitude)
- ["Хронометрия на Марсе"](https://w.wiki/9aRc)
- ["Mars' calendar"](https://www.planetary.org/articles/mars-calendar)
- ["Mars24 Sunclock — Time on Mars"](https://www.giss.nasa.gov/tools/mars24/help/algorithm.html)
- [Mars converter](https://pss-gitlab.math.univ-paris-diderot.fr/sainton/marsconverter)
---
**Выполнили**:
