# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:41:20 2017

@author: 21992674
"""

# from PIL import Image, ImageDraw
from moviepy.editor import VideoClip
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips

traj = np.load('input_possibility_index55.npy')
gt = np.load('label_possibility_index55.npy')
pred_1 = np.load('predicted_possibility_index55_1.npy')
pred_2 = np.load('predicted_possibility_index55_2.npy')
pred_3 = np.load('predicted_possibility_index55_3.npy')


def make_frame(t):
    im_dir = im_dir = './frame/' + str(int(20 * t * 5) + 92360).zfill(6) + '.jpg'
    im = cv2.imread(im_dir)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    index = int(t * 5)
    if index > 0 and index < 20:
        for i in range(index):
            cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 5)
    if index < 20:
        for i in range(index + 1):
            cv2.circle(im, (traj[i][0], traj[i][1]), 5, (255, 255, 0), -1)
    return im


animation = VideoClip(make_frame, duration=4)
animation.write_videofile("index55_obs.mp4", fps=5)


def make_frame_pred(t):
    im_dir = im_dir = './frame/092740.jpg'
    im = cv2.imread(im_dir)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    index = int(t * 5)
    cv2.circle(im, (traj[-1][0], traj[-1][1]), 20, (255, 255, 0), 3)
    if index == 0:

        for i in range(19):
            cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 5)

    if index > 0 and index < 20:
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_1[0][0], pred_1[0][1]), (255, 0, 0), 5)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_2[0][0], pred_2[0][1]), (255, 0, 255), 5)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_3[0][0], pred_3[0][1]), (0, 255, 0), 5)
        for i in range(19):
            cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 5)
        for i in range(index):
            cv2.line(im, (pred_1[i][0], pred_1[i][1]), (pred_1[i + 1][0], pred_1[i + 1][1]), (255, 0, 0), 5)
            cv2.line(im, (pred_2[i][0], pred_2[i][1]), (pred_2[i + 1][0], pred_2[i + 1][1]), (255, 0, 255), 5)
            cv2.line(im, (pred_3[i][0], pred_3[i][1]), (pred_3[i + 1][0], pred_3[i + 1][1]), (0, 255, 0), 5)
    if index >= 20:
        cv2.putText(im, '63.7%', (int(pred_1[-1][0] - 50), int(pred_1[-1][1] + 50)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2,
                    (255, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(im, '35.2%', (int(pred_3[-1][0] - 50), int(pred_3[-1][1] + 50)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2,
                    (0, 255, 0), 5, cv2.LINE_AA)
        cv2.putText(im, '1.1%', (int(pred_2[-1][0] - 50), int(pred_2[-1][1] + 50)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2,
                    (255, 0, 255), 5, cv2.LINE_AA)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_1[0][0], pred_1[0][1]), (255, 0, 0), 5)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_2[0][0], pred_2[0][1]), (255, 0, 255), 5)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_3[0][0], pred_3[0][1]), (0, 255, 0), 5)
        for i in range(19):
            cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 5)
            cv2.line(im, (pred_1[i][0], pred_1[i][1]), (pred_1[i + 1][0], pred_1[i + 1][1]), (255, 0, 0), 5)
            cv2.line(im, (pred_2[i][0], pred_2[i][1]), (pred_2[i + 1][0], pred_2[i + 1][1]), (255, 0, 255), 5)
            cv2.line(im, (pred_3[i][0], pred_3[i][1]), (pred_3[i + 1][0], pred_3[i + 1][1]), (0, 255, 0), 5)
    return im


animation = VideoClip(make_frame_pred, duration=8)
animation.write_videofile("index55_pred_1.mp4", fps=5)


def make_frame_gt(t):
    im_dir = im_dir = './frame/' + str(int(20 * t * 5) + 92760).zfill(6) + '.jpg'
    im = cv2.imread(im_dir)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    index = int(t * 5)
    if index >= 0:
        for i in range(19):
            cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 5)
            cv2.line(im, (pred_1[i][0], pred_1[i][1]), (pred_1[i + 1][0], pred_1[i + 1][1]), (255, 0, 0), 5)
            cv2.line(im, (pred_2[i][0], pred_2[i][1]), (pred_2[i + 1][0], pred_2[i + 1][1]), (255, 0, 255), 5)
            cv2.line(im, (pred_3[i][0], pred_3[i][1]), (pred_3[i + 1][0], pred_3[i + 1][1]), (0, 255, 0), 5)
        cv2.putText(im, '63.7%', (int(pred_1[-1][0] - 50), int(pred_1[-1][1] + 50)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2,
                    (255, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(im, '35.2%', (int(pred_3[-1][0] - 50), int(pred_3[-1][1] + 50)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2,
                    (0, 255, 0), 5, cv2.LINE_AA)
        cv2.putText(im, '1.1%', (int(pred_2[-1][0] - 50), int(pred_2[-1][1] + 50)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2,
                    (255, 0, 255), 5, cv2.LINE_AA)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_1[0][0], pred_1[0][1]), (255, 0, 0), 5)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_2[0][0], pred_2[0][1]), (255, 0, 255), 5)
        cv2.line(im, (traj[-1][0], traj[-1][1]), (pred_3[0][0], pred_3[0][1]), (0, 255, 0), 5)
    if index > 0 and index < 20:
        for i in range(index):
            cv2.line(im, (gt[i][0], gt[i][1]), (gt[i + 1][0], gt[i + 1][1]), (0, 0, 255), 5)
    if index < 20:
        for i in range(index + 1):
            cv2.circle(im, (gt[i][0], gt[i][1]), 10, (0, 0, 255), -1)

    return im


animation = VideoClip(make_frame_gt, duration=4)
animation.write_videofile("index55_gt_1.mp4", fps=5)


def make_frame_show(t):
    im_dir = './frame/092740.jpg'
    im = cv2.imread(im_dir)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    index = int(t * 5)
    if index >= 0:
        cv2.circle(im, (traj[-1][0], traj[-1][1]), 20, (255, 255, 0), 3)
        for i in range(19):
            cv2.line(im, (traj[i][0], traj[i][1]), (traj[i + 1][0], traj[i + 1][1]), (255, 255, 0), 5)

    return im


animation = VideoClip(make_frame_show, duration=1)
animation.write_videofile("index55_show.mp4", fps=5)

clip1 = VideoFileClip("index55_obs.mp4")
clip2 = VideoFileClip("index55_pred_1.mp4")
clip3 = VideoFileClip("index55_gt_1.mp4")
# clip4 = VideoFileClip("index55_show.mp4")
final_clip = concatenate_videoclips([clip1, clip2, clip3])
final_clip.write_videofile("my_concatenation.mp4")
