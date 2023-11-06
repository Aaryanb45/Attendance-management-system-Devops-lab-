from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def AdminLogin(request):
    if not request.user.is_anonymous:
        return redirect("/AdminDashboard")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('AdminDashboard')
        return render(request, 'AdminLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'AdminLogin.html')

def StudentLogin(request):
    if not request.user.is_anonymous:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print('hi')

        if user is not None:
            login(request, user)
            return redirect('')
        return render(request, 'Studentlogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'Studentlogin.html')

def TeacherLogin(request):
    if not request.user.is_anonymous:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('teacher_dashboard')
        return render(request, 'TeacherLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'TeacherLogin.html')

def loginuser(request):
    if not request.user.is_anonymous:
            return redirect('/')
    if request.method=="POST":
        username=request.POST.get('ID')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/admindashboard')              #change dashboard according to where it is coming from
        else:
            messages.error(request, 'Wrong username or password')
            return render(request,'login.html')               #change login.html
    return render(request,'login.html')                       #change login.html
    
def addnewstudent(request):
    if request.method == 'POST':
        student_name = request.POST.get('student')
        student_id = request.POST.get('studentName')
        password = request.POST.get('password')

        return HttpResponse('Student added successfully')
    else:
        return render(request, 'addnewstudent.html')


def AdminDashboard(request):
    return render(request, 'AdminDashboard.html')

def class_mgmt(request):
    return render(request, 'class_mgmt.html')

def courseadd(request):
    return render(request, 'courseadd.html')

def index(request):
    return render(request, 'index.html')

def student_mgmt(request):
    return render(request, 'student_mgmt.html')

def teacher_mgmt(request):
    return render(request, 'teacher_mgmt.html')

def teacher(request):
    return render(request, 'teacher.html')

def viewclass(request):
    return render(request, 'viewclass.html')

def viewfaculty(request):
    return render(request, 'viewfaculty.html')

def viewstudent(request):
    return render(request, 'viewstudent.html')

def logoutuser(request):
    logout(request)
    return redirect('/')


