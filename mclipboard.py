TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}

import sys,pyperclip

if len(sys.argv) <2: #this is the message for the command prompt user
    print('Use: python mclipboard.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} is copied to the clipboard')
else:
    print(f'There is no text for {keyphrase}')



# "sys.argv" variable will store the command line arguments
# 'sys.argv' works like a list in which first item is always the name of the file in this case mclipboard.py