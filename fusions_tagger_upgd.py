#################################################################
'''
fusions_tagger.py
Python Script by Somnath Tagore, (c) 2017
Usage:
	From Command Line: python fusions_tagger.py [options] Text-File 
	From Web: http://biodb.md.biu.ac.il/protfus/
Download Options: https://bitbucket.org/somnathtagore/protfus
Read Text File (PubMed Abstract)
Output:
	List of Fusion Protein instances in the abstract
'''
##################################################################

'''Import Packages and Modules'''
import re
import nltk.data
import sys
import fileinput

'''For Future Upgrades'''
#import tagger_swig_wrap 
##from distutils.core import setup, Extension
# the c++ extension module
##extension_mod = Extension("tagf", ["tagfuse.cxx", "tagcorpus.cxx"])

'''Test Runs'''
#import re
#######text=open('hihi.txt','r')
#lineList = [line.split() for line in open("hihi.txt").readlines()]
#sList = [item.strip() for item in re.split(r' *[\.\?!][\'"\)\]]* *', open("hihi.txt")) if item]
#########################s = open('som_result.txt').read()
#########################wordList = []
#########################for sentence in [item.strip() for item in re.split(r'[!?.]',s) if item]:
#########################    wordList.append(sentence.split())
#########################    print sentence
#######sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
#print('\n',sList)
#text = """\
#Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.
#"""
#sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
######sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

######for stuff in sentences:
######        print(stuff)    
##setup(name = "tagf", ext_modules=[extension_mod])

'''Reg Ex Tests'''
###f=open('demo_file.txt','r')
#cont_f=f.read()
#f.close()
#matches=re.findall("(abstract)?",cont_f)

#print matches

'''For input files (future upgrades)'''
#f=open('pubmed_file.txt','r')
infile=sys.argv[1]
#f=open('a.txt','r')
f=open(infile,'r')
#data_f=f.read()
#print(data_f)
#synonyms_fusion = sys.argv[1]
#rulebase_normalize = sys.argv[2]
#fusioncorpus = sys.argv[3]
#ppicorpus = sys.argv[4]
#rulebase_regex = sys.argv[5]

#f=open('demo_file_1.txt','r')
#f=open('regex_1_2_27Jan16.txt','r')
#f=open('som_result_2.txt','r')

##f=open('output_pubmed_search_3_030316.txt','r')
##f1=open(synonyms_fusion,'r')
##f2=open(rulebase_normalize,'r')
##f3=open(fusioncorpus,'r')
##f4=open(ppicorpus,'r')
##f5=open(rulebase_regex,'r')
##f6=open('outout_output_pubmed_search_3_030316.txt','w')
##f7=open('outout_output_pubmed_search_3_030316.txt','r')
##f8=open('outoutout_output_pubmed_search_3_030316.txt','w')
#f=open('hihi.txt','r')
#######sentences = re.split(r' *[\.\?!][\'"\)\]]* *',f)

