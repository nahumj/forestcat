import matplotlib.pyplot as plt
import numpy as np

def plot_stream(stream, data, r):
    """
    Plots the values of a specific stream over time.
    Inputs: stream - an int indicating the index of the desired stream
    data - An array of all sensor data
    r = a RAVQ object
    Returns: The number of -1s (indicating invalid data) in this stream
    """
    values = []
    negs = 0
    for i in range(len(states)):
        if states[i]  == -1:
            negs += 1
        else:
            values.append(r.models[states[i]].vector[stream])
    plt.plot(data[1][negs:len(states)], values, 'r-')
    return negs
    
def plotColorStatesNoNumber(states):
    """
    Makes a color-bar plot of states over time.
    Inputs: states - a list indicating the state at
    each time step.
    """
    fig = plt.figure(figsize=(9.0,6))
    for i in range(len(states)):
        if states[i] == -1:   
            plt.plot(i, 0, "ko", hold=True)
        elif states[i] == 0:
            plt.plot(i, 1, "|", color="LawnGreen")
        elif states[i] == 1:
            plt.plot(i, 1, "|", color="LimeGreen")
        elif states[i] == 2:
            plt.plot(i, 1, "|", color="teal")
        elif states[i] == 7:
            plt.plot(i, 1, "|", color="DarkGreen")
        elif states[i] == 4:
            plt.plot(i, 1, "b|")
        elif states[i] == 5:
            plt.plot(i, 1, "|", color="DarkBlue")
        elif states[i] == 6:
            plt.plot(i, 1, "|", color="purple")
        elif states[i] == 3:
            plt.plot(i, 1, "|", color="green")
        elif states[i] == 8:
            plt.plot(i, 1, "|", color="yellow")
        elif states[i] == 9:
            plt.plot(i, 1, "|", color="navy")
        elif states[i] == 11:
            plt.plot(i, 1, "|", color="GreenYellow")
        elif states[i] == 10:
            plt.plot(i, 1, "|", color="orange")
        elif states[i] == 12:
            plt.plot(i, 1, "|", color="red")
        else:
            plt.plot(i, 1, "-")
    plt.show()
            
            
def plotColorStates(states, times):
    """
    Makes a plot in which state is on the y axis and time is on the x axis 
    and points are colored by state.
    Input: states - a list of ints representing the state at each time step.
    """
    fig = plt.figure(figsize=(18.0,12))
    for i in range(len(states)):
        if states[i] == -1:   
            plt.plot(times[i], 0, "ko", hold=True)
        elif states[i] == 0:
            plt.plot(times[i], 9, "|", color="LawnGreen")
        elif states[i] == 1:
            plt.plot(times[i], 8, "|", color="LimeGreen")
        elif states[i] == 2:
            plt.plot(times[i], 5, "|", color="teal")
        elif states[i] == 7:
            plt.plot(times[i], 6, "|", color="DarkGreen")
        elif states[i] == 4:
            plt.plot(times[i], 4, "b|")
        elif states[i] == 5:
            plt.plot(times[i], 2, "|", color="DarkBlue")
        elif states[i] == 6:
            plt.plot(times[i], 1, "|", color="purple")
        elif states[i] == 3:
            plt.plot(times[i], 7, "|", color="green")
        elif states[i] == 8:
            plt.plot(times[i], 11, "|", color="yellow")
        elif states[i] == 9:
            plt.plot(times[i], 3, "|", color="navy")
        elif states[i] == 11:
            plt.plot(times[i], 10, "|", color="GreenYellow")
        elif states[i] == 10:
            plt.plot(times[i], 12, "|", color="orange")
        elif states[i] == 12:
            plt.plot(times[i], 13, "|", color="red")
        else:
            plt.plot(times[i], states[i], "*", color="black")
            
def printTransitions(states):
  for i in range(1,len(states)):
      if states[i-1] != states[i]:
          print data[0][i], ":", states[i-1], "->", states[i]

def stateFrequency(states):
    freqDict = {}
    for state in states:
        if freqDict.has_key(state):
            freqDict[state] += 1
        else:
            freqDict[state] = 1.0
            
    for s in freqDict.keys():
        freqDict[s] /= len(states)
    
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ind = np.arange(len(freqDict.keys()))
    print len(ind)
    print len(freqDict.keys())
    ax.bar(ind, [freqDict[i] for i in range(len(freqDict.keys())-1)], .35, color="r")
    plt.show()
    """
    return freqDict
