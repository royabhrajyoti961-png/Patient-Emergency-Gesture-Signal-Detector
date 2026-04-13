import pickle

model = pickle.load(open("gesture_model.pkl", "rb"))

def predict_gesture(data):
    prediction = model.predict([data])[0]
    return prediction
