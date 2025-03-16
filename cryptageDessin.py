# Fichier: cryptageDessin.py
# Auteurs: Kevin Wang et Floriencia Jhon Locht
# Date: 27 mars 2025
#
# Ce programme crypte et décrypte un message de trois manière différentes et
# dessine dessine les trois premières lettres du message en binaire à l'aide 
# de la troisième méthode de cryptographie.

# -------------------------------- Dictionnaire ----------------------------- #

vig = {'A': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F',
             'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
             'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
             'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
             'Y': 'Y', 'Z': 'Z'},
       'B': {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G',
             'G': 'H', 'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M',
             'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
             'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y',
             'Y': 'Z', 'Z': 'A'},
       'C': {'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H',
             'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N',
             'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T',
             'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z',
             'Y': 'A', 'Z': 'B'},
       'D': {'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I',
             'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O',
             'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U',
             'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A',
             'Y': 'B', 'Z': 'C'},
       'E': {'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I', 'F': 'J',
             'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N', 'K': 'O', 'L': 'P',
             'M': 'Q', 'N': 'R', 'O': 'S', 'P': 'T', 'Q': 'U', 'R': 'V', 
             'S': 'W', 'T': 'X', 'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B',
             'Y': 'C', 'Z': 'D'},
       'F': {'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K',
             'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q',
             'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W',
             'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 
             'Y': 'D', 'Z': 'E'},
       'G': {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L',
             'G': 'M', 'H': 'N', 'I': 'O', 'J': 'P', 'K': 'Q', 'L': 'R',
             'M': 'S', 'N': 'T', 'O': 'U', 'P': 'V', 'Q': 'W', 'R': 'X',
             'S': 'Y', 'T': 'Z', 'U': 'A', 'V': 'B', 'W': 'C', 'X': 'D',
             'Y': 'E', 'Z': 'F'},
       'H': {'A': 'H', 'B': 'I', 'C': 'J', 'D': 'K', 'E': 'L', 'F': 'M',
             'G': 'N', 'H': 'O', 'I': 'P', 'J': 'Q', 'K': 'R', 'L': 'S',
             'M': 'T', 'N': 'U', 'O': 'V', 'P': 'W', 'Q': 'X', 'R': 'Y',
             'S': 'Z', 'T': 'A', 'U': 'B', 'V': 'C', 'W': 'D', 'X': 'E',
             'Y': 'F', 'Z': 'G'},
       'I': {'A': 'I', 'B': 'J', 'C': 'K', 'D': 'L', 'E': 'M', 'F': 'N',
             'G': 'O', 'H': 'P', 'I': 'Q', 'J': 'R', 'K': 'S', 'L': 'T',
             'M': 'U', 'N': 'V', 'O': 'W', 'P': 'X', 'Q': 'Y', 'R': 'Z',
             'S': 'A', 'T': 'B', 'U': 'C', 'V': 'D', 'W': 'E', 'X': 'F',
             'Y': 'G', 'Z': 'H'},
       'J': {'A': 'J', 'B': 'K', 'C': 'L', 'D': 'M', 'E': 'N', 'F': 'O',
             'G': 'P', 'H': 'Q', 'I': 'R', 'J': 'S', 'K': 'T', 'L': 'U',
             'M': 'V', 'N': 'W', 'O': 'X', 'P': 'Y', 'Q': 'Z', 'R': 'A',
             'S': 'B', 'T': 'C', 'U': 'D', 'V': 'E', 'W': 'F', 'X': 'G',
             'Y': 'H', 'Z': 'I'},
       'K': {'A': 'K', 'B': 'L', 'C': 'M', 'D': 'N', 'E': 'O', 'F': 'P',
             'G': 'Q', 'H': 'R', 'I': 'S', 'J': 'T', 'K': 'U', 'L': 'V',
             'M': 'W', 'N': 'X', 'O': 'Y', 'P': 'Z', 'Q': 'A', 'R': 'B',
             'S': 'C', 'T': 'D', 'U': 'E', 'V': 'F', 'W': 'G', 'X': 'H',
             'Y': 'I', 'Z': 'J'},
       'L': {'A': 'L', 'B': 'M', 'C': 'N', 'D': 'O', 'E': 'P', 'F': 'Q',
             'G': 'R', 'H': 'S', 'I': 'T', 'J': 'U', 'K': 'V', 'L': 'W',
             'M': 'X', 'N': 'Y', 'O': 'Z', 'P': 'A', 'Q': 'B', 'R': 'C',
             'S': 'D', 'T': 'E', 'U': 'F', 'V': 'G', 'W': 'H', 'X': 'I',
             'Y': 'J', 'Z': 'K'},
       'M': {'A': 'M', 'B': 'N', 'C': 'O', 'D': 'P', 'E': 'Q', 'F': 'R',
             'G': 'S', 'H': 'T', 'I': 'U', 'J': 'V', 'K': 'W', 'L': 'X',
             'M': 'Y', 'N': 'Z', 'O': 'A', 'P': 'B', 'Q': 'C', 'R': 'D',
             'S': 'E', 'T': 'F', 'U': 'G', 'V': 'H', 'W': 'I', 'X': 'J',
             'Y': 'K', 'Z': 'L'},
       'N': {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
             'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y',
             'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E',
             'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K',
             'Y': 'L', 'Z': 'M'},
       'O': {'A': 'O', 'B': 'P', 'C': 'Q', 'D': 'R', 'E': 'S', 'F': 'T',
             'G': 'U', 'H': 'V', 'I': 'W', 'J': 'X', 'K': 'Y', 'L': 'Z',
             'M': 'A', 'N': 'B', 'O': 'C', 'P': 'D', 'Q': 'E', 'R': 'F',
             'S': 'G', 'T': 'H', 'U': 'I', 'V': 'J', 'W': 'K', 'X': 'L',
             'Y': 'M', 'Z': 'N'},
       'P': {'A': 'P', 'B': 'Q', 'C': 'R', 'D': 'S', 'E': 'T', 'F': 'U',
             'G': 'V', 'H': 'W', 'I': 'X', 'J': 'Y', 'K': 'Z', 'L': 'A',
             'M': 'B', 'N': 'C', 'O': 'D', 'P': 'E', 'Q': 'F', 'R': 'G',
             'S': 'H', 'T': 'I', 'U': 'J', 'V': 'K', 'W': 'L', 'X': 'M',
             'Y': 'N', 'Z': 'O'},
       'Q': {'A': 'Q', 'B': 'R', 'C': 'S', 'D': 'T', 'E': 'U', 'F': 'V',
             'G': 'W', 'H': 'X', 'I': 'Y', 'J': 'Z', 'K': 'A', 'L': 'B',
             'M': 'C', 'N': 'D', 'O': 'E', 'P': 'F', 'Q': 'G', 'R': 'H',
             'S': 'I', 'T': 'J', 'U': 'K', 'V': 'L', 'W': 'M', 'X': 'N',
             'Y': 'O', 'Z': 'P'},
       'R': {'A': 'R', 'B': 'S', 'C': 'T', 'D': 'U', 'E': 'V', 'F': 'W',
             'G': 'X', 'H': 'Y', 'I': 'Z', 'J': 'A', 'K': 'B', 'L': 'C', 
             'M': 'D', 'N': 'E', 'O': 'F', 'P': 'G', 'Q': 'H', 'R': 'I',
             'S': 'J', 'T': 'K', 'U': 'L', 'V': 'M', 'W': 'N', 'X': 'O',
             'Y': 'P', 'Z': 'Q'},
       'S': {'A': 'S', 'B': 'T', 'C': 'U', 'D': 'V', 'E': 'W', 'F': 'X',
             'G': 'Y', 'H': 'Z', 'I': 'A', 'J': 'B', 'K': 'C', 'L': 'D',
             'M': 'E', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'I', 'R': 'J',
             'S': 'K', 'T': 'L', 'U': 'M', 'V': 'N', 'W': 'O', 'X': 'P',
             'Y': 'Q', 'Z': 'R'},
       'T': {'A': 'T', 'B': 'U', 'C': 'V', 'D': 'W', 'E': 'X', 'F': 'Y',
             'G': 'Z', 'H': 'A', 'I': 'B', 'J': 'C', 'K': 'D', 'L': 'E',
             'M': 'F', 'N': 'G', 'O': 'H', 'P': 'I', 'Q': 'J', 'R': 'K',
             'S': 'L', 'T': 'M', 'U': 'N', 'V': 'O', 'W': 'P', 'X': 'Q',
             'Y': 'R', 'Z': 'S'},
       'U': {'A': 'U', 'B': 'V', 'C': 'W', 'D': 'X', 'E': 'Y', 'F': 'Z',
             'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F',
             'M': 'G', 'N': 'H', 'O': 'I', 'P': 'J', 'Q': 'K', 'R': 'L',
             'S': 'M', 'T': 'N', 'U': 'O', 'V': 'P', 'W': 'Q', 'X': 'R',
             'Y': 'S', 'Z': 'T'},
       'V': {'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z', 'F': 'A',
             'G': 'B', 'H': 'C', 'I': 'D', 'J': 'E', 'K': 'F', 'L': 'G',
             'M': 'H', 'N': 'I', 'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M',
             'S': 'N', 'T': 'O', 'U': 'P', 'V': 'Q', 'W': 'R', 'X': 'S',
             'Y': 'T', 'Z': 'U'},
       'W': {'A': 'W', 'B': 'X', 'C': 'Y', 'D': 'Z', 'E': 'A', 'F': 'B',
             'G': 'C', 'H': 'D', 'I': 'E', 'J': 'F', 'K': 'G', 'L': 'H',
             'M': 'I', 'N': 'J', 'O': 'K', 'P': 'L', 'Q': 'M', 'R': 'N', 
             'S': 'O', 'T': 'P', 'U': 'Q', 'V': 'R', 'W': 'S', 'X': 'T',
             'Y': 'U', 'Z': 'V'},
       'X': {'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B', 'F': 'C',
             'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I',
             'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O',
             'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U',
             'Y': 'V', 'Z': 'W'},
       'Y': {'A': 'Y', 'B': 'Z', 'C': 'A', 'D': 'B', 'E': 'C', 'F': 'D',
             'G': 'E', 'H': 'F', 'I': 'G', 'J': 'H', 'K': 'I', 'L': 'J',
             'M': 'K', 'N': 'L', 'O': 'M', 'P': 'N', 'Q': 'O', 'R': 'P',
             'S': 'Q', 'T': 'R', 'U': 'S', 'V': 'T', 'W': 'U', 'X': 'V',
             'Y': 'W', 'Z': 'X'},
       'Z': {'A': 'Z', 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E',
             'G': 'F', 'H': 'G', 'I': 'H', 'J': 'I', 'K': 'J', 'L': 'K',
             'M': 'L', 'N': 'M', 'O': 'N', 'P': 'O', 'Q': 'P', 'R': 'Q',
             'S': 'R', 'T': 'S', 'U': 'T', 'V': 'U', 'W': 'V', 'X': 'W',
             'Y': 'X', 'Z': 'Y'}}

