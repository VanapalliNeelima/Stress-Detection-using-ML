

## Introduction

##### In this Project I have used Naive Bayes Supervised Machine Learning Algorithm to predict the stress of a person.This Algorithm is used for mainly binary classification .This algorithm is based on Bayes Theorem . The result of this project is 1 if the stress was detected otherwise 0 for respective input.

## Steps For Creating Project

##### 1. Import numpy and pandas
##### 2. Import Dataset
##### 3. Check Description of out data
##### 4. Check if dataset contains null value or not
##### 5. Prepare the text column of this dataset to clean the text column with stopwords,links,special symbols and language errors
##### 6. View the most utilized words by individuals sharing about their life issues  via online entertainment by picturing a word cloud of the text column
##### 7. The label column in this dataset contains labels as 0 and 1. 0 means no stress, and 1 means stress. We will use Stress and No stress lables instead of 1 and 0. So lets prepare this column accordingly and select the text and label columns for the process of training a machine learning model
##### 8. Split the dataset into training and test sets
##### 9. This task is based on the problem of binary classification, We will be using the Bernoulli Naive Bayes algorithm,which one of the best algorithm for binary classification
##### 10. Test the performance of our model on some random sentences based on mental health
######  Ex:- "I think we need to take care of ourselves"
######  Ex:- "I am feeling sad"
