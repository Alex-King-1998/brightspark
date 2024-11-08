# 🌟 Bright Spark CLI Tool

**Bright Spark CLI Tool** is a command-line tool for processing CSV files. It reads CSV records, sorts them by `division` and `points`, and outputs the top records in either YAML or JSON format. This tool is useful for filtering and formatting records from large datasets.

---

## ✨ Features

- 📂 Reads a CSV file and validates its structure.
- 📊 Sorts records by `division` (ascending) and `points` (descending).
- 🔝 Outputs the top records based on a user-specified quantity.
- 🌐 Provides output in YAML or JSON format.
- 💾 Offers options to display the output or save it to a file.
- 🛠 Handles various edge cases, including missing or invalid data.

---

## 🚀 Installation

### Prerequisites

- Python 3.6+
- [pip](https://pip.pypa.io/en/stable/installation/)

### Install from PyPI

Install this tool directly from PyPI:

```bash
pip install bright-spark-cli-tool
```

### Install from Source
1. Clone the repository from GitHub:

```bash
git clone https://github.com/yourusername/bright-spark-cli-tool.git
cd bright-spark-cli-tool
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Install the tool:
   
```bash
pip install .
```

## 🛠️ Usage
Once installed, you can run the tool using the command:

```bash
cli_tool
```

### Interactive Mode
When you run **cli_tool**, it will prompt you to:
1. Enter the path to your CSV file.
2. Specify the number of top records to display (default is 3).
3. Choose the output format (YAML or JSON).
4. Optionally, specify a file to save the output.

### Example
For a CSV file named **sample.csv** with content:
```csv
firstname,lastname,date,division,points,summary
John,Doe,2023-05-05,1,90,Task A
Jane,Smith,2023-06-06,2,85,Task B
```

Running the tool might produce output like:

```yaml
records:
- name: John Doe
  details: In division 1 from 2023-05-05 performing Task A
- name: Jane Smith
  details: In division 2 from 2023-06-06 performing Task B
```

## ⚙️ Command-Line Options
This tool is interactive, so it will guide you through the setup. No command-line arguments are required.

## 🧪 Testing
This project includes unit tests. To run the tests, use:

```bash
python -m unittest discover
```
The tests will validate each major function, including CSV reading, sorting, formatting, and handling invalid data.

## 📄 Requirements
All dependencies are specified in **requirements.txt**.

## 📜 Logging
Logs are saved to **cli_tool.log** and are also displayed on the console for easy tracking.