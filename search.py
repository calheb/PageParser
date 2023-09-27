import requests
from bs4 import BeautifulSoup
import sys

class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.current = 0
        self.bar_length = 40

    def increment(self):
        self.current += 1
        self.render()

    def render(self):
        progress = self.current / self.total
        filled_length = int(self.bar_length * progress)
        bar = f"[{'#' * filled_length}{'-' * (self.bar_length - filled_length)}] {progress * 100:.0f}%"
        sys.stdout.write(f"\r{bar}")
        sys.stdout.flush()

def find_files(url, keywords, matches, progress_bar, depth=0, max_depth=1):
    if depth > max_depth:
        return

    response = requests.get(url)
    response.raise_for_status() # Check if request was successful.
    soup = BeautifulSoup(response.content, 'html.parser')

    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href and href.endswith('/'):  # Assuming dirs end in /
            find_files(url + href, keywords, matches, progress_bar, depth + 1, max_depth)
            if depth == 0:
                progress_bar.increment()

        elif depth == 1:
            for keyword in keywords:
                if keyword in href:
                    match_url = f'{url}{href}'
                    matches.append((keyword, match_url))

base_url = 'https://mirrors.kernel.org/gentoo/distfiles/'
keywords = ['andale32.exe', 'arial32.exe', 'arialb32.exe', 'comic32.exe', 'courie32.exe', 'georgi32.exe', 'impact32.exe', 'times32.exe', 'trebuc32.exe', 'verdan32.exe', 'webdin32.exe'] 

# Count number of dirs on base page.
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')
dir_count = sum(1 for a_tag in soup.find_all('a') if a_tag.get('href', '').endswith('/'))

matches = []
progress_bar = ProgressBar(dir_count)

sys.stdout.write(f'Searching {base_url}...\n')
sys.stdout.flush()

find_files(base_url, keywords, matches, progress_bar)

# Display search summary.
print("\nSearch complete.")
if matches:
    print("Matches found:")
    for keyword, match in matches:
        print(f"{keyword}: {match}")
else:
    print("No matches found.")
