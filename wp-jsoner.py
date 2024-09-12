import requests
import argparse
import sys

def fetch_user_slugs(url):
    try:
        # Append the endpoint to the base URL
        api_url = f"https://{url}/wp-json/wp/v2/users"
        
         # Set a custom User-Agent header to mimic a browser. This is needed as some Wordpress instances block requests from the requests library due to the User-Agent used:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        
        # Send a GET request with the custom headers
        response = requests.get(api_url, headers=headers)        
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Failed to retrieve data from {api_url} (Status code: {response.status_code})")
            sys.exit(1)
        
        # Parse the JSON response
        users = response.json()
        
        # Extract and print the value of the 'slug' field which contains the user name for each disclosed user
        for user in users:
            print(f"User: {user.get('slug', 'N/A')}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Fetch and display users disclosed by the wp-json/wp/v2/users endpoint")
    parser.add_argument('-u', '--url', required=True, help="The base URL of the WordPress site (e.g., 'example.com').")

    args = parser.parse_args()

    # Fetch and print user slugs
    fetch_user_slugs(args.url)

if __name__ == "__main__":
    main()
