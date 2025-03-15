import os
import shutil
import re

def sort_files(source_folder, destination_folder, dry_run=False):
    # Regular expression to match files starting with 2 or 3 capital letters
    initials_pattern = r'^[A-Z]{2,3}'
    # Keywords for sorting with specific conditions
    keywords = {
        '_IEP_': 'IEPs',  
        'Meeting_Notice': 'meeting_notice',
        'Eval_Consent': 'eval_consent',
        'PWN': 'PWN',
        'POC': 'POC',
        'speech_eval': 'speech_eval',
        '_SEC_': 'SEC'
    }

    # List all files in the source directory
    for filename in os.listdir(source_folder):
        # Check if the filename matches the initials pattern
        if re.match(initials_pattern, filename):
            # Determine the destination subfolder based on keywords
            for keyword, subfolder in keywords.items():
                if keyword in filename:
                    source_path = os.path.join(source_folder, filename)
                    destination_path = os.path.join(destination_folder, subfolder, filename)
                    
                    if dry_run:
                        print(f"Would move '{filename}' to '{subfolder}' folder.")
                    else:
                        try:
                            shutil.move(source_path, destination_path)
                            print(f"Moved '{filename}' to '{subfolder}' folder.")
                        except FileNotFoundError:
                            print(f"File '{filename}' not found.")
                        except PermissionError:
                            print("Permission denied. Please check your access rights.")
                        except Exception as e:
                            print(f"An error occurred: {e}")
                    # Stop checking other keywords once a match is found
                    break

# Define the source and destination directories
source_folder = '/Users/laurenkraynak/Documents' # TODO: Move these to .env file so we don't have to change the github code for different machines
destination_folder = '/Users/laurenkraynak/Documents/spotsy'

# Example usage with dry run
sort_files(source_folder, destination_folder, dry_run=False)