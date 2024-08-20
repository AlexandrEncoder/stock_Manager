import openpyxl
import addBook

def searc_title(title):
    
    Workbook = openpyxl.load_workbook("library.xlsx")
    colunas = Workbook.active
    cel = colunas['A']
    for e in cel:
        title_book = e.value
        if title == title_book:
            print("existe")
        else:
            choiceAdd = str(input("Deseja adicionar o titulo? YES ou NOT")).lower()
            if choiceAdd == "yes":
                
   