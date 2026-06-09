from datetime import datetime
import os

def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Generate filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write file
    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")

    # Confirmation message
    print(f"Log written to {filename}")

    return filename