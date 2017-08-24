# coding: UTF-8
from django.http import HttpResponse
from django.shortcuts import render
from models import User
from forms import NameForm
# Create your views here.

def login(request):
	if request.method == 'POST':  
		return post(request)
	else:
		return get(request)
def get(request):
	form = NameForm()
	return render(request,'login.html',{'form':form})
def post(request):
	form = NameForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		print(username + ":" + password)
		if not username or not password:
			return HttpResponseRedirect('/register/')
		else:
			user = User.objects.get(username = username)
			if user.password == password:
				return render(request,'main.html')
			else:
				return HttpResponse("用户名或密码错误!")
	else:
		return HttpResponse("请输入用户名或密码")
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if username == "" or password1 == "":
			return HttpResponse("请输入用户名或密码")
		if password1 != password2:
			return HttpResponse("密码不一致")
		user = User.objects.filter(username = username)
		if user :
			return HttpResponse("用户名已存在")
		else:
			User.objects.create(username = username,password = password1)
			return HttpResponse('注册成功')
	else:
		return render(request,'register.html')
		