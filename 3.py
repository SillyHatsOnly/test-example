'''
Мы сохраняем время присутствия каждого пользователя на уроке  виде интервалов. В функцию передается словарь,
содержащий три списка с таймстемпами (время в секундах):
— lesson – начало и конец урока 
— pupil – интервалы присутствия ученика 
— tutor – интервалы присутствия учителя 
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами
(начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия
ученика и учителя на уроке (в секундах). 

Будет плюсом: Написать WEB API с единственным endpoint’ом для вызова этой функции.
'''

from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/', methods=['POST'])
def data():
    if not request.is_json:
        abort(400)
    if 'data' not in request.json:
        return {
            'status': 'error',
            'message': 'missing data'
            }
    answer = appearance(request.json['data'])
    return {
        'answer': answer,
        }

def appearance(ntr):
    l = ntr['lesson']
    p = sorted(groupn(ntr['pupil'], 2))
    t = sorted(groupn(ntr['tutor'], 2))
    x_l, y_l = l
    result = 0
    for p_tuples in p:
        x_p,y_p = p_tuples
        for t_tuples in t:
            x_t,y_t = t_tuples
            if x_t in range(x_p, y_p+1) or x_p in range(x_t, y_t+1):
                x = max(x_l, x_p, x_t)
                y = min(y_l, y_p, y_t)
                result += y - x
    return result

def groupn(list, n):
    groups = []
    for x in range(0, len(list), n):
        groups.append(list[x:x+n])
    return groups
