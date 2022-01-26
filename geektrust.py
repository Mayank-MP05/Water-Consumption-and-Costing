import sys

def main():
    input_file = sys.argv[1]
    opened_file_ptr = open(input_file,'r')
    while True:
        line = opened_file_ptr.readline()
        if not line:
            break
        print("---",line)

        

if __name__ == "__main__":
    main()