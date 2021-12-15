with open("input.txt", "r") as file:
    passports = file.read().split("\n\n")

par = (
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid",
)

# Part1
valid = 0
for i, p in enumerate(passports):
    if all(e in p for e in par):
        valid += 1
print(valid)

# Part2
valid = 0
for i, p in enumerate(passports):
    dados = p.split()
    d = { d.split(":")[0] : d.split(":")[1] for d in dados }
    if (
        all(p in d for p in par)
        and "1920"<=d["byr"]<="2002"
        and "2010"<=d["iyr"]<="2020"
        and "2020"<=d["eyr"]<="2030"
        and ("150cm"<=d["hgt"]<="193cm" if "cm" in d["hgt"] else "59in"<=d["hgt"]<="76in")
        and len(d["hcl"]) == 7 and d["hcl"][0] == "#" and all("0"<=i<="9" or "a"<=i<="f" for i in d["hcl"][1:])
        and d["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        and len(d["pid"])==9 and "000000000"<=d["pid"]<="999999999"
    ):
        valid += 1
print(valid)