import datetime

def get_sols_from_ls(ls: float):
    '''
    Функция вычисляет количество марсианских дней (sols) по solar longitude (ls)
    '''
    sector = int(ls / 30)
    # значения для вычислений взяты из таблички с сайта:
    # https://web.archive.org/web/20210222101952/http://www-mars.lmd.jussieu.fr/mars/time/solar_longitude.html
    match sector:
        case 0: # от 0 до 30 градусов
            sols = 61.2 * ls / 30
        case 1: # от 30 до 60 градусов
            sols = 61.2 + 65.4 * (ls - 30) / 30
        case 2:
            sols = 126.6 + 66.7 * (ls - 60) / 30
        case 3:
            sols = 193.3 + 64.5 * (ls - 90) / 30
        case 4:
            sols = 257.8 + 59.7 * (ls - 120) / 30
        case 5:
            sols = 317.5 + 54.4 * (ls - 150) / 30
        case 6:
            sols = 371.9 + 49.7 * (ls - 180) / 30
        case 7:
            sols = 421.6 + 46.9 * (ls - 210) / 30
        case 8:
            sols = 468.5 + 46.1 * (ls - 240) / 30
        case 9:
            sols = 514.6 + 47.4 * (ls - 270) / 30
        case 10:
            sols = 562.0 + 50.9 * (ls - 300) / 30
        case 11: # от 330 до 360 градусов
            sols = 612.9 + 55.7 * (ls - 330) / 30
            # ровно 360 градусов в датасете нет, поэтому case 12 невозможен
    return sols


def get_sols_from_year(martian_year: int) -> float:
    '''
    Функция вычисляет количество марсианских дней (sols) по марсианскому году
    '''
    return (martian_year - 1) * 668.6


def sols_to_days(sols: float) -> float:
    '''
    Конвертирует марсианские дни в земные
    соотношение сол/сутки = 1.0274912510
    источник: Википедия "Хронометрия на Марсе"
    '''
    return sols * 1.0274912510


def get_earth_date(ls: float, martian_year: int):
    '''
    Data set: https://zenodo.org/records/7082889
    Data Set S1 (spicam_obs.csv) 

    Функция принимает 2 значения, взятые из таблицы:
    ls - solar longitude -- положение Марса относительно Солнца в течение марсианского года
    martian_year -- марсианский год (687 земных дней)
    
    ls (float) может принимать значения от 0 до 360
    martian_year (int) может принимать значения от 1 (в текущем датасете от 27 до 35)

    функция переводит марсианский день в земной
    и возвращает кортеж: (day, month, year) 
    '''
    
    days_from_ls = sols_to_days(get_sols_from_ls(ls))
    days_from_year = sols_to_days(get_sols_from_year(martian_year))
    total_earth_days: int = round(days_from_ls + days_from_year)
    
    # 1 марсианский год начался 11 апреля 1955 по UTC
    start_date = datetime.date(1955, 4, 11)
    delta = datetime.timedelta(days=total_earth_days)

    result_date = start_date + delta
    return (result_date.day, result_date.month, result_date.year)


if __name__ == "__main__":
    # небольшой тест
    ls = float(input("ls: "))
    year = int(input("year: "))
    print(f"res: {get_earth_date(ls, year)}")
