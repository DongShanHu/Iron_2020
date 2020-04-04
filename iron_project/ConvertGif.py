import imageio
import os

# 讀取檔案
file = os.path.abspath('2020_graduate_lunch.mp4')
# imageio.plugins.ffmpeg.download()


def Convert_to_GIF(inputPath, targetFormat):
    # print(inputPath)
    outputPath = os.path.splitext(inputPath)[0]+targetFormat
    # print(outputPath)
    print(f'convert{inputPath}  \n to {outputPath}')
    # 取得來源
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frame in reader:
        writer.append_data(frame)
        print(f'Frame{frame}')
    print("finished!!!!")
    writer.close()


Convert_to_GIF(file, '.gif ')
