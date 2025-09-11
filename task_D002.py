import traceback
import re
html = """<HTML><HEAD><TITLE> Title Here</TITLE></HEAD> <BODY BGCOLOR= ""FFFFF"> <CENTER><IMG SRC="clouds.jpg" ALIGN="BOTTOM"> </CENTER> <HR> <a href="http://somegreatsite.com" name="asd" surname="">Link Name</a> <P> This is a new paragraph! <BR> <B><I>This is a new sentence without a paragraph break, in bold italics.</I></B> <HR></BODY></HTML>"""
def func(html):
    res1 = len(re.findall("<", html))
    res2 = len(re.findall(">", html))
    if res1 == res2:
        print (res1)

