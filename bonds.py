
from abc import ABC, abstractmethod


class Bonds(ABC):
    def __init__(self,isin, coupon, maturity, price, currency, outstanding,**krwargs):
        self.isin = isin
        self.coupon = coupon
        self.maturity = maturity
        self.price = price
        self.currency = currency
        self.outstanding = outstanding
    def calculate_yield(self):
        # Placeholder for yield calculation logic
        return (self.coupon / self.price) * 100
    def calculate_market_value(self):
        return ((self.price)/100) * self.outstanding
    def to_dict(self):
        return {
            "isin": self.isin,
            "coupon": self.coupon,
            "maturity": self.maturity,
            "price": self.price,
            "currency": self.currency,
            "outstanding": self.outstanding
        }
    @abstractmethod
    def get_risk_level(self): #Stratergy pattern 
        pass
    def investment_grade(self):
        pass
    def __str__(self):
        return f"Bond(ISIN: {self.isin}, Coupon: {self.coupon}%, Maturity: {self.maturity}, Price: {self.price}, Currency: {self.currency}, Outstanding Amount: {self.outstanding})"

class GovernmentBond(Bonds):
    def __init__(self, isin, coupon, maturity, price, currency, outstanding, issuer, rating, bond_type,**krwargs):
        super().__init__(isin, coupon, maturity, price, currency, outstanding, **krwargs)
        self.issuer = issuer
        self.rating = rating
        self.bond_type = bond_type
    def to_dict(self):
        data = super().to_dict()
        data["issuer"] = self.issuer
        data["rating"] = self.rating
        data["bond_type"] = self.bond_type
        return data
    def __str__(self):
        return f"GovernmentBond(ISIN: {self.isin}, Coupon: {self.coupon}%, Maturity: {self.maturity}, Price: {self.price}, Currency: {self.currency}, Outstanding Amount: {self.outstanding}, Issuer: {self.issuer}, Rating: {self.rating}, Bond Type: {self.bond_type})"
    def get_risk_level(self):
        if self.rating.startswith('A'):  # AAA, AA, A
            return "Low Risk"
        elif self.rating.startswith('BBB'):  # BBB+, BBB, BBB-
            return "Medium Risk"
        else:  # BB, B, CCC, etc.
            return "High Risk"
        
class CorporateBond(Bonds):
    def __init__(self, isin, coupon, maturity, price, currency, outstanding, issuer, rating, bond_type,**krwargs):
        super().__init__(isin, coupon, maturity, price, currency, outstanding, **krwargs)
        self.issuer = issuer
        self.rating = rating
        self.bond_type = bond_type
    def to_dict(self):
        data = super().to_dict()
        data["issuer"] = self.issuer
        data["rating"] = self.rating
        data["bond_type"] = self.bond_type
        return data
    def __str__(self):
        return f"CorporateBond(ISIN: {self.isin}, Coupon: {self.coupon}%, Maturity: {self.maturity}, Price: {self.price}, Currency: {self.currency}, Outstanding Amount: {self.outstanding}, Issuer: {self.issuer}, Rating: {self.rating}, Bond Type: {self.bond_type})"
    def get_risk_level(self):
        if self.rating.startswith('A'):  # AAA, AA, A
            return "Low Risk"
        elif self.rating.startswith('BBB'):  # BBB+, BBB, BBB-
            return "Medium Risk"
        else:  # BB, B, CCC, etc.
            return "High Risk"
    def investment_grade(self):
        ig_ratings = ["AAA", "AA+", "AA", "AA-", 
                  "A+", "A", "A-", 
                  "BBB+", "BBB", "BBB-"]
        return self.rating in ig_ratings

class HighYieldBond(CorporateBond):
    def __init__(self, isin, coupon, maturity, price, currency, outstanding, issuer, rating, bond_type,**krwargs):
        super().__init__(isin, coupon, maturity, price, currency, outstanding,issuer, rating, bond_type, **krwargs)
        self.issuer = issuer
        self.rating = rating
        self.bond_type = bond_type
    def to_dict(self):
        data = super().to_dict()
        data["issuer"] = self.issuer
        data["rating"] = self.rating
        data["bond_type"] = self.bond_type
        return data
    def __str__(self):
        return f"HighYieldBond(ISIN: {self.isin}, Coupon: {self.coupon}%, Maturity: {self.maturity}, Price: {self.price}, Currency: {self.currency}, Outstanding Amount: {self.outstanding}, Issuer: {self.issuer}, Rating: {self.rating}, Bond Type: {self.bond_type})"
    def get_risk_level(self):
            return "High Risk"
    def investment_grade(self):
        return False  # High Yield Bonds are not investment grade