# Affichage table Vigenère sous forme d'un tableau:
print(' ', ' '.join(vig['A']))
for k, v in vig.items():
    print(k, ' '.join(list(vig[k].values())))

########################### Message et clef ##################################

msg = 'La vie est belle'
clefCesar = 5
clefAutre = 'secret'

################################# Cesar  #####################################

# fonction qui retourne le message crypté à l’aide de la clef en partant d’un 
# message en clair
def cryptCesar(message, clef):
    
    # initialisation du message crypté
    messageCrypte = ""  
    
    for lettre in message:
        
        if lettre.isalpha(): # si c'est une lettre de l'alphabet

            # conversion du caractère en entier 
            lettrePosition = ord(lettre.lower()) - ord('a')
            
            # formule sur le décalage de lettres
            lettreChiffre = (lettrePosition + clef) % 26
            
            # conversion de l'entier à la lettre d'alphabet correspondante
            lettreAlphabet = chr(ord('a') + lettreChiffre)
            
            # si c'est la lettre du message était en majuscule                     
            if lettre.isupper():
                lettreAlphabet = lettreAlphabet.upper()               
            
            messageCrypte += lettreAlphabet  # incrémentation du message crypté
                                 
        else:
            messageCrypte += lettre  # incrémentation du message crypté
    
    # retourner le message en cryptage                             
    return messageCrypte

