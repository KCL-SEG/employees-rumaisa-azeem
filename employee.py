"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, rate, num_hours=None, commission_type=None, commission_amount=None, num_contracts=None):
        
        if contract_type not in ['monthly', 'hourly']:
            raise ValueError('Contract type must be either monthly or hourly')
        if not isinstance(rate, int) or rate < 0:
            raise ValueError('Rate must be a positive integer')
        if contract_type == 'hourly' and num_hours is None:
            raise ValueError('Number of hours must be provided for hourly contracts')
        if contract_type == 'monthly' and num_hours is not None:
            raise ValueError('Number of hours cannot be provided for monthly contracts')
        if commission_type not in [None, 'bonus', 'per_contract']:
            raise ValueError('Commission type, if not None, must be either bonus or per_contract')
        if commission_type is not None and commission_amount is None:
            raise ValueError('Commission amount must be provided if commission type is not None')
        if commission_type == 'bonus' and num_contracts is not None:
            raise ValueError('Number of contracts cannot be provided if commission type is bonus')
        if commission_type == 'per_contract' and num_contracts is None:
            raise ValueError('Number of contracts must be provided if commission type is per_contract')

        self.name = name
        self.contract_type = contract_type
        self.rate = rate
        self.num_hours = num_hours
        self.commission_type = commission_type
        self.commission_amount = commission_amount
        self.num_contracts = num_contracts

    def get_pay(self):
        # calculate contract pay
        if self.contract_type == 'hourly':
            contract_pay = self.rate * self.num_hours
        else:
            contract_pay = self.rate
        # calculate commission pay
        if self.commission_type == 'per_contract':
            commission_pay = self.commission_amount * self.num_contracts
        elif self.commission_type == 'bonus':
            commission_pay = self.commission_amount
        else:
            commission_pay = 0
        
        return contract_pay + commission_pay

    def __str__(self):
        contract_details = "monthly salary" if self.contract_type == "monthly" else "contract"
        pay_details = str(self.rate) if self.contract_type == "monthly" else f"{self.num_hours} hours at {self.rate}/hour"
        if self.commission_type == 'per_contract':
            commission_details = f" and receives a commission for {self.num_contracts} contract(s) at {self.commission_amount}/contract"
            pay_details += commission_details
        elif self.commission_type == 'bonus':
            commission_details = f" and receives a bonus commission of {self.commission_amount}"
            pay_details += commission_details
    
        return f"{self.name} works on a {contract_details} of {pay_details}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, commission_type='per_contract', commission_amount=200, num_contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150, commission_type='per_contract', commission_amount=220, num_contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, commission_type='bonus', commission_amount=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120, commission_type='bonus', commission_amount=600)
