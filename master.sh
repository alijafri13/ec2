
source venv/bin/activate
# Obtain url's from search terms


for i in {1..30}
do

  python3 keyword_batch_write.py

  cd Stage1_search_to_PDFURL
  bash Stage-1-main.sh
  cd ..
  # Download PDF's into papers

  mkdir Stage3_OpenIE_RELEX_Pipeline/PDF/
  cd Stage2_PDFURL_to_Papers
  bash Stage-2-main.sh

  ##Relationship Extraction
  cd ..
  cd Stage3_OpenIE_RELEX_Pipeline
  bash Stage-3-main.sh
  #
  cd ..
  cd Stage4_CleanUp
  bash Stage-4-main.sh
  cd ..

done
