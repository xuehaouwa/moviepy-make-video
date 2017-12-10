# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:46:26 2017

@author: 21992674
"""

from moviepy.editor import VideoClip
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
from scipy.spatial import distance
from sklearn.cluster import DBSCAN
from sklearn import metrics

def file2matrix(filename):
    data = np.loadtxt(filename, dtype=int)
    data = np.reshape(data, [-1, 3])
    return data

def get_coord_from_txt(filename, ped_ID):
    data = file2matrix(filename)
    coord = []
    for i in range(len(data)):
        coord.append([ped_ID, data[i][-1], data[i][0], data[i][1]])
    coord = np.reshape(coord, [-1, 4])
    return coord

def select_trajectory(data, frame_num):
    if len(data) >= frame_num:
        return True
    else:
        return False

def get_all_trajectory(total_pedestrian_num):
    
    data = []
    
    for i in range(total_pedestrian_num):
        filename = './Annotation/' + str(i+1).zfill(6) + '.txt'
        ped_ID = i+1
        data.append(get_coord_from_txt(filename, ped_ID))
        
    return data
#clip1 = VideoFileClip("NYGC_background.avi").subclip(0, 5)
#
#clip1.write_videofile("background.mp4")


data_NYGC = get_all_trajectory(12684)

frame_0_list = []
for i in range(len(data_NYGC)):
    if data_NYGC[i][0][1] == 0:
        frame_0_list.append(data_NYGC[i])


#def draw_line(traj, im, length):
#    for i in range(length):
#        cv2.line(im, (traj[i][0], traj[i][1]), (traj[i+1][0], traj[i+1][1]), (255,255,0), 5)
#    
#def search_ped(frame_ID, data):
#    
#    ped = []
#    for i in range(len(data)):
#        if frame_ID == data[i][1]:
#            ped.append([data[i][-2], data[i][-1]])
#    
#    return ped
#
#def frame_ped_list(start_frame, end_frame, data):
#    
#    frame_list_length = end_frame - start_frame
#    
#    frame_ped = []
#    
#    for i in range(frame_list_length):
#        frame_ped.append(search_ped(i+start_frame), data)
#        
#    return frame_ped
#
def make_frame_intro(t):
    im_dir = './frame/' + str(int(20*t*8)).zfill(6) + '.jpg'
    im = cv2.imread(im_dir)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    index = int(t*8)
    
    if index > 0:
        for i in range(len(data_NYGC)):
            if data_NYGC[i][0][1] == int(20*t*8):
                frame_0_list.append(data_NYGC[i])
            
    
    for ped in range(len(frame_0_list)):
        ped_temp = frame_0_list[ped]
        
        if index < len(ped_temp):
            for i in range(index+1):
                cv2.circle(im, (ped_temp[i][2], ped_temp[i][3]), 5, (255,255,0), -1)
                
            for i in range(index):
                cv2.line(im, (ped_temp[i][2], ped_temp[i][3]), (ped_temp[i+1][2], ped_temp[i+1][3]), (255,255,0), 5)
    
    
#    if index >= 0:
#        for i in range(len(data[0:1000])):
#            draw_line(data[i], im, 39)

    return im
#
animation = VideoClip(make_frame_intro, duration=8)
animation.write_videofile("new_intro.mp4", fps=8)
##
#
#clip1 = VideoFileClip("background.mp4")
#clip2 = VideoFileClip("intro.mp4")
#final_clip = concatenate_videoclips([clip1,clip2])
#final_clip.write_videofile("NYGC_intro.mp4")

