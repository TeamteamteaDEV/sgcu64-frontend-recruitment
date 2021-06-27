# Addtional Idea: Make program can countdown 


def time_checking(time):
    if (int(time[1]) not in range(0,60)) or (int(time[2]) not in range(0,60)) :
        print("                              \n\
         •          •         \n\
 __  __  •  __  __  •  __  __ ")
        return False
    return True

def time_to_sec(time) :
    return int(time[0:2])*60*60 + int(time[2:4])*60 + int(time[4:6])

def sec_to_time(sec) :
    time = ""
    hr = sec//3600
    mn = (sec%3600)//60
    sec = sec%60
    if len(str(hr)) == 1 : time += "0" + str(hr)
    else : time += str(hr)
    if len(str(mn)) == 1 : time += "0" + str(mn)
    else : time += str(mn)    
    if len(str(sec)) == 1 : time += "0" + str(sec)
    else : time += str(sec)
    return time


#rounds    1      2      3
num = [[" __ ","|  |","|__|"],    #0
       ["    ","   |","   |"],    #1
       [" __ "," __|","|__ "],    #2
       [" __ "," __|"," __|"],    #3
       ["    ","|__|","   |"],    #4
       [" __ ","|__ "," __|"],    #5
       [" __ ","|__ ","|__|"],    #6
       [" __ ","   |","   |"],    #7
       [" __ ","|__|","|__|"],    #8
       [" __ ","|__|"," __|"]]    #9

InputTime = input("Input: ").strip().split(":")   
if time_checking(InputTime) :
    Time = "".join(InputTime)               

    import time
    Sec = time_to_sec(Time)
    ShowTime = ""
    while Sec > -1 :
        for rounds in range(3):
            for i in range(6):
                ShowTime += num[int(Time[i])][rounds]
                if i in [1,3] and rounds != 0 :
                    ShowTime += " • "
                elif i in [1,3] and rounds == 0 :
                    ShowTime += "   "
            print(ShowTime)
            ShowTime = ""

        time.sleep(1)
        Sec -= 1
        Time = sec_to_time(Sec)





            
