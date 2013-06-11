import binascii, sys, struct

def main(szFileName):
    hFile = open(szFileName, "rb")
    szBytes = hFile.readlines()
    hb = binascii.a2b_hex(szBytes[0])
    hFileOut = open("payload.class", "wb")
    hFileOut.write(hb)
    hFileOut.close()
    hFile.close()

# Banner
def Banner():
    print("=================================================")
    print("HexBytes2Bin v0.1                                ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: %s <filename>\n") % (cmd)
    
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Please enter a filename!")
        exit(0)
    main(sys.argv[1])
