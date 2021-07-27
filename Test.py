from logging import debug
import pyodbc
import pandas as pd
import json
from fastapi import FastAPI
from typing import AsyncGenerator, Optional
from flask import Flask,request,redirect
import uvicorn
from json import dumps
from pandas.io.json import json_normalize
from flask import Flask, make_response
app = Flask(__name__)

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:employee0723.database.windows.net,1433;Database=employee;Uid=manager;Pwd={@Zxcdsaqwe44};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

@app.route('/')
def get_data():
    query_veg = "SELECT * from dbo.employee "
    df_veg = pd.read_sql(query_veg, cnxn)
    queryjs = df_veg.to_json(orient = 'records')
    query_data=json.loads(queryjs)
    return make_response(dumps(query_data))

@app.route("/insert",methods=['POST'])
def inser():
    query_veg = "SELECT * from dbo.employee "
    df = pd.read_sql(query_veg, cnxn)
    inserValues=request.get_json()
    temp = []
    tempcol=[]
    for i in inserValues:
        temp.append(inserValues[i])
    values=(tuple(temp))
    print(values)
    num=0
    for i in inserValues:
        tempcol.append(i)
        num=num+1
    print(num)
    valuescols=(tuple(tempcol))
    # query_veg = "insert into dbo.employee"+str(valuescols)+"values "+str(values)
    # df_veg = pd.read_sql(query_veg, cnxn)
    # stringinput="INSERT INTO dbo.employee "+str(valuescols)+"values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,)",str(values)
    # print(stringinput)
    cursor.execute("INSERT INTO dbo.employee (Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",inserValues['Age'],inserValues['Attrition'],inserValues['BusinessTravel'],inserValues['DailyRate'],inserValues['Department'],inserValues['DistanceFromHome'],inserValues['Education'],inserValues['EducationField'],inserValues['EmployeeCount'],inserValues['EmployeeNumber'],inserValues['EnvironmentSatisfaction'],inserValues['Gender'],inserValues['HourlyRate'],inserValues['JobInvolvement'],inserValues['JobLevel'],inserValues['JobRole'],inserValues['JobSatisfaction'],inserValues['MaritalStatus'],inserValues['MonthlyIncome'],inserValues['MonthlyRate'],inserValues['NumCompaniesWorked'],inserValues['Over18'],inserValues['OverTime'],inserValues['PercentSalaryHike'],inserValues['PerformanceRating'],inserValues['RelationshipSatisfaction'],inserValues['StandardHours'],inserValues['StockOptionLevel'],inserValues['TotalWorkingYears'],inserValues['TrainingTimesLastYear'],inserValues['WorkLifeBalance'],inserValues['YearsAtCompany'],inserValues['YearsInCurrentRole'],inserValues['YearsSinceLastPromotion'],inserValues['YearsWithCurrManager'])
    cnxn.commit()
    return '新增資料成功'

@app.route('/delete', methods = ['POST'])
def delete():
    delete_Values=request.get_json()
    target_id=delete_Values['EmployeeNumber']
    cursor.execute("DELETE FROM dbo.employee WHERE EmployeeNumber=" +target_id)
    cnxn.commit()
    return "刪除資料成功"

@app.route('/update',methods=['POST','GET'])
def update():
    inserValues=request.get_json()
    if request.method == 'POST':
        cursor.execute("""Update dbo.employee SET Age=?,Attrition=?,BusinessTravel=?,DailyRate=?,Department=?,DistanceFromHome=?,Education=?,EducationField=?,EmployeeCount=?,EnvironmentSatisfaction=?,Gender=?,HourlyRate=?,JobInvolvement=?,JobLevel=?,JobRole=?,JobSatisfaction=?,MaritalStatus=?,MonthlyIncome=?,MonthlyRate=?,NumCompaniesWorked=?,Over18=?,OverTime=?,PercentSalaryHike=?,PerformanceRating=?,RelationshipSatisfaction=?,StandardHours=?,StockOptionLevel=?,TotalWorkingYears=?,TrainingTimesLastYear=?,WorkLifeBalance=?,YearsAtCompany=?,YearsInCurrentRole=?,YearsSinceLastPromotion=?,YearsWithCurrManager=? WHERE EmployeeNumber=?""",inserValues['Age'],inserValues['Attrition'],inserValues['BusinessTravel'],inserValues['DailyRate'],inserValues['Department'],inserValues['DistanceFromHome'],inserValues['Education'],inserValues['EducationField'],inserValues['EmployeeCount'],inserValues['EnvironmentSatisfaction'],inserValues['Gender'],inserValues['HourlyRate'],inserValues['JobInvolvement'],inserValues['JobLevel'],inserValues['JobRole'],inserValues['JobSatisfaction'],inserValues['MaritalStatus'],inserValues['MonthlyIncome'],inserValues['MonthlyRate'],inserValues['NumCompaniesWorked'],inserValues['Over18'],inserValues['OverTime'],inserValues['PercentSalaryHike'],inserValues['PerformanceRating'],inserValues['RelationshipSatisfaction'],inserValues['StandardHours'],inserValues['StockOptionLevel'],inserValues['TotalWorkingYears'],inserValues['TrainingTimesLastYear'],inserValues['WorkLifeBalance'],inserValues['YearsAtCompany'],inserValues['YearsInCurrentRole'],inserValues['YearsSinceLastPromotion'],inserValues['YearsWithCurrManager'],inserValues['EmployeeNumber']) 
        cnxn.commit()
        return "修改資料成功"
 
if __name__ == '__main__':    
    app.run(host='127.0.0.1',port='5000',debug=True)
# © 2021 GitHub, Inc.
# Terms
# Privacy
# Security
# Status
# Docs
# Contact GitHub
# Pricing
# API
# Training
# Blog
# About