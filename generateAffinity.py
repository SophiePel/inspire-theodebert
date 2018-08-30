# coding: utf-8
"""
Created on Wen Feb 14 2018

@author: Sophie Pelisson
"""
# Importation des packages nécessaires au fonctionnement du programme
import pandas as pd                   # package d'outils de traitement pour tableaux stat
import numpy as np                    # package d'outils pour l'analyse numérique
import selection_base as sb
#import boost

################################################################################

# Connexion à la base de données MongoDB
# retourne une variable db permettant d'accéder à la base de données
u,pistes,favoris = sb.input_theodebert()

################################################################################

# Sélection des inscrits depuis septembre 2017
mask = (u['createdAt']>='2017-09-01')
u = u.loc[mask]

# Sélection des utilisateurs ayant un compte actif 
prof = u['profile'].apply(pd.Series)
act = prof[prof['status']=='actif']
actecl = act[act['role']=='eclaireur'] # index des éclaireurs
actly = act[act['role']=='lyceen']     # index des lycéens

# Séparation des groupes par filières de bac
list_lyc_general =  actly[actly['filiere'].isin(['SVT','SI','EAT','ES','L'])].index.tolist()
list_ecl_general = actecl[actecl['filiere'].isin(['SVT','SI','EAT','ES','L'])].index.tolist()

list_lyc_techno = actly[actly['filiere'].isin(['STMG','STI2D','ST2S','STL','STAV','STD2A','STHR','hotellerie','TMD'])].index.tolist()
list_ecl_techno = actecl[actecl['filiere'].isin(['STMG','STI2D','ST2S','STL','STAV','STD2A','STHR','hotellerie','TMD'])].index.tolist()

list_lyc_pro = actly[actly['filiere'].isin(['bac_pro','Autres'])].index.tolist()
list_ecl_pro = actecl[actecl['filiere'].isin(['bac_pro','Autres'])].index.tolist()

# Tableau des éclaireurs et de leur pistes associées
ecl_G_pistes = u['profile'][list_ecl_general].apply(pd.Series)
ecl_G_pistes = ecl_G_pistes['pisteId']
ecl_G_id = u['_id'][list_ecl_general]
ecl_G = pd.concat([ecl_G_id,ecl_G_pistes],axis=1)

ecl_T_pistes = u['profile'][list_ecl_techno].apply(pd.Series)
ecl_T_pistes = ecl_T_pistes['pisteId']
ecl_T_id = u['_id'][list_ecl_techno]
ecl_T = pd.concat([ecl_T_id,ecl_T_pistes],axis=1)

ecl_P_pistes = u['profile'][list_ecl_pro].apply(pd.Series)
ecl_P_pistes = ecl_P_pistes['pisteId']
ecl_P_id = u['_id'][list_ecl_pro]
ecl_P = pd.concat([ecl_P_id,ecl_P_pistes],axis=1)

# Tableau des lycéens et des résultats donnés par Gondebaud
lyc_G_result = u['algoResults'][list_lyc_general].dropna()
lyc_G_id = u['_id'][list_lyc_general]

# Importation des favoris des lycéens
fav_G = favoris.ix[list_lyc_general].dropna()
fav_T = favoris.ix[list_lyc_techno].dropna()
fav_P = favoris.ix[list_lyc_pro].dropna()



