# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:44:16 2019

@author: Alexis Bautista
"""



import twint
import nest_asyncio

#Para evitar que de errores a la hora de obtener los tweets, es decriq ue vengan de forma asíncrona
nest_asyncio.apply()

# Configure
c = twint.Config()
c.Username = "aeb_bautista"
c.Search = "#osint"
c.Format = "Tweet id: {id} | Tweet: {tweet}"

twint.run.Search(c)
#Seguidores
c.Limit = 20
twint.run.Followers(c)
# Siguiendo

twint.run.Following(c)

#Favourites 
twint.run.Favorites(c)


#tweets de un usuario.
twint.run.Profile(c)

#Obtener información de un usuario
twint.run.Lookup(c)


twint.run.Search(c)
tweets = twint.output.tweets_object



c = twint.Config()

c.Username = 'noneprivacy'
c.Limit = 10
c.Store_object = True

twint.run.Search(c)
tweets = twint.output.tweets_object



c = twint.Config()

c.Username = 'aeb_bautista'
c.Store_object = True
c.User_full = True
twint.run.Followers(c)
followers = twint.output.user_object




