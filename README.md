# OpenTargets
# Test A
Files for test A contains all requirement methods for parsing json-file with Python default library for bets perfomance. If program runs without any arguments it shows total overall scrore (with standart deviation, mean, max and min). Program supports all requirement agruments and handle exceptions if it runs with too many or not enought arguments. Unit testing is  built-in program and starts with parameter "--test". The test checks program output to stdout and compares it with already valid output.

# Test B
Files for test B contain methods for processing the file with series of JSON objects. Program reads file line by line and process each line as normal json-object and store all needed information in [Python] dictionary. After that program process the dictionary and save it as CSV-file. For large amount of data (like this case) using database should be more efficent.
