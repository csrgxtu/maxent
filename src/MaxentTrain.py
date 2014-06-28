#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 25/Jun/2014
# File: MaxentTrain.py
# Des: train state of the Maximum Entropy
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
  if len(sys.argv) != 4:
    print "Usage: MaxentTrain.py features.mat labels.mat modelName"
    sys.exit(1)
  
  features = featureMatrice(sys.argv[1])
  labels = labelLst(sys.argv[2])
  
  model = MaxentModel()
  # add data into model
  model.begin_add_event()
  for i in range(len(labels)):
    model.add_event(features[i], str(labels[i]), 1)
  
  model.end_add_event()
  
  # start training
  #model.train()
  model.train(1000, "gis", 2)
  #model.train(30, "lbfgs")
  
  # save the model
  model.save(sys.argv[3])


if __name__ == "__main__":
  main()
