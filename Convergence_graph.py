from matplotlib import pyplot as plt
import time

class convergence_graph:
    def __init__(self,n:int=1) -> None:
        self.max_fitness = [[]for i in range(n)]
        self.min_fitness = [[]for i in range(n)]
        self.avg_fitness = [[]for i in range(n)]
        self.start=time.time()
    def draw(self,x,y,data: list[float],max_g,plotwhere: str=1,move: bool =True) -> None:
        """create a plot to show the fitness of each generation
        Args:
            data (list[float]): the fitness of each generation
            plotwhere (str): the plot will be shown in which window
            move (bool, optional): if the plot will be moved. Defaults to True.
        """
        
        ax=plt.subplot(x,y,plotwhere)
        self.max_fitness[plotwhere-1].append(max(data))
        self.min_fitness[plotwhere-1].append(min(data))
        self.avg_fitness[plotwhere-1].append((sum(data))/len(data))
        ax.clear()
        #runing time
        ax.text(0.5, 0.5, f'Running Time: {round(time.time()-self.start,2)}s', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        ax.plot(self.max_fitness[plotwhere-1], label='Max Fitness')
        ax.plot(self.min_fitness[plotwhere-1], label='Min Fitness')
        ax.plot(self.avg_fitness[plotwhere-1], label='Avg Fitness')
        if move:
            ax.set_xlim(max(0,len(self.min_fitness[plotwhere-1])-20), min(max_g,len(self.min_fitness[plotwhere-1])+20))
            if len(self.min_fitness[plotwhere-1])>=11:
                ax.set_ylim(min(self.min_fitness[0][-10:])*0.95,max(self.max_fitness[0][-10:])*1.05)
        elif max_g==0:
            max_g=len(self.min_fitness[plotwhere-1])
        else:
            ax.set_xlim(0, max_g)
        ax.set_xlabel('Generation')
        ax.set_ylabel('Fitness')
        if plotwhere==1:
            ax.set_title(f'Fitness by Generation{len(self.min_fitness[plotwhere-1])}; Running Time: {round(time.time()-start,2)}s')
        ax.legend()
        plt.pause(0.001)

if __name__=="__main__":
    fig,ax=plt.subplots(2,1)
    import numpy as np
    start=time.time()
    convergence=convergence_graph(n=2)
    for i in range(100):
        dt=np.random.randint(50-i//2,105-i//1.5,3)
        convergence.draw(2,1,dt,100,plotwhere=1,move=False)
        convergence.draw(2,1,dt,100,plotwhere=2,move=True)
        time.sleep(0.1)
    plt.show()
