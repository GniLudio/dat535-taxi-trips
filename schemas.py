from pyspark.sql import types as t

schema_nyc_bronze = t.StructType(
    [
        t.StructField("VendorID", t.StringType()),
        t.StructField("tpep_pickup_datetime", t.StringType()),
        t.StructField("tpep_dropoff_datetime", t.StringType()),
        t.StructField("passenger_count", t.StringType()),
        t.StructField("trip_distance", t.StringType()),
        t.StructField("pickup_longitude", t.StringType()),
        t.StructField("pickup_latitude", t.StringType()),
        t.StructField("RateCodeID", t.StringType()),
        t.StructField("store_and_fwd_flag", t.StringType()),
        t.StructField("dropoff_longitude", t.StringType()),
        t.StructField("dropoff_latitude", t.StringType()),
        t.StructField("payment_type", t.StringType()),
        t.StructField("fare_amount", t.StringType()),
        t.StructField("extra", t.StringType()),
        t.StructField("mta_tax", t.StringType()),
        t.StructField("tip_amount", t.StringType()),
        t.StructField("tolls_amount", t.StringType()),
        t.StructField("improvement_surcharge", t.StringType()),
        t.StructField("total_amount", t.StringType()),
    ],
)


schema_chicago_bronze = t.StructType(
    [
        t.StructField("taxi_id", t.IntegerType()),
        t.StructField("trip_start_timestamp", t.TimestampType()),
        t.StructField("trip_end_timestamp", t.TimestampType()),
        t.StructField("trip_seconds", t.IntegerType()),
        t.StructField("trip_miles", t.FloatType()),
        t.StructField("pickup_census_tract", t.IntegerType()),
        t.StructField("dropoff_census_tract", t.IntegerType()),
        t.StructField("pickup_community_area", t.IntegerType()),
        t.StructField("dropoff_community_area", t.IntegerType()),
        t.StructField("fare", t.FloatType()),
        t.StructField("tips", t.FloatType()),
        t.StructField("tolls", t.FloatType()),
        t.StructField("extras", t.FloatType()),
        t.StructField("trip_total", t.FloatType()),
        t.StructField("payment_type", t.StringType()),
        t.StructField("company", t.IntegerType()),
        t.StructField("pickup_latitude", t.IntegerType()),
        t.StructField("pickup_longitude", t.IntegerType()),
        t.StructField("pickup_location", t.StringType()),
        t.StructField("dropoff_latitude", t.IntegerType()),
        t.StructField("dropoff_longitude", t.IntegerType()),
        t.StructField("dropoff_location", t.StringType()),
    ]
)

schema_nyc_silver = t.StructType(
    [
        t.StructField("VendorID", t.IntegerType(), nullable=False),
        t.StructField("tpep_pickup_datetime", t.TimestampType(), nullable=False),
        t.StructField("tpep_dropoff_datetime", t.TimestampType(), nullable=False),
        t.StructField("passenger_count", t.IntegerType(), nullable=False),
        t.StructField("trip_distance", t.FloatType(), nullable=False),
        t.StructField("pickup_longitude", t.FloatType()),
        t.StructField("pickup_latitude", t.FloatType()),
        t.StructField("RateCodeID", t.IntegerType(), nullable=False),
        t.StructField("store_and_fwd_flag", t.BooleanType(), nullable=False),
        t.StructField("dropoff_longitude", t.FloatType()),
        t.StructField("dropoff_latitude", t.FloatType()),
        t.StructField("payment_type", t.IntegerType(), nullable=False),
        t.StructField("fare_amount", t.FloatType(), nullable=False),
        t.StructField("extra", t.FloatType(), nullable=False),
        t.StructField("mta_tax", t.FloatType(), nullable=False),
        t.StructField("tip_amount", t.FloatType(), nullable=False),
        t.StructField("tolls_amount", t.FloatType(), nullable=False),
        t.StructField("improvement_surcharge", t.FloatType(), nullable=False),
        t.StructField("total_amount", t.FloatType(), nullable=False),
    ],
)
schema_nyc_dropped_silver = t.StructType(
    [
        t.StructField("reason", t.StringType(), nullable=False),
        *schema_nyc_bronze.fields,
    ],
)

schema_chicago_silver = t.StructType(
    [
        t.StructField("taxi_id", t.IntegerType()),
        t.StructField("trip_start_timestamp", t.TimestampType()),
        t.StructField("trip_end_timestamp", t.TimestampType()),
        t.StructField("trip_seconds", t.IntegerType()),
        t.StructField("trip_miles", t.FloatType()),
        t.StructField("pickup_census_tract", t.IntegerType()),
        t.StructField("dropoff_census_tract", t.IntegerType()),
        t.StructField("pickup_community_area", t.IntegerType()),
        t.StructField("dropoff_community_area", t.IntegerType()),
        t.StructField("fare", t.FloatType()),
        t.StructField("tips", t.FloatType()),
        t.StructField("tolls", t.FloatType()),
        t.StructField("extras", t.FloatType()),
        t.StructField("trip_total", t.FloatType()),
        t.StructField("payment_type", t.StringType()),
        t.StructField("company", t.IntegerType()),
        t.StructField("pickup_latitude", t.IntegerType()),
        t.StructField("pickup_longitude", t.IntegerType()),
        t.StructField("pickup_location", t.StringType()),
        t.StructField("dropoff_latitude", t.IntegerType()),
        t.StructField("dropoff_longitude", t.IntegerType()),
        t.StructField("dropoff_location", t.StringType()),
    ]
)
schema_chicago_dropped_silver = t.StructType(
    [
        t.StructField("reason", t.StringType(), nullable=False),
        *schema_chicago_bronze.fields,
    ],
)


schema_merged_silver: t.StructType = t.StructType(
    [
        # ADDED
        t.StructField("city", t.StringType(), nullable=False),
        t.StructField("duration_minutes", t.IntegerType(), nullable=False),
        t.StructField("speed_mph", t.FloatType(), nullable=True),
        t.StructField("tip_pct", t.FloatType(), nullable=True),
        # BOTH
        t.StructField("datetime_start", t.TimestampType(), nullable=False),
        t.StructField("datetime_end", t.TimestampType(), nullable=False),
        t.StructField("distance_miles", t.FloatType(), nullable=False),
        t.StructField("payment_type", t.IntegerType(), nullable=False),
        t.StructField("fare_amount", t.FloatType(), nullable=False),
        t.StructField("extra_amount", t.FloatType(), nullable=False),
        t.StructField("tip_amount", t.FloatType(), nullable=False),
        t.StructField("tolls_amount", t.FloatType(), nullable=False),
        t.StructField("total_amount", t.FloatType(), nullable=False),
        # NYC
        t.StructField("vendor_nyc", t.IntegerType(), nullable=True),
        t.StructField("passenger_count_nyc", t.IntegerType(), nullable=True),
        t.StructField("rate_code_nyc", t.IntegerType(), nullable=True),
        t.StructField("mta_tax_amount_nyc", t.FloatType(), nullable=True),
        t.StructField("improvement_surcharge_amount_nyc", t.FloatType(), nullable=True),
        # CHICAGO
        t.StructField("taxi_id_chi", t.IntegerType(), nullable=True),
        t.StructField("community_area_pickup_chi", t.IntegerType(), nullable=True),
        t.StructField("community_area_dropoff_chi", t.IntegerType(), nullable=True),
        t.StructField("company_chi", t.IntegerType(), nullable=True),
    ],
)
