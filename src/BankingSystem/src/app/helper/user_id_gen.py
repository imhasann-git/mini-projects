def generate_user_id(full_name: str, dob: str) -> str:
    """
    Generates a user ID based on:
    - First 3 letters of the name (lowercased)
    - Last 2 digits of the birth year from DOB (yyyy-mm-dd)

    Example:
    Name: Hasan
    DOB: 2005-03-16
    → user_id: has05
    """
    name_part = full_name.strip().lower().replace(" ", "")[:3]
    
    try:
        year = dob.strip().split("-")[0]
        year_part = year[-2:]
    except (IndexError, ValueError):
        raise ValueError("Invalid DOB format. Expected yyyy-mm-dd")

    return name_part + year_part