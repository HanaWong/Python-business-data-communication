def createnew():
  eventname = input("What is the name of your event: ")
  with open("create.txt","w") as file:
    file.write(eventname + "\n")
    file.write("Name(s),Email(s)\n")
  

def register():
  # read the name of event
  with open("create.txt","r") as file:
    event = file.readlines()[0]
  print("The current event is:", event)

  name = input('Please enter your name. Enter x to quit without saving: ')
  if name == "x":
    print("You exit without saving the information.")
    return
  while True:
    email = input("Please enter your email. It must be a valid @ucr.edu email: ")
    if email[-8:] != "@ucr.edu":
      print("Please enter your email. It must be a valid @ucr.edu email.")
    else:
      break

  with open("create.txt","a") as file:
    file.write(name + "," + email + "\n")
  

def view():
  with open("create.txt","r") as file:
    lines = file.readlines()
    print("Event name: " + lines[0]) 
    for line in lines[1:]:
      data = line.split(",")
      print(data[0] + "\t\t\t"+ data[1])

  
print("Welcome To The UNO Tournament Registration System.")
choice = None

while(True):
  choice = input("What would you like to do?\n(c)Create a new event.\n(r)Register attendees for the current event.\n(v)View the registered attendees.\n(x)Exit.\n")
  if(choice == 'c'):
    createnew()
    
  
  elif(choice == 'r'):
    register()

  
  elif(choice == 'v'):
    view()
    
  
  elif(choice == 'x'):
    print('Goodbye!')
    break
  
  else:
    print("Please enter a valid choice.")