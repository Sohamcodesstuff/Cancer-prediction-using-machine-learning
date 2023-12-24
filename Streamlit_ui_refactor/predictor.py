import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


def predict(parameters):

    features = [float(x) for x in parameters]
    final_features = [np.array(features)]
    final_features = scaler.transform(final_features)    
    prediction = model.predict(final_features)
    y_probabilities_test = model.predict_proba(final_features)
    y_prob_success = y_probabilities_test[:, 1]
    # print("final features",final_features)
    # print("prediction:",prediction)
    output = round(prediction[0], 2)
    y_prob=round(y_prob_success[0], 3)
    # print(output)

    return [output,y_prob]
        
print(predict([9.71,143.50,0.42,6.8,0.2,0.01,0.08,0.9,0.16,0.07]))