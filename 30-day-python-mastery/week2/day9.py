# ---------------------------
# Descriptor for Positive Numbers
# ---------------------------
class PositiveNumber:
    """
    A reusable descriptor that ensures
    a value is always a positive number.
    """

    def __set_name__(self, owner, name):
        # Automatically called when the descriptor
        # is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        # Called when the attribute is accessed
        if instance is None:
            return self  # If accessed from class
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # Called when the attribute is assigned
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        instance.__dict__[self.name] = value


# ---------------------------
# Loan Class
# ---------------------------
class Loan:
    # Descriptor enforces positive values
    principal = PositiveNumber()
    interest_rate = PositiveNumber()

    def __init__(self, borrower, principal, interest_rate):
        self.borrower = borrower
        self.principal = principal          # Calls descriptor __set__
        self.interest_rate = interest_rate  # Calls descriptor __set__

    # ---------------------------
    # Property for total repayment
    # ---------------------------
    @property
    def total_payment(self):
        """
        Read-only property.
        Calculates total repayment dynamically.
        """
        return self.principal + (self.principal * self.interest_rate)

    # ---------------------------
    # Property with setter
    # ---------------------------
    @property
    def borrower_name(self):
        return self.borrower

    @borrower_name.setter
    def borrower_name(self, value):
        if not value.strip():
            raise ValueError("Borrower name cannot be empty")
        self.borrower = value


# ---------------------------
# Usage
# ---------------------------

loan = Loan("Alice", 10000, 0.1)

print("Principal:", loan.principal)
print("Interest Rate:", loan.interest_rate)
print("Total Payment:", loan.total_payment)

loan.borrower_name = "Alice Johnson"
print("Borrower:", loan.borrower_name)

# loan.principal = -5000  # ❌ Raises ValueError
