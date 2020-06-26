from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#MVT model view template , mvc


def index(request):
    return HttpResponse('xin chao')


def handle_uploaded_file(f, tenfile):
    with open(tenfile, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        so_1 = request.POST.get('so1')
        so_2 = request.POST.get('so2')
        kq = int(so_1) + int(so_2)
        print()
        handle_uploaded_file(request.FILES['file1'], 'ten1.jpg')
        du_lieu = {
            'ketqua': kq
        }
        return render(request, 'index.html', du_lieu)



class TinhToanView(View):
    def get(self, request):
        so_1 = request.GET.get('so1')
        so_2 = request.GET.get('so2')
        kq = int(so_1) + int(so_2)
        #ketqua = str(kq) + ' - theo kieu get'
        du_lieu = {
            'ketqua': kq
        }
        return render(request, 'index.html', du_lieu)

class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('login thanh cong')
        else:
            return HttpResponse('login that bai')

class ForgotPassword(View):

    def get(self, request):
        return render(request, 'forgot-password.html')
class FormView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'form.html')