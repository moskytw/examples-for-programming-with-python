#!/usr/bin/env python
# -*- coding: utf-8 -*-

import enhancedyaml
import vector

def roots_of_n_poly_eq(n, x, var_upper_bounds=tuple()):
    '''find the all possible non-negative interger roots of a `n`-term polynomial equals `x`.'''

    countdown = lambda: xrange(x if not var_upper_bounds else var_upper_bounds[0], -1, -1)

    if n <= 0:
        return []
    elif n == 1:
        return map(lambda i: [i], countdown())
    elif n == 2:
        return map(lambda i: [i, x-i], countdown())
    else:
        roots = []
        for i in countdown():
            for root in roots_of_n_poly_eq(n-1, x-i, var_upper_bounds[1:]):
                roots.append([i] + root)
        return roots

class Arc(enhancedyaml.YAMLObject):

    @property
    def max_cap(self):
        '''as the `C` in paper'''
        if not hasattr(self, '_max_cap'):
            self._max_cap = max(self.caps)
        return self._max_cap

    def calc_flow(self, commdity_idx, demand):
        return self.consumed_caps[commdity_idx] * demand

    def __repr__(self):

        if hasattr(self, 'anchor'):
            return '<Arc &%s>' % self.anchor
        else:
            return repr(self)

class Network(enhancedyaml.YAMLObject):

    def is_through(self, path_idx, arc):
        '''return Is the path through this arc?'''

        if not hasattr(self, '_through_table'):

            for arc_idx, arc in enumerate(self.arcs):
                arc.network = self
                arc.idx = arc_idx

            self._through_table = []
            for path_idx, path in enumerate(self.paths):
                self._through_table.append([False] * (arc_idx+1))
                for arc in path:
                    self._through_table[path_idx][arc.idx] = True

        return self._through_table[path_idx][arc.idx]

    def calc_flow(self, arc, current_commodties_demands):
        '''the flow of the paths of an arc with specific demand case'''

        consumed_cap = .0
        for commdity_idx, demands in enumerate(current_commodties_demands):
            for path_idx, demand in enumerate(demands):
                if self.is_through(path_idx, arc):
                    consumed_cap += arc.calc_flow(commdity_idx, demand)

        from math import ceil

        return int(ceil(consumed_cap))

    def gen_feasible_flow_vectors(self):
        '''return feasible flow vectors (`Fs`) by enumerating all demand cases'''

        from itertools import product

        parts_of_possible_flow_vectors = {}
        for x in self.max_demands:
            if x not in parts_of_possible_flow_vectors:
                parts_of_possible_flow_vectors[x] = roots_of_n_poly_eq(len(self.paths), x)

        for i, possible_flow_vector in enumerate(product(*[parts_of_possible_flow_vectors[x] for x in self.max_demands])):

            if any(self.calc_flow(arc, possible_flow_vector) > arc.max_cap for arc in self.arcs):
                continue

            yield possible_flow_vector

    def trans_to_cap_vector(self, flow_vectors):
        '''translate the flow vectors (`Fs`) into capacity vector (`Xs`)'''

        cap_vectors = []
        for flow_vector in flow_vectors:
            cap_vector = tuple(self.calc_flow(arc, flow_vector) for arc in self.arcs)
            if cap_vector not in cap_vectors:
                cap_vectors.append(cap_vector)

        return cap_vectors

    def calc_minimal_cap_vectors(self):
        '''merge serval steps into this method'''

        feasible_flow_vectors = self.gen_feasible_flow_vectors()
        cap_vectors = self.trans_to_cap_vector(feasible_flow_vectors)

        return vector.min(cap_vectors)

if __name__ == '__main__':

    locals().update(enhancedyaml.load(open('data.yaml')))

    from pprint import pprint

    print '# Example 1'
    print
    print '## paths'
    print
    pprint(example1.paths)
    print
    print '## feasible flow vectors'
    print
    feasible_flow_vectors = list(example1.gen_feasible_flow_vectors())
    pprint(feasible_flow_vectors)
    print
    print '## capacity vectors'
    print
    cap_vectors = example1.trans_to_cap_vector(feasible_flow_vectors)
    pprint(cap_vectors)
    print
    print '## minimal capacity vectors'
    print
    pprint(vector.min(cap_vectors))
    print
