File Control and Deletion Utility
This Python script allows you to control and delete files from a specified directory based on a list of filenames provided in a configuration file.

Description
The script reads filenames from a configuration file (config.txt) and combines them with filenames from selected text files. It then checks a target directory for files that are not in the combined list and deletes them.

Usage
Create a configuration file named config.txt and add filenames to it, each on a separate line.
Run the script and select text files containing additional filenames when prompted.
The script will combine the filenames from the configuration file and selected text files, and then delete any files in the target directory that are not in the combined list.
Requirements
Python 3.x
path library
Installation
Ensure you have Python 3.x installed on your system.
Install the path library:
pip install path
Configuration
config.txt: Create this file and add filenames to it, each on a separate line.
HEDEF: Replace this variable with the path to your target directory.
Usage Example
Suppose you have a config.txt file with the following filenames:
file1.txt
file2.txt
And you select a text file named additional_files.txt containing:
file3.txt
file4.txt
The script will combine these filenames and delete any files in the target directory that are not in the combined list.

Important Notes
Ensure that you have appropriate permissions for deleting files in the target directory.
Use caution when deleting files, as the script permanently removes them from the target directory.
License
This project is licensed under the MIT License.

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Açıklama : 
Bu uygulamada verilen .txt belgesindeki verileri kaynak dizinden silmek için kullanılmaktadır.
