from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Member
from django.utils import timezone
import requests
from django.views.generic.list import ListView
from cms.models import Book
# Create your views here.

def main(request):
    return render(request,'homepage/main.html',{})


def join_agree(request):
    return render(request,'homepage/join_agree.html',{})



def join(request):
                                                    # 일반가입
    if request.method=='GET':
        return render(request, 'homepage/join.html', {})
    else:
        user_id = request.POST['user_id']
        user_pwd = request.POST['user_pwd']
        user_name = request.POST['user_nick']
        user_email = request.POST['user_email']

        member = Member(user_id=user_id,
                        user_pwd=user_pwd,
                        user_nick=user_name,
                        user_email=user_email)
        member.c_date = timezone.now()
                                                    # 지갑생성
        session = requests.Session()
        method = 'net_version'
        params = [user_pwd]
        newAccount = {"jsonrpc": "2.0",
                   "method": "personal_newAccount",
                   "params": params,
                   "id": 3}
        headers = {'Content-Type': 'application/json'}
        response = session.post('http://52.78.196.137:8545', json=newAccount, headers=headers)
        myAdress = format(response.json()['result'])
                                                    # 지갑주소 포함 디비에 저장
        member.myAdress = myAdress
        member.save()

        return render(request,'homepage/main.html',{})



def ID_check(request):

    user_id = request.POST['user_id']
    id_confirm = request.POST['id_confirm']

    try:
        Member.objects.get(user_id=user_id)
    except Member.DoesNotExist as e:
        pass
        res = {'user_id': user_id, 'msg': '가입 가능','id_confirm':True}
        return JsonResponse(res)
    else:
        res = {'user_id': user_id, 'msg': '가입 불가','id_confirm':False}
        return JsonResponse(res)

def nick_check(request):

    user_nick = request.POST['user_nick']
    nick_confirm = request.POST['nick_confirm']

    try:
        Member.objects.get(user_nick=user_nick)
    except Member.DoesNotExist as e:
        pass
        res = {'user_nick': user_nick, 'msg': '가입 가능','nick_confirm':True}
        return JsonResponse(res)
    else:
        res = {'user_nick': user_nick, 'msg': '가입 불가','nick_confirm':False}
        return JsonResponse(res)



def login(request):
    result = ''
    if request.method=='GET':
        return render(request, 'homepage/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_pwd = request.POST['user_pwd']
        
        try:
           m = Member.objects.get(user_id = user_id,
                           user_pwd = user_pwd)
        except Member.DoesNotExist:
            return HttpResponse('로그인 실패')
        else:
            request.session['user_id'] = user_id
            request.session['user_nick'] = m.user_nick
            request.session['myAdress'] = m.myAdress
            return HttpResponse('로그인 완료')

def logout(request):
    request.session['user_id'] = ''
    request.session['user_nick'] = ''
    request.session['myAdress'] = ''
    return render(request, 'homepage/logout.html', {})

    
def find_id(request):
    if request.method == "GET":
        return render(request, 'homepage/find_id.html', {})
    else:
        user_email = request.POST['user_email']

        try:
            m = Member.objects.get(user_email = user_email)
        except Member.DoesNotExist:
            return HttpResponse('')
        else:
            return HttpResponse(m.user_id)

def find_pwd(request):
    if request.method == "GET":
        return render(request, 'homepage/find_pwd.html', {})
    else:
        user_id = request.POST['user_id']
        user_email = request.POST['user_email']
        try:
            Member.objects.get(user_id = user_id, user_email=user_email)
        except Member.DoesNotExist as e:
            return HttpResponse('존재하지 않는 계정입니다.')
        else:
            request.session['pwd_id'] = user_id
            return HttpResponse('확인 완료')

def pwd_reset(request):
    if request.method == "GET":
        return render(request, 'homepage/pwd_reset.html', {})
    else:
        if request.session['user_id']:
            user_id = request.session['user_id']
        elif request.session['pwd_id']:
            user_id = request.session['pwd_id']

        user_pwd = request.POST['user_pwd']
        m = Member.objects.get(user_id = user_id)
        m.user_pwd = user_pwd
        m.save()
        return HttpResponse('변경 완료')

class myList(ListView):
    model = Book
    context_object_name = "books"
    template_name = "homepage/mypage.html"
    paginate_by = 5

    def get(self, request):
        user_id = request.session.get('user_id')
        book = Book.objects.get_queryset().filter(publisher = user_id)
        books = book.all().order_by("id")
        self.object_list = books
        context = self.get_context_data(object_list = self.object_list, book=book)
        return self.render_to_response(context)
    

def balance(request):
    if request.method=="GET":
        return render(request,'homepage/mypage.html',{})
    else:
        user_id = request.session['user_id']
        session = requests.Session()
        m = Member.objects.get(user_id=user_id)
        myAdress = m.myAdress
        method = 'net_version'
        params = [myAdress, "latest"]
        balance = {"jsonrpc":"2.0",
                "method":"eth_getBalance",
                "params":params,
                "id":3}
        headers = {'Content-Type': 'application/json'}
        response = session.post('http://52.78.196.137:8545', json=balance, headers=headers)
        result = int(format(response.json()['result']),16)/1000000000/1000000000
        return HttpResponse(result)