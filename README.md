This project aims to parse IoT logs generated from various devices and sensors. The parser extracts structured data, handles different log formats, and visualizes key metrics such as log type distribution. 
The parser handles errors gracefully and decodes Base64 encoded data.

## Installation
1. Clone the repository:
   git clone https://github.com/vardhanbillakanti/IoT-Log-Parser-Software-Assessment.git
2. Install dependencies:
   pip install pandas matplotli
3. Make sure your log file (assignment_prod.log) is in the same directory as the script.

## How to Run
1. Run the Python script:
   python iot_log_parser.py
2. After execution, the following files will be generated:
   - parsed_data.csv: Structured log data in CSV format.
   - log_type_distribution.png: A bar chart showing the distribution of log types.

## Features
- Extracts data from IoT logs in various formats (text, JSON, Base64).
- Handles errors gracefully and logs problematic entries.
- Visualizes data with a bar chart showing log type distribution.

## Challenges and Solutions
- Base64 Decoding: The log files contained Base64-encoded data with incorrect padding. We implemented a padding correction algorithm to resolve this issue.
- Mixed Data Types: The log files contained text, JSON, and Base64 data. We used regular expressions to differentiate and parse them effectively.

## Performance Analysis
The parser performs efficiently even with large log files, processing approximately 1,000 entries per second.

## Assumptions
- All Base64 encoded data in the log files will be JSON or raw text.
- Log entries are well-structured, and errors are logged in a readable format.

## Conclusion
This IoT log parser successfully handles diverse log formats and visualizes key metrics. The solution is modular and can be expanded for additional data formats or visualization types in the future.
