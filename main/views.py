from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Video
import subprocess

def upload_video(request):
    if request.method == 'POST':
        video = Video(video_file=request.FILES['video_file'], title=request.FILES['video_file'])
        video.save()
        encode_video(video.id)  # кодируем видео
        print(type(video.id))
        return HttpResponse("Video uploaded and encoding started.")
    return render(request, 'main/index.html')

def encode_video(video_id):
    video = Video.objects.get(id=video_id)
    video.is_encoding = True
    video.save()
    input_file = video.video_file.path
    print(input_file)
    output_file = r'C:\\Users\\Windows 10\\Desktop\\stazhirovka\\output\\output.m3u8'  # Путь к HLS-потоку
    command = ['ffmpeg',
                '-i',
                input_file,
                '-hls_time',
                '10',
                '-hls_list_size',
                '6',
                '-hls_flags',
                'delete_segments',
                output_file]
    subprocess.Popen(command)
    video.hls_url = r'C:\\Users\\Windows 10\\Desktop\\stazhirovka\\output\\output.m3u8'
    video.is_encoding = False
    video.save()

