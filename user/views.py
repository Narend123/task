from django.shortcuts import render,redirect	
from django.http import HttpResponse

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']

		if register.objects.filter(email=email,password=password):
		
			
			request.session['login'] = email

			messages.info(request,'Login Success.....!')

			return render(request,'user.html',)
			
		else:
			messages.warning(request,'Invalid Credentials....!')
			return redirect('/login')

	else:
		return render(request,'login.html',)
	

def home(request):
	return render(request,'index.html',)
def users(request):
	return render(request,'users.html',)

def logout(request):
	return render(request,'index.html',)

def sign_up(request):
	return render(request,'sign_up.html',)	


