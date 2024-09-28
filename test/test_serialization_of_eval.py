# encoding: utf-8
"""
testSeralizationOfEval.py

Created by Chimezie Ogbuji on 2010-08-15.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import unittest
from rdflib import Literal, RDF, Variable
from FuXi.LP.BackwardFixpointProcedure import BFP_RULE, BFP_NS
from FuXi.Horn.PositiveConditions import Uniterm
from FuXi.Horn.HornRules import Rule, Clause


class testSeralizationOfEvalTests(unittest.TestCase):

    def testSerializingEvalPred(self):
        nsBindings = {'bfp': BFP_NS, 'rule': BFP_RULE}
        evaluateTerm = Uniterm(
            BFP_NS.evaluate,
            [BFP_RULE[str(1)], Literal(1)],
            newNss=nsBindings)
        self.assertTrue(repr(evaluateTerm), "bfp:evaluate(rule:1 1)")
        xVar = Variable('X')
        yVar = Variable('Y')
        bodyTerm = Uniterm(RDF.rest, [xVar, yVar], newNss=nsBindings)
        rule = Rule(Clause(bodyTerm, evaluateTerm), declare=[xVar, yVar])
        self.assertEqual(repr(rule),
                         "Forall ?X ?Y ( bfp:evaluate(rule:1 1) :- rdf:rest(?X ?Y) )")

if __name__ == '__main__':
    unittest.main()
