


#'''This is a module to retrieve and work with and display pubmed articles which match a keyword'''
import re
import sys
import os, os.path
from Bio import Entrez
from distutils.core import setup, Extension
Entrez.email = "somnathtagore@gmail.com"
global article
global query 
article= " "
global cpf1
global cpf2
cpf1=" "
cpf2=" "
global filename1
global filepath1
global numofrec
#global filename2
#global filepath2
filename1= " "
filename2= " "
numofrec= " "
#filepath1= " "
#filepath2= " "
#query = "fusion proteins[All Fields] AND interactions[All Fields]" #sets the query; should make this an input field
#query = "fusion proteins[All Fields]" #sets the query; should make this an input field
#query = "fusion proteins OR protein-protein interactions[All Fields]" #sets the query; should make this an input fiel
#query = "fusion proteins[All Fields] AND interactions[All Fields] OR protein-protein interaction[All Fields]" #sets the query; should make this an input field
##################important#######query = "(('Nucl Eng Des/Fusion'[Journal] OR fusion[All Fields] OR FUSION[Journal] OR fusion[All Fields]) AND (proteins[MeSH Terms] OR proteins[All Fields])) OR (protein-protein[All Fields] AND interactions[All Fields])" #sets the query; should make this an input field
query="EZR-ROS1[All Fields] OR (EZR[All Fields] AND ROS1[All Fields]) OR EZR_ROS1[All Fields] OR (EZR[All Fields] AND ROS1[All Fields]) "
#query = " (fusion[All Fields] OR ('Nucl Eng Des/Fusion'[Journal] OR FUSION[Journal]) OR fusion[All Fields]) AND (proteins[MeSH Terms] OR (proteins[MeSH Terms] OR proteins[All Fields])) OR protein-protein[All Fields] AND interactions[All Fields] AND ('2015/01/01'[PDAT] : '2016/04/01'[PDAT]) " #sets the query; should make this an input field
#query = "bcr-abl[All Fields] OR bcr abl[All Fields] OR bcr/abl[All Fields] " #sets the query; should make this an input field
#query = "aff1-mll mllt1-mll rara-pml ell-mll runx1-runx1t1 npm1 rara mll-mmlt4 crebbp-kat6a fusion proteins[All Fields] AND protein-protein interactions[All Fields] " #sets the query; should make this an input fiel$d
#query = "gene fusions OR NPM1-RARA OR RARA OR BCR OR ABL OR AFF1-MLL OR BCR/ABL OR BCR-ABL OR bcr-abl OR PML-RARA OR MLLT1-MLL OR ELL-MLL OR RUNX1-RUNXITI OR proteins OR fusion proteins OR fusions OR genes OR fusion genes OR interactions OR PPI or protein protein interactions OR protein-protein interactions" #sets the query; should make this an input field
filename1=sys.argv[1]
#filepath1=sys.argv[2]
filename2=sys.argv[2]
numofrec=sys.argv[3]
#filepath2=sys.argv[4]
        #filename = "output_pubmed_search_2.txt" #% article_id #sets filename for output file to be the gi number.xml
        #filename = "output_pubmed_search_2.txt" #% article_id #sets filename for output file to be the gi number.xml
def get_article_abstract(article_id):

	article_handle = Entrez.efetch(db="pubmed", id=article_id, rettype="abstract", retmode="text")
	article = article_handle.read()
	print article	

def pubmed_statistics():
#'''Retrieves general information about the PubMed database'''
	handle = Entrez.einfo(db="pubmed") # gets information about the Entrez pubmed database
	record = Entrez.read(handle) #parses pubmed information
	total_records = record["DbInfo"]["Count"] #obtains a count of total records in the PubMed database
	last_updated = record["DbInfo"]["LastUpdate"] #obtains the most recent update to the PubMed database

