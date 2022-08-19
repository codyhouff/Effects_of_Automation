import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math

excel_link = 'C:/Users/00MrK/Desktop/graduate_school_stuff/Georgia_Institute_of_Technology/Research/Effects_of_Automation/computer_progress/speed_of_computers.xlsx'
text_name = 'AI_progress_summary_training'

#df = pd.read_excel(excel_link, sheet_name='AI Systems Clean 2', usecols="A,B,C,G,H,J,M,N,O,P",nrows=252) #252
#print(df)
df2 = pd.read_excel(excel_link, sheet_name='AI Systems Clean 2', usecols="A,B,C,G,H,M,N,O,P,Z", nrows=259) #259
#print(df2)
##########################################

#max_parameters = df2[df2.groupby(['Domain'])['Parameters'].transform(max) == df2['Parameters']].drop_duplicates(subset='Parameters', keep="first").sort_values('Parameters', ascending=True)
max_training = df2[df2.groupby(['Domain'])['Training compute (FLOPs)'].transform(max) == df2['Training compute (FLOPs)']].drop_duplicates(subset='Training compute (FLOPs)', keep="first").sort_values('Training compute (FLOPs)', ascending=False)
#print(max_parameters.to_string())
print(max_training.to_string())

##########################################
#fig = px.bar(max_parameters, x="bar_graph_x1", y="Parameters", log_y=True, text="Domain", color = "Domain") # barmode="overlay"   category_orders = [])
fig = px.bar(max_training, x="Domain", y="Training compute (FLOPs)", log_y=True, hover_name="System", color = "Domain") #log_y=True, #text="Domain", 
#fig.show()
#########################################
#lines = [10**12,125*10**12,100*125*10**12,60629*125*10**12,10**10*125*10**12]
#lines = [10**24,10**26,10**29,10^30,10^31,10^34,10^36]
#line_names = ['mouse synapses','human synapses','100 humans synapses','company synapses','humanity synapses']
#########################################
lines = [7.88*10**24,10**26,3*10**29,3*10**30,3*10**31,10**34,10**36]
#lines = [10**24,10**26,10**29,10^30,10^31,10^34,10^36]
line_names = ['Human 25y','Lifetime Anchor','Short Horizon','Genome Anchor','Medium Horizon','Long Horizon','Evolution Anchor']
#########################################
text_lines = map(math.log10, lines)   #[9,12,16,18,20.7827,26])

print(text_lines)
for line, text_line, line_name in zip(lines, text_lines, line_names):
    fig.add_hline(y=text_line, line_width=0, annotation_text=line_name, annotation_position="top right")
    fig.add_hline(y = line, line_width=1)


fig.update_layout(
        title_text="Training Completed (FLOPs)", title_x=0.5, #  title_y=0.93, #{'text': 'AI Systems - Training Completed (FLOPs)','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},
        #yaxis_title="FLOPs",
        showlegend=False,
        yaxis_range=[20,37],
        #yaxis_range=[4.5,25],
        yaxis = dict(showexponent = 'all',exponentformat = 'e',dtick=1),
        yaxis_title="FLOPs",
        xaxis_title="Domain",
        #xaxis = dict(dtick=5),
        margin=dict(l=10, r=10), #b = 10, t = 85), # right margin: 10px      
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
