import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, animation

def animate3d(C,dt,phi,frames=100,interval=50,cmin=0,cmax=1):
  """Creates an animation of a time series of scalar values on a 2D grid.
     The scalar field is plotted as a surface mesh."""
  step = len(C)//frames
  C = np.vstack([C[0],C[1::step]])

  n = int(np.sqrt(len(C[0])))
  (x,y) = np.meshgrid(range(n),range(n))

  def init():
    surf = ax.plot_surface(x,y,C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
    time_text.set_text('t={0:.4f} s'.format(0))
    return (surf,time_text)

  def animate(i):
    #ax.collections.clear()
    surf = ax.plot_surface(x,y,C[i].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
    time_text.set_text('t={0:.4f} s'.format(i*dt*step))
    return (surf,time_text)

  fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
  surf = ax.plot_surface(x,y,C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
  time_text = ax.text2D(0.7, 0.9, 't=0 s', transform=ax.transAxes, fontsize=12)
  phi_text = ax.text2D(0.1, 0.9, r'$\phi=$%.2f'%phi, transform=ax.transAxes, fontsize=12)
  fig.colorbar(surf, label=r'$C/C_0$')
  ax.axes.set_zlim3d(bottom=cmin, top=1)
  ax.set_title('Concentration Profile')
  ax.set_xlabel('x')
  ax.set_ylabel('y')

  ani = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=len(C), interval=interval, blit=True)
  plt.close()
  return ani

def animate2d(C,dt,phi,cmin=1,cmax=1,frames=100,interval=50):
    """Creates an animation of a time series of scalar values on a 2D grid.
       The scalar field is plotted as a heatmap."""
    step = len(C)//frames
    C = np.vstack([C[0],C[1::step]])

    n = int(np.sqrt(len(C[0])))
    
    def init():
      surf = ax.imshow(C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
      time_text.set_text('t={0:.4f} s'.format(0))
      return (surf,time_text)

    def animate(i):
      surf = ax.imshow(C[i].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
      time_text.set_text('t={0:.4f} s'.format(i*dt*step))
      return (surf,time_text)

    fig, ax = plt.subplots()
    surf = ax.imshow(C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
    time_text = ax.text(0.6, 0.9, 't=0 s', transform=ax.transAxes, color='w', fontsize=14)
    phi_text = ax.text(0.05, 0.9, r'$\phi=$%.2f'%phi, transform=ax.transAxes, color='w', fontsize=14)
    fig.colorbar(surf, label=r'$C/C_0$')
    ax.set_title('Concentration Profile')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ani = animation.FuncAnimation(fig, animate, init_func=init,
                                  frames=len(C), interval=interval, blit=True)
    plt.close()
    return ani
