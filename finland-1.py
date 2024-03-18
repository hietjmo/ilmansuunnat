import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.transforms import offset_copy
import matplotlib
import cartopy.crs as ccrs
import cartopy.feature as cf
import numpy as np
from matplotlib import rcParams
import matplotlib.font_manager as fm
from gridlines_with_labels import *

extent = [14, 35.55, 59, 70.2]
central_lon = np.mean (extent[:2])
central_lat = np.mean (extent[2:])

ppr = ccrs.Orthographic (central_lon, central_lat)

fig = plt.figure (figsize=(8, 8))
ax = plt.axes (projection=ppr)
ax.set_extent(extent)

ax.coastlines(resolution='50m')
#ax.add_feature(cf.OCEAN)
#ax.add_feature(cf.LAND, edgecolor='black', facecolor='none')
#ax.add_feature(cf.LAKES, edgecolor='black', facecolor='none')
# ax.add_feature(cf.RIVERS)
ax.add_feature(cf.BORDERS)
ax.gridlines(linestyle='--',linewidth=0.5, color='black', alpha=0.6)
# gridlines_with_labels(ax)


outpng = "finland-1.png"
plt.savefig(outpng, bbox_inches='tight')
print (f"Wrote {outpng}.")
