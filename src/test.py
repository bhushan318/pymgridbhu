from  MicrogridGenerator_edit import MicrogridGenerator as  MicrogridGenerator1
from MicrogridGenerator import MicrogridGenerator

mg1 = MicrogridGenerator1(arch={'PV': 1, 'battery':1, 'genset':0, 'grid':1})

mg1.generate_microgrid()
mg = MicrogridGenerator()
mg.generate_microgrid()