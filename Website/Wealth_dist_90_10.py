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
        y = a*x+b
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
        y = a*x+b
        x_array +=[x]
        y_array +=[y]
  
    return x_array, y_array


excel_link = 'C:/Users/00MrK/Desktop/graduate_school_stuff/Georgia_Institute_of_Technology/Research/Effects_of_Automation/Wealth_and_employment/Wealth_data.xlsx'
text_name = 'wealth_dist_90_10'

df = pd.read_excel(excel_link, sheet_name='Wealth_dist_percent_graph', usecols="A,B,C,D,E,F,G,H,I", nrows=128)

#df2 = pd.read_excel(excel_link, sheet_name='GPU_Data_Vintage_Graph_Clean', usecols="A,B,C,D,I", nrows=261)
print(df)
#print(df[:52])
##########################################
fig1 = px.scatter(df, x='Year Count', y=['Top 10%'],color_discrete_sequence=['rgb(99, 110, 250)'], trendline="ols")

future_x, future_y = future_trend(fig1, df['Year Count'].iloc[-1], 2060)
fig1f1 = px.scatter(x=future_x, y=future_y, trendline="ols", color_discrete_sequence=['rgb(99, 110, 250)'])
fig1f1.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})

'''
newnames = {'Top 1 (FLOP/s)':'#1 Supercomputer'}
fig1.for_each_trace(lambda t: t.update(name = newnames[t.name],legendgroup = newnames[t.name],hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))

future_x, future_y = future_trend(fig1,df['Year'].iloc[-1],2040)
fig1f1 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(99, 110, 250)'])
fig1f1.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})

future_x, future_y = future_trend_cust(0.0830523,-149.6,2023,2060)
fig1f2 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(99, 110, 250)'])
fig1f2.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})

future_x, future_y = future_trend_cust(0.0830523,-147.35,2036,2060)
fig1f3 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(99, 110, 250)'])
fig1f3.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})
#fig.update_traces(patch={"line": {"dash": 'dot'}})
'''
##########################################
fig2a = px.scatter(df, x='Year Count', y=['Everyone else 90%'], color_discrete_sequence=['rgb(239, 85, 59)'], trendline="ols")

future_x, future_y = future_trend(fig2a, df['Year Count'].iloc[-1], 2060)
fig2f1 = px.scatter(x=future_x, y=future_y, trendline="ols", color_discrete_sequence=['rgb(239, 85, 59)'])
fig2f1.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})
'''
fig2b = px.scatter(df[52::], x='Year', y=['Top 500 (FLOP/s)'], log_y=True, trendline="ols", trendline_options=dict(log_y=True), hover_name='Top 500 model', color_discrete_sequence=['rgb(239, 85, 59)'])

newnames = {'Top 500 (FLOP/s)':'#500 Supercomputer'}
fig2a.for_each_trace(lambda t: t.update(name = newnames[t.name],legendgroup = newnames[t.name],hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))
fig2b.for_each_trace(lambda t: t.update(name = newnames[t.name],legendgroup = newnames[t.name],hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))


future_x, future_y = future_trend(fig2a,df[:52]['Year'].iloc[-1],2025)
fig2f1 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(239, 85, 59)'])
fig2f1.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})

future_x, future_y = future_trend(fig2b,df[52::]['Year'].iloc[-1],2060)
fig2f2 = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(239, 85, 59)'])
fig2f2.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})
'''
##########################################
'''
fig3a = px.scatter(df2[:120], x='Year', y=['FLOP/s per $1000 GPU (2021)'], log_y=True, trendline="ols", trendline_options=dict(log_y=True), hover_name="model",color_discrete_sequence=['rgb(0, 204, 150)'])
fig3b = px.scatter(df2[120::], x='Year', y=['FLOP/s per $1000 GPU (2021)'], log_y=True, trendline="ols", trendline_options=dict(log_y=True), hover_name="model",color_discrete_sequence=['rgb(0, 204, 150)'])

newnames = {'FLOP/s per $1000 GPU (2021)':'$1000 GPU'}
fig3a.for_each_trace(lambda t: t.update(name = newnames[t.name],legendgroup = newnames[t.name],hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))
fig3b.for_each_trace(lambda t: t.update(name = newnames[t.name],legendgroup = newnames[t.name],hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))

   
future_x, future_y = future_trend(fig3b,df2['Year'].iloc[-1],2060)
fig3f = px.scatter(x=future_x, y=future_y, log_y=True, trendline="ols", trendline_options=dict(log_y=True), color_discrete_sequence=['rgb(0, 204, 150)'])
fig3f.update_traces(marker_size=.01, patch={"line": {"dash": 'dot'}})
'''
##########################################
#fig.update_traces(cliponaxis=False, selector=dict(type='scatter'))
#fig.add_scatter(x=df.Year_Count, y=df.Top_500, mode = 'markers')
#fig3a.add_scatter(x=[2022,2023,2025,2026], y=[10**19,10**20,10**23,10**22])

#fig3.add_scatter(x=df.Year_Count, y=df.Top_500, mode = 'markers')
#fig4 = px.scatter(x=[2022,2023,2025,2026], y=[10**19,10**20,10**23,10**22], log_y=True, trendline="ols", trendline_options=dict(log_y=True))


#fig = go.Figure(data = fig1.data + fig1f1.data + fig1f2.data + fig1f3.data + fig2a.data + fig2b.data + fig2f1.data + fig2f2.data + fig3a.data + fig3b.data + fig3f.data)
fig = go.Figure(data = fig1.data + fig1f1.data + fig2a.data + fig2f1.data)
#fig.update_yaxes(type="log")

'''
lines = [10**9,10**12,10**16,10**18,60629*10**16,10**26]
line_names = ['Bee Brain','Mouse Brain','Human Brain','100 Human Brains','Fortune 500 Company','All of Humanity']
text_lines = map(math.log10, lines)   #[9,12,16,18,20.7827,26])

for line, text_line, line_name in zip(lines, text_lines, line_names):
    fig.add_hline(y=text_line, line_width=0, annotation_text=line_name, annotation_position="top right")
    fig.add_hline(y = line, line_width=1)
'''

fig.update_layout(
        title = {'text': 'Wealth Distribution: Top 10% vs 90%','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},
        yaxis_title="Wealth Percent",
        #yaxis = dict(showexponent = 'all',exponentformat = 'e',dtick=1),
        yaxis_range=[0,100],
        xaxis_title="Year",
        xaxis = dict(dtick=5),
        #legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01),
        xaxis_range=[1989,2060]
)

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
