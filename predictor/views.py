from django.shortcuts import render
import pandas as pd
import pickle
import os
from django.conf import settings

def index_func(request):
    res = None
    if request.method == 'POST':
        try:
            # Captura os dados enviados pelo formulário HTML
            year = request.POST.get('year', 2018)
            km = request.POST.get('km_driven', 45000)
            fuel = request.POST.get('fuel', 1)
            dealer = request.POST.get('dealer', 1)
            trans = request.POST.get('trans', 1)
            seats = request.POST.get('seats', 5)
            rpm = request.POST.get('torque_rpm', 3000)
            mil = request.POST.get('mil', 15)
            eng = request.POST.get('eng', 1200)
            power = request.POST.get('power', 80)
            owner = request.POST.get('owner', '1')

            # Converte o owner através da função Helper para o formato que o modelo espera
            Ownership = Helper(owner)
            
            df2 = pd.DataFrame([{
                'year': int(year),
                'km_driven': float(km),
                'fuel': float(fuel),
                'seller_type': int(dealer),
                'transmission': int(trans),
                'seats': int(seats),
                'torque_rpm': float(rpm),
                'mil_kmpl': float(mil),
                'engine_cc': float(eng),
                'max_power_new': float(power),
                'First Owner': Ownership[0],
                'Fourth & Above Owner': Ownership[1],
                'Second Owner': Ownership[2],
                'Test Drive Car': Ownership[3],
                'Third Owner': Ownership[4]
            }])
            
            # Carrega o modelo treinado da pasta modelos/
            model_path = os.path.join(settings.BASE_DIR, 'modelos', 'CarSelling.pickle')
            with open(model_path, 'rb') as f:
                loaded_model = pickle.load(f)
                
            prediction = loaded_model.predict(df2)[0]
            res = f"{prediction:,.2f}"
        except Exception as e:
            res = f"Erro: {e}"

    return render(request, "predictor/index.html", {'prediction': res})

def Helper(x):
    if x == '1':
        return [1, 0, 0, 0, 0]
    elif x == '2':
        return [0, 0, 1, 0, 0]
    elif x == '3':
        return [0, 0, 0, 0, 1]
    elif x == '4':
        return [0, 1, 0, 0, 0]
    elif x == '5':
        return [0, 0, 0, 1, 0]
    return [1, 0, 0, 0, 0]