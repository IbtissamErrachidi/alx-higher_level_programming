#!/usr/bin/python3
"""Script to fetch X-Request-Id variable from response header"""
import urllib.request
import sys

if __name__ == "__main__":
    # Récupérer l'URL depuis les arguments de la ligne de commande
    url = sys.argv[1]

    # Créer une requête et envoyer la requête à l'URL spécifiée
    with urllib.request.urlopen(url) as response:
        # Récupérer la valeur de l'en-tête X-Request-Id
        x_request_id = response.getheader('X-Request-Id')

        # Afficher la valeur de l'en-tête X-Request-Id
        print(x_request_id)