# fonction permettant de transformer un message crypté en un message décrypté                                
def decryptCesar(message, clef):
                                 
    # initialisation du message décrypté
    messageDecrypte = ""  
    
    for lettre in message:
        
        if lettre.isalpha():  # si c'est une lettre de l'alphabet         
            
            # conversion du caractère en entier
            lettrePosition = ord(lettre.lower()) - ord('a')
            
            # formule pour inverser le décalage de lettres
            lettreDecrypte = (lettrePosition - clef) % 26  
            
            # conversion de l'entier à la lettre d'alphabet correspondante
            lettreDecryptage = chr(ord('a') + lettreDecrypte)
            
            # si la lettre était en majuscule                     
            if lettre.isupper(): 
                lettreDecryptage = lettreDecryptage.upper()                 
                                 
            # ajout de la lettre décryptée au message
            messageDecrypte += lettreDecryptage 
            
        else:
            messageDecrypte += lettre # incrémentation du message décrypté
    
    return messageDecrypte  # retourner le message en décryptage

############################### Vigenère #####################################

# fonction qui vérifie si la lettre à la position spécifiée du mot est en
# en majuscule
def isLower(mot, ind) :

    majusculeMot = ''     # initialisation du chaine vide majusculeMot
    rep = ind % len(mot)  # s'assurer qu'on répète le mot
    
    # si le caractère est en miniscule
    if mot[rep].islower() :
        
        # changement du caractère en majuscule
        majusculeMot = mot[rep].upper()  
        
        return majusculeMot # retourne la lettre en majuscule
    
    else : # si le caractère est déjà en majuscule
        return mot[rep] # Retourne la lettre en majuscule.

