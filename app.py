


# 1. Library imports
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

pickle_in = open("get_sim.pkl","rb")
util=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    text1=data['text1']
    text2=data['text2']
   
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    emb1 = model.encode(text1)
    emb2 = model.encode(text2)
    similarity = util.cos_sim(emb1,emb2)

    return {
         'prediction': similarity
    }    

    # if(prediction[0]>0.5):
    #     prediction="Fake note"
    # else:
    #     prediction="Its a Bank note"
    # return {
    #     'prediction': prediction
    

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)