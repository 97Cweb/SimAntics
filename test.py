# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 13:12:44 2025

@author: 97cweb
"""

from steamworks import STEAMWORKS

steamworks = STEAMWORKS()
steamworks.initialize()
my_steam64 = steamworks.Users.GetSteamID()
