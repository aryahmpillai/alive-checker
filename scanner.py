print("""

   
  /$$$$$$  /$$       /$$$$$$ /$$    /$$ /$$$$$$$$        /$$$$$$  /$$   /$$ /$$$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$      |_  $$_/| $$   | $$| $$_____/       /$$__  $$| $$  | $$| $$_____/ /$$__  $$| $$  /$$/| $$_____/| $$__  $$
| $$  \ $$| $$        | $$  | $$   | $$| $$            | $$  \__/| $$  | $$| $$      | $$  \__/| $$ /$$/ | $$      | $$  \ $$
| $$$$$$$$| $$        | $$  |  $$ / $$/| $$$$$         | $$      | $$$$$$$$| $$$$$   | $$      | $$$$$/  | $$$$$   | $$$$$$$/
| $$__  $$| $$        | $$   \  $$ $$/ | $$__/         | $$      | $$__  $$| $$__/   | $$      | $$  $$  | $$__/   | $$__  $$
| $$  | $$| $$        | $$    \  $$$/  | $$            | $$    $$| $$  | $$| $$      | $$    $$| $$\  $$ | $$      | $$  \ $$
| $$  | $$| $$$$$$$$ /$$$$$$   \  $/   | $$$$$$$$      |  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$  | $$
|__/  |__/|________/|______/    \_/    |________/       \______/ |__/  |__/|________/ \______/ |__/  \__/|________/|__/  |__/
                                                                                                                             
                                                                                                                             
                                                                                                                                      

""")


import requests

alive_count = 0


def alive_checker(site):

    global alive_count

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(site, headers=headers, timeout=3)

        if r.status_code == 200:

            alive_count += 1

            print(f"[200] ---> {site}")

            with open("alive.txt", "a") as f:

                f.write(site + "\n")

    except:
        pass


target_name = input("ENTER FILE : ").strip()


with open(target_name) as arya:

    for line in arya:

        alive_checker(line.strip())


print(f"\nTOTAL ALIVE HOSTS : {alive_count}")