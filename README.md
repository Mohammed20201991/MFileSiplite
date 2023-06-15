# MFileSiplite

How to run it ? 
~~~bash  
git clone https://github.com/Mohammed20201991/MFileSiplite.git
cd MFileSiplite
~~~

Siplit big corpus to small uints: 
use : <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/Siplit_corpus_to_spesfic_lines.ipynb"> corpus_to_small_files </a>

Break Hungarain lines to spesfic length such as 8,9,10,11: 
use : <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/Siplit_hu_to_break_lines.ipynb"> break_lines_to_spesfic_length </a>

Open your terminal : setupt your input & out directory 
~~~bash  
python3 run.py
~~~
- Pass your max lines to prompt (should be integer) <br>
- give file name ex:  brown.txt

<hr> 
<h2> Data Used : </h2>

<ul>
  <li>Brown Corpus </li>
  <li>
  <ol>
  <li> <a href="http://www.sls.hawaii.edu/bley-vroman/brown_corpus.html">Data link</a></li>
  <li> Line level in txt file format</li>
  <li>Handwritten generated from text file in form format as image (png extention)   <a href="https://10015.io/tools/text-to-handwriting-converter"> used tool </a></li>
</ol>   
  </li>
  
</ul>  

<h2>Hungarain Corpus for 60GB </h2>

<ol>
  <li> <a href="https://data.statmt.org/cc-100/hu.txt.xz">Data link</a> </li>
  <li> Big data text (Corpus) siplited to small text files each one with 5000000 lines </li>
  <li>link to data (later on cloud) </li>
</ol> 


<h2>File Size small Comparession </h2>
<p>At this point I am doing small comparession for <a href="https://huggingface.co/datasets/AlhitawiMohammed22/SROIE_2019_text_recognition23/blob/main/test.jsonl"> Test set from SROIE </a>by converting them to differnt data format using <a href = "https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/jsonl_to_parquet.py">script</a> </p>
<ol>
  <li> The data format in CSV give size <a href ="https://github.com/Mohammed20201991/MFileSiplite/blob/main/size_comparession/csv_out.csv">974 KB</a> </li>
  
  <li> The data format in jsonl  give size <a href ="https://github.com/Mohammed20201991/MFileSiplite/blob/main/size_comparession/test.jsonl">1432 KB </a>   </li>
  <li> The data format in parquet give size <a href ="https://github.com/Mohammed20201991/MFileSiplite/blob/main/size_comparession/out.parquet.csv">808 KB</a> </li>
  
  <li> To Sumup the above comparession parquet format is more efficent way for saving BigData  </li>
  
</ol> 

<h2>How to convert Text & Jsonl file and Pandas to Parquet format<a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/jsonl_to_parquet.py"> Script </a> </h2>

~~~bash
cd MFileSiplite/JupLab/
python3 jsonl_to_parquet.py path/to/input/file  path/to/output/file
~~~
An Example: 

~~~bash
python3 jsonl_to_parquet.py /home/ngyongyossy/mohammad/Data/SROIE_2019_text_recognition/test.jsonl  /home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/out.parquet
~~~
To convert data into <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/convert_to_SROEI.py">SROIE</a> format :
~~~bash
python3 convert_to_SROEI.py
~~~

For <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/IAM%20_processing.py">IAM data processing</a>:
~~~bash
python3 IAM_processing.py path/to/data_source
~~~

For <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/washingtondb-v1.0.py"> Washingtondb</a> data processing:
~~~bash
python3 washingtondb-v1.0.py path/to/data_source
~~~

For <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/process_missing.py">process_missing </a> process missing data:
~~~bash
python3 process_missing.py path/to/data_source
~~~

To <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/random_choice.py"> Choice Random randomly  </a> samples from generated data:
~~~bash
python3 random_choice.py
~~~

To <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/make_one_data.py"> Mearge two differnt datasets  </a>:
~~~bash
python3 make_one_data.py
~~~

To <a href="https://github.com/Mohammed20201991/MFileSiplite/blob/main/JupLab/zipFile.py"> Compress data after generation and processing </a>:
~~~bash
python3 zipFile.py
~~~

## References 
- <a href="http://www.sls.hawaii.edu/bley-vroman/brown_corpus.html">Brown corpus</a>
- <a href="https://data.statmt.org/cc-100/">Hungarain corpus : hu.txt.xz</a>
- <a href="https://huggingface.co/AlhitawiMohammed22">Dataset processed could be found here </a>
- <a href="https://fki.tic.heia-fr.ch/databases/washington-database">washington-database</a>
- <a href="https://fki.tic.heia-fr.ch/">IAM database</a>
- <a href="https://paperswithcode.com/dataset/sroie">SROIE</a>
