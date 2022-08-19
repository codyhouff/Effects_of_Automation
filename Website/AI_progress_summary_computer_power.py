import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math

excel_link = 'C:/Users/00MrK/Desktop/graduate_school_stuff/Georgia_Institute_of_Technology/Research/Effects_of_Automation/computer_progress/speed_of_computers.xlsx'
text_name = 'AI_progress_summary_computer_power'

#print(df)
df = pd.read_excel(excel_link, sheet_name='super_computer', usecols="A,B,C,D,E,F,G", skiprows=range(1, 63), nrows=59)
df2 = pd.read_excel(excel_link, sheet_name='GPU_Data_Vintage_Graph_Clean', usecols="A,B,C,D,I", nrows=261)
#print(df2)
##########################################

max_supercomputer_1 = df.iloc[[df['Top 1 (FLOP/s)'].idxmax()]]
max_supercomputer_500 = df.iloc[[df['Top 500 (FLOP/s)'].idxmax()]]
max_1000_gpu = df2.iloc[[df2['FLOP/s per $1000 GPU (2021)'].idxmax()]]

print(max_supercomputer_1.to_string())
print(max_supercomputer_500.to_string())
print(max_1000_gpu.to_string())

df_combined = pd.DataFrame({'Computers':['#1 Supercomputer','#500 Supercomputer','$1,000 GPU'],
                   'Model':[max_supercomputer_1.iloc[0]['Top 1 model'], max_supercomputer_500.iloc[0]['Top 500 model'], max_1000_gpu.iloc[0]['model']],
                   'Date':[max_supercomputer_1.iloc[0]['Date'], max_supercomputer_500.iloc[0]['Date'], max_1000_gpu.iloc[0]['Date']],
                   'FLOP/s':[max_supercomputer_1.iloc[0]['Top 1 (FLOP/s)'], max_supercomputer_500.iloc[0]['Top 500 (FLOP/s)'], max_1000_gpu.iloc[0]['FLOP/s per $1000 GPU (2021)']],
                   'Bar':[1, 1, 1]})

print(df_combined.to_string())


##########################################
#fig = px.bar(max_parameters, x="bar_graph_x1", y="Parameters", log_y=True, text="Domain", color = "Domain") # barmode="overlay"   category_orders = [])
fig = px.bar(df_combined, x="Computers", y="FLOP/s", log_y=True, hover_name="Model", color = "Computers") #log_y=True, # x="bar_graph_x1",  text="Computers",
#fig.show()
#########################################
lines = [10**9,10**12,10**16,10**18,60629*10**16,10**26]
line_names = ['Bee Brain','Mouse Brain','Human Brain','100 Human Brains','Fortune 500 Company','All of Humanity']
#########################################
text_lines = map(math.log10, lines)   #[9,12,16,18,20.7827,26])

print(text_lines)
for line, text_line, line_name in zip(lines, text_lines, line_names):
    fig.add_hline(y=text_line, line_width=0, annotation_text=line_name, annotation_position="top right")
    fig.add_hline(y = line, line_width=1)


fig.update_layout(
        title_text="Computing Power (FLOP/s)", title_x=0.5, #title_y=0.93,
        #yaxis_range=[20,36.5],
        showlegend=False,
        yaxis_range=[8,27],
        yaxis = dict(showexponent = 'all',exponentformat = 'e',dtick=1),
        yaxis_title="FLOP/s",
        xaxis_title="System",
        #xaxis = dict(dtick=5),   font=dict(color="white")
        margin=dict(l=10, r=10) #, b = 10, t = 85), # right margin: 10px      
)
fig.update_xaxes(tickangle=-90)
# legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01),
#yaxis_range=[7.5,27],
#xaxis_range=[1989,2060]
#fig.update_xaxes(showgrid=True,ticks="inside") #,tickson="boundaries")
# template="plotly_white",
#fig.update_layout( yaxis = list(zeroline=False, showline=True, showgrid=True,ticks="inside") )


fig.show(config= dict(displayModeBar = False))

#plotly.offline.plot(fig, filename='file.html')
div_string = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

with open('text_files/'+text_name+'.txt', 'w+') as text_file:
    text_file.write(div_string)

