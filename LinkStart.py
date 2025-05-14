import subprocess
import time
import sys

def run_radar_setup():
    try:
        # 第一部分：设置串口权限
        print("Setting serial port permissions...")
        subprocess.run(
            ["sudo", "chmod", "777", "/dev/ttyUSB0"],
            check=True,
            stderr=subprocess.PIPE
        )

        # 第二部分：运行标定脚本
        print("Starting calibration...")
        calibration_process = subprocess.Popen(
            ["python3", "calibration.py"],
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        calibration_process.wait()  # 等待标定完成

        # 等待1秒
        print("Calibration completed. Waiting 1 second...")
        time.sleep(1)

        # 第三部分：运行主程序
        print("Starting main application...")
        main_process = subprocess.Popen(
            ["python3", "main.py"],  # 如果使用虚拟环境，请替换为实际路径
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        main_process.wait()

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode()}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
        sys.exit(0)

if __name__ == "__main__":
    run_radar_setup()