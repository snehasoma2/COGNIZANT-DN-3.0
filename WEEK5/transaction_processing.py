# transaction_processing.py

import os
from datetime import datetime

def process_transaction(transaction):
    try:
        # Simulate transaction processing logic
        if not isinstance(transaction, dict):
            raise ValueError("Transaction data must be a dictionary.")
        
        if 'amount' not in transaction or 'type' not in transaction:
            raise KeyError("Transaction must include 'amount' and 'type' fields.")
        
        amount = transaction['amount']
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Transaction amount must be a positive number.")
        
        # Process the transaction (this is just a placeholder)
        print(f"Processing transaction: {transaction}")
        
    except (ValueError, KeyError) as e:
        log_error(e)
        print(f"Error: {e}. Please correct the transaction data.")
    except Exception as e:
        log_error(e)
        print("An unexpected error occurred. Please try again later.")

def log_error(error):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    error_message = f"{timestamp} - {type(error).__name__}: {error}\n"
    
    with open("error_log.txt", "a") as log_file:
        log_file.write(error_message)

    print(f"Error logged at {timestamp}")

def validate_transaction(transaction):
    errors = []
    
    if not isinstance(transaction, dict):
        errors.append("Transaction must be a dictionary.")
    
    if 'amount' not in transaction:
        errors.append("Transaction must include an 'amount'.")
    elif not isinstance(transaction['amount'], (int, float)) or transaction['amount'] <= 0:
        errors.append("Amount must be a positive number.")
    
    if 'type' not in transaction:
        errors.append("Transaction must include a 'type'.")
    
    return errors


def process_transaction(transaction):
    errors = validate_transaction(transaction)
    
    if errors:
        for error in errors:
            log_error(error)
            print(f"Validation Error: {error}")
        return
    
    try:
        # Process the transaction
        print(f"Processing transaction: {transaction}")
        
    except Exception as e:
        log_error(e)
        print("An unexpected error occurred. Please try again later.")


def main():
    transactions = [
        {'amount': 100, 'type': 'deposit'},
        {'amount': -50, 'type': 'withdrawal'},  # Invalid amount
        {'type': 'deposit'},  # Missing amount
        'invalid_transaction',  # Not a dictionary
    ]
    
    for transaction in transactions:
        process_transaction(transaction)

if __name__ == "__main__":
    main()
