import numpy as np
import pandas as pd

def shift(dataframe, timeshift):
	if timeshift > 0:
		return dataframe[timeshift:]
	elif timeshift < 0:
		return dataframe[:timeshift]