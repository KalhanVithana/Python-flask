from flask import Flask,request,render_template
import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import pickle
import json
import mysql.connector
import datetime
from flask import jsonify
from flask import jsonify
from PIL import Image

app = Flask(__name__)
model = pickle.load(open('img_model.p','rb'))


@app.route("/test",methods =['POST'])
def home():

   x = { "game": "pubg mobile", 
        "type":"action" ,
        "details": "PUBG is a player versus player shooter game in which up to one hundred players fight in a battle royale, a type of large-scale last man standing deathmatch where players fight to remain the last alive." ,
        "about":"https://en.wikipedia.org/wiki/PUBG:_Battlegrounds"}
   y = json.dumps(x)
   return y

@app.route("/upload",methods =['POST'])
def predict():

   
    #CATEGORIES = ['Free Fire Fotos','call of duty mobile characters','pubg mobile game characters']
    CATEGORIES = ['pa','ca']
    imageFile = request.files['img']
    imagePath = './images/'+imageFile.filename
    imageFile.save(imagePath)

    img = Image.open(imagePath)
    flat_data = []
    img = np.array(img)
    img_resized = resize(img,(150,150,3))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data)
    print(img.shape)
    plt.imshow(img_resized)
    y_out = model.predict(flat_data)
    y_out =CATEGORIES[y_out[0]]
    print(f'Predicted out put{y_out}')
    mydate = datetime.datetime.now()
   
    if y_out == 'pa':
        x = { "game": "pubg mobile", 
        "type":"action" ,
        "details": "PUBG is a player versus player shooter game in which up to one hundred players fight in a battle royale, a type of large-scale last man standing deathmatch where players fight to remain the last alive." ,
        "about":"https://en.wikipedia.org/wiki/PUBG:_Battlegrounds"}
        y = json.dumps(x)
        return y

    else:
        x = { "game": "Call of Duty",
         "type": "action",
         "details": "Call of Duty: Mobile is a free-to-play shooter game developed by TiMi Studio Group and published by Activision for Android and iOS. It was released on October 1, 2019, where it was one of the largest mobile game launches in history, generating over US$480 million with 270 million downloads within a year" ,
         "about":"https://en.wikipedia.org/wiki/Call_of_Duty:_Mobile" }
        y = json.dumps(x)
        return y

   
    

# @app.route("/games",methods=['GET'])
# def game():
#     args = request.args
#     print(args)
#     gameType = args.get("type")
    
#     if gameType == 'code':
#         mycursor.execute("SELECT * FROM codemobile")
#         myresult = mycursor.fetchall()
#         games = []
#         for x in myresult:
#           games.append(x)

#         return json.dumps(games)
        
        

#     else:
#         mycursor.execute("SELECT * FROM pubg")
#         myresult = mycursor.fetchall()
#         games = []
#         for x in myresult:
#           games.append(x)
#         return json.dumps(games)
        
# //:w !sudo tee %

#     //sudo kill -9 $(sudo lsof -t -i:8080)
# # HTTP -> 80
# # HTTPS -> 443
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)