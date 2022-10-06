# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:31:13 2021

@author: Varun
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
#Create figure
fig=plt.figure(facecolor= "lightgreen")
fig.set_size_inches(7, 5)
ax=fig.add_subplot(1,1,1)

#Pitch Outline & Centre Line
plt.plot([0,0],[0,80], color="black")
plt.plot([0,120],[80,80], color="black")
plt.plot([120,120],[80,0], color="black")
plt.plot([120,0],[0,0], color="black")
plt.plot([60,60],[0,80], color="black")

#Left Penalty Area
plt.plot([18,18],[62,18],color="black")
plt.plot([0,18],[62,62],color="black")
plt.plot([18,0],[18,18],color="black")

#Right Penalty Area
plt.plot([120,102],[62,62],color="black")
plt.plot([102,102],[62,18],color="black")
plt.plot([102,120],[18,18],color="black")

#Left 6-yard Box
plt.plot([0,6],[50,50],color="black")
plt.plot([6,6],[50,30],color="black")
plt.plot([6,0],[30,30],color="black")

#Right 6-yard Box
plt.plot([120,114],[50,50],color="black")
plt.plot([114,114],[50,30],color="black")
plt.plot([114,120],[30,30],color="black")

#Prepare Circles
centreCircle = plt.Circle((60,40),10,color="black",fill=False)
centreSpot = plt.Circle((60,40),0.8,color="black")
leftPenSpot = plt.Circle((12,40),0.8,color="black")
rightPenSpot = plt.Circle((108,40),0.8,color="black")

#Draw Circles
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)

#Prepare Arcs
leftArc = Arc((12,40),height=20,width=20,angle=0,theta1=310,theta2=50,color="black")
rightArc = Arc((108,40),height=20,width=20,angle=0,theta1=130,theta2=230,color="black")

#Draw Arcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)
#goals post
plt.plot([0,0],[36,44], color="red")
plt.plot([120,120],[36,44], color="red")
plt.plot([-0.8,-0.8],[36,44], color="red")
plt.plot([120.8,120.8],[36,44], color="red")

#hide axis
plt.axis('off')
plt.show()