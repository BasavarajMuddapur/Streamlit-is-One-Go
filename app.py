from streamlit import *

title("Title->GeeksForGeeks")                                                   #title
header("Header->GeeksForGeeks")                                                 #Header
subheader("Subheader->GeeksForGeeks")                                           #subheader
text("Text->GeeksForGeeks")                                                     #Text


markdown("# Hi")                                                                #markdown
markdown("## Hi")
markdown("### Hi")
markdown("#### Hi")
markdown("##### Hi")


success("Success!")                                                             #success
info("Information!")                                                            #Information
warning("Warning!")                                                             # WARNING
error("error!")                                                                 #error
exception(ZeroDivisionError("Division not possible with 0"))                    #exception

help(ZeroDivisionError)                                                         #help


write("range (1,10)")                                                           #write
write(range (1,10))
write("1+2+3")
write(1+2+3)
write(1*2*3)


code("x=10\n"                                                                   #code
      "for i in range(x):\n"
      "    print(i)")


checkbox("Male")                                                                #checkbox
checkbox("Female")
if(checkbox("Adult")):                                                          #checkbox with validation
    write("you're an adult ")

radio("Select : ",("Check","Uncheck"))                                          #radio
#radio("Select : ",("Male","Female","Other"))

radioButton=radio("Select : ",("Male","Female","Other"))
if(radioButton=="Male"):
    write("You're a Male")
elif(radioButton=="Female"):
    write("you're a Female")
elif(radioButton=="Other"):
    write("you're an Other Gender")


subheader("Select Box")                                                         #selectBox
selectBox=selectbox("Data Science : ", [  "Data Analysis","Web Scraping","Machine Learning",
                                          "Deep Learning","Natural Language Processing",
                                          "Computer Vision","Image Processing"])
write("You've selected" , selectBox)


subheader("MultiSelect Box")                                                    #MultiselectBox
multiselectBox=multiselect("Data Science : ", [  "Data Analysis","Web Scraping","Machine Learning",
                                                 "Deep Learning","Natural Language Processing",
                                                 "Computer Vision","Image Processing"])
write("You've selected : ", len(multiselectBox) ,"Courses")
write(multiselectBox)


subheader("Button")                                                             #button
#button("click me")
if(button("click me")):
    write("Thanks for Clicking me")


subheader("Slider")                                                             #Slider
vol=slider("Select the volumn",1,100,step=1)
write("Volumn is : ",vol)


#subheader("Text Input")                                                         #Text-Input
#username=text_input("Enter your name : ")
#if (username):
#    write("Hi", username)

subheader("Text Input")                                                         #Text-Input
username=text_input("Enter your name     : ")
password=text_input("Enter your password : " , type="password")


subheader("Text Area")                                                          #Text-Area
textArea=text_area("write something interesting about yourself in 500 words")
write(textArea)

subheader("Input Number")
number_input("Select your age : ",18,110)                                       #Input-Number

subheader("Input Date")
date_input("Date")                                                              #Input-Date

subheader("Input Time")
time_input("Time")                                                              #Input-time
