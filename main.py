import pandas as pd

print("Phishing Email Detection System")

email = input("Enter email text: ")

suspicious_words = [
    "urgent",
    "verify",
    "click",
    "password",
    "bank",
    "account"
]

score = 0

for word in suspicious_words:
    if word.lower() in email.lower():
        score += 1

if score >= 2:
    print("Potential Phishing Email")
else:
    print("Likely Safe Email")
