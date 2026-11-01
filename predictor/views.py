from django.shortcuts import render
import pickle
import numpy as np
import os
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'modelos', 'CarSelling.pickle')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def predict_price(request):
    prediction = None
    if request.method == 'POST':
        year = float(request.POST.get('year'))
        km_driven = float(request.POST.get('km_driven'))
        fuel = float(request.POST.get('fuel'))
        seller_type = float(request.POST.get('seller_type'))
        transmission = float(request.POST.get('transmission'))

        features = np.array([[year, km_driven, fuel, seller_type, transmission]])
        pred_value = model.predict(features)[0]
        prediction = f"{pred_value:,.2f}"

    return render(request, 'predictor/index.html', {'prediction': prediction})