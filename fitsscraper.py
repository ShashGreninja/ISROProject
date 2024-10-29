# Script for extracting data from downloaded fits files in directory fitsfiles. For scraping from the lakhs of links in the website itself, another script has been commented below the one beneath this comment.

from astropy.io import fits
import os

def scrape_fits_data(fits_file):
    # Open the FITS file
    with fits.open(fits_file) as hdul:
        # Print the structure of the FITS file
        hdul.info()  # Display information about the HDUs

        # Check if SPECTRUM HDU exists
        if 'SPECTRUM' in hdul:
            spectrum_hdu = hdul['SPECTRUM']
            print(f"\nProcessing: {fits_file}")
            print("SPECTRUM HDU data shape:", spectrum_hdu.data.shape)

            # Access the data
            data = spectrum_hdu.data
            print("Column names:", data.columns)  # Print column names
            
            # Extract CHANNEL and COUNTS columns
            channels = data['CHANNEL']  
            counts = data['COUNTS']  
            
            # Filter non-zero counts
            non_zero_indices = counts != 0
            non_zero_channels = channels[non_zero_indices]
            non_zero_counts = counts[non_zero_indices]

            # Print the non-zero values in a compact format (multiple entries in one line)
            if len(non_zero_channels) > 0:
                print("\nNon-Zero Channel Data (Channel-Count pairs):")
                for i in range(0, len(non_zero_channels), 5):  # Print 5 entries per line
                    entries = [
                        f"({ch}, {ct:.2f})" for ch, ct in zip(
                            non_zero_channels[i:i+5], non_zero_counts[i:i+5]
                        )
                    ]
                    print(" ".join(entries))  # Join entries and print in a single line
            else:
                print("All counts are zero.")
        else:
            print("SPECTRUM HDU not found.")

def process_fits_files(directory):
    # Iterate over all FITS files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.fits'):
            full_path = os.path.join(directory, filename)
            scrape_fits_data(full_path)

if __name__ == "__main__":
    # Specify the folder containing the .fits files
    fits_directory = 'fitsfiles'
    process_fits_files(fits_directory)

# ##############################################################################################################################
# #BELOW IS THE CODE THAT WILL SCRAPE ALL .fits EXTENSION FILES FROM THE GIVEN WEBSITE USING BEAUTIFULSOUP MODULE AND WILL RUN THE SCRIPT TO EXTRACT CHANNEL AND COUNTS FROM EACH FILE WITHOUT ACTUALLY HAVING TO DOWNLOAD SO MANY FILES.

# #CONSIDERED THE NEXT BUTTON FUNCTIONALITY OF THE PAGE TO GET MORE LINKS AND THE POSSIBILITY OF A SERVER TIMEOUT HENCE ADDED A TIME DELAY BETWEEN REQUESTS
# ##############################################################################################################################

# #import requests
# from bs4 import BeautifulSoup
# from astropy.io import fits
# import time

# # Function to scrape all .fits links from the paginated website
# def scrape_fits_links(start_url):
#     fits_links = []
#     next_page = start_url

#     while next_page:
#         # Make a request to the current page
#         response = requests.get(next_page)
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Extract .fits links on the current page
#         links_on_page = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.fits')]
#         fits_links.extend(links_on_page)

#         # Print the links found on this page
#         print(f"Found {len(links_on_page)} .fits links on {next_page}")

#         # Find the "Next" button and get the URL for the next page
#         next_button = soup.find('a', text='Next')
#         if next_button:
#             next_page = next_button['href']
#             if not next_page.startswith('http'):  # Handle relative URLs
#                 next_page = requests.compat.urljoin(start_url, next_page)
#         else:
#             next_page = None  # No more pages

#         # Sleep between requests to avoid overloading the server
#         time.sleep(1)  # Adjust sleep time as needed

#     return fits_links

# # Function to open a .fits file from a URL and extract relevant data
# def process_fits_file(fits_url):
#     response = requests.get(fits_url)
#     with fits.open(response.content) as hdul:
#         # Print the structure of the FITS file
#         hdul.info()  # Display information about the HDUs

#         # Check if SPECTRUM HDU exists
#         if 'SPECTRUM' in hdul:
#             spectrum_hdu = hdul['SPECTRUM']
#             print("SPECTRUM HDU data shape:", spectrum_hdu.data.shape)

#             # Access the data
#             data = spectrum_hdu.data

#             # Print column names for clarity
#             print("Column names:", data.columns)  # Print column names

#             # Extract the CHANNEL and COUNTS columns
#             channel = data['CHANNEL']  # Replace 'CHANNEL' with the actual column name
#             counts = data['COUNTS']    # Replace 'COUNTS' with the actual column name

#             # Filter out non-zero counts
#             non_zero_counts = [(ch, ct) for ch, ct in zip(channel, counts) if ct != 0]

#             # Print non-zero channel and counts in a clean format
#             if non_zero_counts:
#                 print("Non-zero CHANNEL and COUNTS values:")
#                 for ch, ct in non_zero_counts:
#                     print(f"Channel: {ch}, Count: {ct}")
#             else:
#                 print("All values are zero.")
#         else:
#             print("SPECTRUM HDU not found.")

# # Main function to scrape all .fits links and process each file
# def scrape_and_process_fits(start_url):
#     fits_links = scrape_fits_links(start_url)
    
#     for fits_url in fits_links:
#         print(f"Processing: {fits_url}")
#         process_fits_file(fits_url)

#         # Sleep to avoid overloading the server
#         time.sleep(1)  # Adjust as needed

# if __name__ == "__main__":
#     # Provide the starting page of the website containing the .fits links
#     start_url = 'https://example.com/first-page-with-links'  # Replace with actual URL
#     scrape_and_process_fits(start_url)
