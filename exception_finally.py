import sys
import time

try:
    fhand = open('C:/Users/xly/Desktop\poem.txt')
    for line in fhand:
        print(line, end='')
        sys.stdout.flush()
        print('Press ctrl+c now')
        time.sleep(2)
except IOError:
    print('Could not find file poem.txt')
except InterruptedError:
    print('!! You canceled the reading from the file.')
finally:
    if fhand:
        fhand.close()
    print('(Cleaning up: Closed the file)')
