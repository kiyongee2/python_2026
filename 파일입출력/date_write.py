
from datetime import datetime, date 

def write_date_to_file(file_path):
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Format the date and time as a string (e.g., "2024-06-01 12:34:56")
    datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    # Write the date and time string to the specified file
    with open(file_path, 'w') as file:
        file.write(datetime_string)
        
# Example usage
if __name__ == "__main__":
    write_date_to_file('output/current_datetime.txt') 