## lopco-csv-to-json-lines-worker

Converts each row of a CSV file to a JSON object and saves these objects as rows of a new file.

### Configuration

`delimiter`: Delimiter used in the CSV file.

`sub_table_headers`: Declare columns containing "sub tables" here by using the following notation: `column_name_A:sub_column_name_a;sub_column_name_b,column_name_B:sub_column_name_a`

`sub_table_delimiters`: Set the delimiters used by "sub tables".

`data_types`: Provide data types (`float`, `int`, `bool`) for selected columns by using the following notation: `float:column_name_C;column_name_D,int:column_name_A.sub_column_name_a;column_name_B.sub_column_name_a`
(omitted columns will will be treated as strings)

### Inputs

Type: single

`source_csv`: Input CSV file.

### Outputs

Type: single

`output_file`: File containing JSON objects.

### Description

    {
        "name": "CSV To JSON Lines",
        "image": "platonam/lopco-csv-to-json-lines-worker:dev",
        "data_cache_path": "/data_cache",
        "description": "Convert a Comma-Separated Values files to JSON lines.",
        "configs": {
            "delimiter": null,
            "sub_table_headers": null,
            "sub_table_delimiters": null,
            "data_types": null
        },
        "input": {
            "type": "single",
            "fields": [
                {
                    "name": "source_csv",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "output": {
            "type": "single",
            "fields": [
                {
                    "name": "output_file",
                    "media_type": "text/plain",
                    "is_file": true
                }
            ]
        }
    }
