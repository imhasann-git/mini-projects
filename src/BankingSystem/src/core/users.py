# TODO:
#  get_user_input_for_registration() → insert_user_info(): done
#  get_user_input_for_update() → update_user_info(): done
#  confirm_and_delete_user() → delete_user(): done
#  search_user_by_id() → search_data('users_info'): done

from db.operations import (
    insert_user_info,
    update_user_info,
    delete_user,
    search_data,
)

from app.helper.dob_checker import is_user_18_or_older
from app.helper.user_id_gen import generate_user_id
from getpass import getpass


def get_user_input_for_registration(connection):
    user_name = input("Enter the name: ").strip()
    user_number = input("Enter the number here: ").strip()
    user_address = input("Enter your address: ").strip()
    user_dob = input("Enter dob (yyyy-mm-dd): ").strip()
    try:
        if not is_user_18_or_older(dob_str=user_dob):
            print("You must be at least 18 years old to register.")
            return
    except Exception as e:
        print(f"Invalid DOB format or error: {e}")
        return
    
    user_password = getpass("Enter your password (input hidden): ").strip()
    branch_id = input("Enter your branch ID: ").strip()
    user_id = generate_user_id(user_name, user_dob)
    
    user_data = {
        "user_id": user_id,
        "user_full_name": user_name,
        "user_phone_number": user_number,
        "user_address": user_address,
        "user_password": user_password,
        "branch_id": branch_id
    }
    
    success = insert_user_info(connection, user_data)
    if success:
        print(f"User registered successfully with user ID: {user_id}")
    else:
        print("Failed to register user.")
        
def get_user_input_for_update(connection):
    """
    Prompts the user to update their information.
    Calls update_user_info(user_id, update_fields_dict) internally.
    """
    print("\n--- Update User Info ---")
    user_id = input("Enter your User ID (required): ").strip()
    if not user_id:
        print("User ID is required to update records.")
        return

    updates = {}

    # Prompt for each updatable field
    user_name = input("Enter new name (or press Enter to skip): ").strip()
    if user_name:
        updates['user_full_name'] = user_name

    user_number = input("Enter new phone number (or press Enter to skip): ").strip()
    if user_number:
        updates['user_phone_number'] = user_number

    user_address = input("Enter new address (or press Enter to skip): ").strip()
    if user_address:
        updates['user_address'] = user_address

    # If no updates provided
    if not updates:
        print("No updates provided. Nothing was changed.")
        return

    # Call your DB update function
    try:
        update_user_info(connection, user_id, updates)
        print("User info updated successfully.")
    except Exception as e:
        print(f"Failed to update user info: {str(e)}")

def confirm_and_delete_user(connection):
    user_id = input("Enter the user id: ").strip()
    if not user_id:
        print("User id is mandatory")
        return
    
    try:
        delete_user(connection, user_id)
        print("User deleted successfully.")
    except Exception as e:
        print(f"Failed to delete user info: {str(e)}")
                
def search_user_by_id(connection):
    """
    Prompts the user for a user ID and searches the users_info table.
    """
    print("\n--- Search User By ID ---")
    user_id = input("Enter the User ID to search: ").strip()
    
    if not user_id:
        print("User ID is required to perform search.")
        return

    try:
        search_params = {"user_id": user_id}
        result = search_data(connection, 'users_info', search_params)
        if result:
            print("\nUser Found:")
            for row in result:
                for key, value in row.items():
                    print(f"{key}: {value}")
        else:
            print("No user found with the provided ID.")
    except Exception as e:
        print(f"An error occurred while searching: {str(e)}")