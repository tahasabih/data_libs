import numpy as np
import pandas as pd

# to keep it binary, no change is treated as a positive
def rise_fall(stock_array, positive_label=None, negative_label=None):
	if positive_label == None:
		positive_label = "rise"
	if negative_label == None:
		negative_label = "fall"
	cat_array = [None] * (len(stock_array) - 1)
	for i in range(1, len(stock_array) - 1):
		if stock_array[i] - stock_array[i-1] >= 0:
			cat_array[i-1] = positive_label
		elif stock_array[i] - stock_array[i-1] < 0:
			cat_array[i-1] = negative_label
	return cat_array

def percentage_change(stock_array):
	cat_array = [None] * (len(stock_array) - 1)
	for i in range(1, len(stock_array) - 1):
		cat_array[i-1] = calculate_percentage(stock_array, i)
	return cat_array

def calculate_percentage(stock_array, i):
	return (stock_array[i] - stock_array[i-1])/stock_array[i-1]