import requests
import subprocess


def download_image(url, file_name):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.midjourney.com/',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    })

    response = session.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded successfully: {file_name}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


def display_image(file_name):
    try:
        subprocess.run(['chafa', file_name])
    except FileNotFoundError:
        print("chafa is not installed. Please install it using 'sudo apt-get install chafa'")


def main():
    url = "https://cdn.midjourney.com/e5c8e85d-3b2a-427d-b8a4-a9b6284bc631/0_0.png"
    url = "https://i.ibb.co/2jLCsqK/0-0.png"
    file_name = "image.png"

    download_image(url, file_name)
    display_image(file_name)


if __name__ == "__main__":
    main()
