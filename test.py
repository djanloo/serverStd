from serverstd import serverStdout, serverStderr
import matplotlib.pyplot as plt
import sys
sys.stdout = serverStdout()
sys.stderr = serverStderr()

print("This is a test line")
print("This is another test line. But longer.")
print("The next one will be an error.")
c = "42" + 420

