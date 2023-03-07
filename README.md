# MFileSiplite

How to run it ? 
~~~bash  
!git clone https://github.com/Mohammed20201991/MFileSiplite.git
!cd MFileSiplite
~~~

Open your terminal : setupt your input & out   directory 
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

<h2>How to convert Text & Jsonl file and Pandas to Parquet format </h2>

~~~bash
!cd MFileSiplite/JupLab/
python3 jsonl_to_parquet.py path/to/input/file  path/to/output/file
~~~
An Example: 

~~~bash
python3 jsonl_to_parquet.py /home/ngyongyossy/mohammad/Data/SROIE_2019_text_recognition/test.jsonl  /home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/out.parquet
~~~

