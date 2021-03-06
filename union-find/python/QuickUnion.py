#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import UnionFind

class QuickUnion(UnionFind.UnionFind):

	def __init__(self, N):
		super().__init__(N)
		self.roots = [x for x in range(N)]

	def union(self, p, q):
		p_root = self.getRoot(p)
		q_root = self.getRoot(q)
		self.roots[q_root] = p_root

	def connected(self, p, q):
		return self.getRoot(p) == self.getRoot(q)

	def getRoot(self, i):
		while i != self.roots[i]:
			i = self.roots[i]
		return i

	def __repr__(self):
		return str(self.roots)

def main():
	UnionFind.main(QuickUnion)

if __name__ == "__main__":
	main()
