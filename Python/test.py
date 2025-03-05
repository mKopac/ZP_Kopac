import time
import subprocess

start_time = time.time()
subprocess.run(["C:/Users/marti/AppData/Local/Programs/Python/Python312/Scripts/black.exe", "1.py"])
end_time = time.time()

print(f"Formátovanie trvalo {end_time - start_time} sekúnd.")
