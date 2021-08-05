"""
Break the Flask Initialisation into a separate file
"""

#Create the App
import xss_trainer.meta
#And import the main application
from xss_trainer.views import *
