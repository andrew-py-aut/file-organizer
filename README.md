# Automatic File Organizer

A simple but powerful Python script to automatically organize files in a directory (e.g., your Downloads folder) into subdirectories based on their file types.

## Features

-   **Easy to Configure**: All settings are managed in a simple `config.json` file. No need to edit the code.
-   **Customizable Mappings**: You decide which file extensions go into which folders.
-   **Logging**: The script logs all its actions to a `file_organizer.log` file for easy tracking and debugging.
-   **Safe**: It automatically creates destination folders if they don't exist and skips directories to avoid unintended moves.
-   **Cross-Platform**: Works on Windows, macOS, and Linux.

## Folder Structure

├── .gitignore
├── LICENSE
├── README.md
├── config.json
├── organizer.py
└── requirements.txt


## Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/andrew-py-aut/file-organizer.git
    cd file-organizer
    ```

2.  **Set up a Virtual Environment (Recommended)**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    This script uses only standard Python libraries, so no external packages are needed. The `requirements.txt` is included for good practice.

## How to Use

1.  **Edit the Configuration**
    Open `config.json` and change the `source_directory` to the path of the folder you want to organize (e.g., your Downloads folder).

    **Important**: Use forward slashes `/` for the path, even on Windows.
    ```
    json
    {
      "source_directory": "C:/Users/YourUser/Downloads",
      "mappings": { ... }
    }
    ```
    You can also customize the `mappings` section to add or change file categories and extensions.

2.  **Run the Script**
    Execute the script from your terminal:
    ```bash
    python organizer.py
    ```

3.  **Check the Results**
    The script will move files from your source directory into subfolders like `Images`, `Documents`, etc., within that same source directory. Check `file_organizer.log` to see a detailed report of all actions performed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.