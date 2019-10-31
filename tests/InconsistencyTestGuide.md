**How to test for inconsistent ontologies and unsatisfiable classes**

1. Open the ontology in Protege
2. Under the Reasoner menu, Select the reasoner you want to use (like ['HermiT 1.4.2.456'](http://www.hermit-reasoner.com/))
3. Start reasoner with Strg-R (Ctrl-R) or with menu Reasoner->Start reasoner
   Protege now informs you if the ontology is [inconsistent](https://www.sciencedirect.com/science/article/pii/S1570826805000260/#aep-section-id29) and gives you the option to get explanations.
   This usually happens when [Individuals](https://www.w3.org/TR/owl-features/#s3.1) have conflicting types (are instances of two or more [disjoint superclasses](https://www.w3.org/TR/2012/REC-owl2-primer-20121211/#a_DisjointClasses)).
4. The Class hierarchy will popup and let you see if there is a subclass of owl:Thing called owl:Nothing.
   [Unsatisfiable classes](https://www.sciencedirect.com/science/article/pii/S1570826805000260/#aep-section-id29) will be subclasses of owl:Nothing. 
   This usually happens when there are mutliple [disjoint superclasses](https://www.w3.org/TR/2012/REC-owl2-primer-20121211/#a_DisjointClasses). 
5. Stop reasoner with menu Reasoner->Stop reasoner

Useful when fixing:
- Synchronise reasoner with menu Reasoner-> Synchronise reasoner instead of stopping and starting again
