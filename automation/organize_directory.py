import os
import shutil

# The directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))
script_name = os.path.basename(__file__)

print("Welcome to the GT organize.py script")

# A dictionary to map directories to their file extensions
# This makes it easy to add new file types in the future
DIR_MAPPINGS = {
    "images": (".png", ".jpeg", ".jpg"),
    "videos": (".mp4", ".webm", ".mkv"),
    "docs": (".pdf", ".doc", ".docx"),
    "archives": (".zip", ".rar", ".tar", ".gz", ".7z"),
    "apps": (".dmg", ".exe", ".msi", ".pkg", ".deb"),
    "codes": (".py", ".css", ".html", ".js"),
}

def organize_files():
    """Organizes files in the current directory based on their extension."""
    for filename in os.listdir(current_dir):
        # Skip the script itself and any directories
        if filename == script_name or not os.path.isfile(os.path.join(current_dir, filename)):
            continue

        moved = False
        for dest_folder, extensions in DIR_MAPPINGS.items():
            if filename.lower().endswith(extensions):
                # Create the destination folder if it doesn't exist
                dest_path = os.path.join(current_dir, dest_folder)
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                
                # Move the file
                src_path = os.path.join(current_dir, filename)
                shutil.move(src_path, dest_path)
                print(f"Moved '{filename}' to '{dest_folder}/'")
                moved = True
                break  # Stop checking once the file is moved
        
        if not moved:
            print(f"Skipped '{filename}', no matching category.")

if __name__ == "__main__":
    organize_files()
    print("\nDirectory organization complete.")
