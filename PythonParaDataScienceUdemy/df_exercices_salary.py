# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:19:19 2018

@author: leandro.cotrim
"""

import pandas as pd

sal = pd.read_csv('./data/Salaries.csv')
sal.head()

sal.info()

# Qual é o "BasePay" médio?
sal['BasePay'].mean()

# Qual é a maior quantidade de "OvertimePay" no conjunto de dados?
sal['OvertimePay'].max()

# Qual é o cargo de JOSEPH DRISCOLL? Nota: use todas as maiúsculas, caso contrário você pode obter uma resposta que não coincida (há também um Joseph Driscoll com minúsculas).
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']["JobTitle"]

# Qual o nome da pessoa mais bem paga (incluindo benefícios)? 
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]

# Qual o nome da pessoa paga mais baixa (incluindo benefícios)? Você percebe algo estranho sobre o quanto ele ou ela é paga?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]

# Qual foi a média (média) BasePay de todos os funcionários por ano? (2011-2014)?
group = sal[(sal['Year'] > 2010) & (sal['Year'] < 2015)].groupby('Year')
group['BasePay'].mean()

# Quantos títulos de trabalho únicos existem?
sal['JobTitle'].nunique()

# Quais são os 5 principais empregos mais comuns?
sal['JobTitle'].value_counts()[:5]

# Quantos Títulos de Trabalho foram representados por apenas uma pessoa em 2013? (Por exemplo, títulos de trabalho com apenas uma ocorrência em 2013?)
group = sal[sal['Year'] == 2013].groupby('JobTitle')
df = group.count()
df[df['EmployeeName'] == 1]['EmployeeName'].count()

# Quantas pessoas têm a palavra Chefe em seu cargo? (Isso é bastante complicado)
sal[sal["JobTitle"].str.contains('Chief')]["JobTitle"].count()

# Bônus: Existe uma correlação entre o comprimento da seqüência do título do trabalho e o salário?
sal['title_len'] = sal["JobTitle"].apply(len)
sal[["title_len", "TotalPayBenefits"]].corr()




