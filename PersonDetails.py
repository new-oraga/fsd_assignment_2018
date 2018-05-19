# -*- coding: UTF-8 -*-
import time
from Person import Person


class PersonDetails():
    def __init__(self, name, type , ferryId):
        self.name = name
        self.type = type
        self.ferryId = ferryId
        self.time = time.strftime('%d %b %Y', time.localtime(time.time()))
