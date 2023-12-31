import json
from requests_html import HTMLSession
import csv

session = HTMLSession()

url = ('https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-01-10&checkOut=2024-01-11&'
       'children=0&infants=0&location=London%2C+England%2C+United+Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity')

output = session.get(url)

#returns a list
k = output.html.find('#__NEXT_DATA__') 

# extract data to JSON
y = json.loads(k[0].text)

lis = [1, 2, 3, 4, 5 , 6, 7]
i = 0

list = []

# strip data from JSON here
while (i < len(lis)):

    Room_name = y['props']['pageProps']['initialState']['property']['property']['roomTypes'][i]['name']
    Quests = y['props']['pageProps']['initialState']['property']['property']['roomTypes'][i]['maxOccupantCount']
    policy = y['props']['pageProps']['initialState']['property']['property']['checkInInstructions']

    list.append(Room_name)
    list.append(Quests)
    list.append(policy)

    i += 1

################# CSV DATA ##################
hotel_id = y['props']['pageProps']['initialState']['property']['property']['id']
check_in = "2024-01-09"
check_out = "2024-01-11"
values = [["hotel id  "+hotel_id, "check in "+check_in, "check out "+check_out]]

f = open('Hotels.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerows(values)

# close the file
f.close()
