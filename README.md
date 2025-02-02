## ModSync
ModSync is a Python script that helps compare the contents of two folders to find Minecraft mod files (JARs) that are unique to each folder. It ignores version differences and focuses on file names to ensure synchronization between mod directories.

## Features
- Compares two directories for Minecraft mod files.
- Ignores version numbers in filenames, focusing on the mod name.
- Lists mods that are only present in one directory and not the other.

## Requirements
Python 3.x

---

## Usage
- Clone or download the project.
- Open your terminal and navigate to the project folder.
- Run the script with two folder paths as arguments:
```
python script.py "<folder1>" "<folder2>"
```
Replace <folder1> and <folder2> with the paths to the folders you want to compare.

### Example:
```
python script.py "/path/to/folder1" "/path/to/folder2"
```
The script will display a list of mod files that are unique to each folder.

Example Output
```
Files only found in folder 1:
  AwesomeMod-1.2.3.jar, CoolMod-3.4.5.jar

Files only found in folder 2:
  AnotherMod-2.1.0.jar
```
In this example:
- Folder 1 contains the mods AwesomeMod-1.2.3.jar and CoolMod-3.4.5.jar, but these mods do not appear in Folder 2.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
