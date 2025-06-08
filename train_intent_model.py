# train_intent_model.py
import pandas as pd, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

df = pd.read_csv("training_intents.csv")          # 1  load data
pipe = Pipeline([                                  # 2  build pipeline
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), stop_words="english")),
    ("clf",  LogisticRegression(max_iter=1000))
])
pipe.fit(df["text"], df["intent"])                 # 3  train
joblib.dump(pipe, "ankita_intent_model.pkl")       # 4  save
print("✅ Model trained & saved as ankita_intent_model.pkl")
