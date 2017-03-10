from django.shortcuts import render
from quotesTest_app.models import Quote

# Create your views here.
def get_quotes(request):
    return render(request, "quotesTest/home.html",
                  {'quote_list': Quote.objects.all()})
