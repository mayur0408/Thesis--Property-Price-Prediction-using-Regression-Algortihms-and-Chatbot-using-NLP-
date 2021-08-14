# Thesis : Property Price Prediction using Regression Algortihms and Chatbot using NLP
This is my final year thesis “Property Price Prediction Using Regression Algorithms, Chatbot using NLP”  which is a free to use dynamic website which helps people find approximate prices of their desired property in Mumbai, Thane and nearby localities based on various features user wants like number of rooms, location, area, car parking availability, lift availability and 12 other features by using regression ML model. Apart from that we also developed a fairly intelligent chat bot which could give response to certain specific commands related to website and also has knowledge about politics, sports, joke, humors and various other field. All this features are provided to user with a minimalist dynamic front end which scales automatically depending on laptop or mobile screen aspect ratio and developed using HTML and CSS. 

We also published a technical reseearch paper on our bachelor's thesis : https://www.ijrar.org/viewfull.php?p_id=IJRAR1CCP017 , alternatively you can view "**Final_Published_Paper.pdf**". 

## Folder/Project structure explanation :

1. For training we used dataset which was uploaded on kaggle : https://www.kaggle.com/sameep98/housing-prices-in-mumbai ,alternatively you can also download "**Dataset1.csv**" file.
2. For prediction of property prices we tried various regression machine learning algorithms like **linear regression, k nearest neighours, decision tree, random forest regression, ada boost and gradiant boosting**. We settled with **random forest regression** at the end for model creation as it gave us the maximum **accuracy of 92% (R2 Score)**. All the steps involved in model creation like **exploratory data analysis(EDA), data transformation(log transformation), data visualization** and **model traning** is done in "**propertypriceprediction5.ipynb**" jupyter notebook. Alternatively you can direclty download the ready model file named "**Final_model.pickle**".
3. For front end development we used **HTML** and **CSS**. While for the backend and communication with the website we used **Flask**. For working with Flask it is manditory to have static and template folder structure.
4. The "**template**" folder contains all the HTML codes for all website pages.
5. The "**static**" folder contains all the CSS codes and images used on the website pages.
6. The "**data**" folder has training data on which our chatbot is trained.
7. The "**server.py** and **util.py**" is the python file on which we run our server and data preprocessing is done.
8. The SQLlite and others folder are created while training machine laerning model for property price prediction,chatbot and while installing python in virtual envieronment. 

## Overview

Some visualization to explain our dataset.

![Heatmap_satelliteview](https://user-images.githubusercontent.com/55938093/129437982-692ca7cf-7b7c-4452-bd6e-668dae4a3832.png)

Prices of property depends on the locations. In the heatmap we have green colour representing affordable houses (Outskirts of Mumbai) and yellow colour represents medium priced houses (Central Mumbai) while red represents extremely high priced houses (South Mumbai).

## For running the Flask app :

1. Clone repository to your local directory.
2. Make sure you have python and all the necessary libraries installed on your system. All the required libraries are given in "**requirements.txt**" text document. To install these librabires open command propmt in your local directory and type "**pip install -r requirements.txt**". It will take some time as there are penitude of libraries.
3. Open and run "**server.py**" file. It will take few moment to run and in the end you will get a localhost URL.
4. Copy that URL and paste it in your web browser to run the Flask App. 

Hope you find this project useful. If you have any constructive feedback, please send an email to patelmayur0408@gmail.com.
Thank you!
