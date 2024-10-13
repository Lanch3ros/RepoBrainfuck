import sys
print (sys.argv)

def read_file (name_file):
    f = open (name_file, "r")
    print (f.read())

def main ( ):
    if len(sys.argv) >= 2:
        read_file (sys.argv[1])
    else:
        print ("No se imprimio ya que necesitamos leer un archivo.")

main ( )