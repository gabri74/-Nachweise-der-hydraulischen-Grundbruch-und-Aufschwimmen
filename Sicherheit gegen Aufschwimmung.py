#!/usr/bin/env python
# coding: utf-8

# ### <span style="color:blue;font-family:Tahoma;">Nachweis der Sicherheit gegen Aufschwimmen UPL (Ultimate Limit State – Uplift) EC7</span>
# ### <span style="color:green;font-family:Tahoma;"> A<sub>dst,k</sub> · γ<sub>G,dst</sub> ≤ G<sub>stb,k</sub> · γ<sub>G,stb</sub> </span>
# 
# 

# <span style="color:black;font-family:Tahoma;"> Wasserdruck (Pw) </span>

# In[1]:


n=13
ΔH=4
Δh=ΔH/n
h0=10
nt=11.5
z=4
h=h0-(nt*Δh)
Pw=(h-z)*10
print("Wasserdruck Pw =", Pw)


# **<span style="color:black;font-family:Tahoma;"> Gewichtskraft (G) </span>**

# In[5]:


γm=24
G=γm*2*((4*0.3)+(2*0.3))
print("Gewichtskraft G =", G)


# **<span style="color:red;font-family:Tahoma;"> Auftriebskraft (A) = Wasserdruck Pw * Mächtigkeit L</span>**

# In[6]:


L=2.4              
A=Pw*L
print("Auftriebskraft A =", A)


# <span style="color:blue;font-family:Tahoma;"> Teilsicherheitsbeiwert (stabilisierende 
#  (γG,stb), Teilsicherheitsbeiwert  (destabilisierende (γG,dst) </span>

# In[7]:


γGstb = 0.95
γGdst=1.05


# **<span style="color:black;font-family:Tahoma;">  Stabiliesierende Gewichtskraft (Gst), und destabilisierende Auftriebskraft(Adst) </span>**

# In[8]:


Gst=G* γGstb
print("Stabiliesierende Gewichtskraft Gst =", Gst)
print()
Adst=A*γGdst
print("Distabiliesierende Auftriebskraft Adst =", Adst)




# ### <span style="color:blue;font-family:Tahoma;"> Nachweis der Sicherheit gegen Aufschwimmen nach EC7 </span>
# ### <span style="color:red;font-family:Tahoma;"> A<sub>dst,k</sub> · γ<sub>G,dst</sub> ≤ G<sub>stb,k</sub> · γ<sub>G,stb</sub> </span>
# 

# In[9]:


if G >= Adst :
    print("Nachweis erbracht!")
else:
        print("Nachweis nicht erfüllt!!!!!")
        
        


# In[ ]:




