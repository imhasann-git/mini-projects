from datetime import datetime
def is_user_18_or_older(dob_str: str) -> bool:
    """
    Checks if the user is 18 or older based on DOB.
    
    Args:
        dob_str (str): Date of birth in yyyy-mm-dd format.
        
    Returns:
        bool: True if user is 18 or older, False otherwise.
    """
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age >= 18
    except ValueError:
        raise ValueError("Invalid date format. Please use yyyy-mm-dd")