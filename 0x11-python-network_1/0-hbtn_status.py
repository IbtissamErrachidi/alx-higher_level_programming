#!/usr/bin/python3
"""Fetches a URL."""
import urllib.request

if __name__ == "__main__":


    # Envoyer la requête et lire la réponse
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        # Lire le contenu de la réponse
        data = response.read()
        
        # Afficher le contenu de la réponse avec le format spécifié
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))

