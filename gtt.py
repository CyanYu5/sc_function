import matplotlib.pyplot as plt
import numpy as np

def gtt(path,time_start,time_done,Rlist,Rline=0,Rmax:int=0,atd:float=.0,d:list=0,stup:list=0,rg:int=0,title_word:str="GTT",tx:bool=True,delay:float="",shiplist=""):
    """繪製一張甘特圖，需先開啟圖層!

    Args:
        path (list[list]): 工件編號list[list],eg:[機台一[1,2,3,-1],機台二[4,5]],<-1代表該機台無此工件>
        time_start (_type_): 工件開始時間list[list],eg:[[1,3,8],[2,5]]
        time_done (_type_): 工件結束時間list[list],eg:[[2,7,10],[5,8]]
        Rlist (_type_): 下方數線表,整數時間點的值[1,2,2,3,2 ,1,3,2,2,3]. Defaults to 0.
        Rline (int, optional): 數線表上限值eg:3. Defaults to 0.
        Rmax (int, optional): _description_. Defaults to 0.
        atd (float, optional): _description_. Defaults to .0.
        d (list, optional): _description_. Defaults to 0.
        stup (list, optional): _description_. Defaults to 0.
        rg (int, optional): _description_. Defaults to 0.
        title_word (str, optional): _description_. Defaults to "GTT".
        tx (bool, optional): _description_. Defaults to True.
        delay (float, optional): _description_. Defaults to "".
        shiplist (str, optional): _description_. Defaults to "".
    """

    machine=len(path)
    jobs=len(path[0])
    for i in range(machine):
        for j in range(len(path[i])):
            if path[i][j]!=-1:
                plt.barh(y=i,width=time_done[i][j]-time_start[i][j],left=time_start[i][j],height=0.5,color=plt.cm.tab20c.colors[i%19])
                if tx==True:
                    if d==0:
                        plt.text(x=time_start[i][j]+3,y=i+.1,s='j'+str(path[i][j])+"r"+f"{int(Rlist[i][j])}")
                        plt.text(x=time_start[i][j]+3,y=i-.25,s=time_done[i][j]-time_start[i][j])
                    else:
                        plt.text(x=time_start[i][j]+3,y=i+.1,s='j'+str(path[i][j])+"r"+f"{int(Rlist[i][j])}")
                        plt.text(x=time_start[i][j]+3,y=i+.05,s=f"p:{time_done[i][j]-time_start[i][j]}")  
                        plt.text(x=time_start[i][j]+3,y=i-.05,s=f"s:{int(stup[i][j])}")  
                        plt.text(x=time_start[i][j]+3,y=i-.25,s=f"d:{int(d[i][j])}")          
                        if shiplist!="":
                            plt.text(x=time_start[i][j]+3,y=i-.45,s=f"d:{int(shiplist[i][j])}")   

        plt.draw()
        plt.pause(0.2)   
        if time_done[i]!=[]:                   
            a=int(max(time_done[i]))
            plt.barh(y=1,width=2,left=a,color=plt.cm.tab20c.colors[i%19],height=machine+0.2)
            if tx==True:
                plt.text(x=int(max(time_done[i])),y=1.2*i/machine,s=str(f"{i+1}"))
    y_label = []
    for i in range(machine):
        d=np.array(path[i])
        d=d[d>=0]
        y_label.append(f"{i}--j:{d.shape[0]}")
    if Rmax==0:
        pass
    else:
        Rline_min=np.min(Rline[Rline>0])
        atd=int(atd)
        plt.plot(range(atd),(Rline[:atd]-Rline_min)/Rmax-2,color="red",label="R")
        plt.plot([0,atd],[-1,-1],linestyle="--",label="Rmax")
        plt.text(x=atd*1.001,y=-.4,s=f"<-done{atd}\ndelay:{delay}",c="red")
        plt.text(x=0,y=-.9,s=f"Rmax={Rmax}",c="blue")
    plt.legend()
    plt.yticks(range(machine),y_label,rotation =45)
    plt.title(f"{title_word}")
    plt.ylabel("Machine")
    plt.xlabel("Time")
    if rg!=0:
        plt.xlim(0,rg)
    else:
        plt.xlim(left=0)
if __name__=="__main__":
    path = [[4, -1, -1, -1], [0, 1, 5, 8], [3, 2, 6, 7], [9, -1, -1, -1]]
    time_start = [[376, -1, -1, -1], [188, 656, 836, 1363], [339, 770, 891, 1574], [1081, -1, -1, -1]]
    time_done = [[418, -1, -1, -1], [604, 698, 1348, 1646], [426, 884, 1053, 1681], [1599, -1, -1, -1]]
    Rlist=[[1,2,2,1],[1,2,2,1],[1,2,2,1],[1,2,2,1]]
    rline=np.random.randint(low=0,high=2,size=1700)
    gtt(path,time_start,time_done,Rlist,rline,10,1681)
    plt.pause(0.2)
plt.show()