from astropy.io import fits

def inspect_fits_file(fits_file):
    # Open the FITS file
    with fits.open(fits_file) as hdul:
        # Print the structure of the FITS file
        hdul.info()  # Display information about the HDUs
        
        # Check if SPECTRUM HDU exists
        if 'SPECTRUM' in hdul:
            spectrum_hdu = hdul['SPECTRUM']
            # Display the column names
            print("SPECTRUM HDU column names:", spectrum_hdu.columns)
        else:
            print("SPECTRUM HDU not found.")

if __name__ == "__main__":
    # Provide the correct filename here
    inspect_fits_file('ch2_cla_l1_20240630T203137197_20240630T203145197.fits')
