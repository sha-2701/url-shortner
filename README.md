# url-shortner

This is a Python script that converts long URLs into shortened URLs using the TinyURL API.

## Features
- Converts long URLs into short URLs using TinyURL's API.
- Can accept multiple URLs as command-line arguments.
- Prompts the user for input interactively if no URLs are provided as arguments.

## Prerequisites
- Python 3.x

## How to Use
### Running the Script
1. Save the script as a `.py` file (e.g., `url_shortener.py`).
2. Open a terminal or command prompt.

### Providing URLs as Command-Line Arguments
Run the script and provide one or more URLs as arguments:
```bash
python url_shortener.py <URL1> <URL2> ...
```
Example:
```bash
python url_shortener.py http://example.com https://google.com
```
Output:
```
Shortened URL: http://tinyurl.com/example1
Shortened URL: http://tinyurl.com/example2
```

### Interactive Mode
If no URLs are provided as arguments, the script will prompt you to enter a URL:
```bash
python url_shortener.py
```
Input:
```
Enter a URL to shorten: http://example.com
```
Output:
```
Shortened URL: http://tinyurl.com/example1
```

## Code Overview
### Functions
#### `short_url(url)`
- Takes a long URL as input.
- Sends a request to the TinyURL API.
- Returns the shortened URL.

#### `main()`
- Handles user input.
- Accepts URLs via command-line arguments or interactively.
- Uses the `short_url()` function to shorten each URL and prints the results.

### Key Imports
- `urlencode` and `urlopen` from `urllib.parse` and `urllib.request` for making API requests.
- `contextlib` for safely closing the network connection after use.
- `sys` for handling command-line arguments.
## Notes
- This script uses the free TinyURL API to generate shortened URLs.
- Ensure that your internet connection is active when running the script.