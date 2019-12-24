import subprocess
import sys

def install():
		try:
			subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Chatterbot'])

		except subprocess.CalledProcessError as e:
			print('ERROR: Chatterbot Install Unsuccseful')

		try:
			subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Chatterbot-corpus'])
		except subprocess.CalledProcessError as e:
			print('ERROR: Chatterbot-corpus Install Unsuccseful')

		print('Modules have succsefuly installed') 


install()