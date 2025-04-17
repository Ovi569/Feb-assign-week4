def read_and_modify_file():
    try:
        # Ask the user for the input filename
        input_filename = input(" enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        # Modify the content (example: convert all text to uppercase)
        modified_content = [line.upper() for line in content]

        # Ask the user for the output filename
        output_filename = input("Enter the name of the file to write the modified content: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content has been written to {output_filename} successfully!")

    except FileNotFoundError:
        print("Error: The file you specified does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
    