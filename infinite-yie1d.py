#!/usr/bin/env python3
"""
Interactive CLI Tool Template
A flexible command-line interface with Colorama coloring support
"""

from colorama import Fore, Back, Style, init
import sys
import shlex
import time
import os
import random

# Initialize colorama for cross-platform color support
init(autoreset=True)

print(f"\n\rinfinite yie1d will take a moment to initialize..\n\r")
time.sleep(2.7)

def generate_random_ip() -> str:
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

class CLITool:
    def __init__(self):
        self.running = True
        self.prompt_symbol = f"""
{Fore.BLUE}┌──── ({Style.RESET_ALL}{Fore.RED}iy@user{Style.RESET_ALL}{Fore.BLUE}){Style.RESET_ALL}{Fore.BLUE} [{Style.RESET_ALL}{Fore.WHITE}/{Style.RESET_ALL}{Fore.BLUE}]{Style.RESET_ALL}
{Fore.BLUE}└─ {Style.RESET_ALL}{Fore.RED}#{Style.RESET_ALL}"""
        self.prompt_color = Fore.RED
        self.commands = {
            'help': self.cmd_help,
            'hello': self.cmd_hello,
            'echo': self.cmd_echo,
            'clear': self.cmd_clear,
            'status': self.cmd_status,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
            'dnspoof': self.cmd_dnspoof,
            'pwcrack': self.cmd_bruteforce,
        }
        self.command_descriptions = {
            'help': 'Display this help message',
            'hello': 'Print a greeting message',
            'echo': 'Echo back the provided text',
            'clear': 'Clear the screen',
            'status': 'Show system status',
            'exit': 'Exit the application',
            'quit': 'Exit the application',
            'dnspoof': 'Spoof your DNS',
            'pwcrack': 'Brute force password attack'
        }
        
    def print_header(self):
        """Print application header"""
        print(f"{Fore.RED}{'-'*100}{Style.RESET_ALL}\n")
        print(f"{Fore.RED}{Style.BRIGHT}infinite yie1d{Style.RESET_ALL} - {Fore.CYAN}Powerful Password Cracker{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Type 'help' for available commands{Style.RESET_ALL}\n")
    
    def print_prompt(self):
        """Print the command prompt"""
        print(f"{self.prompt_color}{self.prompt_symbol} {Style.RESET_ALL}", end='')
    
    def print_success(self, message):
        """Print success message"""
        print(f"{Fore.GREEN}✓ {message}{Style.RESET_ALL}")
    
    def print_error(self, message):
        """Print error message"""
        print(f"{Fore.RED}✗ Error: {message}{Style.RESET_ALL}")
    
    def print_info(self, message):
        """Print info message"""
        print(f"{Fore.CYAN}ℹ {message}{Style.RESET_ALL}")
    
    def print_warning(self, message):
        """Print warning message"""
        print(f"{Fore.YELLOW}⚠ {message}{Style.RESET_ALL}")
    
    # ==================== COMMAND HANDLERS ====================
    # Add your custom commands below
    
    def cmd_help(self, args):
        """Display help information"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Available Commands:{Style.RESET_ALL}\n")
        for cmd, desc in sorted(self.command_descriptions.items()):
            print(f"  {Fore.YELLOW}{cmd:<15}{Style.RESET_ALL} {desc}")
        print()
    
    def cmd_hello(self, args):
        """Print a greeting"""
        name = ' '.join(args) if args else 'World'
        print(f"{Fore.MAGENTA}Hello, {Style.BRIGHT}{name}{Style.RESET_ALL}{Fore.MAGENTA}!{Style.RESET_ALL}")
    
    def cmd_echo(self, args):
        """Echo back the arguments"""
        if not args:
            self.print_warning("No text to echo")
            return
        print(f"{Fore.CYAN}{' '.join(args)}{Style.RESET_ALL}")
    
    def cmd_clear(self, args):
        """Clear the screen"""
        print("\033[H\033[J", end='')
        self.print_header()
    
    def cmd_status(self, args):
        """Display system status"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}System Status:{Style.RESET_ALL}")
        print(f"  {Fore.GREEN}Status:{Style.RESET_ALL} Running")
        print(f"  {Fore.GREEN}Commands loaded:{Style.RESET_ALL} {len(self.commands)}")
        print(f"  {Fore.GREEN}Python version:{Style.RESET_ALL} {sys.version.split()[0]}")
        print()
    
    def cmd_exit(self, args):
        """Exit the application"""
        self.print_info("Goodbye!")
        self.running = False
    
    # ==================== ADD YOUR COMMANDS HERE ====================
    # Template for adding new commands:
    #
    # def cmd_yourcommand(self, args):
    #     """Description of your command"""
    #     # Your command logic here
    #     # args is a list of arguments passed to the command
    #     pass
    #
    # Then add to __init__:
    # self.commands['yourcommand'] = self.cmd_yourcommand
    # self.command_descriptions['yourcommand'] = 'Description'
    
    # ================================================================
    
    def cmd_dnspoof(self, args):
        """Spoof the user's DNS"""
        print(f"{Fore.MAGENTA}Spoofing DNS..{Style.RESET_ALL}")
        time.sleep(1.4)
        print(f"{Fore.CYAN}Getting proxy servers...\n")
        time.sleep(0.7)
        print(f"{Fore.WHITE}spoofed DNS to {Style.RESET_ALL}{Fore.CYAN}{generate_random_ip()}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}all traffic will be forwarded to spoofed DNS for anonymization{Style.RESET_ALL}")

    def cmd_bruteforce(self, args):
        """Simulate brute force password attack"""
        
        # Common passwords list for simulation (fallback)
        common_passwords = [
            "123456", "password", "12345678", "qwerty", "abc123",
            "monkey", "1234567", "letmein", "trustno1", "dragon",
            "baseball", "111111", "iloveyou", "master", "sunshine",
            "ashley", "bailey", "passw0rd", "shadow", "123123",
            "654321", "superman", "qazwsx", "michael", "football",
            "welcome", "jesus", "ninja", "mustang", "password1",
            "123456789", "adobe123", "admin", "1234567890", "photoshop"
        ]
        
        print(f"\n{Fore.CYAN}[*] Initializing brute force attack...{Style.RESET_ALL}")
        time.sleep(0.5)
        
        # Ask for password file
        print(f"{Fore.YELLOW}Enter password list file path (or press Enter for default list):{Style.RESET_ALL}")
        wordlist_path = input(f"{Fore.RED}- # {Style.RESET_ALL}").strip()
        
        # Load passwords from file or use default
        passwords = []
        if wordlist_path:
            try:
                print(f"{Fore.CYAN}[*] Loading passwords from {wordlist_path}...{Style.RESET_ALL}")
                time.sleep(0.3)
                
                if not os.path.exists(wordlist_path):
                    self.print_error(f"File not found: {wordlist_path}")
                    print(f"{Fore.YELLOW}[!] Using default password list instead{Style.RESET_ALL}")
                    passwords = common_passwords
                else:
                    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                        passwords = [line.strip() for line in f if line.strip()]
                    
                    if not passwords:
                        self.print_error("Password file is empty")
                        print(f"{Fore.YELLOW}[!] Using default password list instead{Style.RESET_ALL}")
                        passwords = common_passwords
                    else:
                        print(f"{Fore.GREEN}[+] Loaded {len(passwords)} passwords from file{Style.RESET_ALL}")
                        
            except Exception as e:
                self.print_error(f"Could not read file: {e}")
                print(f"{Fore.YELLOW}[!] Using default password list instead{Style.RESET_ALL}")
                passwords = common_passwords
        else:
            print(f"{Fore.CYAN}[*] Using default password list{Style.RESET_ALL}")
            passwords = common_passwords
            print(f"{Fore.GREEN}[+] Loaded {len(passwords)} passwords{Style.RESET_ALL}")
        
        time.sleep(0.5)
        
        # Ask for target
        print(f"{Fore.YELLOW}Enter target (note: stu.randolph... will be automatically added):{Style.RESET_ALL}")
        target = input(f"{Fore.RED}- # {Style.RESET_ALL}").strip()
        
        if not target:
            self.print_error("No target specified")
            return
        
        print(f"{Fore.CYAN}[*] Target: {Style.BRIGHT}{target}@stu.randolph.k12.nc.us{Style.RESET_ALL}")
        time.sleep(0.5)
        print(f"{Fore.CYAN}[*] Loading proxies...{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.CYAN}[*] Starting attack...\n{Style.RESET_ALL}")
        time.sleep(0.9)
        
        # Randomly select the "correct" password
        correct_password = random.choice(passwords)
        
        # Simulate trying passwords
        for i, password in enumerate(passwords, 1):
            # Print trying message
            print(f"{Fore.WHITE}[{i}/{len(passwords)}] Trying: {Fore.YELLOW}{password:<20}{Style.RESET_ALL}", end='')
            time.sleep(random.uniform(0.005, 0.085))
            
            if password == correct_password:
                # Success!
                print(f" {Fore.GREEN}[Found]{Style.RESET_ALL}")
                time.sleep(0.3)
                print(f"\n{Fore.GREEN}{Style.BRIGHT}[+] PASSWORD FOUND: {correct_password}{Style.RESET_ALL}\n")
                print(f"{Fore.BLUE}[+] Username:{target}{Style.RESET_ALL}")
                print(f"{Fore.BLUE}[+] Password:{correct_password}{Style.RESET_ALL}")
                print(f"\n{Fore.GREEN}[+] Password cracked successfully{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[*] Attempts: {i}/{len(passwords)}{Style.RESET_ALL}\n")
                break
            else:
                # Failed
                print(f" {Fore.RED}[Fail]{Style.RESET_ALL}")
        else:
            # This would only execute if we didn't break (shouldn't happen with our logic)
            print(f"\n{Fore.RED}[-] Password not found in dictionary{Style.RESET_ALL}\n")

    def parse_command(self, user_input):
        """Parse user input into command and arguments"""
        try:
            parts = shlex.split(user_input.strip())
        except ValueError as e:
            self.print_error(f"Invalid syntax: {e}")
            return None, []
        
        if not parts:
            return None, []
        
        command = parts[0].lower()
        args = parts[1:]
        return command, args
    
    def execute_command(self, command, args):
        """Execute a command with given arguments"""
        if command in self.commands:
            try:
                self.commands[command](args)
            except Exception as e:
                self.print_error(f"Command execution failed: {e}")
        else:
            self.print_error(f"Unknown command: '{command}'. Type 'help' for available commands.")
    
    def run(self):
        """Main application loop"""
        self.print_header()
        
        while self.running:
            try:
                self.print_prompt()
                user_input = input()
                
                if not user_input.strip():
                    continue
                
                command, args = self.parse_command(user_input)
                
                if command:
                    self.execute_command(command, args)
                    
            except KeyboardInterrupt:
                print()  # New line after ^C
                self.print_info("Use 'exit' or 'quit' to close the application")
            except EOFError:
                print()
                break
        
        print()  # Final newline

def main():
    """Entry point"""
    cli = CLITool()
    cli.run()

if __name__ == '__main__':
    main()