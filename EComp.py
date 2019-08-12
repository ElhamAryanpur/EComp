from sys import argv

if __name__ == "__main__":

    try:
        data = str(argv[1])
    
    except IndexError:
        with open("c.e", 'r') as f:
            data = f.read()

    exec(str("from " + data + " import comp"))
    exec(str("comp()"))