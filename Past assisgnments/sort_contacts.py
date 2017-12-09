

def sort_contacts(contacts):
    sorted_contacts = sorted(contacts)
    final_list = []
    contact_tuple = ()
    first_list = []
    temp = []
    for key in sorted_contacts:
        key_value = (key, contacts[key])
        first_list = list(key_value)
        name = first_list[0]
        temp.append(name)
        phone_number = first_list[1][0]
        temp.append(phone_number)
        email = key_value[1][1]
        temp.append(email)
        temp = tuple(temp)
        final_list.append(temp)
        temp = list(temp)
        temp = list()
    return final_list
        

def main():
    sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
    "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
    "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"), "Kandinsky, Wassily":
    ("1-333-555-9999", "kandinsky@painters.com")})

if __name__ == "__main__":
    main()



