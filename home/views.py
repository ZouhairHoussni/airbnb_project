from django.shortcuts import render

country_list = {
                "France":[],
                "Belgium":[],
                "Netherlands":[],
                "Uk":["Bristol","Edinburgh","London","Manchester"],
                }


def home_view(request):

    context = {"country_list":country_list}

    return render(request, 'home/home_page.html',context= context)