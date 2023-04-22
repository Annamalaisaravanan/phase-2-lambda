from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

class User_input(BaseModel):
      pl : float
      pw : float
      sl : float
      sw : float
      
@app.post('/predict')
def predict(input:User_input):
      arr = np.array([input.sl,input.sw,input.pl,input.pw]).reshape(1,4)
      result = model.predict(arr)
      print('The result in fastAPI end is ',result[0])
      res = int(result[0])
      return res