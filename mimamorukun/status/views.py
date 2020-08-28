from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member

# Create your views here.


def index(request):
    member = Member.objects.order_by('id')
    return render(request, 'status/index.html', {'member': member})

#**********************やっぱいる。　引数にpkないとダメ
def upd(request, pk):
    #pk(プライマリーキープライマリーキー)をもとに更新対象のMemberを取得、tにわたす。
    t = Member.objects.get(pk=pk)

    # workボタンがクリックされた場合の処理
    if 'work' in request.POST:
        if t.status_work:
            t.status_work = 'False'
        else:
            t.status_work = 'True'

    # homeボタンがクリックされた場合の処理
    if 'home' in request.POST:
        if t.status_home:
            t.status_home = 'False'
        else:
            t.status_home = 'True'

    # meetingボタンがクリックされた場合の処理
    if 'meeting' in request.POST:
        if t.status_meeting:
            t.status_meeting = 'False'
        else:
            t.status_meeting = 'True'

    # lunchボタンがクリックされた場合の処理
    if 'lunch' in request.POST:
        if t.status_lunch:
            t.status_lunch = 'False'
        else:
            t.status_lunch = 'True'

    #save()でDBに反映される。
    t.save()

    return redirect('status:index')
