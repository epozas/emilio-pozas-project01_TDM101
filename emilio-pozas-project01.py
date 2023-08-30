import socket
print(socket.gethostname())

import pandas as pd
df = pd.read_csv('/anvil/projects/tdm/data/flights/subset/1991.csv') 
#Kernel unable to run this line of code. Meaning no variable "df" is created.

df[df["Month"]==12].head() # see information about a few of the flights from December 1991

#Calculate cores on anvil sub-clusters A, B, and G
128*(1000+32+16)

#Calculate the memory on anvil sub-clusters A, B and G
1000*256+32*1000+16*500