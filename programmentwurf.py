#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
import pgmpy.inference
import pickle
from time import sleep
import sys

# Data Preperation Helper Functions
# More Information available in iPython Notebook

def normalizeKindAge(age):
    if age == "n.a.":
        return "n.a.";
    elif int(age) < 10:
        return "<10"
    elif int(age) < 18:
        return "<18"
    elif int(age) < 25:
        return "<25"
    else:
        return ">25"

def normalizeIncome(income):
    income = int(income)
    if income < 20000:
        return "<20000"
    elif income < 40000:
        return "<40000"
    elif income < 80000:
        return "<80000"
    elif income < 100000:
        return "<100000"
    else:
        return ">100000"

def aboard(message):
    print(message)
    sys.exit(0)

def main():
    
    print("Searching for bayesan_model.p\n Loading Bayesan Model\n\n")
    try:
        model_recover = pickle.load(open("bayesian_model.p", "rb"))
    except:
        aboard("Error loading model. Aborting.")
    
    print("Success\n\nOpening valuation data...\n")
    try:
       validation_data = pd.read_csv('versicherung_validation.csv', delimiter=';')
    
       validation_data = validation_data.drop(columns=["Tarif"])
       validation_data['aeltestesKind'] = validation_data['aeltestesKind'].apply(normalizeKindAge)
       validation_data['juengstesKind'] = validation_data['juengstesKind'].apply(normalizeKindAge)
       validation_data['Familieneinkommen'] = validation_data['Familieneinkommen'].apply(normalizeIncome)
    except:       
        aboard("Could not read file and/or prepare data")
    print("Predicting Tarif:\n\n")
    print(model_recover.predict(validation_data))

 
if __name__ == "__main__":
	main()