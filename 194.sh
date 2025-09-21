# #Transpose File - Bash/AWK
# Problem solved by Adity
# Time Complexity: O(n*m) - n = number of rows, m = number of columns
# Space Complexity: O(n*m) - stores all elements in array a[i, NR]

awk '
{
    # Loop through each field (column) in the current line
    for (i = 1; i <= NF; i++) {
        a[i, NR] = $i    # Store value in array at position (column i, row NR)
    }
    if (NF > p) { p = NF }  # Keep track of max number of columns
}
END {
    # Loop through each "column" of the original file to form transposed rows
    for (i = 1; i <= p; i++) {
        str = a[i, 1]       # Start the transposed row with first element
        for (j = 2; j <= NR; j++) {
            str = str " " a[i, j]   # Append remaining elements of column i
        }
        print str            # Print the transposed row
    }
}' file.txt



#======================================================
#shorter solution
#======================================================
# awk '
# {
#     for (i=1; i<=NF; i++) a[i]=(a[i]?a[i]" ":"") $i
# }
# END { for (i=1; i<=NF; i++) print a[i] }' file.txt
