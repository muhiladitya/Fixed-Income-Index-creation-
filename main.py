import pandas as pd
from index import *
def create_bond(file_path):
    df = pd.read_csv(file_path)
    bonds = []
    for i in df.to_dict(orient="records"):
        if i["bond_type"].lower() == "government":
            bond = GovernmentBond(**i)
        elif i["bond_type"].lower() == "corporate":
            bond = CorporateBond(**i)
        elif i["bond_type"].lower() == "high_yield":
            bond = HighYieldBond(**i)
        else:
            raise ValueError(f"Unknown bond type: {i['bond_type']}")
        bonds.append(bond)
    return bonds
if __name__ == "__main__":
    bonds = create_bond("data\\bonds.csv")
    index = FixedIncomeIndex("My Bond Index", bonds)
    print(index.get_summary())