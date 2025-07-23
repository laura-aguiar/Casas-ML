import pandas as pd

teste = pd.read_csv(r'C:\Users\beatr\OneDrive\Desktop\CASAS\Usuarios\casas_teste.csv')

#load do modelo
from joblib import load
reg = load(r'C:\Users\beatr\OneDrive\Desktop\CASAS\Modelo\regression.joblib')

#previsão
teste = teste.drop('Unnamed: 0',axis=1)
X_teste = teste.drop('MedHouseVal',axis=1)

#exportação dos arquivos
previsao = reg.predict(X_teste)
X_teste['previsao'] = previsao
X_teste.to_excel(r'C:\Users\beatr\OneDrive\Desktop\CASAS\Usuarios\previsoes_modelo.xlsx')

