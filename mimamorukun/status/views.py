from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.utils import timezone

#ログインユーザーのプライマリーキー 　グローバル変数として宣言するとどのメソッドでも共通して使える。
global user_pk



#ログイン画面
def login(request):
    global user_pk
  
    #POSTメソッド＝ログイン画面でloginボタンを押したとき
    if request.method == "POST":
        username = request.POST['username']

        #ユーザーが存在する場合
        try:
            user = Member.objects.get(name=username)
            user_pk = user.pk
            return redirect('status:index')
          
        #ユーザーが存在しない場合
        except:
            return render(request, 'status/login.html', {'error':'ユーザーが見つかりません'})  
        
    #GETメソッド＝ログイン画面が呼び出されるとき
    return render(request, 'status/login.html')


#ホーム画面呼び出し
def index(request):
    member = Member.objects.order_by('id')
    positionY = request.POST.get('positionY',129)
    return render(request, 'status/index.html', {'member': member,'position':positionY})


#ステータス更新    (member_pkにはindex.htmlのmember.pkが引き渡される)
def upd(request, member_pk):
    global user_pk
  
    #更新対象が自分以外だったら更新しない。
    if member_pk != user_pk:
        member = Member.objects.order_by('id')
        return render(request, 'status/index.html', {'member': member, 'error':'!!自分以外のステータスは更新できません!!','position':0})
    
    #更新対象が自分だったら更新。
    else:
        #pk(プライマリーキー)をもとにMemberテーブルから自分データを取得、tにわたす。
        t = Member.objects.get(pk=user_pk)
    
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
        # LITE-90 meetingとlunchの排他制御実装
        if 'meeting' in request.POST:
            if t.status_meeting:
                t.status_meeting = 'False'
            else:
                t.status_meeting = 'True'
                t.status_lunch = 'False'
    
        # lunchボタンがクリックされた場合の処理
        # LITE-90 meetingとlunchの排他制御実装
        if 'lunch' in request.POST:
            if t.status_lunch:
                t.status_lunch = 'False'
            else:
                t.status_lunch = 'True'
                t.status_meeting = 'False'

        # 最終更新時刻を更新
        t.last_update_time = timezone.localtime()

        #save()でDBに反映される。
        t.save()
    
        return redirect('status:index')
