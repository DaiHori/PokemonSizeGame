from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader
from django.views import View

import pandas as pd
import random
data=pd.read_csv('pokemon.csv')
score = 0
print('身長高いのはどっち？')

a = random.randint(0, 150)
b = random.randint(0, 150)
while a == b:
    b = random.randint(0, 150)

a_name = data[data['No'] == a]['名前'].values[0]
# a_height = data[data['No'] == a]['高さ(m)'].values[0]
b_name = data[data['No'] == b]['名前'].values[0]
# b_height = data[data['No'] == b]['高さ(m)'].values[0]

# while True:
#     a = random.randint(0, 150)
#     b = random.randint(0, 150)
#     while a == b:
#         b = random.randint(0, 150)
#
#     a_name = data[data['No'] == a]['名前'].values[0]
#     a_height = data[data['No'] == a]['高さ(m)'].values[0]
#     b_name = data[data['No'] == b]['名前'].values[0]
#     b_height = data[data['No'] == b]['高さ(m)'].values[0]
#
#     if a_height > b_height:
#         ans = 1
#     elif a_height < b_height:
#         ans = 2
#     elif a_height == b_height:
#         ans = 3
#
#     print('------')
#     print(f'1:{a_name}')
#     print(f'2:{b_name}')
#     print('------')
#     #     print(f'3:同じ大きさ')
#     print('')
#     print('↓↓数字を入力↓↓（※高さが同じ場合は「0」）')
#     user = input()
#     print('------')
#     if ans != int(user):
#         print('')
#         print('不正解(; ･`д･´)')
#         print('------')
#         print(f'1:{a_name} {a_height}cm')
#         print(f'2:{b_name} {b_height}cm')
#         print('------')
#
#         print(f'連続正解数{score}')
#         break
#
#     print('正解')
#     print('')
#     score += 1



def top(request):
    context={
        'a_name':a_name,
        'b_name':b_name
    }
    html=loader.render_to_string('k2/top.html',context=context,request=request)
    return HttpResponse(html)


def resume(request):
    return HttpResponse('職務履歴です。')