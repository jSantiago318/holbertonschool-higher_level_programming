#!/usr/bin/python3
"""Generate personalized invitation files from a template and attendee data."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees.

    Each attendee produces a file named ``output_X.txt`` where ``X`` is the
    attendee's 1-based index. Missing placeholder values are replaced by
    ``"N/A"``.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of dictionaries holding attendee data.
    """
    # Validate the type of the template.
    if not isinstance(template, str):
        print("Error: template must be a string, got {}.".format(
            type(template).__name__))
        return

    # Validate that attendees is a list of dictionaries.
    if not isinstance(attendees, list):
        print("Error: attendees must be a list, got {}.".format(
            type(attendees).__name__))
        return
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Handle an empty template.
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle an empty list of attendees.
    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        with open("output_{}.txt".format(index), "w") as output_file:
            output_file.write(output)
