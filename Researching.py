


import tkinter as tk
from scipy.optimize import curve_fit
from PIL import ImageGrab
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from scipy import*
from scipy.interpolate import spline
import numpy as np
import os
from mss import mss
from PIL import Image
import time


time.sleep(4)


root = tk.Tk()
root.withdraw()


im = ImageGrab.grab()
img = im.rotate(180)

Xpoints = []
Ypoints = []
Xpointsreal = []
Ypointsreal = []
counter = 0
inital = 0
def func(x, a, n):
    return a*x**n
def getpoints(imag):
    points = []
    fig = plt.figure()
    plt.imshow(imag)
    plt.gca().invert_yaxis()
    plt.gca().invert_xaxis()
    def onclick(event):

        #print('button = %d, x = %d, y = %d, xdata = %f, ydata = %f' % (event.button, event.x, event.y, event.xdata, event.ydata))


        points.append((event.xdata,event.ydata)) v
        Ypoints.append(event.ydata)

        Xpoints.append(event.xdata)
        Xpointsreal.append(event.xdata)
        Ypointsreal.append(event.ydata)
        plt.scatter(Xpoints[(len(Xpoints))-1], Ypoints[(len(Ypoints))-1], facecolors = 'none', edgecolors = 'b')
        fig.canvas.draw_idle()
        if (len(points) == 10):
            
            plt.close(event.canvas.figure)


            Starterx = Xpoints[0]
            Startery = Ypoints[0]
            scale = -(Xpoints[-1]-Xpoints[0])
            Xpoints = (Xpoints[0]-Xpoints)/scale
            
            Ypoints = -(Ypoints-Ypoints[0])/scale

            popt, pcov = curve_fit(func,Xpoints,Ypoints,bounds=(0,[np.inf,1]))

            err = np.sqrt(mean((func(Xpoints,*popt)-Ypoints)**2))
            abso = abs(2000/scale)

            xnew = np.linspace(max(Xpoints)*abso, min(Xpoints), 1000000, "-r")
            power_y = popt[0]*xnew**popt[1]

            plt.plot(xnew*-scale+Starterx, -power_y*scale+Startery, "r")
            plt.imshow(im)
            
            plt.imshow(im.rotate(180))
            plt.gca().invert_yaxis()
            plt.gca().invert_xaxis()

            plt.scatter(Xpointsreal,Ypointsreal, facecolors = 'none', edgecolors = 'b')
            plt.plot(Xpoints, func(Xpoints,*popt), "r")
            print()
            print(type(popt[0]))
            print('a='+str(round(popt[0], 3)),'n='+str(round(popt[1], 3)),'scale='+str(round(popt[0], 3)))
            print()
            #print (str(popt[0])+'*'+'x'+'^'+str(popt[1]))
            print()
            #2150 is arbitrary number
            if ((popt[0]*2150**popt[1])>(.49*2150**.29)):
                print("surgery recommended")
                print()
            else:
                print("surgery not recommended")
                print()
            plt.show()

    def keypress(event):
        
        #print(Xpoints)
           
        if event.key == ' ':
            points.pop()
            Xpointsreal.pop()
            Ypointsreal.pop()
            Xpoints.pop()
            Ypoints.pop()


    fig.canvas.mpl_connect('button_press_event', onclick)
    fig.canvas.mpl_connect('key_press_event', keypress)
    plt.draw()
    plt.show()
    return points


getpoints(img)



