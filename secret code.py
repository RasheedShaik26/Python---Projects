st = input("Enter the words")
words = st.split(" ")            # split(" ") converts the sentence into a list of words.

coding = True           # coding = True → Encode the message.  coding = false > decode the messege
if(coding):
    nwords = []
    for word in words:        # Processes each word one by one.
     if(len(word)>3):
        r1 = "yjk"
        r2 = "mlk"
        stnew =  r1 + word[1:] + word[0] + r2
        nwords.append(stnew)
     else:
        nwords.append(word[::-1])      # ::-1] reverses the word.
    print(" ".join(nwords))         # Joins all words into a sentence.


else:
    nwords = []
    for word in words:
     if(len(word)>3):
        stnew =  word[ 3 : -3]                  # Removes first 3 and last 3 characters.
        stnew = stnew[-1] + stnew[:-1]
        nwords.append(stnew)
     else:
        nwords.append(word[::-1])        #Reverse again.
    print(" ".join(nwords))



