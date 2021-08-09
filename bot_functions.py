from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
import random
from random import randint


# The Ui ofthe bot
window = Tk()
icon = PhotoImage(file="logo6.png")
window.iconphoto(True, icon)
window.title("Instagram bot By XCodee")
window.geometry("1300x700")

def your_order():
    
    #Adding Users to the listbox
    def add_users():
        list_box.insert(list_box.size(),entryBox.get())
        list_box.config(height=list_box.size())

    # Sending Message to the Users        
    def send_your_message():
        print("sending Messages")
        driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(username_box.get())
        time.sleep(3)
        driver.find_element_by_name("password").send_keys(password_box.get())
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        for user in list_box.get(first=0, last=10):
            
            # getting to the users' profile
            driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/button").click()
            time.sleep(5)

            #sending text Message
            driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hello")
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()



    # followinf Users
    def follow_users():
        driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(username_box.get())
        time.sleep(3)
        driver.find_element_by_name("password").send_keys(password_box.get())
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        for user in list_box.get(first=0, last=10):
            
            # getting to the users' profile
            driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(10)
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button").click()
            time.sleep(5)

    #unfollowing users         
    def unfollow_users():
        driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(username_box.get())
        time.sleep(3)
        driver.find_element_by_name("password").send_keys(password_box.get())
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        for user in list_box.get(first=0, last=10):
            
            # getting to the users' profile
            driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")

            
    #commenting on Photos
    def comment_photos():
        driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(username_box.get())
        time.sleep(3)
        driver.find_element_by_name("password").send_keys(password_box.get())
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        for user in list_box.get(first=0, last=10):
            
            # getting to the users' profile
            driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(5)

    #Liking Photos
    def like_photos():
        driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element_by_name("username").send_keys(username_box.get())
        time.sleep(3)
        driver.find_element_by_name("password").send_keys(password_box.get())
        time.sleep(random.randint(2,3))
        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        for user in list_box.get(first=0, last=10):
            links = []
            # getting to the users' profile
            driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(5)
            links = driver.find_elements_by_tag_name("a")
            def condition():
                return ".com/p" in link.get_attribute("href")
            valid_links = list(filter(condition, links))

            for i in range(5):
                link = valid_links[i].get_attribute('href')
                if link not in links:
                    links.append(link)


            for link in links:
                driver.get(link)
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button').click()

                driver.find_element_by_class_name('RxpZH').click()
                time.sleep(1)

                driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys("comment")
                time.sleep(2)
                driver.find_element_by_xpath("//button[@type='submit']").click()
                time.sleep(2)

            
    #following Hashtags
    def follow_hashtags():
        for user in list_box.get(first=0, last=10):
            driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
            driver.get("https://www.instagram.com/")
            time.sleep(2)
            driver.find_element_by_name("username").send_keys(username_box.get())
            time.sleep(3)
            driver.find_element_by_name("password").send_keys(password_box.get())
            time.sleep(random.randint(2,3))
            driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
            time.sleep(5)
            # getting to the users' profile
            driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(5)

    
    #Printing the users from the listbox
    def print_users():
        for user in list_box.get(first=0, last=10):
            print(user)
    
    # Message Users(DM)
    if x.get() == 0:
        messageFrame = Frame(window, bg="blue", bd=10, relief=SUNKEN)
        entryBox = Entry(messageFrame)
        list_box = Listbox(messageFrame)
        list_box.config(height=list_box.size())
        addButton = Button(messageFrame, text="Add Users", command=add_users)
        msg_label = Label(messageFrame, text="Write Your message Below", font=("Baloo", 10))
        msg_box = Entry(messageFrame)
        msg_send_button = Button(messageFrame, text="Send Messages", font=("Baloo", 10), command=send_your_message)
        add_user_label = Label(messageFrame, text="Insert Usernames _Message", font=("Baloo", 10))
        #usersButton = Button(messageFrame, text="Print users", command=print_users)
        inserted_label_msg = Label(messageFrame, text="Inserted Usernames")


        inserted_label_msg.pack()
        list_box.pack()
        add_user_label.pack()
        entryBox.pack()
        addButton.pack()
        msg_label.pack()
        msg_box.pack()
        msg_send_button.pack()
        #usersButton.pack()
        messageFrame.place(x=100, y=110)
        
        
    #Follow Users
    if x.get() == 1:
        followFrame = Frame(window, bg="red", bd=10, relief=SUNKEN)
        entryBox = Entry(followFrame)
        list_box = Listbox(followFrame)
        list_box.config(height=list_box.size())
        addButton = Button(followFrame, text="Add Users", command=add_users)
        follow_button= Button(followFrame, text="Follow usera", command=follow_users)
        follow_label = Label(followFrame, text="Insert Usernames __Follow", font=("Baloo", 10))
        box_label = Label(followFrame, text="Inserted Usernames __Follow", font=("Baloo", 10))
        
        box_label.pack()
        list_box.pack()
        follow_label.pack()
        entryBox.pack()
        addButton.pack()
        follow_button.pack()
        followFrame.place(x=307, y=110)
    
    #Unfollow Users
    if x.get() == 2:
        unfollowFrame= Frame(window, bg="green", bd=10, relief=SUNKEN)
        entryBox = Entry(unfollowFrame)
        list_box = Listbox(unfollowFrame)
        list_box.config(height=list_box.size())
        addButton = Button(unfollowFrame, text="Add Users", command=add_users)
        follow_label = Label(unfollowFrame, text="Insert Usernames _unFollow", font=("Baloo", 10))
        box_label = Label(unfollowFrame, text="Inserted Usernames _unFollow", font=("Baloo", 10))
        unfollow_button = Button(unfollowFrame, text="Unfollow Users", command=unfollow_users)
        
        box_label.pack()
        list_box.pack()
        follow_label.pack()
        entryBox.pack()
        addButton.pack()
        unfollow_button.pack()
        unfollowFrame.place(x=500, y=110)
        
        
    #follow Hashtags
    if x.get() == 3:
        hashFrame = Frame(window, bg="yellow", bd=10, relief=SUNKEN)
        entryBox = Entry(hashFrame)
        list_box = Listbox(hashFrame)
        list_box.config(height=list_box.size())
        addButton = Button(hashFrame, text="Add Users", command=add_users)
        follow_htags = Button(hashFrame, text="Follow HashTags", command=follow_hashtags)
        follow_label = Label(hashFrame, text="Insert Hashtags _Follow", font=("Baloo", 10))
        box_label = Label(hashFrame, text="Inserted Hashtags _Follow", font=("Baloo", 10))
        
        box_label.pack()
        list_box.pack()
        follow_label.pack()
        entryBox.pack()
        addButton.pack()
        follow_htags.pack()
        hashFrame.place(x=700, y=110)
        
    #Comment on photos
    if x.get() == 4:
        commentFrame = Frame(window, bg="pink", bd=10, relief=SUNKEN)
        entryBox = Entry(commentFrame)
        list_box = Listbox(commentFrame)
        list_box.config(height=list_box.size())
        addButton = Button(commentFrame, text="Add Users", command=add_users)
        comment_button = Button(commentFrame, text="Comment on photos", command=comment_photos)
        follow_label = Label(commentFrame, text="Insert  Usernames _Comment", font=("Baloo", 10))
        box_label = Label(commentFrame, text="Inserted Usernames _Comment", font=("Baloo", 10))
        
        box_label.pack()
        list_box.pack()
        follow_label.pack()
        entryBox.pack()
        addButton.pack()
        comment_button.pack()
        commentFrame.place(x=890, y=110)
    
    #like Photos
    if x.get() == 5:
        likeFrame = Frame(window, bg="orange", bd=10, relief=SUNKEN)
        entryBox = Entry(likeFrame)
        list_box = Listbox(likeFrame)
        list_box.config(height=list_box.size())
        addButton = Button(likeFrame, text="Add Users", command=add_users)
        like_button = Button(likeFrame, text="Like Photos", command=like_photos)
        follow_label = Label(likeFrame, text="Insert Usernames _Like", font=("Baloo", 10))
        box_label = Label(likeFrame, text="Inserted Usernames _Like", font=("Baloo", 10))
        
        box_label.pack()
        list_box.pack()
        follow_label.pack()
        entryBox.pack()
        addButton.pack()
        like_button.pack()
        likeFrame.place(x=1100, y=110)
        
    
        
        
        
        

x = IntVar()

username_box = Entry(window)
password_box = Entry(window, show="*")
username_label = Label(window, text="Enter your Username Here 👇", font=("Comic Sans MS", 10)) 
password_label = Label(window, text="Enter your Password Herre👇", font=("Comic Sans MS", 10))
username_label.pack()
username_box.pack(fill="x", padx=100)
password_label.pack()
password_box.pack(fill="x", padx=100)

ations_to_perform = ["Msg_dm", "Follow", "Unfollow", "Hashtags", "Comment", "Like"]

choose_option = Label(window, text="Choose Option Bellow", font=("Comic Sans MS", 10))
choose_option.pack()
for index in range(len(ations_to_perform)):
    radio_but = Radiobutton(window,
                            text=ations_to_perform[index], #this adds text toradio button
                            variable=x,
                            value=index,
                            font=("Comic Sans MS", 10),
                            indicatoron=0,
                            command=your_order
                           )
    radio_but.pack(anchor=W)



window.mainloop()

