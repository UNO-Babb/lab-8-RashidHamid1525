def main():
    with open("names.dat", "r") as infile, open("StudentList.csv", "w") as outfile:
        infile.readline()

        for line in infile:
            if line.strip() == "":
                continue

            if "|" in line:
                parts = [p.strip() for p in line.strip().split("|")]
            else:
                parts = line.strip().split()

            if len(parts) < 7:
                continue

            first = parts[0]
            last = parts[1]
            student_id = parts[3]
            year = parts[5]
            major = parts[6]

            last3 = student_id[-3:]
            userid = first[0].lower() + last.lower() + last3
            last = last.ljust(5, "X")
            major_abbrev = major[:3].upper()

            if year.lower().startswith("fresh"):
                year_abbrev = "FR"
            elif year.lower().startswith("soph"):
                year_abbrev = "SO"
            elif year.lower().startswith("jun"):
                year_abbrev = "JR"
            elif year.lower().startswith("sen"):
                year_abbrev = "SR"
            else:
                year_abbrev = "NA"

            major_year = f"{major_abbrev}-{year_abbrev}"
            outfile.write(f"{last},{first},{userid},{major_year}\n")

    print("File 'StudentList.csv' created successfully!")


if __name__ == "__main__":
    main()
