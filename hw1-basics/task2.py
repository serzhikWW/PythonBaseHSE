"""
Задание 2. Парсинг лога.

В расшифрованном в задании 1 отчёте указано, для какого пользователя и с
какого времени искать подозрительную активность. Нужно найти в логе все
события этого пользователя, случившиеся строго позже указанного времени.
"""

def parse_date(date: str) -> tuple[int, int]:
    hour, minutes = map(int, date.split(':'))
    return (hour, minutes)

def compare_dates(date1 : tuple[int, int], date2 : tuple[int, int]) -> bool:
    hour1, minutes1 = date1
    hour2, minutes2 = date2
    if hour2 < hour1:
        return False
    else:
        if hour1 == hour2:
            return minutes1 <= minutes2
        else:
            return True

def filter_events_after(log_lines: list[str], user: str, after_time: str) -> list[str]:
    """
    Вернуть строки лога log_lines, относящиеся к пользователю user, время
    которых строго позже after_time.

    Формат каждой строки лога: "<время> <пользователь> <событие>",
    например "19:05 alice export". Время - часы:минуты в 24-часовом
    формате; часы могут быть записаны без ведущего нуля (например, "9:05").

    Порядок строк в результате должен совпадать с их порядком во входных
    данных log_lines.

    Пример:
        filter_events_after(["10:00 alice login", "14:30 alice click"], "alice", "12:00")
        -> ["14:30 alice click"]
    """
    # TODO: ваш код здесь
    min_time = parse_date(after_time)
    target_user_actions = []

    for line in log_lines:
        str_time, user_name, action = line.split(' ')
        if user_name == user:
            cur_time = parse_date(str_time)
            if compare_dates(min_time, cur_time):
                target_user_actions.append(line)

    return target_user_actions


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/task2_log.txt", encoding="utf-8") as f:
        log_lines = [line.strip() for line in f if line.strip()]

    result = filter_events_after(log_lines, "mktbot7", "19:00")
    print(result)

    # print(filter_events_after(log_lines, "carol", "09:09"))