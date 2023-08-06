import os,subprocess,time
from subprocess import run as srun,call as scall
from os.path import exists,getsize,isfile
from random import randint,random

#time.strftime('%H:%M:%S',time.gmtime(seconds))
#ffprobe -hide_banner  -show_entries stream=codec_type  -show_entries stream_tags=language  -print_format json -loglevel 0
def hhmmss(seconds):
    x = time.strftime('%H:%M:%S',time.gmtime(seconds))
    return x

class ffmpeg:
  def __init__(self):
    self.message='hello'
  def get_duration(file):
    cmd=['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file]
    peo = srun(cmd,capture_output=True)
    if peo.returncode==0:
      return round(float(peo.stdout))
    else:
      return 5
  def ssgen(video, time_stamp):
    out = osjoin(os.getcwd(),str(time.time())+ ".jpg")
    cmd = ["ffmpeg","-ss",f"{hhmmss(time_stamp)}", "-i",f"{video}","-vframes","1","-loglevel","0",out,"-y"]
    peo=srun(cmd,capture_output=True)
    if peo.returncode==0:
      if isfile(out):
        return out
    else:
      return  None
  def sshotfunc(file,count:int):
    picts=[]
    duration=ffmpeg.get_duration(file)
    for i in range(count):
      sshot = ffmpeg.ssgen(file, round((duration-1)*random())) 
      if sshot is not None:
        picts.append(sshot)
    return picts
  def cret_thumb(file):
    duration=ffmpeg.get_duration(file)
    return ffmpeg.ssgen(file,randint(1,duration-1))
  def merge_streams(video=None,audio=None,subtitle=None):
    if (video and audio and subtitle):
      out=video+str(time.time())+'.mkv'
      cmd=['ffmpeg','-i',video,'-i',audio,'-i',subtitle,'-loglevel','0','-c','copy','-map','0:v','-map','0:s?','-map','0:a?','-map','1:s?','-map','1:a','-map','2:s',out,'-y']
      peo=srun(cmd,capture_output=True)
      if peo.returncode==0:
        return out
      else:
        return None
    elif ((video and audio) or (video and subtitle)):
      if (video and audio):
        out=video+str(time.time())+'.mkv'
        cmd=['ffmpeg','-i',video,'-i',audio,'-loglevel','0','-c','copy','-map','0:v','-map','0:s?','-map','0:a?','-map','1:a',out,'-y']
        peo=srun(cmd,capture_output=True)
        if peo.returncode==0:
          return out
        else:
          return None
      else:
        out=video+str(time.time())+'.mkv'
        cmd=['ffmpeg','-i',video,'-i',subtitle,'-loglevel','0','-c','copy','-map','0:v','-map','0:s?','-map','0:a?','-map','1:s',out,'-y']
        peo=srun(cmd,capture_output=True)
        if peo.returncode==0:
          return out
        else:
          return None
    else:
      pass
    
    
    
    
    
    
