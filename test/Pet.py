class Pet(object):
  
  def __init__(self, name, species):
    self.name = name
    self.species = species
  
  def getName(self):
    return self.name
  
  def getSpecies(self):
    return self.species
  
  def __str__(self):
    return "%s is a %s" % (self.name, self.species)
