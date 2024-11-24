import subprocess


def run_app_1_service():
    subprocess.Popen(["C:\\D\\base_dbms\\venv\\Scripts\\python", "driver_app/app.py"])

def run_app_2_service():
    subprocess.Popen(["C:\\D\\base_dbms\\venv\\Scripts\\python", "metro_app/app.py"])

def run_app_3_service():
    subprocess.Popen(["C:\\D\\base_dbms\\venv\\Scripts\\python", "user_app/app.py"])

if __name__ == '__main__':
    run_app_1_service()
    run_app_2_service()
    run_app_3_service()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating all processes. Alvida!")
