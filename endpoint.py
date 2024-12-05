import argparse
from bs4 import BeautifulSoup

# Fungsi untuk membaca dan menampilkan endpoint dari file HTML
def extract_endpoints(filenames):
    for filename in filenames:
        with open(filename, 'r') as file:
            html_content = file.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        endpoints = [link['href'] for link in soup.find_all('a', href=True) if link['href'].startswith('/')]
        
        # Tampilkan hasil
        for endpoint in endpoints:
            print(endpoint)

# Setup argumen
parser = argparse.ArgumentParser(description="Extract endpoints from HTML files with <a href='/...'> tags")
parser.add_argument('filenames', nargs='+', help="List of HTML files to process (e.g., file1.html file2.html file3.html)")
args = parser.parse_args()

# Eksekusi fungsi
extract_endpoints(args.filenames)
