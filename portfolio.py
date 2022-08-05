import pandas as pd
import numpy as np

class Portfolio:
    def __init__(
        self,
        start_date,
        end_date,
        portfolio,
        weights=None,
        data=None,
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.portfolio = portfolio
        self.weights = weights
        self.data = data
        if self.weights is None:
            try:
                self.weights = [1.0 / len(self.portfolio)] * len(self.portfolio)
            except:
                self.weights = 0 
        
