import pyshorteners as ps
url = input("Enter your url: ")
u=ps.Shortener().tinyurl.short(url)
print("your url is: ",u)