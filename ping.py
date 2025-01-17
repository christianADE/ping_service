import subprocess
import platform

plage = input("Entrez la plage d'adresse IP : ")

# Détecte l'option correcte en fonction du système d'exploitation
param = "-n" if platform.system().lower() == "windows" else "-c"

count = 0

for i in range(1, 256):
    ip = f"{plage}{i}"
    try:
        # Exécute la commande ping et capture la sortie
        result = subprocess.run(
            ["ping", param, "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if "unreachable" in result.stdout.lower() or "timed out" in result.stdout.lower():
            continue
        elif result.returncode == 0:
            count += 1
            print(f"{count}°) {ip} is up")
        else:
            print(ip, "is down")
    except Exception as e:
        print(f"Erreur avec l'adresse {ip}: {e}")
