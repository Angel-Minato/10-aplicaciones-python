from django.shortcuts import render
from . import traductor

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        saldia = traductor.traducir(original_text)
        return render(request,'traductor.html',{'output_text':saldia,'original_text':original_text})
    else:
        return render(request,'traductor.html')