import atexit
import os
import subprocess
import sys

APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Запускает API-сервис на фоне
def start_fastapi() -> subprocess.Popen:
    return subprocess.Popen([sys.executable, os.path.join(APP_DIR, "API.py")])

# Запускает Веб-приложение
def start_dash() -> int:
    return subprocess.call([sys.executable, os.path.join(APP_DIR, "app.py")])


def main() -> int:
    fastapi_process = start_fastapi()
    # Выключает API-сервис
    def cleanup() -> None:
        if fastapi_process.poll() is None:
            fastapi_process.terminate()
            try:
                fastapi_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                fastapi_process.kill()

    atexit.register(cleanup)

    try:
        return start_dash()
    finally:
        cleanup()


if __name__ == "__main__":
    raise SystemExit(main())