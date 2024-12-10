import os

INITIAL = "StartingXYZ"
OUTPUT = "OptXYZ"


files = [file for file in os.listdir(INITIAL) if (".xyz" in file)] # Reading for the list of files in INITIAL that are .xyz files

for f in files:
    with open(f"{INITIAL}/{f[:-4]}.inp", "w", encoding="utf-8") as file: # Creating the files
        file.write(f"$write\n  output file = {OUTPUT}/{f[:-4]}.out") # Saving the outputs to OUTPUT path

    with open("runall-opt.sh", "a", encoding="utf-8") as sh:
        sh.write(f"# {f[:-4]}\n")
        sh.write(f"xtb {INITIAL}/{f} --input {INITIAL}/{f[:-4]}.inp --gbsa H2O --opt --chr\n")
        sh.write(f"mv xtbopt.xyz Opt-{OUTPUT}/{f}\n")
