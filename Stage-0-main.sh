#!/bin/bash
#Initializes the process to run the paper addition
# 
echo "Initializing..."
cd ..
python3 -m venv venv
source venv/bin/activate
echo "Downloading Packages..."
## Install packages
# # wget https://maven.ceon.pl/artifactory/kdd-releases/pl/edu/icm/cermine/cermine-impl/1.13/cermine-impl-1.13-jar-with-dependencies.jar -P /Stage3_OpenIE_RELEX_Pipeline
#
#
pip install -U pip setuptools wheel

pip install pandas
pip install rake-nltk
pip install bs4
pip install gremlinpython
pip install tqdm
pip install json5
pip install jsonlines
pip install jsonschema
pip install networkx
pip install spacy
pip install regex
pip install stanfordnlp
pip install stanford-openie
pip install nltk
pip install future
pip install word2number
pip install flair
pip install scispacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.3.0/en_core_sci_sm-0.3.0.tar.gz
pip install regex
pip install requests
pip install numpy
pip install bs4
pip install PyPDF2
pip install wget
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader wordnet
python3 -m nltk.downloader punkt
python3 -m nltk.downloader averaged_perceptron_tagger
#
# # #
# git clone https://github.com/huggingface/neuralcoref.git
# pip install -U spacy
# python3 -m spacy download en_core_web_sm
# python3 -m spacy download en
# #
# cd neuralcoref
# pip install -r requirements.txt
# pip install -e .
# #
# cd ..

# echo "All Packages Installed"

# echo "Connecting sqlite3 database"
# cd Stage0_Initialize
# python3 sqlite_init.py

# cd ..
# deactivate
