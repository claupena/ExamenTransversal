import urllib.parse
import requests


## Variables 
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "V53rpj6hKXMW9jByQyoPkdDcbqH6C9Mc"


while True:
  ##   ##
  orig = input("Starting Location: ")  ## Santiago
  if orig == "quit" or orig == "q":
    break
  dest = input("Destination: ")   ## Ovalle
  if dest == "quit" or dest == "q":
    break
  ##   ##
  url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
  print("URL: " + (url))
  json_data = requests.get(url).json()
  json_status = json_data["info"]["statuscode"]
  if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("=============================================")
    print("Direcciones: " + (orig) + " to " + (dest))
    print("Duracion Viaje: " + (json_data["route"]["formattedTime"]))
    print("Millas: " + str(json_data["route"]["distance"]))
    print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    
    #print("Gasolina Usada (Gal): " + str(json_data["route"]["fuelUsed"]))  ## No funciona, no existe en el API GET
    print("=============================================")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
      print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
      
    print("=======================================\n")
  elif json_status == 402:
    print("**********************************************")
    print("Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations.")
    print("**********************************************\n")
  elif json_status == 611:
    print("**********************************************")
    print("Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations.")
    print("**********************************************\n")
  else:
    print("************************************************************************")
    print("For Staus Code: " + str(json_status) + "; Refer to:")
    print("https://developer.mapquest.com/documentation/directions-api/status-codes")
    print("************************************************************************\n")