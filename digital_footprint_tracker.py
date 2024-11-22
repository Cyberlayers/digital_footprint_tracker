import requests

# List of websites to check
websites = [
    "https://github.com/{}",
    "https://twitter.com/{}",
    "https://instagram.com/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.facebook.com/{}"
]

def track_digital_footprint(username):
    print(f"Tracking digital footprint for: {username}")
    for site in websites:
        url = site.format(username)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Found profile: {url}")
            else:
                print(f"[-] No profile found: {url}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error accessing {url}: {e}")

if __name__ == "__main__":
    username = input("Enter the username to search for: ")
    track_digital_footprint(username)
