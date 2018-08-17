# fname='/Users/justin/Desktop/16685734_181834362309546_3171275376009674752_n.png'
# 'convert -dispose 3 -delay 13.2 -loop 0 in.jpg -crop 640x480 +repage out.gif' % (delay, sprite, width, height, gif)
# rate=14.2

import scipy
from scipy import ndimage
import os
from shutil import copyfile
# from tqdm import tqdm
import matplotlib.pyplot as plt
import subprocess

def numobjs(fname):
	dna = scipy.misc.imread(fname,1)
	dnaf = ndimage.gaussian_filter(dna, 12)
	labeled, nr_objects = ndimage.label(dnaf > 60)
	
	if nr_objects==0:
		dna = scipy.misc.imread(fname,0)
		dnaf = ndimage.gaussian_filter(dna, 5)
		labeled, nr_objects = ndimage.label(dnaf > 75)
	
	# print nr_objects

	labeled=labeled.astype('uint8')
	plt.imshow(labeled)
	plt.show()
	return nr_objects,dna.shape[1],dna.shape[0]

# numobjs('./gifs/Bust a Groove*0.jpg')


def movegifsback():
	fs=[f for f in os.listdir('./gifs/') if '.gif' in f]
	for i in fs:
		elts=i.split('*')
		inf='/Users/justin/Sites/Dropbox/stickers/gifs/'+i
		print inf
		out='/Users/justin/Sites/Dropbox/stickers/'+elts[0]+'/'+elts[1]
		print out
		image=out[:-4]+'.jpg'
		print image
		os.rename(inf,out)
		os.remove(image)

def gifit():
	outf=open('log.txt','r')
	out=outf.read().split('\n')

	for f in out:
		elts=f.split('\t')
		sprite='./gifs/'+elts[0]
		gif='./gifs/'+elts[0][:-4]+'.gif'
		
		image=scipy.misc.imread(sprite)
		h=image.shape[0]
		w=image.shape[1]

		x=int(elts[1])
		y=int(elts[2])
		delete=int(elts[3])
		lastindex=(x*y)-1

		if delete==0:
			delcmd=''
		else:
			delcmd='-delete '
			for i in range(lastindex,lastindex-delete,-1):
				delcmd+=str(i)+','

		width = int(w/x)
		height = int(h/y)

		cmd='convert -dispose 3 -delay %s %s -loop 0 "%s" -crop %sx%s +repage "%s"' % (14, delcmd, sprite, width, height, gif)
		print(cmd)

		os.system(cmd)
	
	outf.close()
gifit()