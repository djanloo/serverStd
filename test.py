from serverstd import serverStdout, serverStderr, splot
import matplotlib.pyplot as plt
import sys
sys.stdout = serverStdout()
sys.stderr = serverStderr()

print("This is a test line")
print("This is another test line. But longer.")

fig, ax = plt.subplots(figsize=(5,5))
ax.plot([0,1,2,3,4], [1,-1,2,-0.5, 4], color='k')
ax.grid(ls=":")
ax.set_title("This is a matplotlib figure")
splot(fig)

print("The next one will be an error.")
c = "42" + 420

