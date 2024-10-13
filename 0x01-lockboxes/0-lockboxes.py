#!/usr/bin/python3
"""
    A module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """
        Determines if all boxes in a list can be unlocked. It assumes the first
        box is already unlocked and uses its keys to unlock other boxes.
    """
    boxlen = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]) - {0}
    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if boxIdx and 0 <= boxIdx < boxlen:
            unseen_boxes |= set(boxes[boxIdx]) - seen_boxes
            seen_boxes.add(boxIdx)
    return len(seen_boxes) == boxlen
