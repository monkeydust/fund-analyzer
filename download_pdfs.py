### HELPER FUNCTION 1###
### DOWNLOAD PDF FILES FROM CSV with URLs ###
import os
import requests
import pandas as pd
from urllib.parse import urlparse

def download_pdfs(csv_path, output_directory="process_pdfs"):
    # Read URLs from CSV file without headers

    try:
        # Read CSV with no header, just a list of URLs
        df = pd.read_csv(csv_path, header=None, names=['urls'])
        url_list = df['urls'].tolist()
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return

    os.makedirs(output_directory, exist_ok=True)
    failed_downloads = []

    for url in url_list:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            content_disposition = response.headers.get('Content-Disposition')
            if content_disposition:
                filename = content_disposition.split('filename=')[1].strip('"\'')
            else:
                filename = os.path.basename(urlparse(url).path)
                if not filename.endswith('.pdf'):
                    filename = f"{filename}.pdf"
            
            filepath = os.path.join(output_directory, filename)
            
            print(f"Downloading: {url}")
            print(f"Saving as: {filename}")
            
            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            
            print(f"Successfully downloaded: {filename}")
            
        except Exception as e:
            print(f"Failed to download {url}: {str(e)}")
            failed_downloads.append(url)
    
    print(f"\nDownload Summary:")
    print(f"Total URLs: {len(url_list)}")
    print(f"Successfully downloaded: {len(url_list) - len(failed_downloads)}")
    print(f"Failed downloads: {len(failed_downloads)}")

# Call the function
csv_file_path = "urls.csv"  # Your CSV file path
download_pdfs(csv_file_path, "process_pdfs")
