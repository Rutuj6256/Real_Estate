import pickle
import json
import config
import numpy as np
from werkzeug.datastructures import MultiDict
import warnings
warnings.filterwarnings('ignore')


class Real_estate():

    def __init__(self, No,X1_transaction_date,X2_house_age,X3_distance_to_the_nearest_MRT_station,X4_number_of_convenience_stores,X5_latitude,X6_longitude) :
        self.No = No
        self.X1_transaction_date= X1_transaction_date
        self.X2_house_age = X2_house_age
        self.X3_distance_to_the_nearest_MRT_station = X3_distance_to_the_nearest_MRT_station
        self.X4_number_of_convenience_stores= X4_number_of_convenience_stores
        self.X5_latitude=X5_latitude
        self.X6_longitude= X6_longitude
        

    def __load_model(self): # Private Method
        # Load Model File
        with open(r'artifacts/linear_reg.pkl', 'rb') as f:
            self.model = pickle.load(f)
            # print('self.model >>',self.model)

        # Load Project Data 
        with open(r'artifacts/project_data.json','r') as f:
            self.project_data = json.load( f)
            # print("Project Data :",self.project_data)



    def get_predicted_rate(self): # Public Method
        self.__load_model()
        test_array = np.zeros((1,self.model.n_features_in_))
        test_array[0][0] = self.No
        test_array[0][1] = self.X1_transaction_date
        test_array[0][2] = self.X2_house_age
        test_array[0][3] = self.X3_distance_to_the_nearest_MRT_station
        test_array[0][4] = self.X4_number_of_convenience_stores
        test_array[0][5] = self.X5_latitude
        test_array[0][6] = self.X6_longitude
       


        # print("Test Array is :",test_array)

        predicted_rate = np.around(self.model.predict(test_array)[0],3)
        # print("Home Rate :", predicted_rate)
        return predicted_rate

if __name__ == '__main__':
    cls =Real_estate(1,23.98,23.22,23.41,12.2,12.3,87.54)
    prediction = cls.get_predicted_rate()
    print(prediction)
    
