# Install with pip install firecrawl-py
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key='fc-204cfc3fbbf345fdbaa2970495536304')

response = app.scrape_url(url='https://www.centre-valdeloire.fr/', params={
	'formats': [ 'markdown' ],
})

import markdown

# Your Markdown text (replace this with the actual text)
markdown_text = str(response)
# Your Markdown text here...

# Create a Markdown instance
md = markdown.Markdown()

# Convert Markdown to HTML
html = md.convert(markdown_text)

# Use a HTML parser to extract the text content
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract text and remove extra whitespace
text = soup.get_text().strip()

# Print the extracted text
print(text)