class BondValidator:
    def __init__(self):
        self.__errors = []

    def __validate_isin(self, bond):
        if not bond.isin or len(bond.isin) != 12:
            self.__errors.append(f"{bond.isin}: ISIN must be 12 characters long.")
            return False
        elif not bond.isin[:2].isalpha():
            self.__errors.append(f"{bond.isin}: ISIN must start with two letters.")
            return False
        return True

    def __validate_coupon(self, bond):
        if bond.coupon < 0:
            self.__errors.append(f"{bond.isin}: Coupon rate cannot be negative.")
            return False
        return True

    def __validate_price(self, bond):
        if bond.price < 0:
            self.__errors.append(f"{bond.isin}: Price cannot be negative.")
            return False
        return True

    def validate_bond(self, bond):
        validators = [
            self.__validate_isin,
            self.__validate_coupon,
            self.__validate_price
        ]
        is_valid = True
        for validator in validators:
            if not validator(bond):
                is_valid = False
        return is_valid

    def get_errors(self):
        return self.__errors.copy()

    def clear_errors(self):
        self.__errors = []

    def has_errors(self):
        return len(self.__errors) > 0