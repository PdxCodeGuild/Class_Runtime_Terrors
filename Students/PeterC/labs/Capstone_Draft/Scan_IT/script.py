def r_script(request):
    if len(sys.argv) == 2:
            target = socket.gethostbyname(sys.argv[1])
    else:
            print("Invalid amount of arguments")
    try:
            for port in range(20,25):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((target,port))
                    if result == 0:
                            print("Port {} is open".format(port))
                    s.close()
    except KeyboardInterrupt:
            sys.exit()     
