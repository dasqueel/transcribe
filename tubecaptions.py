"""
usage:

getCapText(<videoId>, <name of txtfile>)

example:

getCapText("IX1cJLUpJQI", "screencast")
"""

import pysrt
from subprocess import call
import subprocess as sp
import os

def getCapText(vidId, fileName):
	command = "youtube-dl --write-auto-sub --sub-lang en --skip-download -o "+fileName+".%(ext)s http://www.youtube.com/watch?v="+vidId
	call(command.split(), shell=False)

	cmd = "ffmpeg -i "+fileName+".en.vtt "+fileName+".en.srt"
	call(cmd.split(), shell=False)

	subs = pysrt.open(fileName+'.en.srt')
	with open('txts/'+fileName+".txt", "w") as text_file:
		os.remove(fileName+".en.vtt")
		os.remove(fileName+".en.srt")
		text_file.write(subs.text)
		print 'created '+fileName+".txt!"
