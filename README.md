# ProtFus

Text mining has been an active research topic for decades; however, it is only fairly recently that biomedical text-mining tools have been developed that make it practically applicable to a wide range of problems. Mining of full-text articles — not to their supplementary material — is still exploratory in nature, with most applications focusing on mining the more easily available abstracts only. Similarly, large amounts of sequencing data on fusions in cancers have only recently become available, thanks to leaps in sequencing technologies. To make biological sense of these vast amounts of data, however, they must be analyzed in the context of our current biological knowledge. How this should be done in practice remains an open challenge, since most of the knowledge is buried in the literature.

ProtFus is a resource that has information about fusion proteins and their interactions, based on a text mining approach. "Tagging" is a process of registering the mention of given entities in a particular document. With increase in size of scientific literature, efficient methods of text mining will greatly help for extracting and interpreting useful information present in free texts, thus assist in real time queries. Moreover, two or more types of information are tagged concurrently to find co-mentions. For example, human fusion proteins and cancer. Let us assume that we are interested in the fusion protein BCR-ABL1. We want to find all the mentions of BCR-ABL1 in the literature. But, BCR-ABL1 can be spelled in a variety of ways BCR-ABL1, BCR/ABL1, bcr-abl1, bcr/abl1, bcr:abl1, BCR:ABL1, etc. Thus, we have developed ProtFus, a “tagger” which identifes all these jargons. It uses natural language processing methodology for tagging interactions.

It has two files:

1. fusions_tagger_upgd.py - Identify fusions from text.
2. ppi_protfus_pubmed_upgd.py - Identify fusion PPIs from text.
