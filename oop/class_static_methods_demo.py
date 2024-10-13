# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# The following part should be in main.py for testing
if __name__ == "__main__":
    from class_static_methods_demo import Calculator

    def main():
        # Using the static method
        sum_result = Calculator.add(10, 5)
        print(f"The sum is: {sum_result}")

        # Using the class method
        product_result = Calculator.multiply(10, 5)
        print(f"The product is: {product_result}")

    main()

