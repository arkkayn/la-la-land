import os
import shutil
import re

def archive_files(source_folder, archive_root, school_year, dry_run=True):
    """
    Archive ONLY the files that match the Spotsy sorting rules.

    Parameters:
    - source_folder: str, where the original files currently live
    - archive_root: str, top-level archive folder (e.g., '/Users/laurenkraynak/Documents/_archive')
    - school_year: str, e.g., '2025-2026'
    - dry_run: bool, if True, prints actions without moving
    """

    # Only move files starting with 2-3 capital letters
    initials_pattern = r'^[A-Z]{2,3}'

    # Only files that match these keywords were sorted
    keywords = [
        '_IEP_',
        'Meeting_Notice',
        'Eval_Consent',
        'PWN',
        'POC',
        'Speech_Eval',
        '_SEC_',
        ' SPS',
        '_Eligibility',
        '_Screening',
        '_Observation'
    ]

    # Build the archive folder for the year
    archive_year_folder = os.path.join(archive_root, school_year, 'spotsy_originals')
    os.makedirs(archive_year_folder, exist_ok=True)

    print(f"\nArchiving originals for {school_year}")
    print(f"Dry run mode: {dry_run}\n")

    for filename in os.listdir(source_folder):
        # Skip files that don't start with initials
        if not re.match(initials_pattern, filename):
            continue

        # Skip files that don’t match any of the keywords
        if not any(keyword in filename for keyword in keywords):
            continue

        source_path = os.path.join(source_folder, filename)
        if not os.path.isfile(source_path):
            continue

        destination_path = os.path.join(archive_year_folder, filename)

        if os.path.exists(destination_path):
            print(f"[SKIPPED] Already archived: {filename}")
            continue

        if dry_run:
            print(f"[DRY RUN] Would archive: {filename}")
        else:
            try:
                shutil.move(source_path, destination_path)
                print(f"[ARCHIVED] {filename}")
            except Exception as e:
                print(f"[ERROR] {filename}: {e}")


# -----------------------------
# EXAMPLE USAGE
# -----------------------------
if __name__ == "__main__":
    source_folder = '/Users/laurenkraynak/Documents'
    archive_root = '/Users/laurenkraynak/Documents/_archive'
    school_year = '2025-2026'

    # First, do a dry run to see what would be archived
    # archive_files(source_folder, archive_root, school_year, dry_run=True)

    # When ready to archive originals for real, uncomment:
    archive_files(source_folder, archive_root, school_year, dry_run=False)
