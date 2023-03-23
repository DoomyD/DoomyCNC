# Open the input file for reading
with open("g2.gc", "r") as input_file:
    # Read the content of the input file
    content = input_file.read()

# Modify the content by adding "M4" before any "S" letter found
modified_content = ""
for line in content.split("\n"):
    if "S" in line:
        parts = line.split("S")
        # Check if there are digits on the right side of the "S"
        if parts[1]:
            digit_count = 0
            for char in parts[1]:
                if char.isdigit():
                    digit_count += 1
                else:
                    break
            if digit_count > 0:
                new_line = parts[0] + parts[1][digit_count:] + "\n"
                modified_line = "M4 S" + parts[1][:digit_count]
                modified_content += new_line + modified_line + "\n"
            else:
                # modified_line = "M4" + line
                # modified_content += modified_line + "\n"
                print("Error")
        else:
            modified_line = "M4" + line
            modified_content += modified_line + "\n"
    else:
        modified_content += line + "\n"

print(modified_content)