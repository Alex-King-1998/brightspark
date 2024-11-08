import unittest
import logging
import os
from cli_tool import read_csv, get_top_records, format_to_yaml, format_to_json

# Set up logging to capture test outputs for each test case
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class TestCliTool(unittest.TestCase):

    def setUp(self):
        """Set up any necessary data before each test."""
        logging.info("Setting up test data.")

        # Sample data for testing
        self.sample_records = [
            {
                "firstname": "John",
                "lastname": "Doe",
                "date": "2023-05-05",
                "division": 1,
                "points": 90,
                "summary": "Task A",
            },
            {
                "firstname": "Jane",
                "lastname": "Smith",
                "date": "2023-06-06",
                "division": 2,
                "points": 85,
                "summary": "Task B",
            },
            {
                "firstname": "Alex",
                "lastname": "Johnson",
                "date": "2023-07-07",
                "division": 1,
                "points": 80,
                "summary": "Task C",
            },
            {
                "firstname": "Taylor",
                "lastname": "Brown",
                "date": "2023-08-08",
                "division": 2,
                "points": 70,
                "summary": "Task D",
            },
        ]

        # Create a temporary CSV file specifically for testing
        self.test_csv_file = "test_sample.csv"
        with open(self.test_csv_file, "w") as f:
            f.write("firstname,lastname,date,division,points,summary\n")
            f.write("John,Doe,2023-05-05,1,90,Task A\n")
            f.write("Jane,Smith,2023-06-06,2,85,Task B\n")

    def tearDown(self):
        """Clean up any resources after each test."""
        logging.info("Tearing down test environment.")
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)
        if os.path.exists("invalid.csv"):
            os.remove("invalid.csv")

    def test_read_csv_valid(self):
        """Test that read_csv correctly reads and parses a valid CSV file."""
        logging.info("Testing read_csv with a valid CSV file.")
        records = read_csv(self.test_csv_file)
        self.assertGreater(len(records), 0, "CSV should contain records")
        logging.info("read_csv successfully parsed the CSV file.")

    def test_read_csv_invalid_file(self):
        """Test read_csv with a non-existent file."""
        logging.info("Testing read_csv with a non-existent file.")
        with self.assertRaises(SystemExit):
            read_csv("non_existent.csv")
        logging.info("read_csv correctly handled a non-existent file.")

    def test_get_top_records(self):
        """Test that get_top_records correctly returns the top N sorted records."""
        logging.info("Testing get_top_records with sample data.")
        top_records = get_top_records(self.sample_records, 2)
        self.assertEqual(len(top_records), 2)
        self.assertEqual(top_records[0]["firstname"], "John")
        logging.info("get_top_records returned the correct top records.")

    def test_get_top_records_edge_case_empty(self):
        """Test get_top_records with an empty list of records."""
        logging.info("Testing get_top_records with an empty list.")
        top_records = get_top_records([], 3)
        self.assertEqual(len(top_records), 0)
        logging.info("get_top_records correctly handled an empty list.")

    def test_format_to_yaml(self):
        """Test that format_to_yaml outputs records in the expected YAML format."""
        logging.info("Testing format_to_yaml with a single record.")
        yaml_output = format_to_yaml([self.sample_records[0]])
        self.assertIn("name: John Doe", yaml_output)
        self.assertIn(
            "details: In division 1 from 2023-05-05 performing Task A", yaml_output
        )
        logging.info("format_to_yaml produced the expected YAML output.")

    def test_format_to_json(self):
        """Test that format_to_json outputs records in the expected JSON format."""
        logging.info("Testing format_to_json with a single record.")
        json_output = format_to_json([self.sample_records[0]])
        self.assertIn("John Doe", json_output)
        self.assertIn("division 1", json_output)
        logging.info("format_to_json produced the expected JSON output.")

    def test_read_csv_with_invalid_data(self):
        """Test read_csv with a CSV containing invalid data types."""
        logging.info("Testing read_csv with a CSV file containing invalid data.")
        # Create an invalid CSV file specifically for this test
        with open("invalid.csv", "w") as f:
            f.write("firstname,lastname,date,division,points,summary\n")
            f.write("Invalid,User,2023-05-05,invalid_division,invalid_points,Task X\n")

        records = read_csv("invalid.csv")
        self.assertEqual(len(records), 0, "Invalid records should be skipped")
        logging.info("read_csv correctly skipped invalid data.")


if __name__ == "__main__":
    # Run the tests with additional logging information
    logging.info("Starting tests for CLI tool...")
    unittest.main()