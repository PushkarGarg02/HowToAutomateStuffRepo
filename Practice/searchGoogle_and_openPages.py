'''
This script can be called as below:
D:\Users\703224500\AppData\Local\Programs\Python\Python37-32>python.exe D:\Scripts\openGooglePages.py Beautiful Soup

where 'Beautiful Soup' is the search word for google and it will open first 5 pages in browser in different tabs.
'''
#! python3

import sys, requests, bs4, webbrowser
print('Googling....')

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})

print(sys.argv[1:])
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

print(res.text)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.r a')
print(linkElems)

numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
    

'''
Sample linkElems for reference
------------------------------
soup4/&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQFggqMAQ&amp;usg=AOvVaw1
ph5VmBeOCffihw2y84g3y">beautifulsoup4 · PyPI</a></h3><div class="s"><div class="
hJND5c" style="margin-bottom:2px"><cite>https://pypi.org/project/<b>beautifulsou
p</b>4/</cite><div class="Pj9hGd"><div style="display:inline" onclick="google.sh
am(this);" aria-expanded="false" aria-haspopup="true" tabindex="0" data-ved="0ah
UKEwj3ouW7x4DeAhUBKo8KHSg4CYkQ7B0IKzAE"><span class="CiacGf"></span></div><div s
tyle="display:none" class="am-dropdown-menu" role="menu" tabindex="-1"><ul><li c
lass="mUpfKd"><a class="imx0m" href="/url?q=http://webcache.googleusercontent.co
m/search%3Fq%3Dcache:eMAqCvevww4J:https://pypi.org/project/beautifulsoup4/%252BB
eautiful%2BSoup%26hl%3Den%26ct%3Dclnk&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8K
HSg4CYkQIAgtMAQ&amp;usg=AOvVaw1Rc_-QAFd_u5i6M7Q9fFgk">Cached</a></li></ul></div>
</div></div><span class="st"><b>Beautiful Soup</b> is a library that makes it ea
sy to scrape information from web <br>
pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterati
ng,<br>
&nbsp;...</span><br></div></div><div class="g"><table class="ts"><tr><td colspan
="2"><h3 class="r"><a href="/url?q=https://www.youtube.com/watch%3Fv%3DaIPqt-Odm
S0&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQtwIIMDAF&amp;usg=AOvVaw2bVD
Ylh7CwttMDMlmrKppu">Web scraping and parsing with <b>Beautiful Soup</b> &amp; Py
thon Introduction ...</a></h3></td></tr><tr><td valign="top" width="1" style="pa
dding:4px 8px 0 0"><div class="th" style="position:relative;overflow:hidden;widt
h:116px;height:65px"><a href="/url?q=https://www.youtube.com/watch%3Fv%3DaIPqt-O
dmS0&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQuAIIMTAFUAE&amp;usg=AOvVa
w04FSIn0YJvnCmabMfxhRbV"><div style="margin-top:-11px"><img src="https://img.you
tube.com/vi/aIPqt-OdmS0/default.jpg" width="116" alt="Video for Beautiful Soup"
align="middle"></div><div style="position:absolute;bottom:0;right:0;font-size:11
px;color:#fff;background-color:#222;padding:1px 3px;text-decoration:none;font-we
ight:bold;text-align:right">&#9658; 9:49</div></a></div></td><td valign="top" st
yle="padding-top:1px"><cite class="hJND5c">https://www.youtube.com/watch?v=aIPqt
-OdmS0</cite><span class="st"><span class="f"><span class="nobr">24 Oct 2016</sp
an> - <span class="nobr">10 min</span> - <span class="nobr">Uploaded by sentdex<
/span></span><br>Welcome to a tutorial on web scraping with <b>Beautiful Soup</b
> 4. <b>Beautiful Soup</b> is a  Python <b>...</b></span></td></tr></table></div
><div class="g"><h3 class="r"><a href="/url?q=https://en.wikipedia.org/wiki/Beau
tiful_Soup_(HTML_parser)&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQFggzM
AY&amp;usg=AOvVaw3rCu4rDmH6182C4oi9D7sj"><b>Beautiful Soup</b> (HTML parser) - W
ikipedia</a></h3><div class="s"><div class="hJND5c" style="margin-bottom:2px"><c
ite>https://en.wikipedia.org/wiki/<b>Beautiful</b>_<b>Soup</b>_(HTML_parser)</ci
te><div class="Pj9hGd"><div style="display:inline" onclick="google.sham(this);"
aria-expanded="false" aria-haspopup="true" tabindex="0" data-ved="0ahUKEwj3ouW7x
4DeAhUBKo8KHSg4CYkQ7B0INDAG"><span class="CiacGf"></span></div><div style="displ
ay:none" class="am-dropdown-menu" role="menu" tabindex="-1"><ul><li class="mUpfK
d"><a class="imx0m" href="/url?q=http://webcache.googleusercontent.com/search%3F
q%3Dcache:AOgJyWMjzcQJ:https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser
)%252BBeautiful%2BSoup%26hl%3Den%26ct%3Dclnk&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeA
hUBKo8KHSg4CYkQIAg2MAY&amp;usg=AOvVaw298ZnyUbik4i_6sX9M9EgO">Cached</a></li><li
class="mUpfKd"><a class="imx0m" href="/search?ie=UTF-8&amp;q=related:https://en.
wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)+Beautiful+Soup&amp;tbo=1&amp;sa=
X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQHwg3MAY">Similar</a></li></ul></div><
/div></div><span class="st"><b>Beautiful Soup</b> is a Python package for parsin
g HTML and XML documents It <br>
creates a parse tree for parsed pages that can be used to extract data from HTML
<br>
,&nbsp;...</span><br></div></div><div class="g"><h3 class="r"><a href="/url?q=ht
tps://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486&amp;
sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQFgg5MAc&amp;usg=AOvVaw35nj8o-EOi86
As4JHZdAJv">Web Scraping 101 with Python &amp; <b>Beautiful Soup</b> &#8211; cod
eburst</a></h3><div class="s"><div class="hJND5c" style="margin-bottom:2px"><cit
e>https://codeburst.io/web-scraping-101-with-python-<b>beautiful</b>-<b>soup</b>
- bb617be1f486</cite><div class="Pj9hGd"><div style="display:inline" onclick="go
ogle.sham(this);" aria-expanded="false" aria-haspopup="true" tabindex="0" data-v
ed="0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQ7B0IOjAH"><span class="CiacGf"></span></div
><div style="display:none" class="am-dropdown-menu" role="menu" tabindex="-1"><u
l><li class="mUpfKd"><a class="imx0m" href="/url?q=http://webcache.googleusercon
tent.com/search%3Fq%3Dcache:OHAkMxcB7JsJ:https://codeburst.io/web-scraping-101-w
ith-python-beautiful-soup-bb617be1f486%252BBeautiful%2BSoup%26hl%3Den%26ct%3Dcln
k&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQIAg8MAc&amp;usg=AOvVaw1zNdki
2OSR0hR_whdynK8J">Cached</a></li></ul></div></div></div><span class="st">5 May 2
018 <b>...</b> Web Scraping 101 with Python &amp; <b>Beautiful Soup</b>. Webscra
ping is a method of <br>
data mining from web sites that uses software to extract all the&nbsp;...</span>
<br></div></div><div class="g"><h3 class="r"><a href="/url?q=https://readthedocs
.org/projects/beautiful-soup-4/&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CY
kQFgg_MAg&amp;usg=AOvVaw0N0jVku2f6Z8Q01e6LWnPR"><b>Beautiful Soup</b> 4 | Read t
he Docs</a></h3><div class="s"><div class="hJND5c" style="margin-bottom:2px"><ci
te>https://readthedocs.org/projects/<b>beautiful</b>-<b>soup</b>-4/</cite><div c
lass="Pj9hGd"><div style="display:inline" onclick="google.sham(this);" aria-expa
nded="false" aria-haspopup="true" tabindex="0" data-ved="0ahUKEwj3ouW7x4DeAhUBKo
8KHSg4CYkQ7B0IQDAI"><span class="CiacGf"></span></div><div style="display:none"
class="am-dropdown-menu" role="menu" tabindex="-1"><ul><li class="mUpfKd"><a cla
ss="imx0m" href="/url?q=http://webcache.googleusercontent.com/search%3Fq%3Dcache
:gSGVDf71prEJ:https://readthedocs.org/projects/beautiful-soup-4/%252BBeautiful%2
BSoup%26hl%3Den%26ct%3Dclnk&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQIA
hCMAg&amp;usg=AOvVaw2q-n6N5efaNxvS3OFKpp0p">Cached</a></li><li class="mUpfKd"><a
 class="imx0m" href="/search?ie=UTF-8&amp;q=related:https://readthedocs.org/proj
ects/beautiful-soup-4/+Beautiful+Soup&amp;tbo=1&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4
DeAhUBKo8KHSg4CYkQHwhDMAg">Similar</a></li></ul></div></div></div><span class="s
t">Description. <b>Beautiful Soup</b> sits atop an HTML or XML parser, providing
 Pythonic <br>
idioms for iterating, searching, and modifying the parse tree.</span><br></div><
/div><div class="g"><h3 class="r"><a href="/url?q=https://www.digitalocean.com/c
ommunity/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3&amp;
sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQFghFMAk&amp;usg=AOvVaw0Wx_32sIuXDc
T-n0D4IScl">Collecting Data from the Web with Python and <b>Beautiful Soup</b> .
..</a></h3><div class="s"><div class="hJND5c" style="margin-bottom:2px"><cite>ht
tps://www.digitalocean.com/.../how-to-scrape-web-pages-with-<b>beautiful</b>- <b
>soup</b>-and-python-3</cite><div class="Pj9hGd"><div style="display:inline" onc
lick="google.sham(this);" aria-expanded="false" aria-haspopup="true" tabindex="0
" data-ved="0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQ7B0IRjAJ"><span class="CiacGf"></sp
an></div><div style="display:none" class="am-dropdown-menu" role="menu" tabindex
="-1"><ul><li class="mUpfKd"><a class="imx0m" href="/url?q=http://webcache.googl
eusercontent.com/search%3Fq%3Dcache:OQWYDiSatU0J:https://www.digitalocean.com/co
mmunity/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3%252BB
eautiful%2BSoup%26hl%3Den%26ct%3Dclnk&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8K
HSg4CYkQIAhIMAk&amp;usg=AOvVaw28K8_G6UheqmPkYakr6nME">Cached</a></li></ul></div>
</div></div><span class="st">In this Python tutorial, we will collect and parse
a web page with the <b>Beautiful</b> <br>
<b>Soup</b> module in order to grab data and write the information we have gathe
red to <br>
a&nbsp;...</span><br></div></div></ol></div></div></div><div style="clear:both;m
argin-bottom:17px;overflow:hidden"><div style="font-size:16px;padding:0 8px 1px"
>Searches related to <b>Beautiful Soup</b></div><table border="0" cellpadding="0
" cellspacing="0"><tr><td valign="top"><p class="aw5cc" style="margin:3px 8px"><
a href="/search?ie=UTF-8&amp;q=beautiful+soup+download&amp;sa=X&amp;ved=0ahUKEwj
3ouW7x4DeAhUBKo8KHSg4CYkQ1QIISygA">beautiful soup <b>download</b></a></p></td><t
d valign="top" style="padding-left:10px"><p class="aw5cc" style="margin:3px 8px"
><a href="/search?ie=UTF-8&amp;q=beautiful+soup+medium&amp;sa=X&amp;ved=0ahUKEwj
3ouW7x4DeAhUBKo8KHSg4CYkQ1QIITCgB">beautiful soup <b>medium</b></a></p></td></tr
><tr><td valign="top"><p class="aw5cc" style="margin:3px 8px"><a href="/search?i
e=UTF-8&amp;q=intro+to+beautiful+soup&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8K
HSg4CYkQ1QIITSgC"><b>intro to</b> beautiful soup</a></p></td><td valign="top" st
yle="padding-left:10px"><p class="aw5cc" style="margin:3px 8px"><a href="/search
?ie=UTF-8&amp;q=beautifulsoup+tutorial+python+3&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4
DeAhUBKo8KHSg4CYkQ1QIITigD"><b>beautifulsoup tutorial python 3</b></a></p></td><
/tr><tr><td valign="top"><p class="aw5cc" style="margin:3px 8px"><a href="/searc
h?ie=UTF-8&amp;q=beautifulsoup+example&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8
KHSg4CYkQ1QIITygE"><b>beautifulsoup example</b></a></p></td><td valign="top" sty
le="padding-left:10px"><p class="aw5cc" style="margin:3px 8px"><a href="/search?
ie=UTF-8&amp;q=beautifulsoup+github&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHS
g4CYkQ1QIIUCgF"><b>beautifulsoup github</b></a></p></td></tr><tr><td valign="top
"><p class="aw5cc" style="margin:3px 8px"><a href="/search?ie=UTF-8&amp;q=how+to
+use+beautifulsoup&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQ1QIIUSgG"><
b>how to use beautifulsoup</b></a></p></td><td valign="top" style="padding-left:
10px"><p class="aw5cc" style="margin:3px 8px"><a href="/search?ie=UTF-8&amp;q=be
autifulsoup+download+file&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQ1QII
UigH"><b>beautifulsoup download file</b></a></p></td></tr></table></div></div><d
iv id="foot"><table align="center" border="0" cellpadding="0" cellspacing="0" id
="nav"><tr valign="top"><td align="left" class="b"><span class="csb" style="back
ground-position:-24px 0;width:28px"></span><b></b></td><td><span class="csb" sty
le="background-position:-53px 0;width:20px"></span><b>1</b></td><td><a class="fl
" href="/search?q=Beautiful+Soup&amp;ie=UTF-8&amp;prmd=ivns&amp;ei=J2XAW7fzC4HUv
ASo8KTICA&amp;start=10&amp;sa=N"><span class="csb" style="background-position:-7
4px 0;width:20px"></span>2</a></td><td><a class="fl" href="/search?q=Beautiful+S
oup&amp;ie=UTF-8&amp;prmd=ivns&amp;ei=J2XAW7fzC4HUvASo8KTICA&amp;start=20&amp;sa
=N"><span class="csb" style="background-position:-74px 0;width:20px"></span>3</a
></td><td><a class="fl" href="/search?q=Beautiful+Soup&amp;ie=UTF-8&amp;prmd=ivn
s&amp;ei=J2XAW7fzC4HUvASo8KTICA&amp;start=30&amp;sa=N"><span class="csb" style="
background-position:-74px 0;width:20px"></span>4</a></td><td><a class="fl" href=
"/search?q=Beautiful+Soup&amp;ie=UTF-8&amp;prmd=ivns&amp;ei=J2XAW7fzC4HUvASo8KTI
CA&amp;start=40&amp;sa=N"><span class="csb" style="background-position:-74px 0;w
idth:20px"></span>5</a></td><td><a class="fl" href="/search?q=Beautiful+Soup&amp
;ie=UTF-8&amp;prmd=ivns&amp;ei=J2XAW7fzC4HUvASo8KTICA&amp;start=50&amp;sa=N"><sp
an class="csb" style="background-position:-74px 0;width:20px"></span>6</a></td><
td><a class="fl" href="/search?q=Beautiful+Soup&amp;ie=UTF-8&amp;prmd=ivns&amp;e
i=J2XAW7fzC4HUvASo8KTICA&amp;start=60&amp;sa=N"><span class="csb" style="backgro
und-position:-74px 0;width:20px"></span>7</a></td><td><a class="fl" href="/searc
h?q=Beautiful+Soup&amp;ie=UTF-8&amp;prmd=ivns&amp;ei=J2XAW7fzC4HUvASo8KTICA&amp;
start=70&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20
px"></span>8</a></td><td><a class="fl" href="/search?q=Beautiful+Soup&amp;ie=UTF
-8&amp;prmd=ivns&amp;ei=J2XAW7fzC4HUvASo8KTICA&amp;start=80&amp;sa=N"><span clas
s="csb" style="background-position:-74px 0;width:20px"></span>9</a></td><td><a c
lass="fl" href="/search?q=Beautiful+Soup&amp;ie=UTF-8&amp;prmd=ivns&amp;ei=J2XAW
7fzC4HUvASo8KTICA&amp;start=90&amp;sa=N"><span class="csb" style="background-pos
ition:-74px 0;width:20px"></span>10</a></td><td class="b" style="text-align:left
"><a class="fl" href="/search?q=Beautiful+Soup&amp;ie=UTF-8&amp;prmd=ivns&amp;ei
=J2XAW7fzC4HUvASo8KTICA&amp;start=10&amp;sa=N" style="text-align:left"><span cla
ss="csb" style="background-position:-96px 0;width:71px"></span><span style="disp
lay:block;margin-left:53px">Next</span></a></td></tr></table><p class="A8ul6" id
="bfl" style="margin:19px 0 0;text-align:center"><a href="/advanced_search?q=Bea
utiful+Soup&amp;ie=UTF-8&amp;prmd=ivns">Advanced search</a><a href="/support/web
search/bin/answer.py?answer=134479&amp;hl=en">Search Help</a> <a href="/tools/fe
edback/survey/html?productId=196&amp;query=Beautiful+Soup&amp;hl=en-IN">Send fee
dback</a></p><div class="A8ul6" id="fll" style="margin:19px auto 19px auto;text-
align:center"><a href="/">Google&nbsp;Home</a> <a href="/intl/en/ads">Advertisin
g&nbsp;Programmes</a> <a href="/services">Business Solutions</a> <a href="/intl/
en/policies/privacy/">Privacy</a> <a href="/intl/en/policies/terms/">Terms</a> <
a href="/intl/en/about.html">About Google</a></div></div></td><td id="rhs_block"
 valign="top"><ol><div class="g"><div class="VBt9Dc hp-xpdbox"><div class="R8KuR
" style="float:right"><div class="OSMzvb" style="height:55px;width:86px"><a href
="/url?q=https://school.geekwall.in/p/BJWvZMekf/web-scraping-with-python-and-bea
utifulsoup&amp;sa=U&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQndQBCFwwCg&amp;usg=
AOvVaw2uqHLS74ZearbgrvqZ4GN8"><img src="https://encrypted-tbn0.gstatic.com/image
s?q=tbn:ANd9GcSi7jORTKCGRRI2Zux2hv-82P8DjudCOKXy8PWHVGN6aP4jGcL-HKRzKps" style="
margin-left:-5px;margin-right:-6px" title="https://school.geekwall.in/p/BJWvZMek
f/web-scraping-with-python-and-beautifulsoup" alt="Image result for Beautiful So
up"></a></div></div><div class="V7Q8V"><div><div class="FSP1Dd">Beautiful Soup</
div><div class="F7uZG Rlw09">HTML parser</div></div></div><div class="V7Q8V"><di
v class="mraOPb"><span>Beautiful Soup is a Python package for parsing HTML and X
ML documents. It creates a parse tree for parsed pages that can be used to extra
ct data from HTML, which is useful for web scraping.
It is available for Python 2.6+ and Python 3. <a class="fl" href="/url?q=https:/
/en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)&amp;sa=U&amp;ved=0ahUKEwj3ou
W7x4DeAhUBKo8KHSg4CYkQmhMIYigAMAw&amp;usg=AOvVaw1Xo2pmx-lZBrAgUpfW0QKL">Wikipedi
a</a></span></div></div><div class="V7Q8V" style="display:none"></div><div class
="V7Q8V"><span class="cC4Myd">License: </span><span class="A1t5ne"><a class="A1t
5ne fl" href="/search?ie=UTF-8&amp;q=Python+Software+Foundation+License&amp;stic
k=H4sIAAAAAAAAAONgVuLUz9U3sMwry0kBAMwjBo8NAAAA&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4D
eAhUBKo8KHSg4CYkQmxMIZigAMA4">Python Software Foundation License</a> (Beautiful
Soup 3 - an older version) <a class="A1t5ne fl" href="/search?ie=UTF-8&amp;q=MIT
+License&amp;stick=H4sIAAAAAAAAAONgVuLQz9U3MCkryAUA2OquugwAAAA&amp;sa=X&amp;ved=
0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQmxMIZygBMA4">MIT License</a> 4+</span></div><di
v class="V7Q8V"><span class="cC4Myd">Stable release: </span><span class="A1t5ne"
>4.6.0 / May 7, 2017; 16 months ago</span></div><div class="V7Q8V"><span class="
cC4Myd">Written in: </span><span class="A1t5ne"><a class="A1t5ne fl" href="/sear
ch?ie=UTF-8&amp;q=Python&amp;stick=H4sIAAAAAAAAAOPgE-LSz9U3MDIqLEq2UOIAsU2rDOO1l
DLKrfST83NyUpNLMvPz9Ivz00rKE4tSrcqLMktKUvMUMvMAL8-DZjwAAAA&amp;sa=X&amp;ved=0ahU
KEwj3ouW7x4DeAhUBKo8KHSg4CYkQmxMIbCgAMBA">Python</a></span></div><div class="V7Q
8V"><span class="cC4Myd">Platform: </span><span class="A1t5ne"><a class="A1t5ne
fl" href="/search?ie=UTF-8&amp;q=Python&amp;stick=H4sIAAAAAAAAAOPgE-LSz9U3MDIqLE
q2UOIAsU2rDOO1FDLKrfST83NyUpNLMvPz9Ivz00rKE4tSrQpyEkvS8otyAec5OVE6AAAA&amp;sa=X&
amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQmxMIbygAMBE">Python</a></span></div><di
v class="V7Q8V"><span class="cC4Myd">Original author(s): </span><span class="A1t
5ne"><a class="A1t5ne fl" href="/search?ie=UTF-8&amp;q=Leonard+Richardson&amp;st
ick=H4sIAAAAAAAAAONgVuLSz9U3MDXMKs7IAABZM1X2DgAAAA&amp;sa=X&amp;ved=0ahUKEwj3ouW
7x4DeAhUBKo8KHSg4CYkQmxMIcigAMBI">Leonard Richardson</a></span></div><div class=
"dXAUyb"><div class="lHETUb">People also search for</div><div class="xKoZHf B27E
Ld" style="width:72px"><div class="tQOFN" style="height:72px"><a class="FEM55" h
ref="/search?ie=UTF-8&amp;q=Requests+(software)&amp;stick=H4sIAAAAAAAAAONgFuLSz9
U3MDIqLEq2UOIGsQ2NMvIMc4y1-Jzzc3Pz84IzU1LLEyuLAT9NO98rAAAA&amp;sa=X&amp;ved=0ahU
KEwj3ouW7x4DeAhUBKo8KHSg4CYkQsQ4IdjAT"><img alt="Requests" height="72px" src="ht
tps://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiPpSfMCF-wAmy25IVflWM47swBN
c1LilOVZJEv4PqlgMY1x-X9k98sZHpk8yHd0ioDXo" title="Requests" width="72px"></a></d
iv><div class="brYqc"><a class="fl" href="/search?ie=UTF-8&amp;q=Requests+(softw
are)&amp;stick=H4sIAAAAAAAAAONgFuLSz9U3MDIqLEq2UOIGsQ2NMvIMc4y1-Jzzc3Pz84IzU1LLE
yuLAT9NO98rAAAA&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQxA0IdzAT" titl
e="Requests">Requests</a><div class="czonVc" title="Requests"></div></div></div>
<div class="B27ELd" style="width:72px"><div class="tQOFN" style="height:72px"><a
 class="FEM55" href="/search?ie=UTF-8&amp;q=Scrapy&amp;stick=H4sIAAAAAAAAAONgFuL
Sz9U3MDIqLEq2UAKzM9JzqgxKtPic83Nz8_OCM1NSyxMriwHCKuNlKgAAAA&amp;sa=X&amp;ved=0ah
UKEwj3ouW7x4DeAhUBKo8KHSg4CYkQsQ4IeTAT"><img alt="Scrapy" height="72px" src="htt
ps://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQHJk66HIVvNA_VUkEUSgdy7I5BrDx
Vv35er2v_vKGcF0--FnzpOUMJyH2SiEPK69RqHuw" title="Scrapy" width="72px"></a></div>
<div class="brYqc"><a class="fl" href="/search?ie=UTF-8&amp;q=Scrapy&amp;stick=H
4sIAAAAAAAAAONgFuLSz9U3MDIqLEq2UAKzM9JzqgxKtPic83Nz8_OCM1NSyxMriwHCKuNlKgAAAA&am
p;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQxA0IejAT" title="Scrapy">Scrapy<
/a><div class="czonVc" title="Scrapy"></div></div></div><div class="ty7XEe B27EL
d" style="width:72px"><div class="tQOFN" style="height:72px"><a class="FEM55" hr
ef="/search?ie=UTF-8&amp;q=Pip+(package+manager)&amp;stick=H4sIAAAAAAAAAONgFuLSz
9U3MDIqLEq2UAKzM6pyLUxMtPic83Nz8_OCM1NSyxMriwEQ1eOMKgAAAA&amp;sa=X&amp;ved=0ahUK
Ewj3ouW7x4DeAhUBKo8KHSg4CYkQsQ4IfDAT"><img alt="pip" height="72px" src="https://
encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTkfJcDr_OlDukHHUINgUfDroNqiZvqQiQ5
VwS-dS8ry0e_k6yKE8RNFgVY0cVpBf_lxmM" title="pip" width="72px"></a></div><div cla
ss="brYqc"><a class="fl" href="/search?ie=UTF-8&amp;q=Pip+(package+manager)&amp;
stick=H4sIAAAAAAAAAONgFuLSz9U3MDIqLEq2UAKzM6pyLUxMtPic83Nz8_OCM1NSyxMriwEQ1eOMKg
AAAA&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQxA0IfTAT" title="pip">pip
</a><div class="czonVc" title="pip"></div></div></div><br><div class="xKoZHf B27
ELd" style="width:72px"><div class="tQOFN" style="height:72px"><a class="FEM55"
href="/search?ie=UTF-8&amp;q=Selenium+(software)&amp;stick=H4sIAAAAAAAAAONgFuLSz
9U3MDIqLEq2UOIEsZMtjCzKtPic83Nz8_OCM1NSyxMriwHhnJ8PKQAAAA&amp;sa=X&amp;ved=0ahUK
Ewj3ouW7x4DeAhUBKo8KHSg4CYkQsQ4IfzAT"><img alt="Selenium" height="72px" src="htt
ps://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSZ0Q2rMoXqNoUzNSLL7bZt2k6jvZ1
boljCdF8alfopBYQQlW4kfeJW0dRQWf7Auqx30M8" title="Selenium" width="72px"></a></di
v><div class="brYqc"><a class="fl" href="/search?ie=UTF-8&amp;q=Selenium+(softwa
re)&amp;stick=H4sIAAAAAAAAAONgFuLSz9U3MDIqLEq2UOIEsZMtjCzKtPic83Nz8_OCM1NSyxMriw
HhnJ8PKQAAAA&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQxA0IgAEwEw" title
="Selenium">Selenium</a><div class="czonVc" title="Selenium"></div></div></div><
div class="B27ELd" style="width:72px"><div class="tQOFN" style="height:72px"><a
class="FEM55" href="/search?ie=UTF-8&amp;q=Pandas+(software)&amp;stick=H4sIAAAAA
AAAAONgFuLSz9U3MDIqLEq2UAKziwoyCgoKtfic83Nz8_OCM1NSyxMriwF2d98EKgAAAA&amp;sa=X&a
mp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQsQ4IggEwEw"><img alt="pandas" height="72
px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZuSjyN9W1MHoFIXt
0MQVhzQzBvx80PQQjTzABDkQ99ETRoa3TnXZMDR8Kp7Xc8roml-0" title="pandas" width="72px
"></a></div><div class="brYqc"><a class="fl" href="/search?ie=UTF-8&amp;q=Pandas
+(software)&amp;stick=H4sIAAAAAAAAAONgFuLSz9U3MDIqLEq2UAKziwoyCgoKtfic83Nz8_OCM1
NSyxMriwF2d98EKgAAAA&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQxA0IgwEwE
w" title="pandas">pandas</a><div class="czonVc" title="pandas"></div></div></div
><div class="ty7XEe B27ELd" style="width:72px"><div class="tQOFN" style="height:
72px"><a class="FEM55" href="/search?ie=UTF-8&amp;q=Flask&amp;stick=H4sIAAAAAAAA
AONgFuLSz9U3MDIqLEq2UAKzU9KLzY3KtPic83Nz8_OCM1NSyxMriwGVw5O3KgAAAA&amp;sa=X&amp;
ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQsQ4IhQEwEw"><img alt="Flask" height="72px"
src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk0-HkZbz-MHTAzP5oZN2
u2vOJvrrn5fPoNnty3p3ebS09QalcCVJb5avxfW60h1vXOJI" title="Flask" width="72px"></a
></div><div class="brYqc"><a class="fl" href="/search?ie=UTF-8&amp;q=Flask&amp;s
tick=H4sIAAAAAAAAAONgFuLSz9U3MDIqLEq2UAKzU9KLzY3KtPic83Nz8_OCM1NSyxMriwGVw5O3KgA
AAA&amp;sa=X&amp;ved=0ahUKEwj3ouW7x4DeAhUBKo8KHSg4CYkQxA0IhgEwEw" title="Flask">
Flask</a><div class="czonVc" title="Flask"></div></div></div><br></div></div></d
iv></ol></td></tr></tbody></table><script type="text/javascript" nonce="eZybMdZd
LL1iaqkJAGb77A==">(function(){var eventid='J2XAW7fzC4HUvASo8KTICA';google.kEI =
eventid;})();</script><script src="/xjs/_/js/k=xjs.hp.en.1_WUoW7HIO0.O/m=sb_he,d
/rt=j/d=1/rs=ACT90oES3Ss-08DzyJc1xbiPNjWIlbWDHg" nonce="eZybMdZdLL1iaqkJAGb77A==
"></script><script type="text/javascript" nonce="eZybMdZdLL1iaqkJAGb77A==">googl
e.ac&&google.ac.c({"agen":true,"cgen":true,"client":"heirloom-serp","dh":true,"d
hqt":true,"ds":"","ffql":"en","fl":true,"host":"google.com","isbh":28,"jsonp":tr
ue,"msgs":{"cibl":"Clear Search","dym":"Did you mean:","lcky":"I\u0026#39;m Feel
ing Lucky","lml":"Learn more","oskt":"Input tools","psrc":"This search was remov
ed from your \u003Ca href=\"/history\"\u003EWeb History\u003C/a\u003E","psrl":"R
emove","sbit":"Search by image","srch":"Google Search"},"ovr":{},"pq":"Beautiful
 Soup","refpd":true,"rfs":["beautiful soup download","intro to beautiful soup","
beautifulsoup example","how to use beautifulsoup","beautiful soup medium","beaut
ifulsoup tutorial python 3","beautifulsoup github","beautifulsoup download file"
],"sbpl":24,"sbpr":24,"scd":10,"sce":5,"stok":"gZbDcWGkQUkfawmrGehC8wB8GjE","uhd
e":false})</script><script nonce="eZybMdZdLL1iaqkJAGb77A==">(function(){window.g
oogle.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerH
eight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentEl
ement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=goo
gle.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+
google.kEI);}).call(this);})();</script></body></html>
'''

D:\Users\703224500\AppData\Local\Programs\Python\Python37-32>
