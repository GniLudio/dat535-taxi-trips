from pyspark.sql import SparkSession


def setup_spark(
    app_name: str = "DAT535-Taxi-Trips",
    title: str = "",
    *,
    show_progress: bool = True,
) -> SparkSession:
    spark = (
        SparkSession.builder.appName(f"{app_name} - {title}")
        .master("spark://group-11:7077")
        .config("spark.sql.adaptive.enabled", "true")
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
        .config("spark.executor.cores", "4")
        .config("spark.executor.memory", "4g")
        .config("spark.driver.memory", "2g")
        .config("spark.ui.showConsoleProgress", "true" if show_progress else "false")
        .getOrCreate()
    )
    spark.sparkContext.addPyFile("shared.py")
    return spark
