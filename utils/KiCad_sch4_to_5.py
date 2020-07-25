import sys, getopt, os

def main(argv):
    filename = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'Converts KiCAD Schematic files from v4.0 to v5.0\nSpecify full path for file to convert with -i <filepath/filename>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Converts KiCAD Schematic files from v4.0 to v5.0\nSpecify full path for file to convert with -i <filepath/filename>'
            sys.exit()
        elif opt in ('-i'):
            filename = eval('"' + arg.replace('"', '\\"') + '"')
    print 'File to convert is ', filename
    
    if os.path.isfile(filename.decode('string-escape')):
        try: 
            sch_file = open(filename, 'w+')            
        except IOError:
            print 'Unable to open file: {}'.format(filename)
            
        for line in sch_file:
            print line        
    else:
        print 'Unable to open file: {}'.format(filename)

if __name__ == "__main__":
   main(sys.argv[1:])