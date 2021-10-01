import shutil
import os
import re

# path to hosts file on windows
file_path = r'C:\Windows\System32\drivers\etc\hosts'

# Uncomment the following two lines if you would like a copy of the hosts file for whatever reason.
# copy_file_path = r'C:\Windows\System32\drivers\etc\hosts'
# shutil.copyfile(file_path,copy_file_path)


# open file in append + read mode
file_object = open(file_path,'a+')
block_domains = []



def remove_existing_site():
    print( '\n' + ('-' * 30))
    print('\n')
    line_count = 1
    existing_blocked_sites = []
    file_read = open(file_path)
    for line in file_read:
        domain_lines = re.findall('^127.0.0.1',line)
        line_count += 1
        if domain_lines:
            domain_name = line[13:].strip()
            existing_blocked_sites.append(domain_name)
            print(str(line_count) + '\t' +  domain_name)
    delete_line_number = int(input('\nEnter the number of the line you would like to delete: '))
    with open(file_path, 'r') as fr:
        lines = fr.readlines()
        ptr = 1
    with open(file_path, 'w') as fw:
        for line in lines:
            if ptr != delete_line_number:
                fw.write(line)
            ptr += 1
    print("Deleted!")


def remove_listed_site():
    print( '\n' + ('-' * 30))
    print('\n')
    for i, domain in enumerate(block_domains,0):
        print(i, '. ' + domain, sep='',end='\n')
    choice = int(input('\nEnter the number of the item you would like to remove from the list of sites to be blocked: '))
    del block_domains[choice]
    print('Here is your new list of sites to be blocked:\n')
    for domain in block_domains:
        print(domain)


def add_site():
    print( '\n' + ('-' * 30))
    site = input('\n Enter the address of the site you would like to block (ie www.facebook.com or facebook.com): ')
    block_domains.append(site)


def remove_site():
    print( '\n' + ('-' * 30))
    remove_choice = int(input("""\n
    Would you like to...\n
    1) Remove a website that is currently blocked.
    2) Remove a website that you are about to block.

    Enter 1 or 2: """))
    if remove_choice == 1:
        remove_existing_site()
    elif remove_choice == 2:
        remove_listed_site()

def print_sites_to_be_blocked():
    print( '\n' + ('-' * 30))
    print('The following urls will be blocked on this computer:\n')
    for domain in block_domains:
        print(domain)

def print_blocked_sites():
    print( '\n' + ('-' * 30))
    print('The following urls are blocked on this computer:')
    print('\n')
    existing_blocked_sites = []
    file_read = open(file_path)
    for line in file_read:
        domain_lines = re.findall('^127.0.0.1',line)
        if domain_lines:
            domain_name = line[13:].strip()
            existing_blocked_sites.append(domain_name)
            print(domain_name)


build_list = True
while build_list == True:
    print( '\n' + ('-' * 30))
    menu_selection = str(input(

    """\t\n What would you like to do? \n
    1. Add sites to block.
    2. Remove blocked sites.
    3. Print sites to be blocked.
    4. Print already blocked sites
    5. Quit

    Enter your Selection: """))

    if menu_selection == '1':
        add_site()
    elif menu_selection == '2':
        remove_site()
    elif menu_selection == '3':
        print_sites_to_be_blocked()
    elif menu_selection == '4':
        print_blocked_sites()
    elif menu_selection == '5':
        build_list = False
    else:
        print('oops! Choose a valid option please.')
        continue

print( '\n' + ('-' * 30))
for domain in block_domains:
    file_object.write('\n' + '127.0.0.1 \t \t' + domain)
    print(domain + ' is now blocked!')

print('\nGoodbye!')
file_object.close()
