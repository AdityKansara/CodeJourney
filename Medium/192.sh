# Read words.txt, split into one word per line
# sort them alphabetically
# uniq -c counts consecutive duplicates
# sort -rnk1 sorts numerically by count, descending
# awk formats output as "word count"
tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -rnk1 | awk '{print $2, $1}'

# tr -s ' ' '\n' → turn spaces into newlines so each word is on its own line.

# sort → group identical words together.

# uniq -c → count occurrences of each word.

# sort -rnk1 → sort results numerically (-n) by first column (count), reverse order (-r).

# awk '{print $2, $1}' → swap order so output is "word count".