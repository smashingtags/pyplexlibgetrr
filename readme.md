# pyplexlibgetrr

This is a Python script that uses the Plex API to retrieve user data and count the number of files in each library.

## Usage

```git clone https://github.com/smashingtags/pyplexlibgetrr.git```


1. Replace the `base_url` and `token` variables with the URL of your Plex server and your Plex API token, respectively.
2. Run the script using `python pyplexlib.py`.
3. The script will output a list of all your users and their libraries with the corresponding file counts.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

## Example Output

User: Alice
Movies: 1234 files
TV Shows: 567 files
User: Bob
Movies: 678 files
TV Shows: 901 files


## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
