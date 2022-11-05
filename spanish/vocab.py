import subprocess
import os
import time

lines = [line.rstrip('\n') for line in open('dict.txt')]

for line in lines:

    try:
        line = line.title()
        print line
        line_length = len(line)
        print line_length
        dirpath = os.path.dirname(os.path.abspath(__file__))

        imgpath = dirpath+"\\output\\"+line+".png"
        wavpath = dirpath+"\\output\\"+line+".wav"
        mp3path = dirpath+"\\output\\"+line+".mp3"
        mp4path = dirpath+"\\output\\"+line+".mov"
        
        voice = "\"IVONA 2 Brian\""

        subprocess.check_output(["magick", "-background", "transparent", "-gravity","center", "-fill","white", "-font","Verdana", "-size","1820x980", "-density", "120", "-strokewidth", "10", "-stroke", "black", "label:"+line, "-bordercolor", "transparent", "-border", "50x50", imgpath],shell=True)
        subprocess.call(["magick", "composite", imgpath, "background.jpg", imgpath])
        #subprocess.check_output(["balcon.exe", "-n", "IVONA 2 Brian", "-fr", "48", "-t", line, "-o", "--raw", "|", "lame.exe", "-r", "-s", "48", "-m", "m", "-h", "-", mp3path], shell=True)
        #os.system("cmd.exe balcon.exe -n "+voice+" -fr 48 -t "+line+" -o --raw | lame.exe -r -s 48 -m m -h - "+mp3path)

        #convert
        os.system("lame.exe -V2 wavpath mp3path")
        #convert

        f = open('test.cmd', 'w+')
        f.write(""+dirpath+"\\balcon.exe -s -3 -sb 500 -se 500 -n "+voice+" -t "+line+" -w "+mp3path+"")
        #f.write(""+dirpath+"\\balcon.exe -n "+voice+" -fr 48 -t "+line+" -o --raw | "+dirpath+"\\lame.exe -r -s 48 -m m -h - "+dirpath+"\\mp3path")
        f.close()

        os.system("runas /savecred /profile /user:Honza "+dirpath+"\\test.cmd")
        
        subprocess.check_output(["ffmpeg.exe", "-y","-loop", "1", "-i", imgpath, "-i", mp3path, "-c:v", "libx264", "-c:a", "copy", "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2", "-shortest", mp4path], shell=True)

        os.remove(mp3path)
        os.remove(imgpath)
    except:
        print "error with " +str(line)
        f = open ('error.log', 'a')
        f.write(line+"\n")
        f.close()
        pass
