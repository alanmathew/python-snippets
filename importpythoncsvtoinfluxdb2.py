#insert data from a file to influxdb using CLI
import csv
from influxdb_client import InfluxDBClient, Point, WritePrecision
import subprocess

# Configuration
bucket = "your_bucket"
org = "your_org"
token = "your_token"
url = "http://localhost:8086"

# Function to read CSV and write to InfluxDB using CLI
def insert_csv_to_influxdb(csv_file_path):
    command = [
        "influx", "write",
        "--bucket", bucket,
        "--org", org,
        "--token", token,
        "--file", csv_file_path,
        "--format", "csv"
    ]
    subprocess.run(command, check=True)

# Example usage
csv_file_path = "path_to_your_csv_file.csv"
insert_csv_to_influxdb(csv_file_path)