#!/usr/bin/env python

from linked_list import Linked_List

class Queue:

    def __init__(self):
        self._lst= Linked_List()

    def enqueue(self, datum):
        self._lst.insert(datum)

    def dequeue(self):
        trace= self._lst.head
        while trace.pointer.pointer is not None:
            trace.head= trace.pointer
        result= trace.pointer.pointer
        trace.pointer= None
        return result

    def size(self):
        return self._lst.size()
