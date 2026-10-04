"""
Задание 3. Агрегация.

Среди подозрительных событий засветилось несколько пользовательских ID.
Нужно понять, сколько их было, сколько уникальных и кто «наследил» больше
всех.
"""
from collections import Counter
from collections import defaultdict

def analyze_activity(user_ids: list[str]) -> tuple[dict[str, int], int, str]:
    """
    По списку user_ids (одно действие - один id пользователя в списке)
    вернуть кортеж из трёх элементов:

      1. словарь {user_id: количество действий этого пользователя};
      2. количество уникальных пользователей;
      3. id пользователя с наибольшим количеством действий.

    Если максимум количества действий делят несколько пользователей,
    вернуть того из них, кто раньше всех встретился в user_ids (по индексу
    первого появления в списке).

    Пример:
        analyze_activity(["a", "b", "a"]) -> ({"a": 2, "b": 1}, 2, "a")
    """
    # TODO: ваш код здесь
    users_count = defaultdict(int)
    max_activity = 0
    order = []

    for u in user_ids:
        users_count[u] += 1
        order.append(u)

        max_activity = max_activity if max_activity >= users_count[u] else users_count[u]

    max_activity_user = ""

    for u in order:
        if users_count[u] == max_activity:
            max_activity_user = u
            break

    return {u : c for u, c in users_count.items()}, len(users_count.keys()), max_activity_user



if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/task3_users.txt", encoding="utf-8") as f:
        user_ids = [line.strip() for line in f if line.strip()]

    counts, unique_count, top_user = analyze_activity(user_ids)
    print("Счётчики:", counts)
    print("Уникальных пользователей:", unique_count)
    print("Больше всего действий у:", top_user)
