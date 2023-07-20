import streamlit as st
import pandas as pd
import openpyxl


import glob

filepaths = glob.glob("invoices/*xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
