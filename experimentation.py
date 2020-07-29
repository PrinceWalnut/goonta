"""

This is a file to be used for experimentation purposes ONLY. All actual software should be packaged as such.

"""

from TikTokApi import TikTokApi
import numpy as np
import pandas as pd
import matplotlib as mpl
import tensorflow as tf

# Initialize some values
api = TikTokApi()
puke = api.getUser(username='slowpuke')
uid = puke.get('userInfo').get('user').get('id')

def get_users_creator_suggested_to(num_users)
    # Get a list of users that the creator is suggested to

def get_correlated_music(num_sounds)
    # Get TikTok sounds most suggested to users that the creator is suggested to
    
