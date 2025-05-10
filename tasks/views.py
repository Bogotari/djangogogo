from django.shortcuts import render

def thank_you(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # Aquí podrías guardar los datos en la base de datos si lo deseas
    return render(request, "thank_you.html")
