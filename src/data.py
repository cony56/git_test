"""
날짜: 05/09
수정: 개발자A
"""
import pandas as pd

def load_data(data):
	return pd.read_csv(data)

def save_data(file,txt):
	with open(file, "w", encoding="utf-8") as f:
		f.write(txt)