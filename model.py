import pandas as pd
from sklearn.cluster import KMeans
import pickle

data ={
    'Income': [15, 16, 17, 18, 19, 60, 62, 65, 70, 75],
    'Spending': [39, 81, 6, 77, 40, 90, 85, 20, 95, 10]
}

df = pd.DataFrame(data);

model = KMeans(n_clusters=4, random_state=1)
model.fit(df)

with open("model.pkl","wb") as f:
    pickle.dump(model, f)

print("model.pkl created successfully")