'''
Pattern Matches
Dictionaries: Synonyms_fusion_proteins, RuleBase_Normalization, 
Bibliographies: Fusion_Corpus
RuleBase: RuleBase_RegEx
Short Form Recognition: N/A
'''
#######for line in enumerate(f):
#######	for match in re.finditer(sentences,line):
#######	        print(match.groups())    
#pattern=re.compile("(abstract)")
#pattern=re.compile("(<(\d{4,5})>)")
#pattern=re.compile("(\s\w+(\-|\+|\/)\w+\s)")
##               pattern=re.compile("(\s\w+(\-|\+|\/)\w+\s)",re.M)
##               pattern=re.compile("(\s\w+(\-|\+|\/)\w+\s{'fusion'|'fusions'|'chimeric'|'transcripts'|'gene'})",re.M)
#pattern1=re.compile("(\s\w+(\-|\+|\/)\w+\s)",re.M)
#pattern2=re.compile("(\w+(\-|\:)\w+\s('fusion|fusions|chimeric|transcripts|gene|fusion genes|gene fusion|fusion protein|gene|genes|chimeric transcript|chimeric gene|fusion genes|fusion transcript'))(\s(interacts with|interacts)\s\w+)",re.M)
#pattern2=re.compile("(\w+(\-|\:)\w+\s('fusion|fusions|chimeric|transcripts|gene|fusion genes|gene fusion|fusion protein|gene|genes|chimeric transcript|chimeric gene|fusion genes|fusion transcript'))\s\w+",re.M)
#pattern3=re.compile("(\s\w+(\-|\+|\/)\w+\s(fusion protein|fusion transcript)(\s(|interacts with))(\s\w+\s\w+\s\w+\s\w+\s))",re.M)
#pattern4=re.compile("\s\w+(\-|\+|\/)\s(fusion)\s\w+\s(interacts with)(\s\w+)",re.M)
#pattern4=re.compile("\s\w+\s(interacts with)(\s\w+)",re.M)
#pattern5=re.compile("pattern2|pattern3",re.M)
#pattern6=re.compile("((\w+(\-|\:)\w+\s('fusion|fusions|chimeric|transcripts|gene|fusion genes|gene fusion|fusion protein|gene|genes|chimeric transcript|chimeric gene|fusion genes|fusion transcript'))\s\w+)|((\s\w+(\-|\+|\/)\w+\s(fusion protein|fusion transcript)(\s(|interacts with))(\s\w+\s\w+\s\w+\s\w+\s)))",re.M)
################################################################
pattern1=re.compile("(\s\w+(\-|\+|\/)\w+\s)",re.M)
pattern2=re.compile("(\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |proteins'))",re.M)
#pattern3=re.compile("(\s\w+(\-|\:|\/)\w+\s('fusions|fusion|fusion transcript|fusion protein|fusion transcripts|translocation|transcript|chimeric|fusion gene|transcripts|fusion oncogene|gene fusion|gene fusions|fusion proteins|oncofusion proteins|chimera|fusion genes|gene|chimeric fusion|rearrangement|transgene|chimeric gene|variants|oncogene|chimeric transcript|chimeric transcripts '))",re.M)
pattern3a=re.compile("(\s('latent gene'|'lytic gene'))",re.M)
pattern3b=re.compile("(\s('virus'))",re.M)
pattern4=re.compile("(\s\w+(\-|\+|\/)\w+\s(domain|fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and )(\s(of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that))(\s\w+\s\w+\s\w+\s\w+\s))",re.M)
pattern5=re.compile("(\s\w+\s(protein|proteins|gene|genes))(\s\w+(\-|\+|\/)\w+\s(domain|fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |interaction|interactions)(\s(of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that|of the protein interacting with|as an interactor of))(\s\w+\s\w+\s\w+\s\w+\s))",re.M)
pattern6=re.compile("(\s(\w+|protein|proteins|gene|genes|family of|family|chimera|fusion|transcript|interactions among))(\s\w+(\-|\+|\/)\w+\s(interacted with|block in autophagy is dependent on a GTPase activating protein,|and|and is responsible for|with|family|interactions with|in its reduced and a|protein-protein interaction between|genes|proteins|interactions|interaction|gene|protein|domain|fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |interaction|interactions)(\s\w+\s(in|interaction with|and participates, in concert with|of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that|of the protein interacting with|as an interactor of))(\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+))",re.M)
pattern7=re.compile("(\s\w+\s(interaction with|and participates, in concert with|of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that|of the protein interacting with|as an interactor of)(\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+))",re.M)
pattern8=re.compile("(\s\w+(\-|\+|\/)\w+\s(domain|fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |interaction|interactions)(\s(of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that|of the protein interacting with|as an interactor of))(\s\w+\s\w+\s\w+\s\w+\s))",re.M)
pattern9=re.compile("(\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts|')(\w+\s('interacts with'))(\s\w+\s))",re.M)
pattern10=re.compile("((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |proteins')))  |  ((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts|')(\s('interacts with'))(\s\w+\s)))  |  ((\s\w+(\-|\+|\/)\w+\s(domain|fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and )(\s(of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that))(\s\w+\s\w+\s\w+\s\w+\s)))  | ((\s\w+\s(protein|proteins|gene|genes))(\s\w+(\-|\+|\/)\w+\s(domain|fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |interaction|interactions)(\s(of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that|of the protein interacting with|as an interactor of))(\s\w+\s\w+\s\w+\s\w+\s)))     ",re.M)
pattern10=re.compile("((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |proteins'))) | ((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts|')(\s('interacts with'))(\s\w+\s)))      ",re.M)
pattern11=re.compile("((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |proteins'))) | ((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts|')(\s('interacts with'))(\s\w+\s))) | ((\s\w+(\-|\+|\/)\w+\s(domain|fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and )(\s(of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that))(\s\w+\s\w+\s\w+\s\w+\s)))     ",re.M)
pattern12=re.compile("((\s\w+(\-|\:|\/)\w+\s('activate|activates|activating|activator |block|blocks|blocking|blocked|blocks in|blocks with |chimera|chimeric|chimeric gene|chimeric genes|chimeric transcript |depend|dependent|depends on|depends to|depending on |domain|domains|express|expression|expressed in|expressed with|expresses in |family|fusion|fusions|fusion transcript|fusion transcripts|fusion protein|fusion proteins|fusion gene|fusion genes |gene|genes|gene fusion |interaction|interactions|interactions with |protein|proteins|reduce|reduced|reduced form |residue|residues|transcript|transcripts')))|(domains) (((\s('Abolish| abolishes| abolished| abolishing | accelerate| accelerated| accelerating |acceptor| accumulate| accumulates| accumulated| accumulating| accumulation  | acetylate| acetylates| acetylated| acetylating| acetylation | activate| activiated| activating| activation| activator |affect| affect| affected| affecting | alter| alters| altered| altering| alteration | amplify| amplifies| amplified| amplifying| amplification |apoptosis| assemble|assembled| assembling | associate| associated| associating| association | attach| attaches| attached| attaching| attachment |attack| attacked| attacking |bind| binds| bound| binding | block| blocked| blocking | carbamoylate| carbamoylates| carbamoylated| carbamoylating| carbamoylation |carboxylate| carboxylated| carboxylating| carboxylation |catalyze| catalyzed| catalyzing |cleave| cleaved| cleaving |co-immunoprecipitate| co-immunoprecipitates| co-immunoprecipitated| co-immunoprecipitating| co-immunoprecipitation| co-immunoprecipitations |Compare| complex| complexed| complexing| complexation | conjugate| conjugated| conjugating| conjugation | contact| contacted| contacting |Couple| coupled with| coupled to |Covalent|covalently linked to |deaccetylate| deaccetylated| deaccetylating| deaccetylation |deaminate| deaminated| deaminating| deamination |decarboxylate| decarboxylates| decarboxylated| decarboxylating| decarboxylation |decrease| decreased| decreasing |dehydrate|dehydrated| dehydrating| dehydration |dehydrogenate| dehydrogenated| dehydrogenating| dehydrogenation |demethylate| demethylated| demethylating| demethylation |dephosphorylate| dephosphorylated| dephosphorylating| dephosphorylation |deplete| depleted| depleting| depletion | disassemble| disassembles| disassembled| disassembling | discharge| discharged| discharging |dock| docked| docking |down-regulate| down-regulated| down-regulating| down-regulation |downregulate | elevate|  enhance| express |formylate |fusion |glycosylate| hasten| heterodimerize| heterodimer| homodimer|hydrolyse | inactivate| incite| induce| infect| influence|inhibit|initiate|interact| interacts with| isomerize| ligate| mediate| modify| modulate| overexpress|promotes| react| recognize |regulate| repress|split| stimulate| suppress| transactivate| upregulate| up-regulates| up-regulated| up-regulating| up-regulation| up-regulator'))))",re.M)
pattern14=re.compile("((\s\w+(\-|\:|\/)\w+\s('activate|activates|activating|activator |block|blocks|blocking|blocked|blocks in|blocks with |chimera|chimeric|chimeric gene|chimeric genes|chimeric transcript |depend|dependent|depends on|depends to|depending on |domain|domains|express|expression|expressed in|expressed with|expresses in |family|fusion|fusions|fusion transcript|fusion transcripts|fusion protein|fusion proteins|fusion gene|fusion genes |gene|genes|gene fusion |interaction|interactions|interactions with |protein|proteins|reduce|reduced|reduced form |residue|residues|transcript|transcripts')))|(domains) ",re.M)
pattern13=re.compile("((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |proteins'))) | (((domains)(\s(of the protein interacting with|interacts with|interaction|blocks|suppressed|binds|that regulates|regulates|influenced by|stays attached to the|compared to|coupled with|expressed as|covalently links|fusion proteins|binding site in human|enzymatic inhibition|bound to|proteins to histone-tail peptides, DNA or selected|bound at|proteins that |proteins to the|proteins can then be cleaved with|proteins and showed that))(\s\w)))     ",re.M)
pattern15=re.compile("((\s\w+(\-|\:|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts| and |proteins|inhibitors|genes|'))) | ((\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts|')))      ",re.M)
#pattern=re.compile("(\s\w+\-\w+\s)")
#pattern=re.compile("(<(\d{4,5})>?)")
#for i, line in enumerate(open('demo_file.txt')):
''' 
Comments !!!!

patterna=re.compile("(\s\w+(\-|\+|\/)\w+\s)",re.M)
patternb=re.compile("(\s\w+(\-|\+|\/)\w+\s('fusion|fusions|chimeric|transcripts|fusion genes|gene fusion|fusion protein|chimeric transcript|chimeric gene|fusion transcripts'))",re.M)
for i, line in enumerate(f):
	for match in re.finditer(patterna and patternb, line):
               # print '%s' % (match.groups())
        	print 'Found on line %s: %s' % (i+1, match.groups())
               # print  (match.groups())
'''
#p=pattern2.match(str(f))
'''Display Statements'''
#print '------Line No----- || ----------Position-------------||-------------------------------------Token---------------------------------------------------\n'
#print '------Line No----- || ----------Position-------------||-------------------------------------Token---------------------------------------------------\n'
#for i, line in enumerate(f):
for i, line in enumerate(f):
    for match in re.finditer(pattern3a, line):
