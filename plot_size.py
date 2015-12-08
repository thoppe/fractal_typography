import numpy as np
import glob, os
import pandas as pd
import math

F_FILES = sorted(glob.glob("pdf/compressed/level*"))
compress_sizes = np.array([os.stat(f).st_size for f in F_FILES]).astype(float)
compress_sizes /= 2**10

F_FILES = sorted(glob.glob("pdf/level*"))
normal_sizes = np.array([os.stat(f).st_size for f in F_FILES]).astype(float)
normal_sizes /= 2**10
level = range(1,len(normal_sizes)+1)

X = [8**x for x in level]
X = [math.log10(8**x) for x in level]

df = pd.DataFrame(columns=("original pdf", "compressed pdf"),
                  data=np.vstack([normal_sizes,compress_sizes]).T)


print np.polyfit(level,df["original pdf"],1)[0]
print np.polyfit(level,df["compressed pdf"],1)[0]

import seaborn as sns
plt = sns.plt
plt.plot(X,df["original pdf"],label="original pdf (404 bytes per level)")
plt.plot(X,df["compressed pdf"],label="compressed pdf (41 bytes per level)")
plt.legend(loc="best",fontsize=18)

plt.xlabel("$\log_{10}$ number of copies ~ recursion depth",fontsize=18)
plt.ylabel("file size (kB)",fontsize=18)

y = 30
x = np.log10(6.0221e23)
plt.annotate("avogadro's number", xy=(x, y), xytext=(x+20, y+20),
            arrowprops=dict(facecolor='black', shrink=0.05),alpha=0.75)

x = np.log10(4*10e80)
plt.annotate("atoms in universe", xy=(x, y), xytext=(x+20, y+40),
            arrowprops=dict(facecolor='black', shrink=0.05),alpha=0.75)

x = np.log10(1e123)
plt.annotate("Shannon's number", xy=(x, y), xytext=(x+20, y+60),
            arrowprops=dict(facecolor='black', shrink=0.05),alpha=0.75)

plt.axis('tight')
plt.savefig("figures/depth.png")
plt.show()

