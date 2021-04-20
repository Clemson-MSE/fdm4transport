def animate3d(C,frames=100,interval=50):
  """Creates an animation of a time series of scalar values on a 2D grid.
     The scalar field is plotted as a surface mesh."""
  step = len(C)//frames
  C = np.vstack([C[0],C[1::step]])

  def init():
    surf = ax.plot_surface(x,y,C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
    time_text.set_text('t={0:.4f} s'.format(0))
    return (surf,time_text)

  def animate(i):
    #ax.collections.clear()
    surf = ax.plot_surface(x,y,C[i].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
    time_text.set_text('t={0:.4f} s'.format(i*dt*step))
    return (surf,time_text)

  cmax = 1
  cmin = center_concentration(n,phi)

  fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
  surf = ax.plot_surface(x,y,C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
  time_text = ax.text2D(0.8, 0.9, 't=0 s', transform=ax.transAxes, fontsize=12)
  fig.colorbar(surf)
  ax.axes.set_zlim3d(bottom=cmin, top=1)
  ax.set_title('Concentration Profile')
  ax.set_xlabel('x')
  ax.set_ylabel('y')

  ani = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=len(C), interval=interval, blit=True)
  plt.close()
  return ani

def animate2d(C,frames=100,interval=50):
    """Creates an animation of a time series of scalar values on a 2D grid.
       The scalar field is plotted as a heatmap."""
    step = len(C)//frames
    C = np.vstack([C[0],C[1::step]])

    def init():
      surf = ax.imshow(C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
      time_text.set_text('t={0:.4f} s'.format(0))
      return (surf,time_text)

    def animate(i):
      surf = ax.imshow(C[i].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
      time_text.set_text('t={0:.4f} s'.format(i*dt*step))
      return (surf,time_text)

    cmax = 1
    cmin = center_concentration(n,phi)

    fig, ax = plt.subplots()
    surf = ax.imshow(C[0].reshape(n,n),cmap=cm.coolwarm,vmin=cmin,vmax=cmax)
    time_text = ax.text(0.6, 0.9, 't=0 s', transform=ax.transAxes, color='w', fontsize=14)
    fig.colorbar(surf)
    ax.set_title('Concentration Profile')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ani = animation.FuncAnimation(fig, animate, init_func=init,
                                  frames=len(C), interval=interval, blit=True)
    plt.close()
    return ani
