import pickle
import numpy as np
import pandas as pd

df=pd.read_csv('Dataset1.csv')

df['Price_per_sqrft']=df["Price"]/df["Area"]
location_room_encode=df.groupby(df['Location'])['Price_per_sqrft'].median().sort_values().index
loc_encode=location_room_encode.str.replace(' ','')
enumerate(loc_encode,0)
loc_encode={k:i for i,k in enumerate(loc_encode,0)}

with open('Final_model.pickle', 'rb') as file:
    model = pickle.load(file)

def get_estimated_price(Location,Area,Rooms,Gymnasium,LiftAvailable,CarParking,Security,ChildrensPlayArea,Clubhouse,Intercom,
                   LandscapedGardens,IndoorGames,GasConnection,JoggingTrack,SwimmingPool):

    x = np.zeros(15)
    num=int(Area)
    x[0]=np.log(num)
    x[1]=loc_encode[Location]
    x[2]=Rooms
    x[3]=Gymnasium
    x[4]=LiftAvailable
    x[5]=CarParking
    x[6]=Security
    x[7]=ChildrensPlayArea
    x[8]=Clubhouse
    x[9]=Intercom
    x[10]=LandscapedGardens
    x[11]=IndoorGames
    x[12]=GasConnection
    x[13]=JoggingTrack
    x[14]=SwimmingPool
    print([x])
    return round(np.exp(model.predict([x])[0]),2)

if __name__ == '__main__':
    print(get_estimated_price('juhutara',1200,4,1,1,1,1,1,1,1,1,1,1,1,1))