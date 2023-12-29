import json
from requests_html import HTMLSession
import csv


# this request is giving JSON as output : https://www.qantas.com/hotels/api/ui/properties/18482
# but have no authorisation

# or try diehard response.text: used to access payload data in String format

# response = requests.get("https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-01-09&checkOut=2024-01-11&children=0&infants=0&location=London%2C+England%2C+United+Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity")

# string_response = response.text

# print(string_response)

######################## 1 COMB ##########################
# here you can access HTML document and its tags and ids :

session = HTMLSession()

#url = 'https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-01-09&checkOut=2024-01-11&children=0&infants=0&location=London%2C+England%2C+United+Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity'
url = ('https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-01-10&checkOut=2024-01-11&'
       'children=0&infants=0&location=London%2C+England%2C+United+Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity')

output = session.get(url)

k = output.html.find('#__NEXT_DATA__') #returns a list
#c = output.html.render() #find by ID


# print(k)
# print(k[0].text) #access list and its data inside script tag

#print(k[0].text)
y = json.loads(k[0].text)

#print(y['props']['pageProps']['initialState']['property']['property']['roomTypes'][0]['name']) # access Deluxe Double Room JSON elements here
#print(y['props']['pageProps']['initialState']['property']['property']['checkInInstructions']) # access Deluxe Double Room JSON elements here


# create a list :

lis = [1, 2, 3, 4, 5 , 6, 7]
i = 0

list = []

while (i < len(lis)):

    # print(lis[i], end=" ")

    Room_name = y['props']['pageProps']['initialState']['property']['property']['roomTypes'][i]['name']
    Quests = y['props']['pageProps']['initialState']['property']['property']['roomTypes'][i]['maxOccupantCount']
   # policy = y['props']['pageProps']['initialState']['property']['property']['checkInInstructions']

    list.append(Room_name)
    list.append(Quests)
   # list.append(policy)

    i += 1


# test
print(list)

################# CSV DATA ##################
hotel_id = "18482"
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
################# CSV DATA ##################


# Rate_name
# Number of Guests
# Cancellation Policy
# Price Boolean value if the room is a Top Deal
# Currency



#print(rooms['room_0']['name'])


js = json.dumps(k[0].text) #CONVERT LIST to JSON



##################################################


#url = 'https://www.qantas.com/hotels/api/ui/properties/18482'

#r = requests.get(url, headers=headers)


#output_str = r.text

#print(output_str.find())
