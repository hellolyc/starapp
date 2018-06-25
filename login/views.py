# coding: UTF-8
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import User,Competition,UserCompetion
from .forms import NameForm
import smtplib 
import datetime
import time
import io
from email.mime.text import MIMEText
from .code import gene_code 
from django.conf import settings
# Create your views here.

def login(request):
	if request.method == 'POST':  
		return post(request)
	else:
		return get(request)
def get(request):
	if request.session.get('username'):
		user = User.objects.get(username = request.session['username'])
		com = Competition.objects.all()
		usercom = UserCompetion.objects.all()
		return render(request,'main.html',{'user':user,"com":com, "usercom": usercom})
		
	image,text = gene_code()
	buf = io.BytesIO() #io.BytesIO() #io.StringIO() use it to fill str obj
	name = settings.STATIC_ROOT +  "/picture/random.png"
	image.save(name, 'png')
	request.session['checkcode'] = text.lower() 
	print text.lower()
	form = NameForm()
	return render(request,'login.html',{'form':form,'codename' : name})
def post(request):
	form = NameForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		code = request.POST['checkcode']
		print(username + ":" + password + ":" + code)
		if code != request.session['checkcode'] :
			return HttpResponse("验证码错误!")
		if not username or not password:
			return HttpResponseRedirect('/register/')
		else:
			user = User.objects.get(username = username)
			if user.password == password:
				request.session['time'] = time.time()
				request.session['username'] = username
				com = Competition.objects.all()
				usercom = UserCompetion.objects.all()
				return render(request,'main.html',{'user':user,"com":com, "usercom": usercom})
			else:
				return HttpResponse("用户名或密码错误!")
	else:
		return HttpResponse("请输入用户名或密码")
def logout(request):
	del request.session['username']
	return HttpResponseRedirect('/login/')
def checksession(fun):
	def wrapper(request):
		now = datetime.now()
		timedela = now - request.session['time']
		if(timedela.seconds() >= 5 * 60):
			del request.session['username']
			return HttpResponseRedirect('/login/')
		fun(request)
		return wrapper

 
def competionclick(request):
	pass
def competionresult(request):
	pass
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		phonenum = request.POST['phonenum']
		if username == "" or password1 == "":
			return HttpResponse("请输入用户名或密码")
		if password1 != password2:
			return HttpResponse("密码不一致")
		user = User.objects.filter(username = username)
		if user :
			return HttpResponse("用户名已存在")
		else:
			User.objects.create(username = username,password = password1,phonenum = phonenum)
			return render(request,'main.html')
	else:
		return render(request,'register.html')
def code(request):
	image,text = gene_code()
	buf = io.BytesIO() #io.BytesIO() #io.StringIO() use it to fill str obj
	image.save(buf, 'png')
	request.session['checkcode'] = text.lower() 
	print text.lower()
	return HttpResponse(buf.getvalue(), 'image/png')
def forget(request):
	sender = "15800489297@163.com"  
	receivers = ["995938715@qq.com"]  
	message = """ <!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>Bootstrap 101 Template</title>
  </head>
  <body>
  "请勿回复本邮件.点击下面的链接,重设密码<br/><a href="
                        + resetPassHref + " target='_BLANK'>" + resetPassHref
                        + "</a>  或者    <a href=" + resetPassHref
                        + " target='_BLANK'>点击我重新设置密码</a>"
                        + "<br/>tips:本邮件超过30分钟,链接将会失效，需要重新申请'找回密码'" + key
                        + "\t" + digitalSignature;
  </body>
</html>
"""  
	try:  
		MSG = MIMEText(message,'html')
		MSG['subject'] = "修改密码"
		MSG['from'] = "15800489297@163.com"
		MSG['to'] = "995938715@qq.com"
		smtpObj = smtplib.SMTP()  
		smtpObj.connect("smtp.163.com", "25")   
		state = smtpObj.login("15800489297@163.com", "w244759lyc")  
		if state[0] == 235:  
			smtpObj.sendmail(sender, receivers,MSG.as_string())  
			print "success"  
		smtpObj.quit()  
	except smtplib.SMTPException, e:  
		print str(e) 
	return HttpResponse("请注意查收邮件")
		
