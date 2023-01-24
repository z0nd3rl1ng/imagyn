"""
-----------------------------------------------------------------------
# imagyn - AI image generator for terminal
-----------------------------------------------------------------------
"""
__author__ = "z0nd3rl1ng"
__version__ = "1.0.0"

import random, os

try:
    import openai
except ModuleNotFoundError:
    print("[*] install missing module: openai")
    os.system("pip3 install openai")
    import openai
    
openai.api_key = "[PUT YOUR API KEY HERE]"

"""----------------------------------------------------------------"""
    
def genImage():
    while True:
        interact = input("\n[IMAGYN]╼> ")
        if interact == "exit":
            exit()
        else:
            response = openai.Image.create(
                prompt=interact,
                n=1,
                size="1024x1024"
            )
            print("\n"+response['data'][0]['url'])

def banner():
	padding = '  '
	I = [[' ',' ','┬'],
         [' ',' ','│'],
         [' ',' ','┴']]
	M = [[' ','┌','┐','┌','┐'],
	     [' ','│','└','┘','│'],
	     [' ','┴',' ',' ','┴']]
	A = [[' ','┌','─','┐'],
         [' ','├','─','┤'],
         [' ','┴',' ','┴']]
	G = [[' ','┌','─','┐'],
	     [' ','│',' ','┬'],
	     [' ','└','─','┘']]
	Y = [[' ','┬',' ','┬'],
	     [' ','└','┬','┘'],
	     [' ',' ','┴',' ']]
	N = [[' ','┌','┐','┬'],
         [' ','│','│','│'],
         [' ','┴','└','┘']]
	
	banner = [I,M,A,G,Y,N]
	final = []
	print('\r')
	init_color = 38
	txt_color = init_color
	cl = 0

	for charset in range(0, 3):
		for pos in range(0, len(banner)):
			for i in range(0, len(banner[pos][charset])):
				clr = f'\033[38;5;{txt_color}m'
				char = f'{clr}{banner[pos][charset][i]}'
				final.append(char)
				cl += 1
				txt_color = txt_color + 36 if cl <= 3 else txt_color

			cl = 0

			txt_color = init_color
		init_color += 31

		if charset < 2: final.append('\n   ')

	print(f"   {''.join(final)}")
	print(f'{padding}       by z0nd3rl1ng\n')

if __name__ == "__main__":
    banner()
    genImage()
