import re
import json
import base64
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
log_file_path = "assignment_prod.log"  
timestamp_pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+"
base64_pattern = r"BASE64:(.+)"
json_pattern = r"^\{.*\}$"
parsed_data = []
def fix_base64_padding(encoded_str):
    missing_padding = len(encoded_str) % 4
    if missing_padding:
        encoded_str += "=" * (4 - missing_padding)
    return encoded_str
with open(log_file_path, "r") as log_file:
    for line in log_file:
        line = line.strip()
        base64_match = re.match(base64_pattern, line)
        if base64_match:
            try:
                fixed_encoded_str = fix_base64_padding(base64_match.group(1))
                decoded_data = base64.b64decode(fixed_encoded_str).decode("utf-8")
                if re.match(json_pattern, decoded_data):  # Check for JSON content
                    parsed_data.append(json.loads(decoded_data))
                else:
                    parsed_data.append({"type": "unknown_base64", "content": decoded_data})
            except Exception as e:
                parsed_data.append({"type": "error", "error": str(e), "entry": line})
            continue
        if re.match(json_pattern, line):
            try:
                parsed_data.append(json.loads(line))
            except json.JSONDecodeError as e:
                parsed_data.append({"type": "error", "error": str(e), "entry": line})
            continue
        timestamp_match = re.search(timestamp_pattern, line)
        if timestamp_match:
            parsed_data.append({"type": "text_log", "timestamp": timestamp_match.group(0), "entry": line})
            continue
        parsed_data.append({"type": "unknown", "entry": line})
parsed_df = pd.DataFrame(parsed_data)
parsed_df.to_csv("parsed_data.csv", index=False)
log_type_counts = parsed_df["type"].value_counts()
plt.figure(figsize=(8, 5))
log_type_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Distribution of Log Entry Types")
plt.xlabel("Log Type")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("log_type_distribution.png")
plt.show()