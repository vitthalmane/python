import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matirx
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def VitthalTitanicLogistic():
    #step 1 Load dataset
    titanic_data = pd.read_csv("MarvllouTitanicDataset.csv")

    print("First 5 entries from loaded data")
    print(titanic_data.head())
    
    print("Number of passengers are",+str(len(titanic_data)))

    #step 2 Analyze data
    print("Visualization:Servied and non survied passengers")
    figure()
    target="Survied"

    countplot(data=titanic_data, x=target).set_title(
        " Survied and non survied passengers ")
    show()

    print("Visualization:Servied and non survied passengers based on gender")
    figure()
    target="Survied"
    countplot(data=titanic_data, x=target,hue="Sex").set_title("Survied and non survied passengers Based on Gender")
    show()

    print("Visualization:Servied and non survied passenger class")
    figure()
    target="Survied"

    countplot(data=titanic_data, x=target,hue="Pclass").set_title("Survied and non survied passengers Based on Passenger class")
    show()

    print("Visualization:Servied and non survied passenger based on Age")
    figure()
    titanic_data['Age'].plot.hist().set_title("Survied and non survied passengers Based on Age")
    show()

    print("Visualization:Servied and non survied passenger based on Fair")
    figure()
    titanic_data['Fare'].plot.hist().set_title("Survied and non survied passengers Based on Fare")
    show()


    #step 3 Data Cleaning
    titanic_data.drop("Zero",axis=1,inplace=True)

    print("First 5 entries from loaded dataset after removing zero column")
    ptint(titanic_data.head(5))

    print("Value of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("values of Sex column after removing one field")
    Sex=pd.get_dummies(titanic_data["Sex"],drop_first=True)
    print(titanic_data.head(5))

    print("values of Pclass column after removing one field")
    Pclass=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    print(titanic_data.head(5))

    print("values of data set after concatenating new columns")
    titanic_data=pd.concat([titanic_data,Sex,Pclass],axis=1)
    print(titanic_data.hrad(5))

    print("Values of data set after removing irrelevent columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis=1, inplace=True)
    print(titanic_data.head(5))

    x=titanic_data.drop("Survied",axis=1)
    y=titanic_data["Survied"]

    #step 4 Data Traing
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)

    logmodel=LogisticRegression()
    
    logmodel.fit(xtrain,ytrain)


    #step 5 Data Testing
    prediction=logmodel.predict(xtest)

    #step 6 Calculate accuracy
    print("Classification report of Logistic Regression is :")
    print(classification_report(ytest,prediction))

    print("Oonfusion matirx of Logistic Regression is :")
    print(confusion_matrix(ytest,prediction))
                                                               
    print("Accuracy of Logistic Regression is :")
    print(accuracy_score(ytest,prediction))

def main():
    print("-----------------Start-------------")

    print("Supervised machine Learning")
    print("Logistic Regression on Titanic data set")

    VitthalTitanicLogistic()

if __name__=="__main__":
    main()
                                                               
                                                               
    
        

    
                                                                
                                                                
            
    












