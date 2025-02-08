import subprocess
import time

# Set the program execution path.
programs = [
    r"C:\Users\PC\Desktop\Mudfish Launcher.lnk",  # Execution Mudfish vpn
    r"C:\Users\PC\Desktop\　\Play\game\Battlestate Games Launcher.lnk",  # Execution Tarkov
    r"C:\Windows\System32\nvcplui.exe"  # Execution Nvidia control panel
]

# 프로그램 실행
for program in programs:
    try:
        subprocess.Popen(program, shell=True)
        print(f"실행 중: {program}")
        time.sleep(1)  # 프로그램 실행 간 1초씩 대기
    except Exception as e:
        print(f"오류 발생: {program} 실행 실패 - {e}")

print("모든 프로그램 실행 완료!")