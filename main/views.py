from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Kaos hitam polos',
        'amount': 20,
        'description':'Kaos polos pria berbahan Cotton Combed 30s round neck reguler fit',
        'price': 50000,
        'category': 'fashion pria'
        
    }

    return render(request, "main.html", context)