from django.shortcuts import render
import pandas as pd
import pickle


country_list = {
                "France":["Bordeaux","Lyon","Paris","Pays Basque"],
                "Belgium":["Antwerp","Brussels","Ghent"],
                "Netherlands":["Amsterdam","Rotterdam","The Hague"],
                "Uk":["Bristol","Edinburgh","London","Manchester"],
                }

city_dict ={}


for i in country_list:
    for j in country_list[i]:
        city_dict[j] = j





def home_view(request):
    
    context = {"country_list":country_list}

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
    