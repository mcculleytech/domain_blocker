# domain_blocker
A python script to edit the host file on Windows and block website domains by resolving them to the localhost address.


## But Why?

Because I need to practice my python skills, that's why! I also work part time with kids who play on computers and they constantly access game sites when they shouldn't, so I wrote this script in part to help them focus on thier task at hand.


## How's it work? 

The script works by editing the hosts file on a Windows computer. The hosts file, for those who don't know, is like the local address book for your computer to resolve website IP addresses. This script will map whatever domain (for instance www.facebook.com) you enter to the localhost's IP address (127.0.0.1).This means that your computer will think 'www.facebook.com' lives on your local machine, so unless you're Zuckerberg on their webserver, you won't be able to get to facebook.


## Neat! But what else can it do?

I'm glad you asked, I tried to add a little more functionality to the script by allowing you to 'unblock' sites, add more sites, as well as list the existing sites that are blocked. 


## Any plans to improve

I do have a couple of thoughts on improvements to explore some different modules in python. For instance a gui that I could code with tkinter or adding/removing multiple lists at one time. If I keep the CLI, I could opt for some color in the interface and make things look a little nicer. Any suggestions? Let me know.
