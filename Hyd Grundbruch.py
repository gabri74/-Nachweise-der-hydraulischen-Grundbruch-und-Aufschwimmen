#!/usr/bin/env python
# coding: utf-8

# ### <span style="color:red;font-family:Tahoma;">Nachweis der Sicherheit gegen Hydraulischen Grundbruch GZ HYD (Ultimate Limit State – Hydraulic Failure) Euro Code 7 </span>
# ### <span style="color:blue;font-family:Tahoma;"> S<sub>dst,k</sub> · γ<sub>H</sub> ≤ G<sub>stb,k</sub> ·  γ<sub>G,stb</sub></span>
# 

# **<span style="color:black;font-family:Tahoma;"> Gewichtskraft (G) </span>**

# In[10]:


γ=12      #γ'
t=5
V=t*(t/2)*1
G= γ*V
print("Gewichtskraft G =", G)


# ***<span style="color:red;font-family:Tahoma;"> Strömungskraft (S) </span>***
# 
# 

# In[11]:


ΔH=10
n=14
Δh=ΔH/n
h0=18
nt=9
γw=10
i=ΔH*((n-nt)/n)*1/t
S=i*V*γw
print("Strömungskraft S =", S)


# <span style="color:blue;font-family:Tahoma;"> Teilsicherheitsbeiwert (stabilisierende 
#  (γH), Teilsicherheitsbeiwert  (destabilisierende (γG,dst) </span>

# In[18]:


γGst = 0.95
γH=1.45     #günstig


# **<span style="color:black;font-family:Tahoma;">  Stabiliesierende Gewichtskraft (G,stbK), und destabilisierende Strömungskraft(S,dstK) </span>**

# In[19]:


Gst=G* γGst
print("Stabiliesierende Gewichtskraft Gst,K =", Gst)
print()
Sdst=S*γH
print("Distabiliesierende Strömungskraft Sdst,K =", Sdst)




# ### <span style="color:blue;font-family:Tahoma;"> Nachweis der Sicherheit gegen Aufschwimmen nach EC7 </span>
# ### <span style="color:red;font-family:Tahoma;"> G<sub>dst,k</sub> · γ<sub>G,dst</sub> ≤ G<sub>stb,k</sub> · γ<sub>G,stb</sub> </span>
# 

# In[20]:


if G >= Sdst :
    print("Nachweis erbracht!")
else:
        print("Nachweis nicht erfüllt!!!!!")
        
        

