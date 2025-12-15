import os
import shutil
import re

def sort_files(source_folder, destination_root, school_year, dry_run=True):
    """
    Organize files into school-year folders inside spotsy safely.
    
    Parameters:
    - source_folder: str, where files currently live
    - destination_root: str, top-level spotsy folder
    - school_year: str, e.g. '2025-2026'
    - dry_run: bool, if True, prints actions without moving
    """
    
    # Only move files starting with 2-3 capital letters
    initials_pattern = r'^[A-Z]{2,3}'

    # Keywords to map to subfolders
    keywords = {
        '_IEP_': 'IEP',
        'Meeting_Notice': 'meeting_notice',
        'Eval_Consent': 'eval_consent',
        'PWN': 'PWN',
        'POC': 'POC',
        'Speech_Eval': 'speech_eval',
        '_SEC_': 'SEC',
        ' SPS': 'SPS',
        '_Eligibility': 'Eligibility',
        '_Screening': 'Screening',
        '_Observation': 'Observation'
    }

    # Build year folder under spotsy
    year_folder = os.path.join(destination_root, school_year)
    os.makedirs(year_folder, exist_ok=True)

    print(f"\nProcessing files for school year: {school_year}")
    print(f"Dry run mode: {dry_run}\n")

    for filename in os.listdir(source_folder):
        if not re.match(initials_pattern, filename):
            continue

        source_path = os.path.join(source_folder, filename)

        if not os.path.isfile(source_path):
            continue

        for keyword, subfolder in keywords.items():
            if keyword in filename:
                destination_dir = os.path.join(year_folder, subfolder)
                os.makedirs(destination_dir, exist_ok=True)

                destination_path = os.path.join(destination_dir, filename)

                if os.path.exists(destination_path):
                    print(f"[SKIPPED] Already exists: {filename}")
                    break

                if dry_run:
                    print(f"[DRY RUN] Would copy: {filename} → {school_year}/{subfolder}")
                else:
                    try:
                        shutil.copy2(source_path, destination_path)
                        print(f"[COPIED] {filename} → {school_year}/{subfolder}")
                    except Exception as e:
                        print(f"[ERROR] {filename}: {e}")

                break

# -----------------------------
# EXAMPLE USAGE
# -----------------------------
if __name__ == "__main__":
    source_folder = '/Users/laurenkraynak/Documents'
    destination_root = '/Users/laurenkraynak/Documents/spotsy'
    school_year = '2025-2026'

    # First, do a dry run to see what would happen
    # sort_files(source_folder, destination_root, school_year, dry_run=True)

    # When ready to copy, set dry_run=False
    sort_files(source_folder, destination_root, school_year, dry_run=False)
