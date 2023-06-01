# Importing necessary modules
import re

# Opening the HTML file
with open('messages.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Finding all text between div class="text" using regular expressions
texts = re.findall(r'<div class="text">(.*?)</div>', html, flags=re.DOTALL)

# Writing the extracted texts to a new text file
with open('extracted_text.txt', 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(text.strip() + '\n')

