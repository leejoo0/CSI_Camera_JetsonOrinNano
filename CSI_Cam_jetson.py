import subprocess
import signal
import os

def run_gstreamer_pipeline():
    # GStreamer 파이프라인 명령어
    pipeline = "gst-launch-1.0 nvarguscamerasrc sensor_id=0 ! \
                'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1' ! \
                nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=540' ! \
                nvvidconv ! nvegltransform ! nveglglessink -e"

    # 파이프라인 실행
    process = subprocess.Popen(pipeline, shell=True, preexec_fn=os.setsid)

    try:
        # 사용자 입력을 대기하고 'q'를 누를 때까지 실행
        while True:
            user_input = input("Press 'q' to quit: ")
            if user_input.lower() == 'q':
                # 파이프라인이 실행 중인 프로세스 그룹을 종료
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                break
    except KeyboardInterrupt:
        pass  # Ctrl+C를 눌러도 종료

if __name__ == "__main__":
    run_gstreamer_pipeline()
