from django.shortcuts import render,redirect

from student.models import Student


# Create your views here.

def home(request):
    std = Student.objects.all()
    return render(request, "student/home.html", {'std':std})


def add_student(request):
    if request.method == 'POST':
        stud_roll = request.POST.get('student_roll')
        stud_name = request.POST.get('student_name')
        stud_email = request.POST.get('student_email')
        stud_address = request.POST.get('student_address')
        stud_phone = request.POST.get('student_phone')
        # create an object for model
        s = Student()
        s.roll = stud_roll
        s.name = stud_name
        s.email = stud_email
        s.address = stud_address
        s.phone = stud_phone
        s.save()
        return redirect("../home")
    return render(request, "student/add_student.html", {})

def delete_student(request, roll):
    s = Student.objects.get(pk=roll)
    s.delete()
    return redirect('../home')

def update_student(request, roll):
    std = Student.objects.get(pk=roll)

    return render(request, "student/update_student.html", {"std": std})

def do_update_student(request, roll):
    stud_roll = request.POST.get('student_roll')
    stud_name = request.POST.get('student_name')
    stud_email = request.POST.get('student_email')
    stud_address = request.POST.get('student_address')
    stud_phone = request.POST.get('student_phone')

    std = Student.objects.get(pk=roll)

    std.roll = stud_roll
    std.name = stud_name
    std.email = stud_email
    std.address = stud_address
    std.phone = stud_phone
    std.save()
    return redirect('../home')
