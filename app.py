import joblib
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import random
import spacy
from datetime import datetime
import spacy.cli
import os
spacy.cli.download("en_core_web_sm") 
nlp = spacy.load("en_core_web_sm")
model = joblib.load("ankita_intent_model.pkl")
app = Flask(__name__)
CORS(app)
# Load AI data from JSON file
with open("ankita_ai.json", "r", encoding="utf-8") as f:
    ai_data = json.load(f)

# Create storage JSON if not exists
try:
    with open("ankita_ai_storage.json", "r") as f:
        storage_data = json.load(f)
except FileNotFoundError:
    with open("ankita_ai_storage.json", "w") as f:
        json.dump([], f)



def detect_intent(message):
    
      prediction = model.predict([message])[0]
      return prediction

   
def log_user_interaction(user_message, detected_intent, ai_reply, session_id="anonymous"):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_message": user_message,
        "ai_reply": ai_reply,
        "detected_intent": detected_intent,
        "session_id": session_id
    }

    try:
        with open("ankita_ai_storage.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(log_entry)

    with open("ankita_ai_storage.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message'].strip()
    intent = detect_intent(user_msg)
    

    if intent in ai_data['emotion_responses']:
        reply = random.choice(ai_data['emotion_responses'][intent])
    elif intent == 'motivation':
        reply = random.choice(ai_data['motivation'])
    elif intent == 'deep_topics':
        reply = random.choice(ai_data['deep_topics'])
    elif intent == 'stressed':
        reply = random.choice(ai_data['stressed'])
    elif intent == 'sad':
        reply = random.choice(ai_data['sad'])
    elif intent == 'lost':
        reply = random.choice(ai_data['lost'])
    elif intent == 'happy':
        reply = random.choice(ai_data['happy'])
    elif intent == 'morning':
        reply = random.choice(ai_data['morning'])
    elif intent == 'night':
        reply = random.choice(ai_data['night'])
    elif intent == 'anxious':
        reply = random.choice(ai_data['anxious'])
    elif intent == 'insecure':
        reply = random.choice(ai_data['insecure'])
    elif intent == 'peaceful':
        reply = random.choice(ai_data['peaceful'])
    elif intent == 'love':
        reply = random.choice(ai_data['love'])
    elif intent == 'consoling':
        reply = random.choice(ai_data['consoling'])
    elif intent == 'etiquette':
        reply = random.choice(ai_data['etiquette'])
    elif intent == 'value':
        reply = random.choice(ai_data['value'])
    elif intent == 'family':
        reply = random.choice(ai_data['family'])
    elif intent == 'casual':
        reply = random.choice(ai_data['casual'])
    elif intent == 'unknown':
        reply = random.choice(ai_data['unknown'])
    else:
        reply = "Tell me more? I'm here.."


    log_user_interaction(user_msg, intent, reply)
    wisdom = random.choice(ai_data["tiny_wisdom"]) if "tiny_wisdom" in ai_data else None
    return jsonify({'reply': reply, 'intent': intent, 'wisdom': wisdom})


if __name__ == "__main__":
    # app.run(debug=True)
     port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
