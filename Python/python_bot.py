#! /usr/bin/python

from config import getAPI
import os

api = getAPI()

def postStatus(update):
    status = api.PostUpdate(update)
    print(status)

postStatus("tweet")