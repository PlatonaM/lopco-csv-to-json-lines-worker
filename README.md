#### Description

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

Fields containing a "sub table" must be declared via the `sub_table_headers` config option:
    
    field_name_A:sub_field_name_a;sub_field_name_b,field_name_B:sub_field_name_a

Set the delimiters for "sub tables" via `sub_table_delimiters`.

Provide data types (`float`, `int`, `bool`) for certain fields with `data_types` (if omitted all fields will be treated as strings):

    float:field_name_C;field_name_D,int:field_name_A_sub_field_name_a;field_name_B_sub_field_name_a
