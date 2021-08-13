from flask import Flask, request, render_template,request
from flask import Flask, render_template, request
from chatterbot import ChatBot
import nltk
from chatterbot.trainers import ChatterBotCorpusTrainer
import util
import pandas as pd
import numpy as np

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

df=pd.read_csv('Dataset1.csv')
df['Price_per_sqrft']=df["Price"]/df["Area"]
location_room_encode=df.groupby(df['Location'])['Price_per_sqrft'].median().sort_values().index
locations=location_room_encode.str.replace(' ','')

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/analysis', methods=['GET'])
def analysis():
    return render_template('home.html',locations=locations)

@app.route('/predict', methods=['POST'])
def predict():

    Location=request.form.get('Location1')
    Area=request.form['Area1']
    Rooms=request.form['Rooms1']
    Gymnasium=request.form['Gymnasium1']
    LiftAvailable=request.form['LiftAvailable1']
    CarParking=request.form['CarParking1']
    Security=request.form['Security1']
    ChildrensPlayArea=request.form['ChildrensPlayArea1']
    Clubhouse=request.form['Clubhouse1']
    Intercom=request.form['Intercom1']
    LandscapedGardens=request.form['LandscapedGardens1']
    IndoorGames=request.form['IndoorGames1']
    GasConnection=request.form['GasConnection1']
    JoggingTrack=request.form['JoggingTrack1']
    SwimmingPool=request.form['SwimmingPool1']

    output=util.get_estimated_price(Location,Area,Rooms,Gymnasium,LiftAvailable,CarParking,Security,ChildrensPlayArea,Clubhouse,Intercom,
                   LandscapedGardens,IndoorGames,GasConnection,JoggingTrack,SwimmingPool)

    return render_template('home.html',output=output,locations=locations)

@app.route('/chatbot', methods=['GET','POST'])
def chatbot():
    return render_template('chatbot.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(english_bot.get_response(userText))

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction")
    app.run(debug=True)