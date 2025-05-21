# Program : Portfolio

# This is a dictionary that stores your personal and professional details using key-value pairs
Info = {
    "Name": "Jayraj Vinodchandra Panchal",
    "Age": 19,
    "Address": "C-1 Kunj Plaza Raj Mahal Road Vadodara",
    "Qualification": "Diploma : Computer SICE",
    "Skills": {
        "Language": ["Python", "JavaScript", "PHP"],
        "Database": ["MONGODB", "MySQL"]
    },
    "College": "B & B Institute Of Tech"
}
# defines a function named portfolio
def portfolio():
    print("----- My Portfolio -----\n")
    
    for key, value in Info.items(): # .items() is a built-in method to return both the key and its corresponding value from a dictionary.
        if type(value) == dict: #This checks if the value is another dictionary
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {', '.join(sub_value)}") #.join(sub_value) converts the list into a single string separated by commas
        else:
            print(f"{key}: {value}")

# Run the function
portfolio()