#     any (re.match(pattern1,line) for match in [pattern3, pattern2])
     #print 'Found on line %s: %s' % (i+1, regex.groups())
 	  #  print 'line %s: %s\n----------------------------------\n' % (i+1, match.groups(line))
# 	    print '          %s          || %s \n' % (i+1, match.groups(line))
 	  #  print '          %s          || %s || %s \n' % (i+1, match.groups(1),match.groups(3))
 	    #print ' %s || %s  \n' % (i+1, match.groups(line))
# 	    f6.write(' %s || %s  \n' % (i+1, match.groups(line)))
#	    m=pattern2.match(line)
# 	    print '\t %s\t   || %s  \t             || %s\n' % (i+1, match.span(), match.groups(line))
 	    print ' %s\t    %s  \t       %s\n' % (i+1, match.start(), match.end())
# 	    print '\t %s\t      || %s  \n' % (i+1,match.span())

'''Test Pattern Matches '''
#matchobj=re.match(pattern12,f,re.M|re.I)
#print '          %s          || %s \n' % (i+1, matchobj.group(1))

#for line in fileinput.FileInput("outout_output_pubmed_search_3_030316.txt",inplace=1):
#	line=line.replace(" ","\t")

#for line in f7:
#	f8.write(line.replace(' ', '\t'))i

'''File Closure'''
f.close()
#f6.close()
#f7.close()
#f8.close()
#text.close()
