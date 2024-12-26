def print_until_stop():
    dic ={}
    while True:
        word = input("Please enter a word:")
        if word == "stop":
            break
        if word == "":
            print("No word entered, try again.")
            continue   
        if word.lower() in dic:
            dic[word.lower()] += 1
        else:   
            dic[word.lower()] = 1
        
    for key in dic:
        print(key , dic[key])
        

print_until_stop()