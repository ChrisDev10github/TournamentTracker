
validnumber = False
slotvalid=False
cancelbool = False
tour=False

listpart = []
numberpart=0
slotpref=0
cancelslotpref=0
cancelname=''
name=''

def startup():
    global validnumber
    global numberpart
    print("Welcome to Tournaments R Us")
    while validnumber ==False:
        numberpart = int(input('Enter the number of participants: '))
        if numberpart >=0:
            validnumber =True
        else:
            print("Error try again")
    for slot in range(0,numberpart):
        listpart.append('[Empty]')               
    print("There are ",numberpart," participant slots ready for sign-ups")    


def signup():
    global slotvalid
    print('''Participant Sign Up
            =====================''')
    name = str(input('Participant Name: '))
    print(name)
    slotvalid=False
    while slotvalid==False:
        slotpref = int(input(f'Desired Starting slot #[1-{numberpart}]: '))                      #number part not assigned
        if listpart[slotpref-1] == '[Empty]':
            listpart[slotpref-1] = name
            #print(listpart)                     
            slotvalid=True
            mainmenu()
        else:
            print("Slot is FULL try another slot")
            mainmenu()

def cancel():
    global cancelslotpref
    global cancelname
    print('''Participant Cencellation
        =====================''')    
    while cancelbool == False:
        cancelslotpref = int(input('Starting slot: '))
        cancelname = str(input('Participant Name: '))
        if listpart[cancelslotpref] == cancelname:
            listpart[cancelslotpref] = None
            print("Success: ",cancelname," has been cancelled from slot # ",cancelslotpref)
            cancelbool =True
        else:
            print("Error: ", cancelname," is not in that slot")
    

def viewpart():
    global numberpart
    print('''
            View Participants
            ==================
            Strating slot: Participant''')
    for i in range(0,numberpart):
        print(i+1, ": ",listpart[i])


def savechanges():
    print("Save Changes")
    savechangeyn = str(input('Do you want to save(Y/N): '))
    if savechangeyn == 'Y':
        print("You saved")
        savechangebool = True
    
def exit():
    print("Exit")
    exitresponse = str(input('Do you want to exit(Y/N): '))
    if exitresponse == 'Y':
        #exit
        print("You exited")
    else:
        print("You didn't exit")


def mainmenu():
    print('''		
        Participant Menu
		================
		1. Sign Up
		2. Cancel Sign Up
		3. View Participants
		4. Save Changes
		5. Exit''')

    choice = int(input('What do you want to do (1-5): '))

    if choice ==1:
        signup()
    if choice ==2:
        cancel()
    if choice ==3:
        viewpart()
    if choice ==4:
        savechanges()
    if choice ==5:
        exit()


while tour==False:
    starttour = str(input('Are you starting a tournament(Y/N): '))
    if starttour == 'Y':
        startup()
        tour = True
    else:
        tour = True

mainmenu()



