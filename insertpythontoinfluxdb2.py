# insert data into InfluxDB 2.0 using the Point class
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime

# Define your InfluxDB 2.0 connection details
token = "your-token"
org = "your-org"
bucket = "your-bucket"
url = "http://localhost:8086"

# Create an InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)

# Create a write API
write_api = client.write_api(write_options=SYNCHRONOUS)

# Create a point to write
point = Point("measurement_name") \
    .tag("tag_key", "tag_value") \
    .field("field_key", 123.45) \
    .time(datetime.datetime.utcnow(), WritePrecision.NS)

# Write the point to the database
write_api.write(bucket=bucket, org=org, record=point)

# Close the client
client.close()