from django.shortcuts import render, redirect
from django.http import HttpResponse
from department import views as department

def get_login_formn(request):
    return render(request, 'login/login.html')

def handle_btn_login(request):
    if request.method == 'POST':
        # xử lý click
        return HttpResponse("Button clicked!")
