# *Term Paper Research Project: ”Innovation and Word Usage Patterns in Machine Learning”*
- *Department of Economics / University of Brasilia*
- *Vítor Bandeira Borges*
- *Advisor: Daniel Oliveira Cajueiro*

## Introduction

By constructing an original dataset containing abstracts from papers of the most prominent
journals and conferences, this research will be able to analyse the last few decades of
evolutions and innovations that occurred in the machine learning field of study. The main
objective is to use information theory to track the creation, transmission and destruction of
patterns of word-use across the field, observing how different papers were able to innovate
compared to its predecessors and influence its successors.
Using innovative techniques in Natural Language Processing (NLP), a computer program
will be able to systematically compare each text to its counterparts, and extract information
as to how impactful a certain publication was. This kind of data combined with meticulous
descriptive statistics aims to retell the emergence of influential topics that altered Machine
Learning as a whole.

## Background

Machine Learning comes from the mathematical modelling of neural networks by *Pitts and
McCulloch, 1947*. Since then, many variations and models have been developed, and exponential
increases in accessible computing power have allowed for a true revolution in
information processing and predictive modelling. The last few decades were the golden age
for artificial intelligence, and the volume of publications related to ML have consistently
increased.

As knowledge progressed, several subtopics have differentiated into areas of study. Unsupervised
learning, Reinforcement learning, Natural Language Processing and Computer Vision
have gained consistency and are now extensively used in applications by big technology
companies, and also anyone that has access to open-source code.

## Methodology

In linguistics, a text corpus is a language resource consisting of a large and structured set of
documents. Each document talks about certain subjects, and can be classified inside a set
of topics that provide an explicit representation of what is contained in that text.

*Blei et al.*, 2003 proposed a model called *Latent Dirichlet Allocation* (LDA) that trains
on the *tf-idf* (SAX-VSM, 2016) word frequency matrix of a corpus, and is able to assign
probability distributions in a set of topics for every text. With respect to the word-usage
patterns, this distribution will attribute higher probabilities for a document belonging to a
certain topic if its lexicon is closer to what the model observed in other publications. The
results are distributions that contain information about the content in each document.

If a paper is assigned to distinct topics than what was being published before it, this suggests
that the text brought something new to the discussion and the distance between it and its
counterparts can be interpreted as a metric of innovativeness (*Barron et al., 2018* calls this
‘*Novelty*’). The reverse is also measured, so if texts that came after a publication started
using a lexicon closer to it, they were probably influenced (*Barron et al., 2018* calls this
‘*Transience*’). The methodology for measuring the distance between different probability
distributions is called the Kullback-Leibler Divergence metric (Kullback and Leibler, 1951).

## Structure

1. Find the most prominent sources of publications in Machine Learning inside Journals
and Conferences that happened in the last few decades.

> (a) List the web sources for Journals and Conferences that will be scrapped;

> (b) Web Scraping;

2. Structure the data and select features that will be used in the study.

> (a) Abstracts;

> (b) Publication Identifying features;

3. Apply the Methodology and reconstruct the literature
