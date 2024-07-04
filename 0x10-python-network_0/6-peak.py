#!/usr/bin/python3
"""Module for finding a peak in a list of integers."""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def binary_search_peak(arr, left, right):
        mid = (left + right) // 2

        # Check if mid is a peak element
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]

        # If the left neighbor is greater, then there must be a peak on the left side
        if mid > 0 and arr[mid - 1] > arr[mid]:
            return binary_search_peak(arr, left, mid - 1)

        # If the right neighbor is greater, then there must be a peak on the right side
        return binary_search_peak(arr, mid + 1, right)

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)

