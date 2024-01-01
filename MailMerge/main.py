# Mail merge application

# Constants
NAME_PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_content = letter.read()
    with open("./Input/Names/invited_names.txt", mode="r") as invite_names:
        # Use readlines() for converting the content into a new list (Item per line)
        recipients = invite_names.readlines()
        for recipient in recipients:
            # Replacing the name, strip() trims the spaces around the String
            recipient_name = recipient.strip()
            addressed_letter = letter_content.replace(NAME_PLACEHOLDER, recipient_name)
            with open(f"./Output/ReadyToSend/letter_to_{recipient_name}.txt", mode="w") as completed_letter:
                completed_letter.write(addressed_letter)
