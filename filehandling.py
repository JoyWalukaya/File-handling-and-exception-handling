def read_and_write():
    try:
        # Ask user for input file name
        input_filename = input("Enter the filename to read: ")

        # Open the file for reading
        with open(input_filename, "r") as file:
            content = file.read()

        # Modify content ( convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File successfully modified and saved as '{output_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. You don’t have access to this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

read_and_write()
