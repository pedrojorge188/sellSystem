
from msilib.schema import File
import os
from tkinter import INSERT
import pandas as pd
from constants import *
#from twilio.rest import Client


class Node:
   def __init__(self, product=None, value=None, next=None):
        self.product = product
        self.value = value
        self.next = next

   def __repr__(self):
        return 'Produto:%s  | valor:%s ' % (self.product,self.value)

#lista ligada 

class list:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"

def insertList(list, new_product, new_product_value):


    new_node = Node(new_product, new_product_value)

    new_node.next = list.head

    list.head = new_node

#start linked list first node
new_node = Node(None,None)
list.head = new_node
newProduct_list = list

controller = False

def restoreData():
    with open('ProductSave.txt','r') as restore:
        dataProduct = restore.readline()
        dataValue = restore.readline()

        if(dataProduct != ''):

            insertList(newProduct_list,  dataProduct, dataValue)

        while dataProduct != '':

            dataProduct = restore.readline()
            dataValue = restore.readline()
            insertList(newProduct_list,  dataProduct, dataValue)

restoreData()
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

        factor = False

        while factor == False:
            
            new_product = input('Introduza o nome do novo Produto\n')
            product_value = input('\nIntroduza o valor do novo Produto\n')

            insertList(newProduct_list, new_product, product_value)

            with open("productSave.txt",'a') as file:
                file.write(new_product+'\n'+product_value+'\n')

            repeat_product_init = input('\nDeseja inserir mais algum produto (S/N): ')

            if repeat_product_init == 'n' or repeat_product_init == 'N':
                factor = True;
                Start()

    elif initial_value == '3':
        
        #Lista todos os produtos da lista ligada
        print("-------------")
        node = newProduct_list.head
        while node:
            if node.product != None:
                print(node.product)
                print(node.value)
                print("-------------")
                node = node.next
            elif node.product == None:
                print("Sem produtos para listar!")
                Start()
    
    elif initial_value == '4':
         exit()
Start()




