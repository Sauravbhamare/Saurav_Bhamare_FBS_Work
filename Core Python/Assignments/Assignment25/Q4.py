import re

def extract_urls(text):
    
    pattern = r'https?://[^\s,"]+'
    urls = re.findall(pattern , text)
    return urls

text ='''Visit our website at https://www.firstbit.in or follow us on
http://facebook.com/firstbitsolutions.
You can also check https://blog.firstbit.in/articles for more info.'''

result = extract_urls(text)

print("Extracted URLs:")
for url in result:
    print(url)
