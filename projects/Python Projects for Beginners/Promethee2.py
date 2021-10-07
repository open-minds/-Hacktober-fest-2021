#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Authors 
        Oussama FORTAS
        Aimene BAHRI
        Ali Atmani
        Abed Kebir
"""

import sys
import numpy
import csv
import numpy as np
import time
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
np.set_printoptions(precision=3)
print("PROMETHEE 2 METHOD")

print("##################################################")
print(sys.argv[1].split('/media/')[1])
print(sys.argv[2].split('/media/')[1])
print("We will be using AHP : Analytic Hierarchy Process.")
time.sleep(3)
workpath = os.path.dirname(os.path.abspath(__file__))
print('workplace', workpath)
Matrix = np.array(list(csv.reader(open(os.path.join(workpath,sys.argv[1].split('/media/')[1]), "r"))))

print('Matrice de performance',Matrix)

print("STEP 1 : Normalize the Evaluation Matrix")
array_Matrix  = np.array(Matrix)

Alternative_matix = array_Matrix[2:,1:].astype(np.single)
print('Alternative_matix \n',Alternative_matix)

labels = array_Matrix[0,1:]
print('labels \n',labels)

Alternatives = array_Matrix[2:,0]
print('Names \n',Alternatives)

# TODO! Add beneficial and non benificial criterias
maximisation = array_Matrix[1,1:]
print('Beneficial or Not  \n',maximisation)

# Get min and max for each criteria
min_criteria_array = Alternative_matix.min(axis=0)
print('min_criteria_array \n',min_criteria_array)

max_criteria_array = Alternative_matix.max(axis=0)
print('max_criteria_array \n',max_criteria_array)


for i in range(len(Alternative_matix)):
    for j in range(len(Alternative_matix[i])):
        if maximisation[j] == 'yes':
            Alternative_matix[i][j] = (max_criteria_array[j]-Alternative_matix[i][j])/(max_criteria_array[j]-min_criteria_array[j])
        else:
            Alternative_matix[i][j] = (Alternative_matix[i][j]-min_criteria_array[j])/(max_criteria_array[j]-min_criteria_array[j])
print('Alternative_matix \n',Alternative_matix)
time.sleep(3)

print("STEP 2 : Calculate Evaluative ieme per the othere {m1-m2 | m1-m3 | ....}")
# Create the Alternatives Possibilities array[m1-m2,........]
def all_alternatives(Alternatives):
    Alternative_possibilities = []
    for i in range(len(Alternatives)):
        for j in range(len(Alternatives)):
            if i == j:
                pass
            else:
                Alternative_possibilities.append(Alternatives[i]+'-'+Alternatives[j])
    return np.array(Alternative_possibilities).reshape(len(Alternative_possibilities),1)
Alternative_possibilities = all_alternatives(Alternatives)
print('Alternative_possibilities \n', Alternative_possibilities)
time.sleep(3)

# create the matrix of all variables possibilities:
def all_variables(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                pass
            else:
                new_matrix.append(matrix[i]-matrix[j])
    return np.array(new_matrix)

variables_possibilities = all_variables(Alternative_matix)
print('variables_possibilities \n', variables_possibilities)
time.sleep(3)
print('Alternative_possibilities shape \n', Alternative_possibilities.shape)
print('variables_possibilities shape \n', variables_possibilities.shape)

# concatenate the Names and variables related 
the_all_matrix = np.hstack([Alternative_possibilities, variables_possibilities])
print('The All Matrix \n', the_all_matrix)
time.sleep(3)
print("STEP 3 : Calculate the PREFERENCE Function")
# Create an updated matrix that return 0 if value is negative or equal to 0 
# else keep value as it it
def changetozeros(matrix):
    for i in range(len(matrix)) :  
        for j in range(len(matrix[i])) :  
            if matrix[i][j] < 0 :
                matrix[i][j] = 0
    return matrix

Preference_matrix = changetozeros(variables_possibilities)
print('PREFERENCE_matrix \n', Preference_matrix)
time.sleep(3)
# concatenate the Names and preferences related 
the_Preference_matrix = np.hstack([Alternative_possibilities, Preference_matrix])
print('the_Preference_matrix \n', the_Preference_matrix)

# calculate the aggregated preferenbce function
# hna nedourbou f les poids(weights)
# lets call the weights from a csv file
# if sys.argv[1] == 1:
#     weights =list(csv.reader(open("weights_decideur1(politicien).csv", "r"), delimiter=","))
# elif sys.argv[1] == 2:
#     weights =list(csv.reader(open("weights_decideur2(economist).csv", "r"), delimiter=","))
# elif sys.argv[1] == 3:
#     weights =list(csv.reader(open("weights_decideur3(Représentant de l’environnement).csv", "r"), delimiter=","))
# elif sys.argv[1] == 4:
#     weights =list(csv.reader(open("weights_decideur4(Représentant du public).csv", "r"), delimiter=","))
# else:
#     print('Choisissez un des Decideur 1__4')
#     exit(0)
# weights =list(csv.reader(open("weights_decideur2(economist).csv", "r"), delimiter=","))
weights =list(csv.reader(open(os.path.join(workpath,sys.argv[2].split('/media/')[1]), "r")))

print('weights \n', weights)
array_weights = np.asarray(weights[0], dtype='float')
print('array_weights \n', array_weights)
time.sleep(3)
# lets create a fucntion to mult the weights with the matrix of preferences variables
def mult_matrix_vect(matrix, weight):
    for i in range(len(matrix)) :  
        for j in range(len(matrix[i])) :  
            matrix[i][j] = matrix[i][j]* weight[j]
    return matrix
# TODO: Check this multyplie function
def show_mult_matrix_vect(matrix, weight):
    data = []
    for i in range(len(matrix)) :  
       
        for j in range(len(matrix[i])) : 
           
            data.append('{}*{}'.format(weight[j],matrix[i][j]))
    return np.array(data)

Agregate_preference_matrix = mult_matrix_vect(Preference_matrix, array_weights)
show_calculation = show_mult_matrix_vect(Preference_matrix, array_weights)

print('show_calculation \n', show_calculation)
print('Agregate_preference_matrix \n', Agregate_preference_matrix)
time.sleep(3)
# lets add a column to sum these aggregated preferences
def add_aggregated_preferences_line(matrix):
    average_line_weight = []
    
    for i in range(len(matrix)) :
        sum = 0  
        for j in range(len(matrix[i])) :
            sum = sum + matrix[i][j] 
        average_line_weight.append(sum)
        
    matrix = np.vstack([matrix.transpose(), average_line_weight]).transpose()
    return matrix

Agregate_preference_matrix_with_sum = add_aggregated_preferences_line(Agregate_preference_matrix)
print('Agregate_preference_matrix_with_sum \n', Agregate_preference_matrix_with_sum)
time.sleep(3)
aggrsums = Agregate_preference_matrix_with_sum[:,-1]
print(aggrsums)
# take only the aggragated sum values(LAST column) and create aggregated preference Function(matrix)
def create_aggregated_matrix(matrix, aggr):
    # retrieve only the aggregated column(list)
    aggregate_column = np.array(matrix[:, -1].transpose())
    agrs = aggr.tolist()
    print(aggregate_column)
    print("type of aggregate_column")
    print(type(aggregate_column))
  #  aggregated_matrix  = [[len(Alternatives), len(Alternatives) ]]
    #hada el hmar ghadi ylez madam les valeurs yethattou
   # print(np.array(aggregated_matrix).shape)
    for i in range(len(aggregated_matrix)) :  
        for j in range(len(aggregated_matrix[i])) :       
            if i == j:
                aggregated_matrix[i][j] = 0        
            else:  
                aggregated_matrix[i][j]= agrs[0]
                agrs.pop(0) 
            
                
                # aggregated_matrix.append(aggregate_column[j])
    # print('lol',aggregated_matrix)
    print(np.array(aggregated_matrix).shape)
    return aggregated_matrix
    
aggregated_matrix = np.zeros((len(Alternatives), len(Alternatives)))

print("len alternatives")
created_aggregated_matrix = create_aggregated_matrix(aggregated_matrix, aggrsums)

print("HADA created_aggregated_matrix")
print(created_aggregated_matrix)
time.sleep(3)
duplicated = created_aggregated_matrix
#flot entrant w sortant
def sumColumn(matrice):
    return [sum(col) for col in zip(*matrice)] 

sommeeecolonne= sumColumn(created_aggregated_matrix)

sumrows = np.sum(created_aggregated_matrix, axis = 1)
#we need to deivde those calculated values on the number of alternatives -1
newsommecolonne = []
newsumrow= []
for x in sommeeecolonne:
    newsommecolonne.append(x /(len(created_aggregated_matrix) - 1))

for x in sumrows:
    newsumrow.append(x /(len(created_aggregated_matrix) - 1))
   
print("flots entrants \n" , newsommecolonne)
print("flots sortants \n" , newsumrow)

created_aggregated_matrix = np.vstack([created_aggregated_matrix, newsumrow])
print("updated matrix with columns ")
print(created_aggregated_matrix)

newsommecolonne.append(0)
created_aggregated_matrix= np.vstack([created_aggregated_matrix.transpose(), newsommecolonne]).transpose()
print("created_aggregated_matrix kamel\n", created_aggregated_matrix)


#here i'll be using a function to calculate the flots 
def calculateflows(matrix):
    diffs=[]
    for i in range(len(matrix)):
        diffs.append(matrix[i,-1] - matrix[-1, i])
    return diffs

print("flowscreated_aggregated_matrix")
differencesflots = calculateflows(created_aggregated_matrix)
print(differencesflots)


alt = np.append(Alternatives, " ")
duplicated = np.vstack([alt, created_aggregated_matrix.transpose()])
#so far created_aggregated_matrix is transposed 


# def remove_last_element(arr):
#     return arr[np.arange(arr.size - 1)]
# fachnhat = remove_last_element(fachnhat)

talyabachtetsetef  = np.vstack([duplicated, differencesflots]).transpose()
print("sma3")

print("##############")
with numpy.printoptions(threshold=numpy.inf):
    print(talyabachtetsetef[:-1,:])

# Sort 2D numpy array by first column
sortedArr = talyabachtetsetef[talyabachtetsetef[:,-1].argsort()]
print('Sorted 2D Numpy Array')
print("##############")
with numpy.printoptions(threshold=numpy.inf):
    print(np.flipud(sortedArr))
print("Final Sort is : ")
print(sortedArr[:,0])

