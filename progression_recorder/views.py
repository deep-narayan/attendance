from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Student,Results,Subject
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

name=''

def home(request):
	if request.method=='POST':
		u=request.POST['username']
		p=request.POST['password']
		try:
			selUser = authenticate(username=u, password=p)
		except:
			return HttpResponse("Invalid Login Details please fill once more")

		if selUser:
			login(request, selUser)
			return redirect('/login/')

	return render(request,'index.html')

def register(request):
	if request.method=='POST':
		fname=request.POST['nm1']
		lname=request.POST['nm2']
		username=request.POST['username']
		password=request.POST['pwd']
		email=request.POST['email']
		usertype=request.POST['usertype']
		rollno=request.POST['rollno']
		add=request.POST['add']
		age=request.POST['age']
		gender=request.POST['gender']
		u=User(first_name=fname,last_name=lname,email=email,username=username,password=make_password(password))
		u.save()
		if usertype=='teacher':
			rollno=0
		s=Student(user=u,usertype=usertype,gender=gender,address=add,age=age,rollno=rollno)
		s.save()
		print("Data Saved Successfully")



	return render(request,'register.html')

@login_required
def login_call(request):
	s=User.objects.get(username=request.user)
	global name
	name=s.first_name.capitalize()+" "+s.last_name
	sel=Student.objects.get(user_id__username=request.user)
	if(sel.usertype=='student'):
		if request.method=='POST':
			ckre=request.POST['rollno']
			c=Student.objects.get(rollno=ckre)
			s=Results.objects.filter(student=c.user)
			return render(request,'result.html',{'name':name,'n':s})
		return render(request,'dashboard.html',{'name':name})
	elif(sel.usertype=='teacher'):
		return render(request,'dashboard2.html',{'name':name})

	return render(request,'dashboard.html',{'name':name})


def logout_call(request):
	logout(request)
	return redirect('/')

def addsub(request):
	if request.method=='POST':
		sub=request.POST['subject']
		s=Subject(name=sub)
		s.save()
		return redirect('/login/')

	return render(request,'addsub.html',{'name':name})


def viewsub(request):
	s=Subject.objects.all()
	return render(request,'viewsub.html',{'name':name,'sub':s})

def addres(request):
	stu=Student.objects.filter(usertype='student')
	#us=User.objects.filter(id=stu)
	#print(us)
	sub=Subject.objects.all()
	if request.method=='POST':
		r=request.POST['rollno']
		s=request.POST['sub']
		m=request.POST['mark']
		t=request.POST['total']
		#print('rollno',r)
		#print('sub',s)
		#print('marks',m)
		#print('total',t)
		stu=Student.objects.get(rollno=int(r))
		sub=Subject.objects.get(id=int(s))
		res=Results(student=stu.user,subject=sub,marks=m,total=t)
		res.save()
		

		return redirect('/login/')

	return render(request,'addres.html',{'name':name,'stu':stu,'sub':sub})

def usd(request):
	s=Student.objects.filter(usertype='student')

	return render(request,'usd.html',{'name':name,'student':s})






	