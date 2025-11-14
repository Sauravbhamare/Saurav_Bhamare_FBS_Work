import re

def extract_dates(text):
    
    pattern = r"(\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4})"
    
    matches = re.findall(pattern, text)
    return matches


text = '''
Meeting dates:
01/15/2024
23-08-2025
Project started on January 1,2023 and ended on December 31, 2024'''

result = extract_dates(text)
print("Extracted Dates:")
for date in result:
    print("-",date)