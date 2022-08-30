
import os
import pandas as pd
from constants import *
#from twilio.rest import Client


list_tables = ['janeiro','fevereiro','marco','abril']
list_products = []


def Start():

    initial_value = input("Welcome\n1->Deseja Analizar as tabelas\n2->Adicionar Produtos\n3->Listar Produtos da Loja\n4->Sair\n")

    if initial_value == '1':

        os.system('cls')

        for month in list_tables:

            print(month)

            readding_tables =  pd.read_excel(f'{month}.xlsx')

            print(readding_tables)

            condition = readding_tables['Vendas'] > constantDefault

            if (condition).any():

                seller = readding_tables.loc[condition,'Vendedor'].values[0]; 
                sell_value = readding_tables.loc[condition,'Vendas'].values[0];

                number = input("\nIntroduza o seu numero \n")

                # To use next code u need to introduce your data using your twilio account
                account_sid = os.environ['encrypted']
                auth_token = os.environ['encrypted']
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                         body= f'O cliente {seller} passou o limite de vendas com um valor de {sell_value}\n',
                         from_='your phone ... ',
                         to=number
                     )

    elif initial_value == '2':
        #1 -> Adicionar os produtos a lista
        #2 -> criar um ficherio externo
        #3 -> Adicionar os produtos a um ficheiro esterno
        #4 -> perguntar se deseja adicionar mais alguma produto
        factor = False

        while factor == False:
      
            repeat_product_init = input('Deseja inserir mais algum produto (S/N): ')

            if repeat_product_init == 'n' or repeat_product_init == 'N':
                factor = True;
                Start()

Start()




