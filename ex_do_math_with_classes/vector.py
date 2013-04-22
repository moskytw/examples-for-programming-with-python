#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cmp(V, U):
    from operator import sub

    subs = map(sub, V, U)

    if all(s == 0 for s in subs):
        # (1, 2, 3) = (1, 2, 3)
        return 0
    elif all(s <= 0 for s in subs):
        # (0, 1, 2) > (1, 2, 3)
        # (1, 2, 2) > (1, 2, 3)
        return -1
    elif all(s >= 0 for s in subs):
        # (1, 2, 4) > (1, 2, 3)
        # (2, 2, 4) > (1, 2, 3)
        return 1
    else:
        # (1, 2, 3) ? (3, 2, 1)
        # (1, 2, 3) ? (2, 1, 3)
        return None

def min(vectors):

    vectors = vectors[:]
    minimal_vectors = [vectors.pop(0)]

    while vectors:
        vector = vectors.pop(0)

        to_remove = []
        for i, minimal_vector in enumerate(minimal_vectors):
            c = cmp(vector, minimal_vector)
            if c is None:
                continue
            elif c == -1:
                to_remove.append(i)
                continue
            elif c == 0 or c == 1:
                break
        else:
            minimal_vectors.append(vector)

        for i in reversed(to_remove):
            minimal_vectors.pop(i)

    return minimal_vectors


