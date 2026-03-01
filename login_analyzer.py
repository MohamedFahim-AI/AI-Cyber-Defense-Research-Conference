# AI Log Analyzer using Machine Learning (Beginner Version)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (small dataset)
logs = [
    "User login successful",
    "System running normally",
    "Failed login attempt",
    "Unauthorized access detected",
    "Error connecting to database",
    "User logged out",
    "Possible attack from IP",
    "Normal system activity"
]

# Labels: 0 = safe, 1 = suspicious
labels = [0,0,1,1,1,0,1,0]

# Used to Convert text → numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(logs)

# Train simple AI model
model = MultinomialNB()
model.fit(X, labels)

print("\n AI Log Analyzer \n")

# Test log
test_log = ["Multiple failed login attempts detected"]

X_test = vectorizer.transform(test_log)
prediction = model.predict(X_test)

if prediction[0] == 1:
    print("🚨 AI ALERT: Suspicious activity detected!")
else:
    print("✅ AI: Log seems normal.")
