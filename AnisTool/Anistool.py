from Anis.plugins.update import search_for_updates
from Anis.plugins.commun import *

def main():
    clear()
    setTitle(f"Anis Tool Menu Menu v{THIS_VERSION}")
    AnisHome()
    print(f"""      {y}[{b}+{y}]{w} Main Options:
\n          {y}[{w}01{y}]{w} TokenInformation :
\n          {y}[{w}02{y}]{w} Tokens Checker : 
\n          {y}[{w}03{y}]{w} Wehbook Deleter :
\n          {y}[{w}04{y}]{w} WehbookSpammer :
\t\t\t\t\t\t\t\t\t\t\t\t\t {y}[{b}>{y}]{w} Thanks for using Anis Tool""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """)

    if choice == '1' or choice == '01':
        transition()
        exec(open('Anis/10_tokeninfo/TokenInformation.py').read())
    elif choice == '2' or choice == '02':
        transition()
        exec(open('Anis/10_tokenchecker/TokenChecker.py').read())
    elif choice == '3' or choice == '03':
        transition()
        exec(open('Anis/10_wehbookDeleter/Webhook.DLT.py').read())
    elif choice == '4' or choice == '04':
        transition()
        exec(open('Anis/10_wehbookSpammer/WebhookSPM.py').read())
        clear()
        main()