import os 
import pandas as pd
from twilio.rest import Client

list_tables = ['janeiro','fevereiro','marco','abril']

initial_value = input("Welcome\n1->Deseja Analizar as tabelas\n2->Sair\n")

if initial_value == '1':

    os.system('cls')

    for month in list_tables:

        print(month)

        readding_tables =  pd.read_excel(f'{month}.xlsx')

        print(readding_tables)

        condition = readding_tables['Vendas'] > 52

        if (condition).any():

            seller = readding_tables.loc[condition,'Vendedor'].values[0]; 
            sell_value = readding_tables.loc[condition,'Vendas'].values[0];

            number = input("\nIntroduza o seu numero \n")

            account_sid = os.environ['encrypted']
            auth_token = os.environ['encrypted']
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                     body= f'O cliente {seller} passou o limite de vendas com um valor de {sell_value}\n',
                     from_='+15017122661',
                     to=number
                 )

            print(message.sid)







