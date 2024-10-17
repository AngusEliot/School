import csv

def read_csv_to_bitmap(file_path):
    bitmap = []
    
    # Open and read the CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            bitmap_row = []
            for number in row:
                bitmap_row.append(int(number))  # Convert each cell to an integer
            bitmap.append(bitmap_row)  # Add the row to the bitmap
    
    return bitmap

def print_bitmap(bitmap):
    # Mapping of values to characters using a dictionary
    mapping = {
        0: ' ',  # Space
        1: '*',  # Asterisk
        2: '█'   # Block
    }
    
    # Convert the bitmap to a string and print it
    for row in bitmap:
        line = ''
        for cell in row:
            line += mapping[cell]  # Append the corresponding character
        print(line)

# Example usage
file_path = 'image012.csv'  # Replace with your CSV file path
bitmap = read_csv_to_bitmap(file_path)
print_bitmap(bitmap)


#Challenges!!!!

#1 can you create a function that doubles the size of the image? (print every character twice, and every line twice?)

#2 Can you create a function that creates a compressed file using RLE?

#3 Can you create a function that reads your compressed file, so that print_bitmap() can be successfully called on it?
