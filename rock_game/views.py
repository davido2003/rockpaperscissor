from django.shortcuts import render ,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
import random

def check_winner(user_num):
	choices = ['stone','paper','scissor']
	choices_pic = ['media/rock.png','media/papers.png','media/scissor.png']
	n=random.randint(0,2)
	user_choice = choices[user_num]
	bot_choice = choices[n]

	d = dict()
	d['user_pic']=choices_pic[user_num]
	d['bot_pic']=choices_pic[n]
	
	if user_choice ==bot_choice:
		d['msg']='This is Tie'
	elif user_choice=='stone':
		if bot_choice=='paper':
			d['msg']='Paper covers Stone ....Computer won you loose'
		else:
			d['msg']='Stone breaks Scissor ....You Won'
	elif user_choice=='paper':
		if bot_choice=='scissor':
			d['msg']='Scissor cuts paper ....Computer won you loose'
		else:
			d['msg']='Paper covers Stone ....You Won'
	else:
		if bot_choice=='stone':
			d['msg']='Stone Breaks Scissor..... Computer won you loose'
		else:
			d['msg']='Scissor cuts paper ....You Won'
	return d

def home(request):
	return render(request,'home.html')

def rock(request):
	winner=check_winner(0)
	return render(request,'result.html',winner)

def paper(request):
	winner=check_winner(1)
	return render(request,'result.html',winner)

def scissor(request):
	winner=check_winner(2)
	return render(request,'result.html',winner)

def signuppage(request):
   
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was sucessfully created for ' + user)
                return redirect('login/')
        context = {'form':form}
        return render(request, 'signup.html', context)
def loginpage(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username Or Password is Incorrect')
            
    context = {}
    return render(request, 'login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')