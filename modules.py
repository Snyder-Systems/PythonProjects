#use modules to better organize code
import converters #name of the module to be imported is converters.py, imports entire module
from converters import lb_to_kg #imports a specific function

converters.kg_to_lbs(70) #used import in line 1

lb_to_kg(70) #used with from converters import