# fonction qui retourne le message crypté avec l'algorithme de Vigenere
def cryptVigenere(message, clef) :
    
    crypt = '' # initialisation du chaine vide crypt
    
    # boucle pour parcourir tous les caractères du chaine message
    for posit in range(len(message)):
        
        # si le caractère est une lettre de l'alphabet
        if message[posit].isalpha() :    
            
            # stocker la lettre de la clef
            lettreClef = isLower(clef, posit)     
            
            # stocker la lettre du message
            lettreMsg = isLower(message, posit)  
            
            # stocker la valeur du dictionnaire
            lettre = vig[lettreClef][lettreMsg]
            
            # si la lettre du message est en miniscule
            if message[posit].islower() :     
                                         
                lettre = lettre.lower() # transforme en lettre minuscule.
                
            crypt += lettre # incrémentation du chaine crypt
            
        else: # si le caractère n'est pas une lettre
            crypt += message[posit]       
                                        
    return crypt # retourner la chaine crypt                         

# fonction qui retourne le message en clair à partir d'un message crypté et 
# du clef
def decryptVigenere(message, clef):

    decrypt = ''  # Initialisation d'une chaîne vide pour le message décrypté
    
    # Initialisation d'un dictionnaire pour stocker les valeurs liées à la clé
    dictClef = {}
    
    # Tableaux pour stocker temporairement les valeurs et les clés
    tabVal = []
    tabClef = []
    
    # Variables pour stocker les index des lettres dans le message et la clé
    posVal = 0     
    posClef = 0    
    
    # Boucle pour parcourir chaque caractère du message
    for position in range(len(message)):
        
        # Si le caractère actuel est une lettre de l'alphabet
        if message[position].isalpha():
            
            # Calculer la position de la clé correspondante
            repet = position % len(clef) 
            
            # Convertir la lettre de la clé à la position actuelle en majuscule
            majusClef = clef[repet].upper()
            
            # Récupérer le dictionnaire correspondant à cette lettre majuscule
            dictClef = vig[majusClef]
            
            # Extraire les valeurs du dictionnaire sous forme de liste
            tabVal = list(dictClef.values())
            
            # Vérifier si la lettre actuelle du message est en minuscule
            lettre = isLower(message, position)
        
            # Boucle pour trouver la position de la lettre dans le tableau des 
            # valeurs
            for rangee in range(26):
                if tabVal[rangee] == lettre:
                    posVal = rangee  # Stocker la position trouvée
        
            # Extraire les clés du dictionnaire sous forme de liste
            tabClef = list(dictClef.keys())
            
            # Trouver la clé correspondante à la position trouvée
            posClef = tabClef[posVal]
            
            # Si la lettre originale du message était en minuscule
            if message[position].islower():
                # Convertir la clé correspondante en minuscule
                posClef = posClef.lower()
        
            # Ajouter la lettre décryptée au message final
            decrypt += posClef
            
        # Si le caractère n'est pas une lettre (espace, chiffre, symbole, etc.)
        else:
            # Ajouter directement le caractère non alphabétique au message final
            decrypt += message[position]
    
    # Retourner le message décrypté
    return decrypt

