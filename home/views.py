from django.shortcuts import render
import pandas as pd

country_list = {
                "France":["Bordeaux","Lyon","Paris","Pays Basque"],
                "Belgium":["Antwerp","Brussels","Ghent"],
                "Netherlands":["Amsterdam","Rotterdam","The Hague"],
                "Uk":["Bristol","Edinburgh","London","Manchester"],
                }
x = "London"

def home_view(request):
    
    context = {"country_list":country_list}

    return render(request, 'home/home_page.html',context= context)


def result_view(request):

    
    return render(request, 'home/result_page.html')
    