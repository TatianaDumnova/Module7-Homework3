# Напишите код, который форматирует строки для следующих сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:
#
# Использование %:
# Переменные: количество участников первой команды (team1_num).
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "

team1_num = 5
print('В команде Мастера кода участников: %d !' % team1_num)
#
# Переменные: количество участников в обеих командах (team1_num, team2_num).
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
team2_num = 6
print('В команде Волшебники данных участников: %d !' % team2_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))
#
# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
score1 = 40
score2 = 42
print('Команда Мастера кода решила задач: {0} !'.format(score1))
print('Команда Волшебники данных решила задач: {0} !'.format(score2))

#
# Переменные: время за которое команда 2 решила задачи (team1_time).
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
team1_time = 1552.512
team2_time = 2153.31451
print('Мастера кода решили задачи за {0} с !'.format(team1_time))
print('Волшебники данных решили задачи за {0} с !'.format(team2_time))
#
# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
print(f'Команды решили {score1} и {score2} задач.')

# Переменные: исход соревнования (challenge_result).
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
if team1_time < team2_time and score1 > score2 or score1 == score2:
    challenge_result = 'Победа команды Мастера кода!'
elif team2_time < team1_time and score1 < score2 or score1 == score2:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')
#
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
#
tasks_total = score1 + score2
time_avg = round((team1_time + team2_time) / tasks_total, 2)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')

# Комментарии к заданию:

# Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать. Например, для challenge_result:
# if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
# result = ‘Победа команды Мастера кода!’
# elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
# result = ‘Победа команды Волшебники Данных!’ else:
# result = ‘Ничья!’
#
# Пример входных данных
# team1_num = 6 team2_num = 6
# score1 = 40
# score2 = 42
# team1_time = 1552.512 team2_time = 2153.31451 tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'
