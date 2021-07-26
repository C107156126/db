import pyodbc
import pandas as pd
from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI()

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:houseluis.database.windows.net,1433;Database=houseluis;Uid=houseluis;Pwd={aa091120556A};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

@app.get('/')
async def get_data():
    query_veg = "SELECT Id,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount from dbo.Employee"
    
    df_veg = pd.read_sql(query_veg, cnxn)
    df_m = df_veg.to_dict('r')
    return df_m

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port="8000")
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
