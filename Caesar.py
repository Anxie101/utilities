import os

def lire_texte_entree(texte_entree):
    # Si texte_entree est un chemin vers un fichier, lire le fichier et retourner son contenu
    if os.path.isfile(texte_entree):
        with open(texte_entree, 'r') as f:
            return f.read()
    # Sinon, considérer texte_entree comme étant le texte lui-même
    return texte_entree

def chiffrement_cesar(texte_entree, decalage):
    texte_clair = lire_texte_entree(texte_entree)
    texte_chiffre = ""
    for char in texte_clair:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            # Applique le décalage en tenant compte de la casse
            if char.isupper():
                texte_chiffre += chr((ord(char) - 65 + decalage) % 26 + 65)
            else:
                texte_chiffre += chr((ord(char) - 97 + decalage) % 26 + 97)
        else:
            texte_chiffre += char  # Conserve les caractères non alphabétiques
    return texte_chiffre

# Exemple d'utilisation
texte_entree = input("Entrez le texte à chiffrer ou le chemin du fichier texte : ")
decalage = int(input("Entrez le décalage : "))
texte_chiffre = chiffrement_cesar(texte_entree, decalage)
print("Texte chiffré:", texte_chiffre)
