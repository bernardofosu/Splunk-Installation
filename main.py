import re
import requests 

# pattern = re.compile(r"^(\+\d{2,4})-(\d{3})-(\d{3})-(\d{3})(\d{1})?$")
# # pattern = re.compile(r"^\+\d{1,3}-\d{4}-\d{3}-\d{3}$")

# # pattern = re.compile(r"^.{8,15}$")


# # user = input("Enter Your Password: ")
# user = input("Enter Your Phone Number: ")

# # print(pattern.search("H"))
# # print(pattern.search("Hello"))
# print(pattern.search(user))


response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)