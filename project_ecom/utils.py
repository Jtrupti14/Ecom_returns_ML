import pickle
import json
import numpy as np
import config

class ArticleReturns():
    def __init__(articleID, colorCode,sizeCode,productGroup,quantity,price,rrp,deviceID,paymentMethod):
        self.articleID      = articleID
        self.colorCode      = colorCode
        self.sizeCode       = sizeCode
        self.productGroup   = productGroup
        self.quantity       = quantity
        self.price          = price
        self.rrp            = rrp
        self.deviceID       = deviceID
        self.paymentMethod  = paymentMethod
    def load_model(self):
        # we are reading model and json file"
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file)
        with open(config.JOSN_FILE_PATH,"r") as file:
            self.json_data = json.load(file)
    def get_predict_returns(self):
        self.load_model() # calling above model function
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.articleID
        test_array[1] = self.colorCode
        test_array[2] = self.sizeCode
        test_array[3] = self.productGroup
        test_array[4] = self.quantity
        test_array[5] = self.price
        test_array[6] = self.rrp
        test_array[7] = self.deviceID
        test_array[8] = self.paymentMethod


        predict_returns = self.model.predict([test_array])
        return predict_returns