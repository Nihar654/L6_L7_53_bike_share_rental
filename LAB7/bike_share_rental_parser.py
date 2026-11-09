def parse_ride_duration(text):
    """
    Converts a ride duration written as HH:MM into minutes.
    Returns None for invalid inputs.
    """
    if not isinstance(text, str):
        return None

    text = text.strip()

    if text.count(':') != 1:
        return None

    hours, minutes = text.split(':')

    if not hours.isdigit() or not minutes.isdigit():
        return None

    hours = int(hours)
    minutes = int(minutes)

    if minutes >= 60:
        return None

    return hours * 60 + minutes


def format_station_code(code):
    """
    Formats a station code as ZONE-NUMBER, e.g. 'a12' -> 'A-12'.
    Returns None for invalid inputs.
    """
    if not isinstance(code, str):
        return None

    code = code.strip().upper()

    if not code:
        return None

    return code[0] + '-' + code[1:]


def parse_ride_log(line):
    """
    Parses 'bike_type,minutes,subscriber' into a tuple.
    Returns None for invalid inputs.
    """
    if not isinstance(line, str):
        return None

    parts = line.split(',')

    if len(parts) != 3:
        return None

    bike_type = parts[0].strip()
    minutes_text = parts[1].strip()
    subscriber = parts[2].strip().lower()

    if not bike_type or not minutes_text:
        return None

    if not minutes_text.isdigit():
        return None

    if subscriber not in ('yes', 'no'):
        return None

    minutes = int(minutes_text)

    return bike_type, minutes, subscriber == 'yes'


def main():
    print("==== Running parse_ride_duration ====")
    value = input("Enter a ride duration as HH:MM (e.g. 01:15): ")
    print("Duration in minutes:", parse_ride_duration(value))

    print("\n==== Running format_station_code ====")
    value = input("Enter a station code (e.g. a12): ")
    print("Formatted station code:", format_station_code(value))

    print("\n==== Running parse_ride_log ====")
    value = input("Enter a ride log line as type,minutes,subscriber (e.g. electric,45,yes): ")
    print("Parsed ride log:", parse_ride_log(value))


if __name__ == "__main__":
    main()
