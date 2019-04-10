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

def abort(message):
    print(message)
    sys.exit(0)

def main():

    print("Searching for bayesan_model.p\n Loading Bayesan Model\n\n")
    try:
        model_recover = pickle.load(open("bayesian_model.p", "rb"))
    except:
        abort("Error loading model. Aborting.")

    print("Success\n\nOpening valuation data...\n")
    try:
        validation_data = pd.read_csv('versicherung_validation.csv', delimiter=';')

        # Remove the column that we want to predict
        if "Tarif" in validation_data:
            validation_data = validation_data.drop(columns=["Tarif"])

        # Cluster continuous data
        if 'aeltestesKind' in validation_data:
            validation_data['aeltestesKind'] = validation_data['aeltestesKind'].apply(normalizeKindAge)

        if 'juengstesKind' in validation_data:
            validation_data['juengstesKind'] = validation_data['juengstesKind'].apply(normalizeKindAge)

        if 'Familieneinkommen' in validation_data:
            validation_data['Familieneinkommen'] = validation_data['Familieneinkommen'].apply(normalizeIncome)
    except:
        abort("Could not read file and/or prepare data")

    print("Predicting Tarif & appending to new 'prediction tarif' column:\n\n")
    prediction = model_recover.predict(validation_data)
    validation_data["Predicted Tarif"] = prediction["Tarif"]
    print(validation_data)


    print("\n\nPrinting out CPDs to cpd_exp.txt")
    cpds = model_recover.get_cpds()

    # Create and/or cleanup file
    open("cpd_exp.txt", "w").write('')

    for cpd in cpds:
        open("cpd_exp.txt", "a").write(cpd._make_table_str())

if __name__ == "__main__":
    main()
