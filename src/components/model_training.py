import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import AdaBoostClassifier , GradientBoostingRegressor , RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score , mean_absolute_error , mean_squared_error

from src.exception import CustomException
from src.logger import logging