def author_search(query):
	handle = Entrez.esearch(db="pubmed", term=query, retmax=numofrec) #searches PubMed for the specified query
	record = Entrez.read(handle) #parses the entrez search results
        article_id = record["IdList"] #gets the first article in the list
#	print record["Count"]
	article_handle = Entrez.efetch(db="pubmed", id=article_id, rettype="medline", retmode="text") #retrieves the first article as xml

#	cpf1=os.path.join(filepath1,filename1)
        outhandle = open(filename1, "w") 
#	filename = "output_pubmed_search_2_2.txt" #% article_id #sets filename for output file to be the gi number.xml
#	outhandle = open(filename, "w") #generates and opens the output file
	outhandle.write(article_handle.read()) #writes article to output file
	outhandle.close()
	article_handle.close()
#	print "Saved as output_pubmed_search_2.txt" % filename #prints a completion output

def cited_articles(article_id):
#'''retrieves all articles indexed by PubMedCentral which cite a given article'''
	cited_articles = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", LinkName="pubmed_pmc_refs", from_uid=article_id)) #gets pubmed central articles which cite the article
	cited_article_ids = [link["Id"] for link in cited_articles[0]["LinkSetDb"][0]["Link"]]
	cited_pmid = Entrez.read(Entrez.elink(dbfrom="pmc", db="pubmed", LinkName="pmc_pubmed", from_uid=",".join(cited_article_ids)))
	if cited_pmid:
		#print "This article was cited by:\n %s" % get_article_abstract(cited_pmid[0]["IdList"][0])
		print get_article_abstract(cited_pmid[0]["IdList"][0])
	else:
		print "This article has not been cited in PubMed Central"
'''
def readwrite():
	inFile=open('output_pubmed_search_2.txt','r')

	inFile_contents=inFile.read()
	print (inFile_contents)
	inFile.close()
'''
def secondfile():
#	inFile = open("output_pubmed_search_2_2.txt")
#	outFile = open("som_result_2.txt", "w")
	inFile = open(filename1)
#        cpf2=os.path.join(filepath2,filename2)
        outFile = open(filename2, "w")
	buffer = []
	for line in inFile:
	    if line.startswith("LID - "):	
	        buffer = ['']	
	    elif line.startswith("CI  - "):
	        outFile.write("".join(buffer))
	        buffer = []
	    elif buffer:
	        buffer.append(line)
	inFile.close()
	outFile.close()

def thirdfile():
	f=open(filename1,'r')
	f1=open(filename1,'r')
