# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:13:05 2017

@author: 21992674
"""

from moviepy.editor import VideoClip
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips

rc_2_obs = np.load('./route_class_data/data_2.npy')
rc_4_obs = np.load('./route_class_data/data_4.npy')
rc_6_obs = np.load('./route_class_data/data_6.npy')
rc_2_label = np.load('./route_class_data/label_2.npy')
rc_4_label = np.load('./route_class_data/label_4.npy')
rc_6_label = np.load('./route_class_data/label_6.npy')

rc_2 = np.concatenate((rc_2_obs, rc_2_label), axis=1)
rc_4 = np.concatenate((rc_4_obs, rc_4_label), axis=1)
rc_6 = np.concatenate((rc_6_obs, rc_6_label), axis=1)


def make_frame_rc(t):
    im_dir = im_dir = './frame/092740.jpg'
    im = cv2.imread(im_dir)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    index = int(t * 5)
    if index < 40:
        for j in range(len(rc_6[0: 100])):
            traj = rc_6[j]
            for i in range(index):
                cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 2)

    if index >= 40:
        for j in range(len(rc_6[0: 100])):
            traj = rc_6[j]
            for i in range(39):
                cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 2)

    return im


animation = VideoClip(make_frame_rc, duration=5)
animation.write_videofile("NYGC_rc_6_demo.mp4", fps=10)

clip1 = VideoFileClip("NYGC_rc_2_demo.mp4")
clip2 = VideoFileClip("NYGC_rc_4_demo.mp4")
clip3 = VideoFileClip("NYGC_rc_6_demo.mp4")
final_clip = concatenate_videoclips([clip1, clip2, clip3])
final_clip.write_videofile("NYGC_rc.mp4")

clip1 = VideoFileClip("NYGC_background.avi").subclip(0, 5)
clip2 = VideoFileClip("NYGC_rc.mp4")
clip3 = VideoFileClip("NYGC_pred.mp4")
final_clip = concatenate_videoclips([clip1, clip2, clip3])
final_clip.write_videofile("NYGC_demo.mp4")
