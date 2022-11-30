from django.shortcuts import render
import pickle

def home_view(request):
    country_list = {
        "france":["bordeaux","lyon","paris","pays_Basque"],
        "belgique":["antwerp","brussels","ghent"],
        "netherlands":["amsterdam","Rotterdam","the_Hague"],
        "united_Kingdom":["bristol","edinburgh","london","greater_manchester"],
    }
    context = {
        "country_list" : country_list
    }

    return render(request, 'home/home_page.html',context= context)

def result_view(request, pays, ville):
    pickle_in = open(f'pickle/{pays}_{ville}.pkl', 'rb')
    data = pickle.load(pickle_in)


    context = {
        "data" : data,
        "pays" : pays,
        "ville" : ville
        }

    return render(request, 'home/result_page.html',context=context)
    