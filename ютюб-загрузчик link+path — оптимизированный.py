from pytube import YouTube
import os

yt = YouTube(
	str(input("Введи ссылку на ютюб: \n>> ")))

# https://www.youtube.com/watch?v=o_v9MY_FMcw&ab_channel=OneDirectionVEVO

video = yt.streams.get_highest_resolution()

print("Введи путь сохранения (жми enter для сохранения в текущей папке)")
destination = str(input(">> ")) or '.'

try:
    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
except:
	print("Ошибка!")

# result of success
print(yt.title + " успешна загружена.")

