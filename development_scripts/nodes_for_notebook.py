import networkx as nx

from mpl_toolkits.basemap import Basemap
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('vpreston', 'tcx2wn8rfb')

from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.offline import plot
from plotly.graph_objs import Scatter
init_notebook_mode()


############### Imports above to be added to the beginning

m = Basemap()
def make_scatter(x,y):
    return Scatter(x=x,y=y,mode='lines',line=Line(color='black'),name=' ')

def polygons_to_traces(poly_paths, N_poly):
    ''' 
    pos arg 1. (poly_paths): paths to polygons
    pos arg 2. (N_poly): number of polygon to convert
    '''
    traces = []  # init. plotting list 

    for i_poly in range(N_poly):
        poly_path = poly_paths[i_poly]
        
        # get the Basemap coordinates of each segment
        coords_cc = np.array(
            [(vertex[0],vertex[1]) 
             for (vertex,code) in poly_path.iter_segments(simplify=False)]
        )
        
        # convert coordinates to lon/lat by 'inverting' the Basemap projection
        lon_cc, lat_cc = m(coords_cc[:,0],coords_cc[:,1], inverse=True)
        
        # add plot.ly plotting options
        traces.append(make_scatter(lon_cc,lat_cc))
     
    return traces

def get_coastline_traces():
    poly_paths = m.drawcoastlines().get_paths() # coastline polygon paths
    N_poly = 91  # use only the 91st biggest coastlines (i.e. no rivers)
    return polygons_to_traces(poly_paths, N_poly)

traces_cc = get_coastline_traces()


############################## FRAME ABOVE FOR MAP, FRAME BELOW FOR NODES

G=nx.from_pandas_dataframe(latLonPopulated_RT, source='tweetId',target='retweeter')

pos = {}
color = {}
for i,tweet in latLonPopulated_RT.iterrows():
    pos[tweet['tweetId'].upper()] = np.asarray([tweet['x'],tweet['y']])
    pos[tweet['retweeter'].upper()] = np.asarray([tweet['x'],tweet['y']])
    color[tweet['tweetId'].upper()] = tweet['node_color']
    color[tweet['retweeter'].upper()] = tweet['node_color']

for n,p in pos.iteritems():
    G.node[n]['pos'] = p

for n,c in color.iteritems():
    G.node[n]['color'] = c
    
pos = nx.get_node_attributes(G,'pos')

edge_trace = Scatter(
    x=[], 
    y=[], 
    line=Line(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

for edge in G.edges():
    x0, y0 = G.node[edge[0]]['pos']
    x1, y1 = G.node[edge[1]]['pos']
    edge_trace['x'] += [x0, x1, None]
    edge_trace['y'] += [y0, y1, None]

node_trace = Scatter(
    x=[], 
    y=[], 
    text=[],
    mode='markers', 
    hoverinfo='text',
    marker=Marker(
        color=[], 
        size=[],         
        line=dict(width=2)))

for node in G.nodes():
    x, y = G.node[node]['pos']
    node_trace['x'].append(x)
    node_trace['y'].append(y)
    c = G.node[node]['color']
    node_trace['marker']['color'].append(c)

for node, adjacencies in enumerate(G.adjacency_list()):
    node_trace['marker']['size'].append(len(adjacencies))
    node_info = '# of connections: '+str(len(adjacencies))
    node_trace['text'].append(node_info)

fig = Figure(data=Data([edge_trace, node_trace]+traces_cc),
             layout=Layout(
                title='<br>',
                titlefont=dict(size=16),
                showlegend=False, 
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=XAxis(range=[-180,180],showgrid=False, zeroline=False, showticklabels=False),
                yaxis=YAxis(range=[-75,75],showgrid=False, zeroline=False, showticklabels=False)))

iplot(fig)