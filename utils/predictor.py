import pickle

model = pickle.load(open("gesture_model.pkl", "rb"))

def predict_gesture(data):
    return model.predict([data])[0]
