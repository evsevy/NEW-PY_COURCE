"""
This script produces a video analysis proving for the first time in history
that bacterial populations grow exponentially. See the result here:
http://i.imgur.com/uoITKiA.gif
We proceed as follows:
- Download a video of bacteria growing under a microscope.
- Cut the video to keep only the first 7 seconds.
- Threshold each frame to find where the bacteria are, and compute the
  total number of pixels that they occupy
- Make an animated plot of the number of pixels occupied versus time
- Assemble the original video, the thresholded version, and the plot,
  and write everything to a file.
I don't know the source of the original video so I can't give credits,
sorry guys !
"""

import numpy as np
import matplotlib.pyplot as plt
from moviepy.video.io.bindings import mplfig_to_npimage
from moviepy.editor import VideoFileClip, VideoClip, clips_array

# DOWLOAD THE VIDEO Requires Youtube-dl installed.

import os
os.system("youtube-dl gEwzDydciWc -o growth.mp4") # requires Youtube-dl

# LOAD THE VIDEO, SELECT THE EXCERPT BETWEEN t=0-7 seconds

video = VideoFileClip("growth.mp4",  audio=False).subclip(0,7)


# THRESHOLD THE FRAMES TO GET THE POPULATION AREA
# We normalize each frame by the luminosity of its upper left corner
# to correct for the changing luminosity of the video

thresholder = lambda im: ( 1.0*im[:,:,1]/np.mean(im[:50,:50]) ) < 0.8
thresholded = video.fl_image(thresholder)
thresholded_RGB = thresholded.set_ismask(True).to_RGB() # RGB Version for movie

areas = [(t,frame.sum())
           for (t,frame) in thresholded.iter_frames(with_times=True)]


# ESTIMATE THE GROWTH RATE

tt, aa = [np.array(e) for e in zip(*areas)] # times and areas
gr_rate, a0 = np.polyfit(tt, np.log(aa),1)


# PLOT THE FIGURE

fig, ax = plt.subplots(1, figsize=(3,2.5), facecolor=(1,1,1))
ax.plot(tt, np.exp(a0+gr_rate*tt), lw=2, ls='--', c='k', label = r"$Ae^{rt}$")
l, = ax.plot(tt, aa, lw=3, c='r')
ax.set_ylabel("Pop. surface (pixels)")
ax.set_xlabel("time (unit unknown)")
ax.legend(loc=2)
fig.tight_layout() # <- I love this function :D


# ANIMATE THE FIGURE WITH MOVIEPY

def plot_until_t(t):
    tt, aa = zip(*[(t_,v) for (t_,v) in areas if t_<=t])
    l.set_xdata(tt)
    l.set_ydata(aa)
    return mplfig_to_npimage(fig)

plotclip = VideoClip(plot_until_t, duration=video.duration)


# ASSEMBLE ALL THE CLIPS, WRITE TO A FILE

final_clip = clips_array([[clip.margin(2, color=[255,255,255]) for clip in
                [video.resize(.6), thresholded_RGB.resize(.6), plotclip]]],
                bg_color=[255,255,255])


final_clip.write_videofile('growth2.mp4', fps=15)
#final_clip.write_gif('growth.gif', fps=15, opt="OptimizeTransparency", fuzz=10)
