contactList = []
Favorites = []

def menu():
    print("""\nMenu de opções: 
    1. Adicionar um contato 
    2. Ver contatos cadastrados
    3. Editar um contato
    4. Marcar/desmarcar um contato como favorito
    5. Ver contatos favoritados
    6. Apagar um contato
    7. Sair """)

def addContact (name, telefone, email):
    contact = {"Nome": name,"Telefone": telefone, "Email": email, "Favorite": False}
    contactList.append(contact)

def viewContactList():
    for index in range(len(contactList)):
        print(f"""{index+1}. Contato:
        Nome: {contactList[index]["Nome"]} 
        Telefone: {contactList[index]["Telefone"]}
        Email: {contactList[index]["Email"]}""")

def updateContact(indexContact, indexOption, newName):
    contactForChange = contactList[indexContact - 1]
    n = 0
    chaves = list(contactForChange.keys())
    contactForChange[chaves[indexOption - 1]] = newName
    print("Alteração realizada com sucesso!")

def viewFavorites():
    notFavorites = 0
    FavoritesCount = 0
    for index in range(len(contactList)):
        if contactList[index]["Favorite"] == False:
            notFavorites += 1
            
        
                
    if notFavorites == len(contactList):
        print("Não há favoritos")

    else:
        for index in range(len(contactList)):
            if contactList[index]["Favorite"] == True:
               FavoritesCount += 1
               Favorites.append(contactList[index])
               print(f"""{FavoritesCount}. Contato:
                    Nome: {contactList[index]["Nome"]} 
                    Telefone: {contactList[index]["Telefone"]}
                    Email: {contactList[index]["Email"]}""")

def markDismark():
    markOrDesmark = input("Você deseja marcar ou desmarcar? ").lower()

    if markOrDesmark == "marcar":
        viewContactList()
        IndexFavorite = int(input("Qual contato você quer adicionar aos favoritos? "))
        contactList[IndexFavorite - 1]["Favorite"] = True
        print("Contato marcado como favorito")
    elif markOrDesmark == "desmarcar":
        viewFavorites()
                    
        indexDesmarkFavorite = int(input("Qual contato você quer desmarcar? "))

        Favorites[indexDesmarkFavorite - 1]["Favorite"] = False
        print("Contato desmarcado como favorito")
    else:
        print("Opção inexistente, tente novamente!")

        

menu()
resposta =  int(input("Selecione a opção que deseja: "))

while resposta != 7:
    while resposta <= 0 or resposta > 7:
        print("Opção inexistente, dígite novamente")
        menu()
        resposta =  int(input("Selecione a opção que deseja: "))

    if resposta != 1 and contactList == []:
        print("Não há contatos cadastrados")
        menu()
        resposta =  int(input("Selecione a opção que deseja: "))

    else:
        if resposta == 1:
            name = input("Dígite o nome do contato: ")
            telefone = input("Dígite o telefone do contato: ")
            email = input("Dígite o email do contato: ")
            addContact(name, telefone, email)
            print("Contato adicionado!")

        if resposta == 2:
           viewContactList()
        
        if resposta == 3:
            viewContactList()
            indexContact = int(input("Qual contato você quer alterar? "))
            indexOption = int(input("""Qual opção você deseja alterar? 
1. Nome
2. Telefone
3.Email \n"""))
            if indexOption == 1:
                newName = input("Qual o novo nome? ")
            
            if indexOption == 2:
                newName = input("Qual o novo telefone? ")
            
            if indexOption == 3:
                newName = input("Qual o novo email? ")
            updateContact(indexContact, indexOption, newName)

        if resposta == 4:
            markDismark()
            
        if resposta == 5:
            viewFavorites()
        
        if resposta == 6:
            viewContactList()
            contatcDelete = int(input("Qual contato você deseja apagar? "))
            del contactList[contatcDelete - 1]
            print("Contato deletado")

    menu()
    resposta =  int(input("Selecione a opção que deseja: "))



