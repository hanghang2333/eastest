import os,shutil
def changefilecontent(rootpath,rootname,sourcepath,filename):
    outfilename = os.path.join(rootpath+rootname)
    out = open(outfilename,'w')
    f = open(os.path.join(sourcepath,filename),'r').readlines()
    for i in f:
        i = i.split('\t')
        i = (i[2]+' '+i[3]).replace('\n','').split()
        i = ','.join(i)
        out.write(i+'\n')
    out.close()


rootpath = 'data/train/'
if os.path.exists(rootpath):
    pass
else:
    os.makedirs(rootpath)

imgcount = 0
source_path = ['training_data/','new_training_data/']
for path in source_path:
    imglist = os.listdir(path)
    for imgname in imglist:
        if imgname.endswith('.png'):
            labelfile = imgname+'.gt'
            changefilecontent(rootpath,str(imgcount)+'.txt',path,labelfile)
            shutil.copyfile(os.path.join(path,imgname),os.path.join(rootpath,str(imgcount)+'.png'))
            imgcount += 1
        if imgname.endswith('.jpg'):
            labelfile = imgname.append('gt')
            changefilecontent(rootpath,str(imgcount)+'.txt',path,labelfile)
            shutil.copyfile(os.path.join(path,imgname),os.path.join(rootpath,str(imgcount)+'.jpg'))
            imgcount += 1