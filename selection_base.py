# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 2018

@author: Sophie Pelisson
"""
import pymongo
import pandas as pd

# Connexion à la base de données MongoDB
# retourne une variable db permettant d'accéder à la base de données
#
def input_theodebert():
    uri = "mongodb://inspire-readonly:I9xsZX1VpPyqJZwL@inspire-production-shard-00-00-pmah6.mongodb.net:27017,inspire-production-shard-00-01-pmah6.mongodb.net:27017,inspire-production-shard-00-02-pmah6.mongodb.net:27017/inspire?ssl=true&replicaSet=inspire-production-shard-0&authSource=admin"
    client = pymongo.MongoClient(uri)
    db = client.inspire                 # selection de la base de données

    coll_users = db['users']            # collection des utilisateurs => regroupe l'ensemble des données de profil
    coll_pistes = db['pistes']          # collection des pistes d'études
    coll_fav = db['piste-feedback']     # collection contenant les pistes favorites des élèves

    # Création des dataframes contenant les données d'intérêt de chaque collection ci-dessus
    u = pd.DataFrame(list(coll_users.find()),columns=['_id','createdAt','profile','algoResults'])
    pistes = pd.DataFrame(list(coll_pistes.find()),columns=['_id','name','deleted'])
    favoris = pd.DataFrame(list(coll_fav.find()),columns=['pisteId','userId'])

    return u,pistes,favoris
################################################################################
