import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import time

plt.ion()

#filepath_resistance = r"D:\Data\2022\11 Nov\15 Tue\1521_BaMn2As2_CurrentTest_pm60mA.txt"
# filefolder = r"D:\Data\2022\11 Nov\15 Tue\1642_calibration"
filefolder = r"C:\Users\tomikawa1\Box\3Kotai\experiment\BaMn2As2\IR_Camera\15 Tue\1642_calibration"
filepaths = [x for x in Path(filefolder).iterdir() if x.is_file()]

#t, I, V, T = np.loadtxt(filepath_resistance).T

plts = plt.subplots(4,6, figsize=(10,5.5))[1].reshape(-1)

img0 = mpimg.imread(filepaths[-1])/255 * 100

for i,filepath in enumerate(filepaths[::1]):
    img = mpimg.imread(filepath)/255 *100 # The range is 0 to 100C
    # img -= img0
    
    # filename = filepath.split('/')[-1]
    filename = filepath.name
    #filetime = time.mktime(time.strptime(filename[:-4], '%Y%m%d_%H%M%S'))
    # Find the datapoint whose time t matches with filetime
    #filecurrent = I[np.argmin(np.abs(t-filetime))]

    # plts[i].imshow(img, cmap=plt.cm.magma, clim=(90,100))
    imshowed = plts[i].imshow(img, cmap=plt.cm.magma, clim=(10,100))
    plts[i].axis('off')
    #plts[i].text(.02, .95, r'$%+.2g\,$mA'%(filecurrent*1e3),
   #              va='top',
                # transform=plts[i].transAxes, color='w')# if i < 18 else 'k')
plt.colorbar(imshowed, label= 'Temperature (C)')

plt.tight_layout()
plt.savefig('Calibration_PlottedImages.png', dpi=300)