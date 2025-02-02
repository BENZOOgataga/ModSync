## ModSync
ModSync is a Python script that helps compare the contents of two folders to find Minecraft mod files (JARs) that are unique to each folder. It ignores version differences and focuses on file names to ensure synchronization between mod directories.

Features
Compares two directories for Minecraft mod files.
Ignores version numbers in filenames, focusing on the mod name.
Lists mods that are only present in one directory and not the other.

## Requirements
Python 3.x

## Usage
- Clone or download the project.
- Open your terminal and navigate to the project folder.
- Run the script with two folder paths as arguments:
```
python modsync.py "<folder1>" "<folder2>"
```
Replace <folder1> and <folder2> with the paths to the folders you want to compare.

### Example:
```
python script.py "/path/to/folder1" "/path/to/folder2"
```
The script will display a list of mod files that are unique to each folder.

### Example Output
```
Fichiers présents uniquement dans le dossier 1:
  AwesomeMod-1.2.3.jar, CoolMod-3.4.5.jar

Fichiers présents uniquement dans le dossier 2:
  AnotherMod-2.1.0.jar
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
