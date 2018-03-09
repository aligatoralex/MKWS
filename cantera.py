from cantera import cantera
gas = cantera.Solution('gri30.cti')
h2o = cantera.PureFluid('liquidvapor.cti', 'water')
