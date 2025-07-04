class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: no access to self or cls
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: access to cls, uses class attribute
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
