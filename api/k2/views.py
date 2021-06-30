from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader
from django.views import View

import copy
import pandas as pd
import random
import os
print(os.getcwd())
data=pd.read_csv('k2/pokemon.csv')




# def top(request):
#     context={
#         'a_name':a_name,
#         'b_name':b_name
#     }
#     html=loader.render_to_string('k2/top.html',context=context,request=request)
#     return HttpResponse(html)



# a = random.randint(0, 150)
# b = random.randint(0, 150)
# while a == b:
#     b = random.randint(0, 150)
count=1
a_name_prev = ''
a_height_prev = ''
b_name_prev = ''
b_height_prev = ''

def top(request):
    global count
    global a_height_prev
    global b_height_prev
    global a_name_prev
    global b_name_prev

    userans = request.POST.get("userans", 999)


    restart = request.POST.get("restart",0)
    print(restart)
    if restart=="もう一度チャレンジ":
        count=1
        a_name_prev = ''
        a_height_prev = ''
        b_name_prev = ''
        b_height_prev = ''

    returntop = request.POST.get("returntop",0)
    print(returntop)
    if returntop=="TOP":
        count=1
        a_name_prev = ''
        a_height_prev = ''
        b_name_prev = ''
        b_height_prev = ''

    a = random.randint(0, 150)
    b = random.randint(0, 150)
    while a == b:
        b = random.randint(0, 150)

    a_name = data[data['No'] == a]['名前'].values[0]
    a_height = data[data['No'] == a]['高さ(m)'].values[0]
    b_name = data[data['No'] == b]['名前'].values[0]
    b_height = data[data['No'] == b]['高さ(m)'].values[0]

    a_name_prev_tmp = copy.copy(a_name_prev)
    b_name_prev_tmp = copy.copy(b_name_prev)
    a_height_prev_tmp = copy.copy(a_height_prev)
    b_height_prev_tmp = copy.copy(b_height_prev)

    dic = {
        "msg": userans,
        "count": count-1,
        "number": count,
        "result": count-2,
        'a_name': a_name,
        'b_name': b_name,
        'a_height': a_height,
        'b_height': b_height,
        'a_name_prev': a_name_prev_tmp,
        'b_name_prev': b_name_prev_tmp,
        'a_height_prev': a_height_prev_tmp,
        'b_height_prev': b_height_prev_tmp
    }

    if a_height_prev > b_height_prev:
        ans = 1
    elif a_height_prev < b_height_prev:
        ans = 2
    elif a_height_prev == b_height_prev:
        ans = 3

    a_name_prev = copy.copy(a_name)
    b_name_prev = copy.copy(b_name)
    a_height_prev = copy.copy(a_height)
    b_height_prev = copy.copy(b_height)

    if int(userans) == 999:
        count += 1
        return render(request, 'k2/top.html', dic)

    elif ans == int(userans):
        dic['check']='正解！！'
        print('count start')
        count += 1
        print('count end')
        return render(request, 'k2/at_least_one_ans.html', dic)
    else:
        if count<4:
            dic['rank'] = 'モンスターボール'
        elif count<7:
            dic['rank'] = 'スーパーボール'
        elif count<11:
            dic['rank'] = 'ハイパーボール'
        else:
            dic['rank'] = 'マスターボール'
        dic['check'] = '不正解'
        return render(request, 'k2/result.html', dic)


# def index(request):
    # return render(request, "k2/test.html")
    # return HttpResponse("Hello, world.")



def index(request):
    global count
    message = request.POST.get("userans", "World")
    dic = {
        "msg": message,
        "count": count
    }
    count += 1
    return render(request, 'k2/test.html', dic)


def about(request):
    return render(request, 'k2/about.html')