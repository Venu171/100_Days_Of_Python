
def band_name_generator():
    print("Welcome to Band Name Generator.")
    city_name = input("What's the name of city you grew up in?\n")
    pet_name = input("What's your pet name?\n")
    print(f"{city_name} {pet_name}")


# Here we are using __name__=="__main__" for the file to run by passing the python <filename>
if __name__ == "__main__":
    band_name_generator()
else:
    print("Module is imported and it's running successfully.")
