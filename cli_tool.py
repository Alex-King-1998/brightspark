import csv
import sys
import yaml
import json
import logging
from datetime import datetime

# Set up logging for error tracking and debugging
# Logs to both console and a file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("cli_tool.log"), logging.StreamHandler(sys.stdout)],
)


def read_csv(file_path):
    """
    Reads a CSV file and validates its content.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        list of dict: A list of records where each record is a dictionary with keys
                      'firstname', 'lastname', 'date', 'division', 'points', and 'summary'.

    Raises:
        SystemExit: If the file cannot be read or processed.
    """
    records = []
    required_columns = {
        "firstname",
        "lastname",
        "date",
        "division",
        "points",
        "summary",
    }

    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)

            # Check if all required columns are present
            if not required_columns.issubset(reader.fieldnames):
                missing = required_columns - set(reader.fieldnames)
                logging.error(f"Missing required columns in CSV file: {missing}")
                sys.exit(1)

            for row in reader:
                try:
                    # Validate and parse each row
                    division = int(row["division"])
                    points = int(row["points"])
                    date = datetime.strptime(row["date"], "%Y-%m-%d").date()
                    records.append(
                        {
                            "firstname": row["firstname"],
                            "lastname": row["lastname"],
                            "date": row["date"],
                            "division": division,
                            "points": points,
                            "summary": row["summary"],
                        }
                    )
                except ValueError as ve:
                    # Log and skip rows with invalid data formats
                    logging.warning(f"Skipping invalid row {row}: {ve}")
        if not records:
            logging.warning("CSV file contains no valid records.")
        return records
    except Exception as e:
        # Log an error if the file cannot be read
        logging.error(f"Error reading CSV file: {e}")
        sys.exit(1)


def get_top_records(records, top_n):
    """
    Sorts records by division and points, then selects the top N records.

    Args:
        records (list of dict): List of records to sort.
        top_n (int): Number of top records to return.

    Returns:
        list of dict: Sorted list containing the top N records.
    """
    # Sort by division (ascending) and points (descending)
    sorted_records = sorted(records, key=lambda x: (x["division"], -x["points"]))
    return sorted_records[:top_n]


def format_to_yaml(records):
    """
    Formats records into YAML format.

    Args:
        records (list of dict): List of records to format.

    Returns:
        str: YAML formatted string.
    """
    output = {"records": []}
    for record in records:
        # Construct name and details for YAML output
        name = f"{record['firstname']} {record['lastname']}"
        details = f"In division {record['division']} from {record['date']} performing {record['summary']}"
        output["records"].append({"name": name, "details": details})
    return yaml.dump(output, sort_keys=False)


def format_to_json(records):
    """
    Formats records into JSON format.

    Args:
        records (list of dict): List of records to format.

    Returns:
        str: JSON formatted string.
    """
    output = {"records": []}
    for record in records:
        # Construct name and details for JSON output
        name = f"{record['firstname']} {record['lastname']}"
        details = f"In division {record['division']} from {record['date']} performing {record['summary']}"
        output["records"].append({"name": name, "details": details})
    return json.dumps(output, indent=2)


def interactive_menu():
    """
    Provides an interactive menu for user input to configure the CSV processing options.

    Returns:
        tuple: Contains file_path (str), top_n (int), output_format (str), and output_file (str or None).
    """
    # Get the CSV file path from the user
    file_path = input("Enter the path to the CSV file: ").strip()

    # Choose the number of top records, default to 3 if not specified or invalid
    try:
        top_n = int(
            input("Enter the number of top records to display (default is 3): ") or "3"
        )
    except ValueError:
        print("Invalid input. Defaulting to 3.")
        top_n = 3

    # Choose the output format (YAML by default)
    print("Choose output format:")
    print("1) YAML (default)")
    print("2) JSON")
    format_choice = input("Enter your choice (1 or 2): ").strip()
    output_format = "json" if format_choice == "2" else "yaml"

    # Choose to save to a file or display on stdout
    save_choice = (
        input("Would you like to save the output to a file? (y/n, default is n): ")
        .strip()
        .lower()
    )
    output_file = (
        input("Enter the output file path: ").strip() if save_choice == "y" else None
    )

    return file_path, top_n, output_format, output_file


def main():
    """
    Main function to execute the CLI tool.

    This function gathers user input, processes the CSV file, and outputs the results
    in the chosen format and location (either stdout or a file).
    """
    # Get user inputs from the interactive menu
    file_path, top_n, output_format, output_file = interactive_menu()

    # Read and validate records from the CSV file
    logging.info(f"Processing file: {file_path}")
    records = read_csv(file_path)
    if not records:
        logging.error("No valid records found. Exiting.")
        sys.exit(1)
    logging.info(f"Successfully read {len(records)} records from {file_path}")

    # Sort and get top N records
    top_records = get_top_records(records, top_n)
    logging.info(f"Selected top {top_n} records for output.")

    # Format output based on chosen format
    output = (
        format_to_json(top_records)
        if output_format == "json"
        else format_to_yaml(top_records)
    )
    logging.info(f"Formatted output as {output_format.upper()}.")

    # Output to file or stdout based on user choice
    if output_file:
        try:
            with open(output_file, "w") as f:
                f.write(output)
            logging.info(f"Output written to {output_file}")
        except IOError as e:
            logging.error(f"Failed to write output to file: {e}")
            sys.exit(1)
    else:
        print(output)
        logging.info("Output printed to stdout.")


if __name__ == "__main__":
    main()