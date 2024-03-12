import subprocess


def push_rtsp_stream(source, stream_id=0):
    command = [
        'ffmpeg',
        '-re',  # 以本地帧速率发送流
        '-stream_loop', '-1',  # 循环播放
        '-i', source,
        '-rtsp_transport', 'tcp',  # 传输协议
        # '-bufsize', '1000000k',
        # '-preset:v', 'ultrafast',
        # '-tune:v', 'zerolatency',
        '-vcodec', 'copy',
        # '-acodec', 'aac',
        '-f', 'rtsp',
        'rtsp://127.0.0.1:8554/stream' + str(stream_id)
    ]
    subprocess.Popen(command)


if __name__ == "__main__":
    source = [
        r'E:\Projects\test_data\video\MOT\MOT16\train\MOT16-09.mp4',
        r'E:\Projects\test_data\video\MOT\MOT16\train\MOT16-10.mp4',
        r'E:\Projects\test_data\video\MOT\MOT16\train\MOT16-11.mp4',
        r'E:\Projects\test_data\video\MOT\MOT16\train\MOT16-13.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\test\MOT17-01.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\test\MOT17-03.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\test\MOT17-07.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\test\MOT17-08.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\test\MOT17-12.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\test\MOT17-14.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\train\MOT17-02.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\train\MOT17-04.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\train\MOT17-09.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\train\MOT17-10.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\train\MOT17-11.mp4',
        r'E:\Projects\test_data\video\MOT\MOT17\train\MOT17-13.mp4',
    ]
    for i, s in enumerate(source):
        push_rtsp_stream(s, i)
    while True:
        pass
