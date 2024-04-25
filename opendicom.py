# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 05:23:08 2019

@author: JOHNJAIRO
"""

import numpy as np
import cv2
import pydicom as dicom

ds=dicom.dcmread('E:\dicom dentista\paciente zero\Tomografia\pollyanna, florcena 11_20_2015polianaface0571.dcm')
dcm_sample=ds.pixel_array*18
print(type(dcm_sample))
cv2.imshow('sample image dicom',dcm_sample)

cv2.waitKey()