from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import EmployeeDetail
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import EmployeeExperience  # Correct import statement
from .models import EmployeeEducation  # Correct import statement
from django.core.exceptions import ObjectDoesNotExist





# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['emcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        
        try:
        
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            # Save fullname in EmployeeDetail model
            EmployeeDetail.objects.create(user=user, emcode=ec)
            EmployeeExperience.objects.create(user=user, emcode=ec) # type: ignore
            EmployeeEducation.objects.create(user=user, emcode=ec) # type: ignore
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('emp_login')  # Redirect to login page after successful registration
        except IntegrityError:
            error = "An account with this email already exists. Please use a different email."

    return render(request, 'registration.html', {'error': error})

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST.get('email')
        p = request.POST.get('password')
        print(f"Email: {u}, Password: {p}")  # Debugging print statement
        user = authenticate(username=u, password=p)
        print(f"Authenticated User: {user}")  # Debugging print statement
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'emp_login.html', {'error': error})
def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')


def Logout(request):
    logout(request)
    return redirect('index')


# profile edit code

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    user = request.user

    # Handle case where EmployeeDetail does not exist
    try:
        employee = EmployeeDetail.objects.get(user=request.user)
    except EmployeeDetail.DoesNotExist:
        # Create a new EmployeeDetail record for the user if it doesn't exist
        employee = EmployeeDetail(user=request.user)
        employee.save()

    if request.method == "POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ec = request.POST.get('employeecode')
        det = request.POST.get('department')
        designation = request.POST.get('designation')
        contact = request.POST.get('contact')
        gen = request.POST.get('gender')
        jdate = request.POST.get('joining_date')

        # Assigning updated values to employee fields
        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.emcode = ec
        employee.empdept = det
        employee.designation = designation
        employee.contact = contact
        employee.gender = gen

        # Validating joining date and updating
        if jdate:
            employee.joiningdate = jdate

        try:
            # Save employee and related user data
            employee.user.save()
            employee.save()
            error = "no"
        except Exception as e:
            error = f"yes: {str(e)}"

    return render(request, 'profile.html', locals())

# admin code 
def admin_login(request):
    return render(request, 'admin_login.html')


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    try:
        exp = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        exp = None  # Set to None if no experience is found

    return render(request, 'my_experience.html', {'exp': exp})  # Pass 'exp' to the template






def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user

    # Handle case where EmployeeExperience does not exist
    try:
        experience = EmployeeExperience.objects.get(user=request.user)
    except EmployeeExperience.DoesNotExist:
        experience = EmployeeExperience(user=request.user)

    if request.method == "POST":
        company1name = request.POST.get('company1name')
        company1desig = request.POST.get('company1desig')
        company1salary = request.POST.get('company1salary')
        company1duration = request.POST.get('company1duration')

        company2name = request.POST.get('company2name')
        company2desig = request.POST.get('company2desig')
        company2salary = request.POST.get('company2salary')
        company2duration = request.POST.get('company2duration')

        company3name = request.POST.get('company3name')
        company3desig = request.POST.get('company3desig')
        company3salary = request.POST.get('company3salary')
        company3duration = request.POST.get('company3duration')

        # Assigning updated values to employee fields
        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            # Save the experience instance
            experience.save()
            error = "no"
        except Exception as e:
            error = f"yes: {str(e)}"

    return render(request, 'edit_myexperience.html', {'error': error, 'experience': experience})


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user
    try:
        education = EmployeeEducation.objects.get(user=user)
    except EmployeeEducation.DoesNotExist:
        education = None  # Set to None if no experience is found

    return render(request, 'my_education.html', {'education': education})  # Pass 'exp' to the template






from django.shortcuts import render, redirect
from .models import EmployeeEducation  # Ensure this is the correct model import

def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user

    # Handle case where employeeducation does not exist
    try:
        education = EmployeeEducation.objects.get(user=request.user)
    except EmployeeEducation.DoesNotExist:  # Correct the exception class
        education = EmployeeEducation(user=request.user)  # Create a new instance if not found

    if request.method == "POST":
        # Get data from the form
        coursepg = request.POST.get('coursepg')
        schoolclgpg = request.POST.get('schoolclgpg')
        yearofpassingpg = request.POST.get('yearofpassingpg')
        percentagepg = request.POST.get('percentagepg')

        coursegra = request.POST.get('coursegra')
        schoolclggra = request.POST.get('schoolclggra')
        yearofpassinggra = request.POST.get('yearofpassinggra')
        percentagegra = request.POST.get('percentagegra')

        coursessc = request.POST.get('coursessc')
        schoolclgssc = request.POST.get('schoolclgssc')
        yearofpassingssc = request.POST.get('yearofpassingssc')
        percentagessc = request.POST.get('percentagessc')

        coursehsc = request.POST.get('coursehsc')
        schoolclgsc = request.POST.get('schoolclgsc')
        yearofpassingsc = request.POST.get('yearofpassingsc')
        percentagesc = request.POST.get('percentagesc')

        # Assigning updated values to education fields
        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schoolclgsc = schoolclgsc
        education.yearofpassingsc = yearofpassingsc
        education.percentagesc = percentagesc

        try:
            # Save the education instance
            education.save()
            error = "no"
        except Exception as e:
            error = f"yes: {str(e)}"

    return render(request, 'edit_myeducation.html', {'error': error, 'education': education})



def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user

    if request.method == "POST":
        # Get data from the form
       c = request.POST['currentpassword']
       n = request.POST['newpassword']
    try:

            if user.check_password(c):
                user.set_password(n)
            # Save the education instance
                user.save()
                error = "no"
            else:
                error = "not"
            
    except Exception as e:
            error = f"yes: {str(e)}"

    return render(request, 'change_password.html', locals())


