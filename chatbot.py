print ("--------Welcome to Chatbot--------")


while True:
    user = input ("You : ").lower()

    if user == "hello" :
        print ("Chatbot : Hi ! ")


    elif user == "how are you?":
        print ("Bot : im fine, thanks ")

    elif user == "bye" :
        print ("Bot : bye ")
        break 


    else : 
        print ("sorry i dont understand")
    