################################# XOR ########################################

# fonction qui retourne le binaire correspondant au caractère char                                
def getBinaire(char):                                                          
     
    # si la chaine dépasse 1                            
    if len(char) > 1:  
        return("La chaine doit seulement avoir un caractère.")
    
    # si la chaine est exactement de 1
    if len(char) == 1:
        
        # retourner le caractère char en binaire sur huit bits (octet)                           
        binaire = bin(ord(char))[2:]
     
        # si la longueur du binaire n'est pas de 8                             
        while len(binaire) < 8:    
            binaire = '0' + binaire # concaténation du string binaire
                                 
        return binaire # retourner la chaine de caractères en binaire

# fonction qui permet de transformer les octets en un caractère
def getChar(binaire):
    
    # Transformer la chaîne binaire en entier décimal
    code = int(binaire)
    
    # Calculer la longueur du nombre binaire
    longueur_binaire = len(str(code))
    
    # Initialisation des variables pour la conversion
    nombre_decimal = 0  # Nombre en base 10 correspondant au binaire
    caractere = ''      # Caractère ASCII final
    dernier_chiffre = 0 # Reste de la division pour isoler chaque chiffre binaire

    # Boucle pour convertir le nombre binaire en nombre décimal
    for position in range(longueur_binaire):
        # Récupérer le chiffre à la position des unités
        dernier_chiffre = code % 10
        
        # Ajouter à nombre_decimal sa conversion en base 10, en fonction de sa position
        nombre_decimal += dernier_chiffre * 2 ** position
        
        # Enlever le dernier chiffre binaire en divisant par 10 (division entière)
        code //= 10          

    # Convertir le nombre en base 10 obtenu en caractère ASCII
    caractere = chr(nombre_decimal)
    
    # Retourner le caractère ASCII correspondant au binaire
    return caractere

# fonction qui fait l'opération XOR sur deux octets 
def opXor(char1, char2):

    xor = '' # Initialisation de la chaîne résultante XOR
    
    # Boucle pour appliquer l'opération XOR sur chaque bit
    for num in range(8):  # La longueur des chaînes binaires est de 8 bits.
        
        # Vérifie si les bits aux positions correspondantes dans les deux 
        # chaînes sont identiques
        if getChar(char1[num]) == getChar(char2[num]):
            xor += '0'  # Si les bits sont identiques, ajoute '0' au résultat
        else:
            xor += '1'  # Si les bits sont différents, ajoute '1' au résultat
    
    # Retourne la chaîne résultante après l'opération XOR
    return xor

