import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# SourceData = spark.read.format('csv').options(header=True, inferSchema=True, encoding='utf-8').load('s3://bigdata-on-youtube-raw-apsouth1-krd-dev/youtube/raw-stats/')
# AWSGlueDataCatalog_node1644252652837 = DynamicFrame.fromDF(SourceData, glueContext, "AWSGlueDataCatalog_node1644252652837")

predicate_pushdown = "region in ('ca','gb','us')"

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1644252652837 = glueContext.create_dynamic_frame.from_catalog(
    database="db-youtube-raw",
    table_name="raw_stats",
    transformation_ctx="AWSGlueDataCatalog_node1644252652837",
    push_down_predicate = predicate_pushdown
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1644252652837,
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "long", "category_id", "bigint"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "long", "views", "bigint"),
        ("likes", "long", "likes", "bigint"),
        ("dislikes", "long", "dislikes", "bigint"),
        ("comment_count", "long", "comment_count", "bigint"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "boolean", "comments_disabled", "boolean"),
        ("ratings_disabled", "boolean", "ratings_disabled", "boolean"),
        ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"),
        ("description", "string", "description", "string"),
        ("region", "string", "region", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.getSink(
    path="s3://bigdata-on-youtube-cleansed-apsouth1-krd-dev/youtube/raw-stats/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="S3bucket_node3",
)
S3bucket_node3.setCatalogInfo(
    catalogDatabase="db-youtube-cleansed", catalogTableName="ref_stats"
)
S3bucket_node3.setFormat("glueparquet")
S3bucket_node3.writeFrame(ApplyMapping_node2)
job.commit()
