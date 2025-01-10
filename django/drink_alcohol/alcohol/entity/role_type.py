from django.db import models
from enum import Enum


class RoleType(Enum):
    BEER = "BEER"
    WHISKEY = "WHISKEY"
    WINE = "WINE"


    def __str__(self):
        return self.value


