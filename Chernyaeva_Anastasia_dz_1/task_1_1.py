def convert_time(duration: int) -> str:
    if duration < 60:
        return (f'{duration} сек')
    else:
        min = duration // 60
        sec = duration % 60
        if min < 60:
            return (f'{min} мин {sec} сек')
        else:
            hour = min // 60
            min = min % 60
            if hour < 24:
                return (f'{hour} час {min} мин {sec} сек')
            else:
                day = hour // 24
                hour = hour % 24
                return (f'{day} дн {hour} час {min} мин {sec} сек')

duration = 400153
result = convert_time(duration)
print(result)



