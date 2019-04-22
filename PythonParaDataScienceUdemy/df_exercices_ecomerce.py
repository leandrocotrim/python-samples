# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:37:31 2018

@author: leandro.cotrim
"""

# Importe pandas e leia o arquivo csv "Ecommerce Purchases" e configure-o para um DataFrame chamado ecom.
import pandas as pd
ecom = pd.read_csv("./data/Ecommerce Purchases")

# Verifique o "head" do DataFrame.
ecom.head()

# Quantas linhas e colunas existem?
ecom.info()

# Qual é o preço de compra médio?
ecom['Purchase Price'].mean()

# Quais foram os preços de compra mais altos e mais baixos?
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()

# Quantas pessoas têm Inglês 'en' como sua língua de escolha no site? 
ecom['Language'].value_counts().loc['en']

# Quantas pessoas têm o cargo de "Advogado"?
ecom['Job'].value_counts().loc['Lawyer']

# Quantas pessoas fizeram a compra durante a AM e quantas pessoas fizeram a compra durante o PM?
ecom['AM or PM'].value_counts()

# Quais são os 5 títulos de trabalho mais comuns?
ecom['Job'].value_counts()[:5]

# Alguém fez uma compra que veio do Lot: "90 WT", qual foi o preço de compra para esta transação?
ecom[ecom['Lot'] == '90 WT']['Purchase Price']

# Qual é o email da pessoa com o seguinte número do cartão de crédito: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']

# Quantas pessoas têm o American Express como seu fornecedor de cartão de crédito * e * fizeram uma compra acima de US $ 95?
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)]['CC Provider'].value_counts()

# Difícil: quantas pessoas tem um cartão de crédito que expira em 2025?
len([i for i in ecom['CC Exp Date'].str.split('/') if i[1] == '25'])
sum(ecom['CC Exp Date'].apply(lambda x: x.split('/')[1]) == '25')

# Difícil: quais são os 5 principais provedores de e-mail / hosts mais populares (por exemplo, gmail.com, yahoo.com, etc ...) 
pd.Series([i[1] for i in ecom['Email'].str.split('@')]).value_counts()[:5]
ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts()[:5] 








