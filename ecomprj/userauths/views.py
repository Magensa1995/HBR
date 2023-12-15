from django.shortcuts import render
from userauths.forms import UserRegisterForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("Your account register successfully!!!")
    else:
        print("Register cannot be successful!!!")
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)

def login_view(request):
    return render (request, "userauths/sign-in.html")