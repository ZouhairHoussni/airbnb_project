from django.shortcuts import render
import pandas as pd

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



def result_view(request,id):

    df = pd.read_csv(f"CSV_files/{id}_listings.csv")
    df1 = df[["host_id","host_name"]].head(10)
    R1 = df1.to_html()
    context = {"article" : city_dict[id],
                "R1": R1}

    return render(request, 'home/result_page.html',context=context)
    