from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
#MVT model view template , mvc


def index(request):
    return HttpResponse('xin chao')


def handle_uploaded_file(f, tenfile):
    with open(tenfile, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class IndexView(View):
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
        ketqu = str(kq) + ' - theo kieu get'
        du_lieu = {
            'ketqua': ketqu
        }
        return render(request, 'index.html', du_lieu)