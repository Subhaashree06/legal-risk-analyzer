high_risk_words = ["terminate", "liability", "indemnify", "waive"]
medium_risk_words = ["suspend", "restriction", "condition"]

def classify_risk(text):

    text = text.lower()

    for word in high_risk_words:
        if word in text:
            return "High Risk"

    for word in medium_risk_words:
        if word in text:
            return "Medium Risk"

    return "Low Risk"