# fonction convertit un message en binaire.
def binMsg(message):  
    
    binMsg = []  # initialisation du tableau binMsg
    
    # Mettre en binaire chaque caractère du message.
    for chiffre in range(len(message)):
        
        lettre = message[chiffre]  # Stocker la lettre à la position i.
        
         # Transformer la lettre en sa forme binaire
        binLettre = getBinaire(lettre)  
        
        # Ajouter la forme binaire au tableau binMsg
        binMsg.append(binLettre) 
    
    return binMsg  # Retourner le tableau binMsg

# fonction qui applique l'opération XOR entre chaque élément du message et de
# clef
def appXor(tabMsg, tabClef, clef):
    
    tabXor = []  # initialisation du tableau tabXor
    
    dimension = len(clef)  # longueur de clef

    # boucle pour parcourir chaque élément du tableau de message 
    for i in range(len(tabMsg)):
        
        iteration = i % dimension  #  pour faire répéter la clef
        
        # Appliquer l'opération XOR entre le message et la clé correspondante 
        xor = opXor(tabMsg[i], tabClef[iteration])
        
        # Ajouter le résultat de l'opération XOR au tableau de résultats 
        tabXor.append(xor)
    
    # Retourner le tableau contenant tous les résultats de l'opération XOR.
    return tabXor

# fonction crypte un message en utilisant l'opération XOR
def cryptXor(message, clef):
    
    # Initialisation de la chaîne vide pour le message crypté
    crypt = ''  # Initialisation de la chaîne vide pour le message crypté
    
    tabMsg = binMsg(message)  # Tableau binaire du message
    tabClef = binMsg(clef)    # Tableau binaire de la clé
    
    # Appliquer l'opération XOR entre le tableau binaire du message et du clé
    tabXor = appXor(tabMsg, tabClef, clef)  
    
    # Convertir chaque résultat en caractère et l'ajouter au message crypté
    for fois in range(len(tabXor)):  
        
        # Récupérer la lettre binaire à la position spécifiée
        binChar = tabXor[fois]  
        
        # Convertir la valeur binaire en caractère
        char = getChar(binChar)
        
        crypt += char  # incrémentation du chaine crypt
    
    return crypt # retourner le message crypté

# fonction décrypte un message en utilisant l'opération XOR 
def decryptXor(message, clef):
    
    decrypt = '' # Initialisation du message décrypté
    
    tabMsg = binMsg(message)  # Tableau binaire du message
    tabClef = binMsg(clef)    # Tableau binaire de la clé
    
    tabXor = appXor(tabMsg, tabClef, clef)  # Résultat du XOR dans un tableau
    
    # Parcourir le tableau binaire du XOR
    for numero in range(0, len(tabXor)):  
        
        binChar = tabXor[numero]  # Récupérer la lettre binaire à la position i
        
        char = getChar(binChar)  # Convertir la valeur binaire en caractère
        
        decrypt = decrypt + char  # Ajouter le caractère au message décrypté
    
    # Retourner le message décrypté
    return decrypt

############################# Tortue XOR #####################################

# Dessin tortue en trois parties
# fonction qui trace un carré dans le plan cartésien
def carre(largeur) :                 
    for cote in range(4): 
        fd(largeur)                    
        lt(90)                         

# fonction qui positionne la tortue dans le plan cartésien        
def positionner(x,y) :                 
    pu()                           
    fd(x)                             
    lt(90)                           
    fd(y)                            
    rt(90)                           
    pd()                               

