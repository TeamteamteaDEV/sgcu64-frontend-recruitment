# Assumption 1 : User always type in english.
# Assumption 2 : Every location in Chula does not have resemble names
#                for example "Sara" and "Sarab". If this program division this case, resault is the same place.
# Assumption 3 : User can type either short/full name for example Samyan or Samyan Mitr.
# Assumption 4 : User can type wrong but still enough to convey meaning.
# Assumption 5 : User never type number of available command and number wrong.

# Additional Idea : Add a function that user can input location themself and also add function that able to detect misspelling.
#                   So when we have function that user can type a location, that is mean when the location list increase,
#                   there is a probability that user miss the location list and type the exist location themself.
#                   This program have a function that can detect
#                   - type wrong case
#                   - short/full written case
#                   For example -> "Mahamongkut" == "Mahamankut"
#                               -> "Samyan Mitr" == "Mite" == "Samyan" == "Sammyanm"
#
                    
# Incompleteness of the program :
# 1. Can not detect merge word -> "Saraprakaew" != "Sara Prakaew"
# 2. Can not check the correct spelling
# 3. Can not detect repeat word such as "building" -> "Eng Building" == "Mahamankut Building"
# 4. Can not check sub-location -> "100 year building" != "Faculty of Engineering"
# 5. Neglect the case that user typing wrong that make words longer/shorter than 2 alphabet



def count_alphabet(word) :
    count = {}
    for c in word.lower() :
        if c in count :
            count[c] += 1
        else :
            count[c] = 1
    return count


def correct_check(sublo,pla):
    char_sublo = count_alphabet(sublo)
    for subpla in pla.split() :
        if abs(len(sublo)-len(subpla)) > 2 :    # Typing wrong from user can not make words longer/shorter than 2 alphabet
                continue                        # When it is longer than 2, that is mean two of them is not the same word
        char_subpla = count_alphabet(subpla)
        fraction = 0
        denominator = 0
        for k in char_subpla.keys() :
            if k in char_sublo :
                if char_subpla[k] > char_sublo[k] :
                    fraction += char_sublo[k]
                    denominator += char_subpla[k]
                else :
                    fraction += char_subpla[k]
                    denominator += char_subpla[k]
            else :
                denominator += char_subpla[k]
        if fraction/denominator > 2/3 :
            return True
    return  False


def exist_place(lo) :
    for sublo in lo :
        for pla in places :
            if correct_check(sublo,pla) :
                return (pla, True)
    return (" ".join(lo), False)
            


places = ["Mahamakut Building","Sara Phra Kaew","CU Sport Complex","Sanam Juub" \
         ,"Samyan Mitr Town"]
phone = set()
track = {"Mahamakut Building":set(),
         "Sara Phra Kaew":set(),
         "CU Sport Complex":set(),
         "Sanam Juub":set(),
         "Samyan Mitr Town":set()}

while True :
    print("Welcome to Chula Chana!!!\n\
Available commands:\n\
        1. Check in user\n\
        2. Check out user\n\
        3. Print people count")
    command = int(input("Please input any number: ").strip())
    print("----------------------------------------\n")


    if command==1 :
        print("Check In")
        phn = input("Enter phone number: ").strip()
        for i in range(len(places)) :
            print("        "+str(i+1)+". "+places[i])
        print("        "+str(len(places)+1)+". "+"Enter another location")
        pl = int(input("Please input any number: ").strip())

        #--------------------------------------------------------# Detecting existing location
        if pl == len(places)+1 :
            (newlo,exist)= exist_place(input("Enter Location : ").strip().split())
            if exist :
                for i in range(len(places)) :
                    if newlo == places[i] :
                        pl = i+1
            else :
                places.append(newlo)
                track[newlo] = set()
        #--------------------------------------------------------#

        if phn not in phone :
            track[places[pl-1]].add(phn)
            phone.add(phn)
            print("Check in "+places[pl-1])
        else :
            for k,v in track.items() :
                if (phn in v) and (places[pl-1] == k):
                    print("Already check in.")
                    break
                if (phn in v) and (places[pl-1] != k):
                    print("Check out "+k+" and check in "+places[pl-1]+".")
                    track[k].remove(phn)
                    track[places[pl-1]].add(phn)
                    break


    if command==2 :
        phn = input("Enter phone number: ").strip()
        if phn not in phone :
            print("Haven't checked in yet. Can not check out")
        else :
            phone.remove(phn)
            for k,v in track.items() :
                if phn in v :
                    track[k].remove(phn)
                    print("Check out "+k)
                    break
            

    if command==3 :
        print("Current Population")
        for i in range(len(places)) :
            print("        "+str(i+1)+". "+places[i]+": "+str(len(track[places[i]])))
        

   
    print("----------------------------------------\n")
