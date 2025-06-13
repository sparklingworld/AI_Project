# AI_Project
This project uses:

 A custom-built NLP intent detection system

 A JSON-based personality and emotional response model

 A clean frontend UI with Kibo avatar

 Flask backend deployed via Render(to be done)

How It Works

 The user sends a message via the frontend.

 The message is sent to the backend Flask app.

 The trained ML model (ankita_intent_model.pkl) detects the intent.

 It matches the intent + emotion in json file.

 then its responds in a way that fits my given vibe and values.

Frontend	         Backend	                ML/NLP                    	         Hosting
HTML, CSS, JS	     Flask (Python)          Scikit-learn, SpaCy (or custom)      GitHub Pages + Render
                                          