# fonction qui trace la grille
def grilleLigneBin(nx, ny, y, pas, largeur, char):
    
    # Parcours des indices de 0 à 7
    for x in range(8):
        
        moitiePas = pas // 2  # Calculer la moitié du pas (taille d'un carré)
        
        # Positionner la tortue à la position (x*pas, y*pas)
        positionner(x * pas, y * pas)  
        
        # Tracer le carré de la largeur spécifiée
        carre(largeur)  
        
        # Positionner la tortue au centre du carré pour écrire le caractère
        positionner(moitiePas, moitiePas) 
        
        # Écrire le caractère binaire à cette position
        write(char[x]) 
        
        # Retourner la tortue à la position de départ du carré
        positionner(-moitiePas, -moitiePas) 
        
        # Retourner la tortue à la position de départ
        positionner(-x * pas, -y * pas)
 
# fonction qui trace une grille avec un code binaire à l'intérieur
def grilleBinaire(tabChar): 
    for y in range(3):
        grilleLigneBin(8, 3, y, 20, 20, tabChar[y])

# ---------------------------- Tests unitaires -------------------------------

# fonction des tests unitaires pour la fonction cryptCesar              
def testCryptCesar() :
    assert cryptCesar('abc', 5) == 'fgh'   # cas gérénal
    assert cryptCesar('abc', 0) == 'abc'   # cas où la valeur de clef est de 0
    assert cryptCesar(' ', 5) == ' '       # cas d'un espace
    assert cryptCesar('abc', 27) == 'bcd'  # cas d'une clef plus grande que 26
    assert cryptCesar('5', 1) == '5'       # cas d'un chiffre dans message
    assert cryptCesar('A', 5) == 'F'       # cas d'une majuscule dans message
    assert cryptCesar('abc', -2) == 'yza'  # cas d'une clef de valeur négative
    
testCryptCesar() # appel des test unitaires

# fonction des tests unitaires pour la fonction decryptCesar                  
def testDecryptCesar() :
    assert decryptCesar('fgh', 5) == 'abc'   # cas gérénal
    assert decryptCesar('abc', 0) == 'abc'   # cas avec clef de valeur nulle
    assert decryptCesar(' ',5) == ' '        # cas d'un espace dans message
    assert decryptCesar('bcd', 27) == 'abc'  # cas d'une clef supérieure à 26
    assert decryptCesar('5', 1) == '5'       # cas de la présence de chiffre
    assert decryptCesar('F',5) == 'A'        # cas d'une majuscule 
    assert decryptCesar('yza',-2) == 'abc'   # cas d'une clef négative

testDecryptCesar() # appel des test unitaires   

# fonction des tests unitaires pour la fonction isLower
def testIsLower() :
    assert isLower('AAAH',2) == 'A'   # cas majuscule
    assert isLower('aaah',2) == 'A'   # cas minuscule
    assert isLower('mot',5) == 'T'    # cas i > len(mot)
    assert isLower('mot',-2) == 'O'   # cas i < 0

testIsLower() # appel des test unitaires   

# fonction des tests unitaires pour la fonction cryptVigenere    
def testCryptVigenere() :
    assert cryptVigenere('leci','abri') == 'lftq'        # cas général
    assert cryptVigenere('lecimot','abri') == 'lftqmpk'  # cas répétition clef
    assert cryptVigenere(' ','mot') == ' '               # cas d'un espace
    assert cryptVigenere('5','mot') == '5'               # cas de chiffre
    assert cryptVigenere('A','mot') == 'M'               # cas de majuscule
    
testCryptVigenere() # appel des test unitaires

# fonction des tests unitaires pour la fonction decryptVigenere        
def testDecryptVigenere() :
    assert decryptVigenere('lftq','abri') == 'leci'       # cas général
    assert decryptVigenere('lftqmpk','abri') == 'lecimot' # cas répétition clef
    assert decryptVigenere(' ','mot') == ' '              # cas d'un espace
    assert decryptVigenere('5','mot') == '5'              # cas de chiffre
    assert decryptVigenere('M','mot') == 'A'              # cas de majuscule

