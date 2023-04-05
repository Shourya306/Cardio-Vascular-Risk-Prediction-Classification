# Cardiovascular Risk Prediction

## Abstract:

Healthcare is an inevitable task to be done in human life. Cardiovascular disease is a broad category for a range of diseases that are affecting heart and blood vessels. The early methods of forecasting cardiovascular diseases helped in making decisions about the changes to have occurred in high-risk patients which resulted in the reduction of their risks. The healthcare industry contains lots of medical data, therefore machine learning algorithms are required to make decisions effectively in the prediction of heart diseases.

## Problem Statement:

The dataset is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has a 10-year risk of future coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes. Each attribute is a potential risk factor. There are demographic, behavioural, and medical risk factors.

## Attribute Information:

**Sex**: male or female("M" or "F")

**Age**: Age of the patient

**Is_smoking**: whether or not the patient is a current smoker ("YES" or "NO")

**Cigs Per Day**: the number of cigarettes that the person smoked on average in one day.

**BP Meds**: whether or not the patient was on blood pressure medication 

**Prevalent Stroke**: whether or not the patient had previously had a stroke 

**Prevalent Hyp**: whether or not the patient was hypertensive

**Diabetes**: whether or not the patient had diabetes 

**Tot Chol**: total cholesterol level 

**Sys BP**: systolic blood pressure 

**Dia BP**: diastolic blood pressure

**BMI**: Body Mass Index

**Heart Rate**: heart rate

**Glucose**: glucose level

**Education**: education level of a person.

**The 10-year risk of coronary heart disease (CHD)**(binary: “1”, means “Yes”, “0” means “No”): Informs us whether that person has a 10-year risk of CHD or not.

## Introduction:

Heart disease is a catch-all phrase for a variety of conditions that affect the heart’s structure and how it works. Coronary heart disease is a type of heart disease where the arteries of the heart cannot deliver enough oxygen-rich blood to the heart. It is the leading cause of death in the United States. About 18.2 million American adults have coronary artery disease, making it the most common type of heart disease in the United States, according to the Centers for Disease Control and Prevention.

The cause of coronary heart disease depends on the type. Coronary artery disease is often caused by cholesterol, a waxy substance that builds up inside the lining of the coronary arteries forming plaque. This buildup can partially or totally block blood flow in the large arteries of the heart. Coronary microvascular disease happens when the heart’s tiny blood vessels do not work normally. For most people, coronary heart disease is preventable with a heart-healthy lifestyle.

Symptoms of coronary heart disease may be different from person to person even if they have the same type of coronary heart disease. However, because many people have no symptoms, they do not know they have coronary heart disease until they have chest pain, blood flow to the heart is blocked causing a heart attack, or the heart suddenly stops working, also known as cardiac arrest.

## Models Used: 

1. Logistic Regression:

Logistic regression is a classification algorithm that predicts the probability of an outcome that can only have two values (i.e. a dichotomy). A logistic regression produces a logistic curve, which is limited to values between 0 and 1. Logistic regression models the probability that each input belongs to a particular category. Logistic regression is an excellent tool known for classification problems, which are problems where the output value that we wish to predict only takes on only a small number of discrete values. Here we'll focus on the binary classification problem, where the output can take on only two distinct classes.

Assumptions of logistic regression:
* Binary logistic regression requires the dependent variable to be binary and ordinal logistic regression requires the dependent variable to be ordinal.
* Logistic regression requires the observations to be independent of each other.  In other words, the observations should not come from repeated measurements or matched data.
* Logistic regression requires there to be little or no multicollinearity among the independent variables.  This means that the independent variables should not be too highly correlated with each other. 

2. K-nearest Neighbors:

K-nearest neighbours (kNN) is a supervised machine learning algorithm that can be used to solve both classification and regression tasks. kNN as an algorithm seems to be inspired by real life. People tend to be affected by the people around them. Our behaviour is guided by the friends we grew up with. Our parents also shape our personalities in some ways. If you grow up with people who love sports, it is highly likely that you will end up loving sports. There are of course exceptions. KNN works in a similar fashion.


Below are the steps involved in KNN:

Step-1: Select the number K of the neighbours

Step-2: Calculate the Euclidean distance of K number of neighbours

Step-3: Take the K nearest neighbours as per the calculated Euclidean distance.

Step-4: Among these k neighbours, count the number of the data points in each category.

Step-5: Assign the new data points to that category for which the number of neighbours is maximum.

Step-6: Our model is ready.

Characteristics of kNN
* K-Nearest Neighbors is one of the simplest supervised learning algorithms.
* KNN algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the     available categories.
* KNN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be     easily classified into a good suite category by using the kNN algorithm.
* KNN algorithm can be used for regression as well as for classification problems.
* KNN is a non-parametric algorithm, which means it does not make any assumption on underlying data.
* It is also called a lazy learner algorithm because it does not learn from the training set immediately instead it stores the dataset and at the time of   classification, it performs an action on the dataset.
* KNN algorithm at the training phase just stores the dataset and when it gets new data, then it classifies that data into a category that is much         similar to the new data.

## Model Deployment:

Deployed the model on streamlit cloud. 
The link for the same [Streamlit app](https://shourya306-supervised-machine-learning-classificatio-app-daxohx.streamlit.app/)

Link to Docker Image [Docker Image](https://hub.docker.com/repository/docker/shourya306/classification_project/general)


## Conclusion:

After implementing two models for the classification task I came to the conclusion that using KNN would provide fruitful results.








