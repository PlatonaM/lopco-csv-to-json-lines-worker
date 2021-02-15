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
            "use_null": "0"
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