testDecryptVigenere() # appel des test unitaires

# fonction des tests unitaires pour la fonction getBinaire    
def testGetBinaire() :
    assert getBinaire('A') == '01000001'   # cas d'une lettre en majuscule
    assert getBinaire('a') == '01100001'   # cas d'une lettre en minuscule
    assert getBinaire(' ') == '00100000'   # cas de présence d'un espace
    assert getBinaire('|') == '01111100'   # cas d'un autre type de caractère

testGetBinaire() # appel des test unitaires

# fonction des tests unitaires pour la procédure opXor  
def testOpXor() :
    assert opXor('01000001', '01100001') == '00100000'  # cas général
    assert opXor('00000000', '11111111') == '11111111'  # cas de rien en commun
    assert opXor('01110011', '01110011') == '00000000'  # cas où tous en commun
    
testOpXor() # appel des test unitaires

# fonction des tests unitaires pour la fonction getChar        
def testGetChar() :
    assert getChar('01000001') == 'A'   # cas de lettre en majuscule
    assert getChar('01100001') == 'a'   # cas de lettre en minuscule
    assert getChar('00100000') == ' '   # cas de présence d'un espace
    assert getChar('01111100') == '|'   # cas de présence d'un autre type

testGetChar() # appel des test unitaires

# fonction des tests unitaires pour la fonction binMsg                           
def testBinMsg() :
    
    # cas de lettres de l'alphabet
    assert binMsg('leci') == ['01101100','01100101','01100011','01101001']
    
    # cas avec un chiffre 
    assert binMsg('5a') == ['00110101','01100001']  
    
    # cas avec des caractères spéciaux et des espaces
    assert binMsg('% @ ^') == ['00100101','00100000','01000000','00100000', 
                               '01011110']
    
testBinMsg() # appel des test unitaires
    
# fonction des tests unitaires pour la fonction appXor      
def testAppXor() :
    
    # cas où les longueurs des deux chaines sont identiques
    assert appXor(['01101100','01100101'],['00110101','01100001'],
                  '5a') == ['01011001', '00000100']
    
    # cas où la longueur du message est plus petite que celle de clef
    assert appXor(['00000000'],                      
                  ['11111110','00110000'],
                  '~0') == ['11111110']
    
    # cas où la longueur du message est plus grande que celle du clef
    assert appXor(['00101111','00100101'],       
                  ['00100001'],
                  '!') == ['00001110','00000100']
    
testAppXor() # appel des test unitaires

# fonction des tests unitaires pour la procédure cryptXor    
def testCryptXor() :
    assert cryptXor('A','a') == ' '                # cas général
    assert cryptXor('5 m',                         # cas avec espace et chiffre
                    '0') == chr(5) + chr(16) + ']'
    assert cryptXor('%;','mot') == 'HT'            # cas avec autres types 
    
testCryptXor() # appel des test unitaires

# fonction des tests unitaires pour la procédure decryptXor    
def testDecryptXor() :
    assert decryptXor(' ','a') == 'A'              # cas général
    assert decryptXor(chr(5) + chr(16) + ']',      # cas avec espace et chiffre
                      '0') == '5 m' 
    assert decryptXor('HT','mot') == '%;'          # cas avec autres types

testDecryptXor() # appel des test unitaires   
    
# --------------------------------- Affichage --------------------------------

# Crypter le message pour César
print(cryptCesar(msg, clefCesar))                                               

# Crypter le message pour Vigenère
print(cryptVigenere(msg, clefAutre))

# Crypter le message pour XOR
print(cryptXor(msg, clefAutre))

# Stocker les trois premiers caractères d'un message crypté dans un tableau 
msg3Str = msg[0:2]
msg3Bin = binMsg(msg)[0:3]
msg3Xor = cryptXor(msg, clefAutre)[0:2]

# Dessiner la grille avec les trois premiers caractères sous forme d'octets
grilleBinaire(msg3Bin)