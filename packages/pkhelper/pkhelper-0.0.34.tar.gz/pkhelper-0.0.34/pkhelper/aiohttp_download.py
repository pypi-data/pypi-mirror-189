import os,aiohttp,asyncio,sys,time
from requests import head as rhead
exts=['mkv','mp4','mp3','m4a','mov','rst','html','php','tar','gz','gzip','md','py','cxx','cpp','3gp','3gpp','rar','7z','pdf','jpg','png','webm','weba','webp','zip','rar','mobi','epub','winzip','jpeg','apk','m4v','mka']
from urllib.parse import unquote

def extfind(filename):
 ext=filename.split(".")[-1]
 if ext in str(exts):
      pass
 else:
    for ent in exts:
            if ext.find(ent)>=0:
                ext=ent
            else:
                pass
 return ext

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def spd(start,down):
   diff=time.time()-start
   ge=down/diff
   speed=f"""{humanbytes(ge)}/s"""
   return speed

#dl_header=rhead(url).headers
#filename=str(dl_header.get("content-disposition")).split('filename="')[-1].replace('"',"").encode('raw-unicode-escape').decode('utf-8')

def url2name(url):
  filename=str(unquote(url)).split("/")[-1]
  if len(filename) == 0:
     try:
        #dl_header=rhead(url).headers
        #filename=str(dl_header.get("content-disposition")).split('filename="')[-1].replace('"',"").encode('raw-unicode-escape').decode('utf-8')
        if len(filename)==0:
           filename="DefaultName"
     except:
         filename="DefaultName"
  else:
     try:
       ext=extfind(unquote(filename))
       nai=str(filename).split('.')
       if len(nai) == 2:
          filename=f"""{str(filename).split('.')[-2]}.{ext}"""
       elif len(nai)>2:
         filename=f"""{str(filename).replace(".","_")}.{ext}"""
       else:
         filename=f"""{str(filename)}.{ext}"""
       if len(filename) > 176:
              filename="DefaultName" + "." + ext 
     except:
            pass
     try:
       filename=str(unquote(str(filename))).replace("+","_")
     except:
        pass
  return filename

async def direct_dl_async(download_url, filename=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(download_url, timeout=None) as response:
            if not filename:
                cont_disp=str(response.headers.get('content-disposition'))
                if "filename=" in cont_disp:
                   filename=cont_disp.split('filename=')[-1].replace('"','').encode('raw-unicode-escape').decode('utf-8')
                else:
                   filename=url2name(download_url)      
            filename = os.path.join(os.getcwd(), unquote(filename))
            total_size = int(response.headers.get("content-length", 1)) or 1024
            downloaded_size = 0
            with open(filename, "wb") as f:
                start=time.time()
                async for chunk in response.content.iter_chunked(8*1024*1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
            return filename

async def ddad(download_url, filename=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(download_url, timeout=None) as response:
            if not filename:
                cont_disp=str(response.headers.get('content-disposition'))
                if "filename=" in cont_disp:
                   filename=cont_disp.split('filename=')[-1].replace('"','').encode('raw-unicode-escape').decode('utf-8')
                else:
                   filename=url2name(download_url)
            filename = os.path.join(os.getcwd(), unquote(filename))
            total_size = int(response.headers.get("content-length", 1)) or 1024
            downloaded_size = 0
            with open(filename, "wb") as f:
                start=time.time()
                print("Downloading",filename,'\n')
                async for chunk in response.content.iter_chunked(8*1024*1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        speed=spd(start,downloaded_size)
                        print(f""" {humanbytes(downloaded_size)}/{humanbytes(total_size)} {str((downloaded_size/total_size)*100)[:4]}%  {speed} """,end="\r")
            print("\n")
            print("Downloaded Successfully✓")
            print(f"""File: {filename}""")
            return filename

def direct_dl(url,filename=None):
 loop=asyncio.get_event_loop()
 r=loop.run_until_complete(ddad(url,filename))
 return r
