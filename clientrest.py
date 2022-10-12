
import requests
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
result=requests.get(url)
result.status_code #should return 200 if connected to API
result.text
data = result.json() #save json data as variable

  #print(t)
def print_menu():       ## menu
    print(30 * "-" , "Check Bitcoin Price" , 30 * "-")
    print("1. USD")
    print("2. GBP")
    print("3. EUR")
    print("4. Exit")
  
loop=True      
  
while loop:          
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-4]: ") 
    if choice == 0:
      break
    elif choice=='1':
        print('Updated: '+data['time']["updated"])     
        print('The price of Bitcoin in USD is '+data['bpi']["USD"]['rate']) #get string from within the bpi object
        print('Press 0 to go back to the menu') 
        print('Press 4 to quit')
        choice = input("Enter your choice [0 or 4]: ")
        if choice=='4':
          print('Goodbye')
          loop=False
    elif choice=='2':
        print('Updated: '+data['time']["updated"])
        print('The price of Bitcoin in GBP is '+data['bpi']["GBP"]['rate']) 
        print('Press 0 to go back to the menu') 
        print('Press 4 to quit')
        choice = input("Enter your choice [0 or 4]: ")
        if choice=='4':
          print('Goodbye')
          loop=False   
    elif choice=='3':
        print('Updated: '+data['time']["updated"])
        print('The price of Bitcoin in EUR is '+data['bpi']["EUR"]['rate'])
        print('Press 0 to go back to the menu') 
        print('Press 4 to quit')
        choice = input("Enter your choice [0 or 4]: ")
        if choice=='4':
          print('Goodbye')
          loop=False        
    elif choice=='4':
        print("Goodbye")
        loop=False        
    else:
        # check for invalid input
        print("Wrong option selection. Try again")
