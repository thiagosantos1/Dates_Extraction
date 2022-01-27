# Dates Extraction Pipeline

This is the code repository for dates extraction using rule-base rules. You can add your own rule-base rules inside of config file (src/config.py)


## Install Dependencies
```bash
pip3 install -r requirements.txt
```

## How to Use the API

You can run the API witht the following script:

```shell
python3 src/main.py --task
```

|Task Input Option| Description            |
|------------|-----------------------------|
|match_dates   | Match any date of a giving tex based on available rules inside of config file                 |
|regex_matches  | Giver a text and which rule to use, return all matches |
|format_date        | Format any date input to a standard date format                         |
|is_date  | Return whether the string can be interpreted as a date                  |


### More details of each available function, including required inputs and return type can be found by running

```shell
python3 src/main.py --help
```



## Example of Extracting Dates using task match_dates

|Input Option| Description            |
|------------|-----------------------------|
|text   | A full text to be annalysed                |
|format  | whether or not to format the output to string |
|eightify        | change all number to 8 (helps on de-identification)                         |
|rules  | Please provide your rule-based rules inside of config.py                  |


```shell
python3 main.py match_dates --text "this is a test with date of 05-02-1998 and also includes 28/12/2022 and can have the format of January, 12 1994. end of example" --format True
```

### Output Example

```json
{"regex_output": {"start": 28, "end": 38, "token": "05-02-1998", "source": "Regex", "type": "Dates"}, "token": "1998-05-02"}
{"regex_output": {"start": 57, "end": 67, "token": "28/12/2022", "source": "Regex", "type": "Dates"}, "token": "2022-12-28"}
{"regex_output": {"start": 95, "end": 111, "token": "January, 12 1994", "source": "Regex", "type": "Dates"}, "token": "1994-01-12"}

```

```shell
python3 main.py match_dates --text "this is a test with date of 05-02-1998 and also includes 28/12/2022 and can have the format of January, 12 1994. end of example" --format False
```

### Output Example

```json
{"regex_output": {"start": 28, "end": 38, "token": "05-02-1998", "source": "Regex", "type": "Dates"}, "token": "05-02-1998"}
{"regex_output": {"start": 57, "end": 67, "token": "28/12/2022", "source": "Regex", "type": "Dates"}, "token": "28/12/2022"}
{"regex_output": {"start": 95, "end": 111, "token": "January, 12 1994", "source": "Regex", "type": "Dates"}, "token": "January, 12 1994"}
```


```shell
python3 main.py match_dates --text "this is a test with date of 05-02-1998 and also includes 28/12/2022 and can have the format of January, 12 1994. end of example" --eightify True --format True
```

### Output Example


```json
{"regex_output": {"start": 28, "end": 38, "token": "05-02-1998", "source": "Regex", "type": "Dates"}, "token": "8888-88-88"}
{"regex_output": {"start": 57, "end": 67, "token": "28/12/2022", "source": "Regex", "type": "Dates"}, "token": "8888-88-88"}
{"regex_output": {"start": 95, "end": 111, "token": "January, 12 1994", "source": "Regex", "type": "Dates"}, "token": "8888-88-88"}
```


```shell
python3 main.py match_dates --text "this is a test with date of 05-02-1998 and also includes 28/12/2022 and can have the format of January, 12 1994. end of example" --eightify True --format False
```

### Output Example

```json
{"regex_output": {"start": 28, "end": 38, "token": "05-02-1998", "source": "Regex", "type": "Dates"}, "token": "88-88-8888"}
{"regex_output": {"start": 57, "end": 67, "token": "28/12/2022", "source": "Regex", "type": "Dates"}, "token": "88/88/8888"}
{"regex_output": {"start": 95, "end": 111, "token": "January, 12 1994", "source": "Regex", "type": "Dates"}, "token": "January, 88 8888"}
```




