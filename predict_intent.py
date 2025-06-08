# predict_intent.py
import joblib

# Load trained model
model = joblib.load("ankita_intent_model.pkl")

# Predict user input
while True:
    text = input("You: ")
    if text.lower() == "exit":
        break
    intent = model.predict([text])[0]
    print("🤖 Intent detected:", intent)
