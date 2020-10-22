# import requests

# response = requests.get('https://api.ipify.org')
# print(response.text) # 76.105.187.182
# print(response.url)
# print(response.text) # 76.105.187.182
# print(response.status_code) # 200
# print(response.encoding) # ISO-8859-1
# print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}

# import requests
# response = requests.get(f"https://jsonplaceholder.typicode.com/todos/1")
# data = response.json()
# print(data)

# import requests

# API_KEY = "8af2aa7fa978da0c3dc608a85406875c"
# API_URL = "http://api.openweathermap.org/data/2.5/weather"

# def getApi(loc):
#     ret = requests.get(f"{API_URL}?q={loc}&appid={API_KEY}")
#     return ret.json()

# def main():
#     try:
#         loc = input("what city ")
#         ret = getApi(loc)
#         weather = ret["weather"][0]["description"]
#         temp = format(float(ret["main"]["temp"]) - 273.1, '.2f')
#         print(f"Its {temp} degrees in {loc} and {weather}")
#     except Exception:
#         print("error")
    

# main()

f = open("book.txt", 'r')
print(f.read())
f.close()

# With open ('book.txt',"r") as document:
# Document_Content = document.read()
# print (document_content)

With open ('book.txt, 'r'') as document:

    size_to_read = 150
    document_content = document.read(size_to_read)
    while len(document_content) > 0:
        print(document_content, end = '*')
        document_content =dpcument.read(size_to_read)
############## Example 

with open("book.txt", "r") as document_read:
    with open("copy_book.txt", 'w') as document_write:
        for line in document_read:
            document_write.write(line)
