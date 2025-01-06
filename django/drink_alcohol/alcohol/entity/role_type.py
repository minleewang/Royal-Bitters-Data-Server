from django.db import models
from enum import Enum

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
class RoleType(Enum):
    BEER = "BEER"
    WHISKEY = "WHISKEY"
    WINE = "WINE"

    def __str__(self):
<<<<<<< Updated upstream
        return self.value
=======
        return self.value
>>>>>>> Stashed changes
