import os
import subprocess

if not os.path.exists("assets"):
    raise Exception("Please Create assets folder and put all videos in it!")

mkv_list = os.listdir("assets")

if not os.path.exists("result"):
    os.mkdir("result")

for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)
    if ext != ".mkv":
        raise Exception("Should contain only MKV files!")

    output_name = name + ".mp4"
    try:
        subprocess.run(
            ["ffmpeg", "-i", f"assets/{mkv}", "-codec", "copy", f"result/{output_name}"], check=True
        )
    except:
        raise Exception(
            "Please setup FFmpeg!"
        )


print(f"{len(mkv_list)} video(s) converted to MP4!")

