------------------------------------------------------------------------
		NAPAbench:Network Alignment Performance Assessment benchmark
------------------------------------------------------------------------
NAPAbench is a synthetic benchmark datasets that can be used for 
evaluating and comparing the performance of various network
alignment algorithms. 

NAPAbench is developed based on
the algorithm presented in the following paper:

- S.M.E. Sahraeian and B.J. Yoon, “A Network Synthesis Model for
Generating Protein Interaction Network Families”, PLoS ONE, 2012, to
appear.

NAPAbench is developed by S.M.E. Sahraeian and Byung-Jun Yoon 
in GSP lab, Department of Electrical and Computer Engineering, 
Texas A&M University.

------------------------------------------------------------------------

NAPAbench has been made freely available as PUBLIC DOMAIN
software and hence is not subject to copyright in the  United
States.  This system and/or any portion of  the  source  code
may be used, modified, or redistributed without restrictions.  
The software is distributed WITHOUT WARRANTY, express or implied.
The authors accept NO LEGAL LIABILITY OR  RESPONSIBILITY  for
loss due to reliance on the program. 

------------------------------------------------------------------------  

NAPAbench consists of three suites of datasets:

pairwise alignment dataset
5-way alignment dataset
8-way alignment dataset

Each each suite has three subcategories: DMR, DMC, and CG, which are named 
based on the network growth model used to construct that set.
In each category, we have 10 independently generated network family sets.

------------------------------------------------------------------------  

pairwise alignment dataset: 
The netwok families in the "pairwise" set consists of two networks generated 
from an ancerstral network  of size 2000 along the following tree:
(A:1000,B:2000)
so the number of nodeos in each network is as follows:
|A|=3000, |B|=4000

5-way alignment dataset: 
The netwok families in the "5-way" set consists of five networks generated 
from an ancerstral network  of size 500 along the following tree:
(A:500,(B:500,(C:500,(D:500,E:500):500):500):500)
so the number of nodeos in each network is as follows:
|A|=1000, |B|=1500, |C|=2000, |D|=2500, |E|=2500

8-way alignment dataset: 
The netwok families in the "8-way" set consists of eight networks generated 
from an ancerstral network  of size 400 along the following tree:
(((A:200,B:200):200,(C:200,D:200):200):200,((E:200,F:200):200,(G:200,H:200):200):200)
so the number of nodeos in each network is as follows:
|A|=1000, |B|=1000, |C|=1000, |D|=1000, |E|=1000, |F|=1000, |G|=1000, |H|=1000

------------------------------------------------------------------------  

Each Family consists of the following data files:

Network files: A.net, B.net, ...
	These files define the structure of each of generated networks.
	
Functional annotation files: A.fo, B.fo, ...
	These files include the functional ortholgy group of each network node.
	
Similarity score files: A-B.sim, A-C.sim, B-C.sim, ...
	These files incude the similarity scores of nodes across the networks.

Data file format:

		Network files: [e.g A.net]
				a1	a2
				a3	a1
				a4	a2
				a2	a3
		
		Functional annotation files: [e.g. A.fo]
				a1	FO:1
				a2	FO:2
				a1	FO:2
				a4	FO:3
		
		Similarity score files: [e.g. A-B.sim]
				a1	b1	153
				a1	b3	55
				a1	b7	49
				a2	b3	444
				a3	b3	211
				a3	b4	122
				a4	b5	251
				a4	b8	71

------------------------------------------------------------------------  
For more information on NAPAbench, please see:

S.M.E. Sahraeian and B.J. Yoon, “A Network Synthesis Model for Generating
Protein Interaction Network Families”, PLoS ONE, 2012, to appear.

By Sayed Mohammad Ebrahim Sahraeian and Byung-Jun Yoon
July 2012
Contact: msahraeian@tamu.edu, bjyoon@ece.tamu.edu
-------------------------------------------------------------------------
