#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

def calculate_sum(arr, center):
    summation = 0
    (row, col) = center
    summation += arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1]
    summation += arr[row][col]
    summation += arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]

    return summation

def find_max_sum(arr):
    maxsum = 0
    coordinates = [(x,y) for x in range(1,5) for y in range(1,5)]
    for coordinate in coordinates:
        hgsum = calculate_sum(arr, coordinate)
        if hgsum > maxsum:
            maxsum = hgsum
    print maxsum

find_max_sum(arr)