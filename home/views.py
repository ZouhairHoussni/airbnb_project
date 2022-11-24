from django.shortcuts import render

country_list = {
                "France":["Bordeaux","Lyon","Paris","Pays Basque"],
                "Belgium":["Antwerp","Brussels","Ghent"],
                "Netherlands":["Amsterdam","Rotterdam","The Hague"],
                "Uk":["Bristol","Edinburgh","London","Manchester"],
                }


def home_view(request):

    context = {"country_list":country_list}

    return render(request, 'home/home_page.html',context= context)