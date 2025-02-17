# -*- coding: utf-8 -*-
"""Desafio 1 - IA Machine Learning Dataset Heart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kEyipqGMTugZmgK00Btzb0zL513gJ8dI
"""

# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Carregando o dataset de doenças cardíacas
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
colunas = ['idade', 'sexo', 'tipo_dor_peito', 'pressao_sanguinea_repouso', 'colesterol', 'acucar_sangue_jejum',
           'resultado_eletrocardiografico', 'frequencia_cardiaca_maxima', 'angina_exercicio', 'depressao_st',
           'inclinação_st', 'vasos_cardiacos', 'talassemia', 'diagnostico_doenca_cardiaca']
dados = pd.read_csv(url, names=colunas)

# Exibir as primeiras linhas do dataset
print(dados.head())

# Tratar valores ausentes, se houver
dados.replace('?', np.nan, inplace=True)
dados.dropna(inplace=True)

# Verificar a distribuição das classes
print(dados['diagnostico_doenca_cardiaca'].value_counts())

# Separar variáveis independentes (X) e alvo (y)
X = dados.drop('diagnostico_doenca_cardiaca', axis=1)
y = dados['diagnostico_doenca_cardiaca']

# Dividir em treino e teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Padronizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Treinar o modelo de Regressão Logística
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Previsão e avaliação
y_pred_log = log_reg.predict(X_test)
print("Acurácia Regressão Logística:", accuracy_score(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log, zero_division=1))

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print("Acurácia KNN:", accuracy_score(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn, zero_division=1))

# SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
print("Acurácia SVM:", accuracy_score(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm, zero_division=1))