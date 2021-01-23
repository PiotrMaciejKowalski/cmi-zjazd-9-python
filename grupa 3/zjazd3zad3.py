# Różnica czasu między Warszawą o Nowym Jorkiem wynosi 6 godzin, tzn. jeśli w Warszawie jest 18.00
# to w Nowym Jorku jest  dopiero 12.00.
#
# Napisz program, który dla podanego czasu w Warszawie obliczy czas w Nowym Jorku.

def warsaw_time_2_nyc_time(strtime : str):
    # jaki format czasu by chcieli podawać
    # 16:15 ->
    hour , minutes = strtime.split(':')
    hour, minutes = int(hour), int(minutes)
    if 0 <= hour <= 23 and 0 <= minutes <= 59:
        hour -= 6
        # jezeli godziny zawsze sa liczbami [0,..,23] -> zbiór reszt z dzielenia przez 24
        # reszta z dzielenia -5 przez 24 -> 19
        hour %= 24
        return f'{hour:02d}:{minutes:02d}'
    else:
        return 'Podano niepoprawna godzine'

print(warsaw_time_2_nyc_time('05:59'))

def warsaw_time_2_nyc_time_AM_PM(strtime : str):
    # jaki format czasu by chcieli podawać
    # 16:15 AM/PM->
    hm , ampm = strtime.split(" ")
    if ampm == 'AM' or ampm == 'PM':
        afternoon = 12 if ampm == 'PM' else 0
    else:
        return 'Niepoprawny format daty'

    hour , minutes = hm.split(':')
    hour, minutes = int(hour) + afternoon, int(minutes)
    if 0 <= hour <= 23 and 0 <= minutes <= 59:
        hour -= 6
        # jezeli godziny zawsze sa liczbami [0,..,23] -> zbiór reszt z dzielenia przez 24
        # reszta z dzielenia -5 przez 24 -> 19
        hour %= 24
        aft2 = "AM"
        if hour > 12:
            hour -= 12
            aft2 = "PM"
        elif hour == 0:
            hour = 12
            aft2 = "PM"
        return f'{hour:02d}:{minutes:02d} {aft2}'
    else:
        return 'Podano niepoprawna godzine'

print(warsaw_time_2_nyc_time_AM_PM('19:00 AM'))