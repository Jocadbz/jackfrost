import os

profile_list = os.listdir("profile/")
print(f"{len(profile_list)} found")

def convert_jacktitas_to_macca(jacktitas):
    # Conversion rate: 1 Macca = 1,000 Jacktitas
    # Therefore, 1 Jacktita = 1 / 1000 Macca
    conversion_rate = 1 / 1000
    macca = jacktitas * conversion_rate
    macca = int(macca)
    return macca

for profile in profile_list:
    if open(f"profile/{profile}/coins", "r+").read() == '':
        with open(f'profile/{profile}/coins', 'w') as f:
            f.write("100")
    elif int(float(open(f"profile/{profile}/coins", "r+").read())) > 1000000000:
        with open(f'profile/{profile}/coins', 'w') as f:
            f.write("100")
        print(f"{profile} updated")
    elif int(float(open(f"profile/{profile}/coins", "r+").read())) < 1000:
        with open(f'profile/{profile}/coins', 'w') as f:
            f.write("100")
        print(f"{profile} updated")
    else:
        try:
            with open(f'profile/{profile}/coins', 'w') as f:
                f.write(str(convert_jacktitas_to_macca(int(float(open(f"profile/{profile}/coins", "r+").read())))))
        except:
            with open(f'profile/{profile}/coins', 'w') as f:
                f.write('100')
        print(f"{profile} updated")