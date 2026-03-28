from flask import Flask, render_template, request
from risk_classifier import classify_risk
import pdfplumber

app = Flask(__name__)

def extract_text_from_pdf(file):
    text=""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()
    return text

@app.route("/",methods=["GET","POST"])
def index():

    results=[]
    high=0
    medium=0
    low=0

    if request.method=="POST":

        text=""

        if "pdf" in request.files and request.files["pdf"].filename!="":
            file=request.files["pdf"]
            text=extract_text_from_pdf(file)

        else:
            text=request.form["document"]

        clauses=text.split(".")

        for clause in clauses:
            clause=clause.strip()

            if clause=="":
                continue

            risk=classify_risk(clause)

            if risk=="High Risk":
                high+=1
            elif risk=="Medium Risk":
                medium+=1
            else:
                low+=1

            results.append((clause,risk))

    total=high+medium+low
    risk_score=round((high*100)/total,2) if total>0 else 0

    return render_template(
        "index.html",
        results=results,
        high=high,
        medium=medium,
        low=low,
        risk_score=risk_score
    )

if __name__=="__main__":
    app.run(debug=True)