from enum import Enum

PATH_SILVER_NYC = "./data/output/silver_nyc_parquet"
PATH_SILVER_CHICAGO = "./data/output/silver_chicago_parquet"
PATH_SILVER_MERGED = "./data/output/silver_merged_parquet"

LOCATION_LONGITUDE_NYC = -73.97
LOCATION_LATITUDE_NYC = 40.7
LOCATION_LINE_TOLERANCE = 1.0
TOTAL_AMOUNT_CALCULATED_TOLERANCE = 1.0
PASSENGER_MIN, PASSENGER_MAX = 0, 10
DISTANCE_MIN, DISTANCE_MAX = 0, 1_000
SECONDS_MIN, SECONDS_MAX = 0, 24 * 60 * 60
MILES_MIN, MILES_MAX = 0, 1000
FARE_MIN = TIPS_MIN = TOLLS_MIN = EXTRAS_MIN = TOTAL_MIN = MTA_TAX_MIN = SURCHARGE_MIN = 0
FARE_MAX = TIPS_MAX = TOLLS_MAX = EXTRAS_MAX = TOTAL_MAX = MTA_TAX_MAX = SURCHARGE_MAX = 1_000
DATETIME_ROUND_TOLERANCE = 60.0
CALCULATED_TOTAL_TOLERANCE = 1.0
COMMUNITY_AREAS_AMOUNT = 77


class VendorNYC(Enum):
    CREATIVE_MOBILE_TECHNOLOGIES = 1
    VERIFONE_INC = 2


class RateCodeNYC(Enum):
    STANDARD_RATE = 1
    JFK = 2
    NEWARDK = 3
    NASSAU_OR_WESTCHESTER = 4
    NEGOTIATED_FARE = 5
    GROUP_RIDE = 6


class PaymentTypeNYC(Enum):
    CREDIT_CARD = 1
    CASH = 2
    NO_CHARGE = 3
    DISPUTE = 4
    UNKNOWN = 5
    VOIDED_TRIP = 6


class PaymentTypeCHI(Enum):
    cash = "Cash"
    credit_card = "Credit Card"
    no_charge = "No Charge"
    unknown = "Unknown"
    dispute = "Dispute"
    pcard = "Pcard"
    prcard = "Prcard"


class City(Enum):
    NYC = "New York City"
    CHICAGO = "Chicago"


class PaymentType(Enum):
    CASH = 1
    CREDIT_CARD = 2
    NO_CHARGE = 3
    DISPUTE = 4
    UNKNOWN = 5
    VOIDED_TRIP_NYC = 6
    PRCARD_CHI = 7
