#Dictionaries with loops
website = {
    "name": None,
    "URL": None,
    "description": None,
    "StarRating": None
}

input_list = input("Input the website name, URL, your description and star rating: ").split()

website['name'] = input_list[0]
website['URL'] = input_list[1]
website['description'] = input_list[2]
website['StarRating'] = input_list[3]

print("\nWebsite Information:\n")
for key, value in website.items():
    print(f"{key}: {value}")

