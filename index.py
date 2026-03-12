from bonds import *
from validator import *
import pandas as pd
import numpy as np

class FixedIncomeIndex:
    def __init__(self, name, constituents):
        self.name = name
        self.constituents = constituents if constituents else []
    def add_bond(self, bond):
        self.constituents.append(bond)  
    def __MarketValue(self):
        return sum(((self.constituents[i].price)/100) * self.constituents[i].outstanding for i in range(len(self.constituents)))
    def remove_bond(self, isin):
        self.constituents = [bond for bond in self.constituents if bond.isin != isin]
    def calculate_weights(self):
            total_value = self.__MarketValue()
            
            if total_value == 0:
                return []
            prices = np.array([bond.price for bond in self.constituents])
            outstandings = np.array([bond.outstanding for bond in self.constituents])
            market_values = (prices / 100) * outstandings
            weights = market_values / total_value
            result = []
            for i in range(len(self.constituents)):
                bond = self.constituents[i]
                bond.weight = weights[i] 
                result.append({"isin": bond.isin, "weight": weights[i]})  
            return result
    def index_yield(self):
        total_value = self.__MarketValue()
        if total_value == 0:
            return 0
        total_coupon = sum((self.constituents[i].coupon / 100) * self.constituents[i].outstanding for i in range(len(self.constituents)))
        return (total_coupon / total_value) * 100
    def get_sector_breakdown(self):
        sector = {}
        for i in range(len(self.constituents)):
            bond = self.constituents[i]
            if isinstance(bond, GovernmentBond):
                sector["Government"] = sector.get("Government", 0) + ((bond.price)/100) * bond.outstanding
            elif isinstance(bond, HighYieldBond):  
                sector["High Yield"] = sector.get("High Yield", 0) + ((bond.price)/100) * bond.outstanding
            elif isinstance(bond, CorporateBond):  
                sector["Corporate"] = sector.get("Corporate", 0) + ((bond.price)/100) * bond.outstanding
        total_value = self.__MarketValue()
        return {sector: value / total_value for sector, value in sector.items() if total_value > 0}
    def get_summary(self):
        return {
            "name": self.name,
            "total_market_value": self.__MarketValue(),
            "index_yield": self.index_yield(),
            "sector_breakdown": self.get_sector_breakdown(),
        }
    def to_dataframe(self):
        data = [bond.to_dict() for bond in self.constituents]
        return pd.DataFrame(data)