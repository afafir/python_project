import csv

char_blacklist = [
    "\n",
    "\t",
    "👌",
    "🥹",
    "🦖",
    "😊",
    "😎",
    "📎",
    "📣",
    "🧩",
    "📍",
    "❕",
    "🔝",
    "🤩",
    "📑",
    "📌",
    "🔥",
    "🏻",
    "🗓",
    "🔸",
    "❗",
    "🔻",
    "📢",
    "✍",
    "🗨",
    "👨",
    "💻",
    " ",
    "☝",
    "👉",
    "‍",
    "⚠",
    "👇",
    "🍀",
    "⃣",
    "🔹",
    "🏦",
    "☀",
    "!️",
    "1️",
    "2️",
    "3️",
    "4️",
    "5️",
    "6️",
    "7️" "Уважаемые студенты!",
    "Уважаемые студенты.",
    "Уважаемые студенты,",
]
with open("messages_itis_4_course.csv", mode="r") as in_file, open(
    "context.csv", mode="w"
) as out_file:
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)
    for row in reader:
        text: str = row[0]
        for char in char_blacklist:
            text = text.replace(char, "")
        text = text.replace("  ", "").strip()
        writer.writerow([text])
