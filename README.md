![](https://github.com/IG-88Alex/Image_repo/blob/master/Logo.png)




<h1 align="center">Welcome to «‎Site Map Generator»‎ 👾 .</h1>

<p align= "center"> Open and free site map generator 🕸️</p>

<h2><i>🐍Installation.</i></h2>



<br> </br>

### __Instalation Python 3.9 (3.8) 🐍__

<h3 align = "left"> 🗗 For Windows:</h3>

* ### If your Windows distribution doesn't have python installed since version 3.8 (3.9), go to the official website, download the latest version of python, and install it on your computer. ⬇

[Download](https://www.python.org/downloads/) the installer from the official website and run it. Make sure that you check the box when installing:

![](https://github.com/IG-88Alex/Image_repo/blob/master/add_path.png)

### __Instalation Site_Map_Generator.__

* ### You can install the tool using one of the following methods:

 * #### 1. First way. ⚡

	* _[Download](https://git-scm.com/download/win) and <b>install Git Bash</b>._ :large_orange_diamond:

	* _Press the key combination <b>Win+r</b>, enter <b>cmd</b>, <b>enter in cmd</b>:_

	                    pip3 install git+https://github.com/IG-88Alex/Site_Map_Generator

	* Example:

			   - (press)           Win + r

			   - (enter)           cmd 

			   - (in cmd enter)    pip3 install git+https://github.com/IG-88Alex/Site_Map_Generator

<br> </br>

* #### 2. Second way. ⬇📦
	* _Download the zip archive and then <b>unpack</b> archive._ 
	* _Open the terminal with the keyboard shortcut <b>Win+R</b>, and enter
	<b>cmd</b>, then enter the <b>path</b> to the folder in the terminal where it is located <b>setup.py</b>_.

	* Example:

			   -                        Unzip Site_Map_Generator-main.zip 
			   			     => (folder) Site_Map_Generator-main

			   - (press)                Win + r

			   - (enter)                cmd 

			   - (in cmd enter path)    cd C:\Users\Administrator\Documents\Site_Map_Generator-main

			   - (in cmd enter)         python3 setup.py install
			   



<br> </br>

<h3 align = "left"> 🐧 For Linux: (Tested on Ubuntu 20.04.1 LTS)</h3>


### Instalation Python 3.9 (3.8) 🐍

 ### If your Linux distribution does not have python installed since version 3.8+ (3.9), please follow these instructions.


 #### 1.⚡⚡ First way (Instalation Python3.9 + instalation Sitemap Generator tool). ⚡⚡
 
#### Open a terminal (Ubuntu: Ctrl + Alt + T) and enter the following commands:

<pre><b>
wget https://raw.githubusercontent.com/IG-88Alex/Site_Map_Generator/main/python3.9_linux_install

chmod +sx ./python3.9_linux_install

sudo ./python3.9_linux_install

</b></pre>


 #### 2.⏱️ Second way 💻.

 #### 2.1. Open the terminal of your Linux distribution and enter the following commands (Ubuntu: Ctrl + Alt + T):

<pre><b>
sudo apt update && sudo apt -y upgrade

sudo apt install build-essential checkinstall 
	
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

sudo apt install python3-tk

sudo apt install wget
</pre></b>

 #### 2.2. [Go to the official python repository on Github](https://github.com/python/cpython/releases) and copy the link to the compressed archive __*tar.gz*__ Python 3.8+ (3.9)

![](https://github.com/IG-88Alex/Image_repo/blob/master/tar-gz_cpython.png)

 #### 2.3. Go to the  __*/opt*__  section and download the compressed archive  __*tar.gz*__  using  __*wget*__:
![](https://github.com/IG-88a-lex/Images/blob/master/wget0.png)
<pre><b>
cd /opt

sudo wget [a link to the archive tar.gz]

sudo tar xzf v3.9.1rc1.tar.gz

cd cpython-3.9.1rc1

./configure --enable-optimizations

make altinstall

cd /opt

rm -f v3.9.1rc1.tar.gz

python3.9 -m pip install git+https://github.com/IG-88Alex/Site_Map_Generator

map
</b></pre>

 ### Instalation Site_Map_Generator.
_If you have a python 3 version (python3 -V) at least >= 3.8 installed enter the following command:_
	
	                 python3 -m pip install git+https://github.com/IG-88Alex/Site_Map_Generator


<br> </br>



<h2><i>✅ Launch.</i></h2>

__It's simple! Enter the `map` or `sitemap` command and the bomber interface will launch. The command is available from any directory.__



<br> </br>


<h2>🔑 Expanded use.</h2>

  Commands       |  Destination
------------     | -------------
   -p            | Allows you to open the Windows Explorer graphical window to select the folder/directorywhere you want to save the site map.
   -g            | Based on the received links, it allows you to see the graph. ✳
 Path to folder  | You can copy the absolute path to the folder/directory where you want to save the site map.


#### _Command Examples:_

```http://example.com/page1/page2  -p   -g``` ✔

```-g http://example.com/page1/page2  -p``` ✔

```http://example.com/page1/page2/   C:\Users\Administrator\Desktop   -g``` ✔

```http://example.com/page1/page2/   C:\Users\Administrator\Desktop``` ✔

```C:\Users\Administrator\Desktop  http://example.com/page1/page2/page3   -g``` ✔

```/home/ig-88a-lex/Desktop -g  http://example.com/page1/page2/page3``` ✔

```-g /home/ig-88a-lex/Desktop http://example.com/page1/page2/page3``` ✔

```http://example.com/page1/page2/page3``` ✔

```http://example.com/page1/page2/page3 -p C:\Users\Administrator\Desktop``` (you can't do this!!!) ❌❗❗❗ (-p with Path)


<h2><i>📝 License.</i></h2>

__The project is distributed under the [MIT License](https://github.com/IG-88Alex/Site_Map_Generator/blob/main/LICENSE) . By downloading the software from this repository, you agree to it. Under the terms of the license, you must upload the source code of your modifications under the same license.__


<br> </br>


