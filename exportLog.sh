
# Define variables
LOG_FILE="/var/log/apache2/access.log"
DESTINATION_FOLDER="/mnt/shared"
DESTINATION_FILE="${DESTINATION_FOLDER}/access_$(date +%Y-%m-%d).log"


# Copy the log file 
# cp "$LOG_FILE" "$DESTINATION_FILE"

# Filter log file for code 400 or 500 and export to destination with date stamp
grep -E " 400 | 500 " "$LOG_FILE" > "$DESTINATION_FILE"

