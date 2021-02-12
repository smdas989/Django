from django.shortcuts import render
from .forms import RegisterForm
from .models import CustomStudentModel
from django.views import View


class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "registration.html", {"form": form})

    def post(self, request, *args, **kwargs):
        template = "registration.html"

        form = RegisterForm(request.POST)
        if form.is_valid():
            if CustomStudentModel.objects.filter(
                username=form.cleaned_data["name"]
            ).exists():
                return render(
                    request,
                    template,
                    {"form": form, "error_message": "Username already exists."},
                )
            elif CustomStudentModel.objects.filter(
                email=form.cleaned_data["email"]
            ).exists():
                return render(
                    request,
                    template,
                    {"form": form, "error_message": "Email already exists."},
                )

            else:

                user = CustomStudentModel.objects.create(
                    username=form.cleaned_data["name"],
                    email=form.cleaned_data["email"],
                    standard=form.cleaned_data["standard"],
                    roll_no=form.cleaned_data["roll_no"],
                    gender=form.cleaned_data["gender"],
                    age=form.cleaned_data["age"],
                )
                user.save()

                students = CustomStudentModel.objects.all()
                details = []

                for student in students:
                    student_info = {
                        "username": student.username,
                        "email": student.email,
                        "standard": student.standard,
                        "roll_no": student.roll_no,
                        "age": student.age,
                        "gender": student.gender,
                    }
                    details.append(student_info)
                    context = {"students": details}

        return render(request, "show_detail.html", context)
