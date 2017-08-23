from urllib import request #a new a short cut method to import module from a library

tata_stl_url = 'http://www.google.com/finance/historical?q=NASDAQ%3AGOOGL&ei=cr6JWYGaIYGtuAScnZT4CQ&output=csv' # link to a csv file

def download_stock_data(csv_url): # here csv_url is a parameter that its a csv file in a url
    response = request.urlopen(csv_url) # function to open the url using response and copy the data
    csv = response.read() # reads the data and stores the data
    csv_str = str(csv) # calling the data a string data and converts the data to string to print it out
    lines = csv_str.split("\\n") # the whole data in rows and colums into the terminal to break up the data it collected in respective line
    dest_url = r'tata_stl.csv' # here ""r"" is use to known it as a raw string and save it to filename.csv
    fx = open(dest_url, "w") #open up the file and load it over ram
    for line in lines: # functn to write a file
        fx.write(line + "\n")
    fx.close()

download_stock_data(tata_stl_url)
