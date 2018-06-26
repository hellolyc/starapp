# coding: UTF-8
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import smtplib 
import datetime
import time
import io
from login.models import User
from email.mime.text import MIMEText
from django.conf import settings
import hashlib
import requests
# Create your views here.

def index(request):
    if request.session.get('username'):
		  user = User.objects.get(username = request.session['username'])
		  return render(request,'main.html',{'email':user})
    return render(request,'index.html')