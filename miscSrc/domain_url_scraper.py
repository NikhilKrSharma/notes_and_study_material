import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_urls(url='https://www.skytowner.com', check_string='skytowner'):

    try:
   
        visited = set()
        urls_to_crawl = [url]

        request_count = 0

        while urls_to_crawl:
            current_url = urls_to_crawl.pop(0)
            current_url = current_url.rstrip('/')

            if current_url not in visited:
                request_count += 1

                try:
                    response = requests.get(current_url)
                    response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    print(f"[!] HTTP error {e} while crawling {current_url}")
                    continue
                except requests.exceptions.RequestException as e:
                    print(f"[!] Request error {e} while crawling {current_url}")
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')
                count = 0
                for link in soup.find_all('a'):
                    count += 1
                    href = link.get('href')

                    if href is not None:
                        full_url = urljoin(current_url, href)   
                        # print(f'\t{count}. {full_url}')              

                        if check_string in full_url and full_url not in visited:
                            urls_to_crawl.append(full_url)

                print(f'[+] Found {count} URLs while crawling {current_url}')

            
            if request_count==100:
                sleep_time = random.randint(1,6)
                time.sleep(sleep_time)
                print(f'*** Sleeping for {sleep_time} seconds after {100} requests ***\n')

            visited.add(current_url)


        return visited
    
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting...")
        return visited

if __name__  == "__main__":
    base_url = input("Enter the URL to start with:\n")
    search_string = input("Enter the string you want to find in URLs:\n")
    if base_url and search_string:
        result = crawl_urls(base_url, search_string)
    else:
        result = crawl_urls()

    with  open('output.txt', 'w') as f:
        f.write('\n'.join(result))

