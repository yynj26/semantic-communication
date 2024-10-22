#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#this is the trainning results of deepsc, loss 
"""
@File Name: results.py

@Author: Jiajia Shi

Created on: 2024/4/12, 11:04
"""

# loss results
train_loss = [4.42095, 3.74598, 3.28928, 2.65918, 2.06921, 1.67637, 1.42849, 1.24440, 1.11687, 0.99269,
              0.93491, 0.85935, 0.80852, 0.77177, 0.71194, 0.68143, 0.65423, 0.61855, 0.60471, 0.57409,
              0.55296, 0.53327, 0.52312, 0.51901, 0.49330, 0.48080, 0.46581, 0.46746, 0.44714, 0.44407,
              0.43555, 0.42590, 0.42171, 0.40715, 0.41988, 0.39752, 0.39037, 0.38676, 0.39129, 0.38539,
              0.37517, 0.36603, 0.37606, 0.35818, 0.35325, 0.35221, 0.34268, 0.34113, 0.32873, 0.32458,
              0.32673, 0.31929, 0.31148, 0.30243, 0.30033, 0.29852, 0.30667, 0.28899, 0.29268, 0.28214,
              0.28433, 0.28245, 0.27474, 0.27802, 0.27276, 0.26903, 0.27220, 0.25661, 0.25649, 0.26423,
              0.25596, 0.25270, 0.25623, 0.25272, 0.24136, 0.23954, 0.24077, 0.24210, 0.23407, 0.24708]
test_loss = [4.43327, 3.72949, 3.26438, 2.58950, 2.02210, 1.65472, 1.42051, 1.24318, 1.11452, 1.01267,
             0.93144, 0.86984, 0.81972, 0.76800, 0.72713, 0.68569, 0.65292, 0.62511, 0.59962, 0.57692,
             0.55690, 0.53849, 0.51842, 0.50764, 0.49113, 0.47608, 0.46553, 0.45389, 0.44329, 0.43496,
             0.42721, 0.41971, 0.41280, 0.40741, 0.40478, 0.39606, 0.38832, 0.38378, 0.37972, 0.37337,
             0.36676, 0.36316, 0.35857, 0.35252, 0.34806, 0.34329, 0.33651, 0.33297, 0.32825, 0.32376,
             0.31734, 0.31416, 0.30880, 0.30583, 0.30077, 0.29948, 0.29622, 0.29138, 0.28854, 0.28299,
             0.28089, 0.27707, 0.27292, 0.27138, 0.26886, 0.26236, 0.26140, 0.25968, 0.25660, 0.25443,
             0.25589, 0.25233, 0.24884, 0.24520, 0.24550, 0.24340, 0.23974, 0.23784, 0.23834, 0.23715]

gram1 = [0.38471956, 0.50054222, 0.63025207, 0.74736708, 0.83984717, 0.89913942, 0.92892137, 0.9414535, 0.94675899, 0.94896582, 0.94973044, 0.95076206, 0.95067025]
gram2 = [0.15595401, 0.27860229, 0.43545697, 0.60040317, 0.73756392, 0.83003255, 0.8762488, 0.89604524, 0.90409835, 0.90691842, 0.90866116, 0.90907963, 0.9099348]


# Print out the contents of pkl files on the screen
# import torch
# content = torch.load('./checkpoints/AWGN (1e-4)/checkpoint_80.pth')  # Specify the path of the pkl file
# print(content)

