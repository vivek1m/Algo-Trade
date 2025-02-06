# plotting code that design the plot fr observation
import pandas as pd
from matplotlib import pyplot as plt

def desired_plot(company,start,end):
    df_original=pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Algo Trade\Data.csv')
    df=df_original.copy(True)
    
    index=0
    start_index=0 
    end_index=0

    for i in range (1,len(df)):
        if df.loc[i,"Date"] == company:
            index=i
            break  
    for i in range(1,len(df.columns)):
        if start==df.columns[i]:
            start_index=i
        if end==df.columns[i]:
            end_index=i
    plt.style.use('dark_background')
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    new_x=[]
    for i in range(start_index,end_index+1):
        new_x.append(str(df.columns[i]))
    
    new_y=[]

    for i in range(start_index,end_index+1):
        y=df.iloc[index,i]
        new_y.append(float(y))

    # new_x=[]
    # new_y=[]
    # for i in range(0,len(Y_axis)):
    #     if Y_axis[i]!=0:
    #         new_x.append(X_axis[i])
    #         new_y.append(Y_axis[i])
            
    fig,axes=plt.subplots(1,1)
    
    
    
    s=df.iloc[index,0]
    plt.title(s+" Stock Analysis",fontsize="x-large",fontweight="bold")
    plt.xlabel("Dates",fontsize="x-large",fontweight="bold")
    plt.ylabel("Stock Prices in Rupees",fontsize="x-large",fontweight="bold")
    
    for i in range(0,(len(new_x)-1)):
        x_val=[new_x[i],new_x[i+1]]
        y_val=[new_y[i],new_y[i+1]]
        
        if y_val[0]<=y_val[1]:
            plt.plot(x_val,y_val,color='lime',linewidth=4,marker='D', markersize=7)
 #             plt.fill_between(x_val, 0, y_val, color='g')
        else:
            plt.plot(x_val,y_val,color='crimson',linewidth=4,marker='D', markersize=7)
 #             plt.fill_between(x_val, 0, y_val, color='y')
        
 #     plt.grid()
    
  
    plt.text(new_x[0],new_y[0],f"{new_y[0]}",fontsize="x-large",weight="bold")
    plt.text(new_x[-1],new_y[-1],f"{new_y[-1]}",fontsize="x-large",weight="bold")
    

    tick=[new_x[0]]
    for i in range(1,(len(axes.get_xticklabels())-1)):
        tick.append(' ')
    tick.append(new_x[-1])
    # axes.set_xticklabels(tick)
    my_xticks=[start,end]
    plt.xticks([my_xticks[0], my_xticks[-1]], visible=True, rotation="horizontal")
    axes.xaxis.set_tick_params(labelsize=13)
    axes.yaxis.set_tick_params(labelsize=13)

        
    # plt.show()
    plt.style.use('default')
    fig.savefig("desired.png")
    # return fig
    # print(df.iloc[0,1])
            

    

    

    
# desired_plot('Aurobindo Pharma Limited','01-02-2017','01-11-2021')
