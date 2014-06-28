#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 25/Jun/2014
# File: MaxentTrain.py
# Des: test the maximum entropy model
#
# Produced By CSRGXTU
import sys
import numpy as np
from maxent import MaxentModel


# featureMatrice
# load feature matrice from file
#
# @param absPath abs path to the feature matrice file
# @return features list
def featureMatrice(absPath):
  # check out the parameter
  
  return np.loadtxt(absPath, delimiter=',').tolist()

# labelLst
# load labels into list
#
# @param absPath abs path to the labels matrice file
# @return labels list
def labelLst(absPath):
  # check out the param
  
  return np.loadtxt(absPath).tolist()


# main
# main method that glue everything up
def main():
  if len(sys.argv) != 2:
    print "Usage: MaxentTest.py modelName"
    sys.exit(1)
  
  model = MaxentModel()
  model.load(sys.argv[1])
  context = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  label = model.eval(context, str(0))
  #result = model.eval_all(context)
  print "Result: ", label

if __name__ == "__main__":
  main()