#	f=open('som_result_2.txt','r')
#	f1=open('som_result_2.txt','r')
#	f1=open('res.txt','w')
	pattern1=re.compile("(\s\w+(\-|\+|\/)\w+\s)",re.M)
	pattern2=re.compile("(\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |proteins'))",re.M)
	pattern112a=re.compile("(\s)(interacted with|interactions with|protein-protein interaction|interaction|participates|interacts with|interaction|blocks|suppressed|binds|regulates|influenced by|coupled with|expressed as|covalently links)(\s)",re.M)
	pattern3=re.compile("(\s\w+(\-|\:|\/)\w+\s('fusions|fusion|fusion transcript|fusion protein|fusion transcripts|translocation|transcript|chimeric|fusion gene|transcripts|fusion oncogene|gene fusion|gene fusions|fusion proteins|oncofusion proteins|chimera|fusion genes|gene|chimeric fusion|rearrangement|transgene|chimeric gene|variants|oncogene|chimeric transcript|chimeric transcripts '))",re.M)

	pattern112=re.compile("(\s)( Abolish| abolishes| abolished| abolishing | accelerate| accelerated| accelerating |acceptor| accumulate| accumulates| accumulated| accumulating| accumulation  | acetylate| acetylates| acetylated| acetylating| acetylation | activate| activiated| activating| activation| activator |affect| affect| affected| affecting | alter| alters| altered| altering| alteration | amplify| amplifies| amplified| amplifying| amplification |apoptosis| assemble|assembled| assembling | associate| associated| associating| association | attach| attaches| attached| attaching| attachment |attack| attacked| attacking |bind| binds| bound| binding | block| blocked| blocking | carbamoylate| carbamoylates| carbamoylated| carbamoylating| carbamoylation |carboxylate| carboxylated| carboxylating| carboxylation |catalyze| catalyzed| catalyzing |cleave| cleaved| cleaving |co-immunoprecipitate| co-immunoprecipitates| co-immunoprecipitated| co-immunoprecipitating| co-immunoprecipitation| co-immunoprecipitations |Compare| complex| complexed| complexing| complexation | conjugate| conjugated| conjugating| conjugation | contact| contacted| contacting |Couple| coupled with| coupled to |Covalent|covalently linked to |deaccetylate| deaccetylated| deaccetylating| deaccetylation |deaminate| deaminated| deaminating| deamination |decarboxylate| decarboxylates| decarboxylated| decarboxylating| decarboxylation |decrease| decreased| decreasing |dehydrate|dehydrated| dehydrating| dehydration |dehydrogenate| dehydrogenated| dehydrogenating| dehydrogenation |demethylate| demethylated| demethylating| demethylation |dephosphorylate| dephosphorylated| dephosphorylating| dephosphorylation |deplete| depleted| depleting| depletion | disassemble| disassembles| disassembled| disassembling | discharge| discharged| discharging |dock| docked| docking |down-regulate| down-regulated| down-regulating| down-regulation |downregulate | elevate|  enhance| express |formylate |fusion |glycosylate| hasten| heterodimerize| heterodimer| homodimer|hydrolyse | inactivate| incite| induce| infect| influence|inhibit|initiate|interact| interacts with| isomerize| ligate| mediate| modify| modulate| overexpress|promotes| react| recognize |regulate| repress|split| stimulate| suppress| transactivate| upregulate| up-regulates| up-regulated| up-regulating| up-regulation| up-regulator|interacted with|interactions with|protein-protein interaction between|interaction|participates|interacts with|binds|regulates|influenced by|coupled with|expressed as|covalently links)(\s)",re.M)
	for i, line in enumerate(f):
		for match in re.finditer(pattern3, line):
#     any (re.match(pattern1,line) for match in [pattern3, pattern2])
     #print 'Found on line %s: %s' % (i+1, regex.groups())
#           print 'line %s: %s\n----------------------------------\n' % (i+1, match.groups(line))
#           print '          %s          || %s \n' % (i+1, match.groups(line))
          #  print '          %s          || %s || %s \n' % (i+1, match.groups(1),match.groups(3))
            #print ' %s || %s  \n' % (i+1, match.groups(line))
#           f6.write(' %s || %s  \n' % (i+1, match.groups(line)))
#           m=pattern2.match(line)
#           print '\t %s\t   || %s  \t             || %s\n' % (i+1, match.span(), match.groups(line))
        		print '  %s\t  %s  \t       %s\n' % (i+1, match.start(), match.end())
#           print '\t %s\t      || %s  \n' % (i+1,match.span())
###print '*********************************\n'
	for j, line1 in enumerate(f1):
        	for match1 in re.finditer(pattern112, line1):
#               print 'line %s: %s\n----------------------------------\n' % (j+1, match1.groups(line1))
                	print '  %s\t  %s  \t       %s\n' % (j+1, match1.start(), match1.end())
###print '---------------------------------\n'
###for k, line2 in enumerate(f2):
###     for match2 in re.finditer(pattern16, line2):
###             print 'line %s: %s\n----------------------------------\n' % (k+1, match1.groups(line2))
###             print ' %s\t    %s  \t       %s\n' % (k+1, match2.start(), match2.end())
###print '-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-\n'

def main():
	pubmed_statistics()
	author_search(query)
#	readwrite()
	secondfile()
	thirdfile()
if __name__=='__main__':
        main()
