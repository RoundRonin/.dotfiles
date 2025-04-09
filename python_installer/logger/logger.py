from colorama import Fore, Style

def info(msg):
    print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} {msg}")

def warning(msg):
    print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {msg}")

def error(msg):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {msg}")

def debug(msg):
    print(f"{Fore.CYAN}[DEBUG]{Style.RESET_ALL} {msg}")