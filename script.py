import os
import sys
import re


def normalize(filename):
    """
    Extracts the mod name without the version.
    Example:
      "AwesomeMod-1.2.3.jar" → "awesomemod"
      "Cool_Mod_2.0.jar"  → "cool_mod"
    """
    name, _ = os.path.splitext(filename)  # Get the file name without extension
    # Looks for a version pattern at the end, optionally preceded by a '-' or '_'
    m = re.match(r"^(.*?)[-_]?(\d+(?:\.\d+)*)?$", name)
    if m:
        return m.group(1).lower()  # Return the mod name in lowercase
    return name.lower()  # Return the mod name in lowercase (if no version is found)


def list_normalized_files(folder):
    """
    Returns a dictionary:
      key   : normalized mod name
      value: list of original files corresponding to that mod name
    """
    files_dict = {}
    try:
        for f in os.listdir(folder):  # Iterate over each file in the folder
            full_path = os.path.join(folder, f)  # Full path of the file
            if os.path.isfile(full_path):  # Check if it's a file (not a folder)
                norm = normalize(f)  # Normalize the file name
                files_dict.setdefault(norm, []).append(f)  # Add to dictionary
    except FileNotFoundError:
        print(f"The folder '{folder}' does not exist.")  # Error if folder doesn't exist
        sys.exit(1)  # Exit the program with an error code
    return files_dict  # Return the dictionary with normalized names


def main():
    # Check if the user provided exactly two folder paths
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder1> <folder2>")
        sys.exit(1)  # Exit the program if incorrect number of arguments

    folder1, folder2 = sys.argv[1], sys.argv[2]  # Get the folder paths from arguments

    files1 = list_normalized_files(folder1)  # Get the files from folder 1
    files2 = list_normalized_files(folder2)  # Get the files from folder 2

    set1 = set(files1.keys())  # Get the set of normalized names from folder 1
    set2 = set(files2.keys())  # Get the set of normalized names from folder 2

    only_in_1 = set1 - set2  # Mods that are in folder 1 but not in folder 2
    only_in_2 = set2 - set1  # Mods that are in folder 2 but not in folder 1

    if only_in_1:  # If there are mods only in folder 1
        print("Files only found in folder 1:")
        for key in sorted(only_in_1):  # Print the sorted mod names
            originals = ", ".join(files1[key])  # List original file names
            print(f"  {originals}")
    else:
        print("No unique files found in folder 1.")  # If no unique files found in folder 1

    if only_in_2:  # If there are mods only in folder 2
        print("\nFiles only found in folder 2:")
        for key in sorted(only_in_2):  # Print the sorted mod names
            originals = ", ".join(files2[key])  # List original file names
            print(f"  {originals}")
    else:
        print("\nNo unique files found in folder 2.")  # If no unique files found in folder 2


if __name__ == "__main__":
    main()  # Run the main function
