#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Imports

import http.client
import json

#Welcome message
print('Bienvenue dans ED-Class-Fetcher =) ! Script Développé par Clément Boittin et Noé Busson')

#Asks to User

username = str(input("Veuillez entrer votre nom d'utilisateur École Directe: "))
password = str(input("Veuillez entrer votre mot de passe École Directe: "))

#Requête HTTPS

conn = http.client.HTTPSConnection("api.ecoledirecte.com")

payload = 'data={"identifiant":'+f'"{username}"'+',"motdepasse":'+f'"{password}"'+'}'

headers = {
                'authority': 'api.ecoledirecte.com',
                'accept': 'application/json, text/plain, */*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-gpc': '1',
                'origin': 'https://www.ecoledirecte.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.ecoledirecte.com/',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
              }

conn.request("POST", "/v3/login.awp", payload, headers)
res = conn.getresponse()
data = res.read()

#Récupération du code de la classe de l'utilisateur

try:
    classe = json.loads(data.decode("utf-8"))['data']['accounts'][0]['profile']['classe']['code']
    print("Le code de votre classe est... ", classe,", vous êtes donc dans la même classe que tous les élèves possédant le même code.\nMerci d'avoir utilisé ED-Class-Fetcher:)")
except:
    print("L'authentification a échoué...\nVeuillez vérifier que vos identifiants sont corrects. \nSi le problème persiste vérifiez qu'École Directe soit en mode année (affichage de tous les module utilisés durant l'année)\nMerci d'avoir utilisé ED-Class-Fetcher:)")

