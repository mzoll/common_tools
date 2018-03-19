'''
Created on Mar 16, 2018

@author: marcel.zoll
'''
import unittest

from common_tools.tools.sort_emit import topoSort_gen

class Test(unittest.TestCase):

    def testTopologicalSort(self):
        class A:
            name = 'A'
            dep = []
        
        class B:
            name = 'B'
            dep = ['A']
            
        class C:
            name = 'C'
            dep = ['B']
            
        class D:
            name = 'D'
            dep =['B','A']
            
        class E:
            name = 'E'
            dep = ['A']
            
        inlist = [E(), D(), C(), B(), A()]
        topoSort_gen(inlist, lambda e: e.name, lambda e: e.dep)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()