from flight_simulation import *
import matplotlib.pyplot as plt

def main():
    plt.figure(figsize=(10, 6))
    #Optimitzing ROC
    #MTOW 100%
    E = Equations()
    x, y = E.getCCO('B767-300ER', 1, 'ROC')
    plt.plot(x,y, label="B767-300ER MTOW: 100%, ROC optimized")

    x, y = E.getCCO('B777-300', 1, 'ROC')
    plt.plot(x,y, label="B777-300 MTOW: 100%, ROC optimized")

    x, y = E.getCCO('B737', 1, 'ROC')
    plt.plot(x,y, label="B737 MTOW: 100%, ROC optimized")

    x, y = E.getCCO('A320-212', 1, 'ROC')
    plt.plot(x,y, label="A320-212 MTOW: 100%, ROC optimized")

    x, y = E.getCCO('A319-131', 1, 'ROC')
    plt.plot(x,y, label="A319-131 MTOW: 100%, ROC optimized")

    #MTOW 80% 
    x, y = E.getCCO('B767-300ER', 0.8, 'ROC')
    plt.plot(x,y, label="B767-300ER MTOW: 80%, ROC optimized")

    x, y = E.getCCO('B777-300', 0.8, 'ROC')
    plt.plot(x,y, label="B777-300 MTOW: 80%, ROC optimized")

    x, y = E.getCCO('B737', 0.8, 'ROC')
    plt.plot(x,y, label="B737 MTOW: 80%, ROC optimized")

    x, y = E.getCCO('A320-212', 0.8, 'ROC')
    plt.plot(x,y, label="A320-212 MTOW: 80%, ROC optimized")

    x, y = E.getCCO('A319-131', 0.8, 'ROC')
    plt.plot(x,y, label="A319-131 MTOW: 80%, ROC optimized")

    plt.legend(fontsize='small', title="Aircraft type and MTOW")
    plt.title("CCO trajectories for different aircraft types and MTOW")
    plt.xlabel("Distance (m)")
    plt.ylabel("Altitude (m)")

    #Optimitzing Gamma
    #MTOW 100%
    E = Equations()
    x, y = E.getCCO('B767-300ER', 1, 'Gamma')
    plt.plot(x,y, label="B767-300ER MTOW: 100%, Gamma optimized")

    x, y = E.getCCO('B777-300', 1, 'Gamma')
    plt.plot(x,y, label="B777-300 MTOW: 100%, Gamma optimized")

    x, y = E.getCCO('B737', 1, 'Gamma')
    plt.plot(x,y, label="B737 MTOW: 100%, Gamma optimized")

    x, y = E.getCCO('A320-212', 1, 'Gamma')
    plt.plot(x,y, label="A320-212 MTOW: 100%, Gamma optimized")

    x, y = E.getCCO('A319-131', 1, 'Gamma')
    plt.plot(x,y, label="A319-131 MTOW: 100%, Gamma optimized")

    #MTOW 80% 
    x, y = E.getCCO('B767-300ER', 0.8, 'Gamma')
    plt.plot(x,y, label="B767-300ER MTOW: 80%, Gamma optimized")

    x, y = E.getCCO('B777-300', 0.8, 'Gamma')
    plt.plot(x,y, label="B777-300 MTOW: 80%, Gamma optimized")

    x, y = E.getCCO('B737', 0.8, 'Gamma')
    plt.plot(x,y, label="B737 MTOW: 80%, Gamma optimized")

    x, y = E.getCCO('A320-212', 0.8, 'Gamma')
    plt.plot(x,y, label="A320-212 MTOW: 80%, Gamma optimized")

    x, y = E.getCCO('A319-131', 0.8, 'Gamma')
    plt.plot(x,y, label="A319-131 MTOW: 80%, Gamma optimized")

    #put the legend outside the plot
    plt.legend(fontsize='small', title="Aircraft type and MTOW", loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title("CCO trajectories for different aircraft types and MTOW")
    plt.xlabel("Distance (m)")
    plt.ylabel("Altitude (m)")

    plt.tight_layout()
    plt.savefig("CCO_trajectories.png", dpi=300)

if __name__ == "__main__":
    main()
