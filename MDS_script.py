import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='jeanmidev', api_key='TFzWKIjCM5H2kCbGR8cc')

def classic_mds(matrice_distance,nbr_dim=2):
    # Wicklemaier
    # print(matrice_distance)
    nbr_elt=len(matrice_distance)
    # print(nbr_elt)
    P2=matrice_distance*matrice_distance
    print("P2:",P2)

    J=np.identity(nbr_elt)-(1.0/nbr_elt)*np.ones(nbr_elt)
    print("J:",J)
    B=-0.5*np.matrix(J)*np.matrix(P2)*np.matrix(J)
    print("B:",B)

    # B=[[5035.0625,-1553.0625,258.9375,-3740.938],[-1553.0625,507.8125,5.3125,1039.938],[258.9375,5.3125,2206.8125,-2471.062],[-3740.9375,1039.9375,-2471.0625,5172.062]]
    w, v = np.linalg.eig(B)

    w=(np.array(w)).real
    print("W:",w)
    print("V:",v)


    l_w=w.tolist()
    w_matrix=np.identity(nbr_dim)
    list_v=[]

    for i in range(nbr_dim):
        w_matrix[i,i]=np.sqrt(w[i])*w_matrix[i,i]
        list_tamp=[]
        for elt in v[:,i]:
            list_tamp.append(float(elt[0]))
        print(list_tamp)
        list_v.append(list_tamp)

    m_v = np.vstack(np.array(list_v)).T
    # print(list_v,w_matrix,m_v)
    #
    #
    print("m_v",m_v)
    print("w_matrix", w_matrix)
    #
    X=np.matrix(m_v)*np.matrix(w_matrix)
    print("X:",X)
    coord_list=[]
    for i in range(nbr_dim):
        coord=[]
        for j in range(nbr_elt):
            print(X[j,i])
            coord.append(X[j,i])
        coord_list.append(coord)

    projection_elt=[P2,J,B,w,v,nbr_dim,X,coord_list]

    return coord_list,projection_elt



list_tick=["cph","aar","ode","aal"]
distance_matrix=np.array([[0,93,82,133],[93,0,52,60],[82,52,0,111],[133,60,111,0]])

[coord_list,projection_elt]=classic_mds(distance_matrix,2)
trace2 = go.Scatter(
    x=coord_list[0],
    y=coord_list[1],
    mode='markers+text',
    name='Markers and Text',
    text=list_tick,
    textposition='bottom'
)

data = [trace2]
layout = go.Layout(
    showlegend=False
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='text-chart-basic')
print("END")
