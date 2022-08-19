import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math

def future_trend_cust(a,b,x1,x2):
    x1 = math.ceil(x1)

    x_array = []
    y_array = []
    for x in range(x1,x2+1):
        y = 10**(a*x+b)
        x_array +=[x]
        y_array +=[y]
  
    return x_array, y_array

def future_trend(fig,x1,x2):
    x1 = math.ceil(x1)
    eq = px.get_trendline_results(fig).iloc[0]["px_fit_results"]
    b = eq.params[0]
    a = eq.params[1]

    x_array = []
    y_array = []
    for x in range(x1,x2+1):
        y = 10**(a*x+b)
        x_array +=[x]
        y_array +=[y]
  
    return x_array, y_array



excel_link = 'C:/Users/00MrK/Desktop/graduate_school_stuff/Georgia_Institute_of_Technology/Research/Effects_of_Automation/computer_progress/speed_of_computers.xlsx'
text_name = 'AI_systems_parameters'

df = pd.read_excel(excel_link, sheet_name='AI Systems Clean 2', usecols="A,B,C,G,H,J,M,N,O,P",nrows=259) #252
#print(df)
#df2 = pd.read_excel(excel_link, sheet_name='AI Systems Clean 2', usecols="A,B,C,D,I", nrows=261)
#print(df)
#print(df[:52])

##########################################
fig1 = px.scatter(df, x='Year', y=['Parameters'], log_y=True, hover_name='System', color = 'Domain')

#future_x, future_y = future_trend(fig1,df['Year'].iloc[-1],2040)
#fig1f1 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(99, 110, 250)'])
#fig1f1.update_traces(marker_size=.01)
'''
future_x, future_y = future_trend_cust(0.0830523,-149.6,2023,2060)
fig1f2 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(99, 110, 250)'])
fig1f2.update_traces(marker_size=.01)

future_x, future_y = future_trend_cust(0.0830523,-147.35,2036,2060)
fig1f3 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(99, 110, 250)'])
fig1f3.update_traces(marker_size=.01)
'''
##########################################
'''
fig2a = px.scatter(df[:52], x='Year', y=['Top 500 (FLOP/s)'], log_y=True, trendline="ols", trendline_options=dict(log_y=True), hover_name='Top 500 model', color_discrete_sequence=['rgb(239, 85, 59)'])
fig2b = px.scatter(df[52::], x='Year', y=['Top 500 (FLOP/s)'], log_y=True, trendline="ols", trendline_options=dict(log_y=True), hover_name='Top 500 model', color_discrete_sequence=['rgb(239, 85, 59)'])

future_x, future_y = future_trend(fig2a,df[:52]['Year'].iloc[-1],2025)
fig2f1 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(239, 85, 59)'])
fig2f1.update_traces(marker_size=.01)

future_x, future_y = future_trend(fig2b,df[52::]['Year'].iloc[-1],2060)
fig2f2 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(239, 85, 59)'])
fig2f2.update_traces(marker_size=.01)
'''
##########################################

##########################################
#fig.update_traces(cliponaxis=False, selector=dict(type='scatter'))
#fig.add_scatter(x=df.Year_Count, y=df.Top_500, mode = 'markers')
#fig3a.add_scatter(x=[2022,2023,2025,2026], y=[10**19,10**20,10**23,10**22])

#fig3.add_scatter(x=df.Year_Count, y=df.Top_500, mode = 'markers')
#fig4 = px.scatter(x=[2022,2023,2025,2026], y=[10**19,10**20,10**23,10**22], log_y=True, trendline="ols", trendline_options=dict(log_y=True))


fig = go.Figure(data = fig1.data)
fig.update_yaxes(type="log")


lines = [10**12,125*10**12,100*125*10**12,60629*125*10**12,10**10*125*10**12]
#lines = [10**24,10**26,10**29,10^30,10^31,10^34,10^36]
line_names = ['Mouse Synapses','Human Synapses','100 Human Synapses','Company Synapses','Humanity Synapses']
text_lines = map(math.log10, lines)   #[9,12,16,18,20.7827,26])

for line, text_line, line_name in zip(lines, text_lines, line_names):
    fig.add_hline(y=text_line, line_width=0, annotation_text=line_name, annotation_position="top right")
    fig.add_hline(y = line, line_width=1)


fig.update_layout(
        title = {'text': 'AI Systems - Number of Parameters','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},
        yaxis_title="Parameters",
        yaxis = dict(showexponent = 'all',exponentformat = 'e',dtick=1),
        xaxis_title="Year",
        xaxis = dict(dtick=5),
        
)
# legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01),
#yaxis_range=[7.5,27],
#xaxis_range=[1989,2060]
#fig.update_xaxes(showgrid=True,ticks="inside") #,tickson="boundaries")
# template="plotly_white",
#fig.update_layout( yaxis = list(zeroline=False, showline=True, showgrid=True,ticks="inside") )


fig.show()

#plotly.offline.plot(fig, filename='file.html')
div_string = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

with open('text_files/'+text_name+'.txt', 'w+') as text_file:
    text_file.write(div_string)


'''
legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=.8
),

    yaxis2 = dict(
        overlaying="y",
        side="right",
        ticktext=line_names,
        tickvals=lines,
        tickmode="array"
'''
