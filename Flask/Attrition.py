from flask import Flask, request, render_template
import pickle
import numpy as np



app = Flask(__name__)
logr=pickle.load(open('Attrition.pkl','rb'))
@app.route('/')
def home():
    return render_template('Att.html')

@app.route('/att')
def att():
    return render_template('Attrition1.html')


@app.route('/predict',methods=['POST'])
def y_predict():
   
    ag = int(request.form["Age"])
    bt = int(request.form["BusinessTravel"])
    dr = int(request.form["DailyRate"])
    dpt = int(request.form["Department"])
    dfh = int(request.form["DistanceFromHome"])
    edu = int(request.form["Education"])
    ef = int(request.form["EducationField"])
    #gen = request.form["Gender"]
    hr = int(request.form["HourlyRate"])
    jl = int(request.form["JobLevel"])
    jr = int(request.form["JobRole"])
    ms = int(request.form["MaritalStatus"])
    mi = int(request.form["MonthlyIncome"])
    mr = int(request.form["MonthlyRate"])
    ncw = int(request.form["NumCompaniesWorked"])
    ot = int(request.form["OverTime"])
    psh = int(request.form["PercentSalaryHike"])
    pr = int(request.form["PerformanceRating"])
    sol = int(request.form["StockOptionLevel"])
    twh = int(request.form["TotalWorkingYears"])
    ttly = int(request.form["TrainingTimesLastYear"])
    yac = int(request.form["YearsAtCompany"])
    yicr = int(request.form["YearsInCurrentRole"])
    yslp = int(request.form["YearsSinceLastPromotion"])
    ywcm = int(request.form["YearsWithCurrManager"])
    ts = int(request.form["Total_Satisfaction"])
    a=np.array([[ag,bt,dr,dpt,dfh,edu,ef,hr,jl,jr,ms,mi,mr,ncw,ot,psh,pr,sol,twh,ttly,yac,yicr,yslp,ywcm,ts]])
    print(a)
    pred=logr.predict(a)
    if(pred == 0):
        output = "Not Attrited"
        print("Not Attrited")
    else:
        output = "Attrited"
        print("Attrited")
    return render_template('Attrition1.html', prediction_text= output)


if __name__ == "__main__":
    app.run()
