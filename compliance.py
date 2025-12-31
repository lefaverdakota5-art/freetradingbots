import logging

def log_compliance(event, details):
    logging.warning(f"[COMPLIANCE] {event}: {details}")

def check_kyc(user):
    # Placeholder: check if user is KYC/AML verified
    return user.get("kyc_verified", False)
