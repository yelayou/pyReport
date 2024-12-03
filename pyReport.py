import re
from collections import defaultdict, Counter
from datetime import datetime

# Get the current date formatted as YYYY-MM-DD to get today's file
current_date = datetime.now().strftime("%Y-%m-%d")

# File path (update the path as needed)
LOG_FILE = "/Users/yelayou/desktop/academy/lhl/shared/access_" + current_date + ".log"
OUTPUT_FILE = "/Users/yelayou/desktop/academy/lhl/shared/error_report.txt"

# Regex pattern for parsing log entries with status codes 400 and 500
LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+).*\s(400|500)\s'

# Create a dictionary to store occurrences of error codes per IP
ip_error_count = defaultdict(lambda: defaultdict(int))

# Reading the log file and parsing the entries
with open(LOG_FILE, 'r') as log_file:
    for line in log_file:
        match = re.search(LOG_PATTERN, line)
        if match:
            ip = match.group(1)  # IP address is the first capture group
            status = match.group(2)  # Status code is the second capture group
            ip_error_count[ip][status] += 1  # Increment the count for this IP and error code

# Write the error counts to the output file
with open(OUTPUT_FILE, 'w') as output_file:
    output_file.write("Source IP | Error Code | Count\n")
    output_file.write("--------------------------------\n")
    for ip, statuses in ip_error_count.items():
        for status, count in statuses.items():
            output_file.write(f"{ip} | {status} | {count}\n")

print(f"Report written to {OUTPUT_FILE}")
