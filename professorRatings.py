import os, re, requests, shutil
from datetime import datetime
from pathlib import Path
import ratemyprofessor


# Download the HTML content from the URL
url = "https://www.farmingdale.edu/course-offerings/fall_schd_2023.html"
response = requests.get(url)
html_content = response.text

# Create the target folder if it doesn't exist
folder_path = Path(os.getcwd(), "FSC WEBSITE1")
folder_path.mkdir(parents=True, exist_ok=True)

# Save the HTML content as a text file in the target folder
file_path = folder_path / "ss23.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

# Extract instructor names from the HTML content using regex
instructors = re.findall('<span style="top: \d+\.\d+pt; left: \d+\.\d+pt; margin-top:0pt;">(.*?)</span>', html_content)

# Remove duplicates in instructor names
unique_instructors = set()
for i in range(len(instructors)):
    if 'Instructor:' in instructors[i]:
        instructor_name = instructors[i+1].strip()
        unique_instructors.add(instructor_name)

# Format instructor names (remove "Dr." prefix and middle names)
formatted_names = {}
for instructor in unique_instructors:
    name = instructor.replace("Dr. ", "")
    name_parts = name.split()
    if len(name_parts) > 2:
        name_parts = [name_parts[0], name_parts[-1]]
        name = " ".join(name_parts)
    formatted_names[instructor] = name
# Get ratings for all professors
college = ratemyprofessor.get_school_by_name("Farmingdale State College")
professor_ratings = {}
for name in formatted_names.values():
    if name == "STAFF":
        professor_ratings[name] = " - Professor has not been chosen yet"
    else:
        professor = ratemyprofessor.get_professor_by_school_and_name(college, name.strip())
        if professor is not None:
            if professor.would_take_again is not None and professor.would_take_again != -1:
                rating_info = f" - Rating: {professor.rating}/5.0, Difficulty: {professor.difficulty}, Total Ratings: {professor.num_ratings}, Would Take Again: {round(professor.would_take_again, 1)}%"
            else:
                rating_info = f" - Rating: {professor.rating}/5.0, Difficulty: {professor.difficulty}, Total Ratings: {professor.num_ratings}"
            professor_ratings[name] = rating_info
        else:
            professor_ratings[name] = " - Professor does not have any ratings or could not be found"
# Generate a timestamp to append to the filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# Create a copy of the ss23.txt file with the timestamp in its name
shutil.copyfile(file_path, folder_path / f'ss23_{timestamp}.txt')

# Open the copy of ss23.txt and make changes to it
with open(folder_path / f'ss23_{timestamp}.txt', 'r+', encoding='UTF8') as f:
    ss23 = f.readlines()
    f.seek(0)
    head_found = False

    for i, line in enumerate(ss23):
        if '<head>' in line and not head_found:
            f.write(line)
            f.write('<!-- Google tag (gtag.js) -->\n')
            f.write('<script async src="https://www.googletagmanager.com/gtag/js?id=G-B42PSGK3GM"></script>\n')
            f.write('<script>\n')
            f.write('  window.dataLayer = window.dataLayer || [];\n')
            f.write('  function gtag(){dataLayer.push(arguments);}\n')
            f.write("  gtag('js', new Date());\n")
            f.write("  gtag('config', 'G-B42PSGK3GM');\n")
            f.write('</script>\n')
            head_found = True
        elif '/course-offerings/' in line:
            new_line = line.replace('/course-offerings/', '')
            f.write(new_line)
        elif '.gif' in line:
            new_line = line.replace('/images/', '')
            f.write(new_line)
        elif "fall_schd_2023.css" in line:
            new_line = line.replace("fall_schd_2023.css", "spring_schd_2023.css")
            f.write(new_line)
        else:
            for orig_name, formatted_name in formatted_names.items():
                rating = professor_ratings[formatted_name]
                if orig_name in line:
                    new_line = line.replace(orig_name, f"{orig_name}{rating}")
                    f.write(new_line)
                    break
            else:
                f.write(line)

    f.truncate()

