import subprocess
from threading import Thread

class Edit:
    def __init__(self):
        Thread(target=self.edit1).start()
        Thread(target=self.edit2).start()
        Thread(target=self.edit3).start()

    def edit1(self):
        subprocess.call("ffmpeg -i /video/1.mp4 -i /video/assets/asset1.mov \
  -filter_complex '[1:v]colorkey=0xff0000:0.1:[ckout];[0:v][ckout]overlay[out]' \
  -map '[out]' assets/out1.mp4", shell=True)

    def edit2(self):
        subprocess.call("ffmpeg -i /video/2.mp4 -i /video/assets/asset2.mov \
  -filter_complex '[1:v]colorkey=0xff0000:0.1:[ckout];[0:v][ckout]overlay[out]' \
  -map '[out]' assets/out2.mp4", shell=True)

    def edit3(self):
        subprocess.call("ffmpeg -i /video/3.mp4 -i /video/assets/asset3.mov \
  -filter_complex '[1:v]colorkey=0xff0000:0.1:[ckout];[0:v][ckout]overlay[out]' \
  -map '[out]' assets/out3.mp4", shell=True)

if __name__ == "__main__":
    e = Edit()
    e