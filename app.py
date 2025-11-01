import pandas as pd
import timeit
from src import logger, database, create_data
from src.utils import DB_TYPE
from src.utils.cache_store import clear_all_cache, ttl_cache

logger.info("Starting the application")
logger.info(f"TTL cache ID: {id(ttl_cache)}")

# Mapping function data
create_data_function_mapping = {
    "role": create_data.create_role,
    "account": create_data.create_account,
    "course_category": create_data.create_course_category,
    "teacher_academic": create_data.create_teacher_academic,
    "teacher_degree": create_data.create_teacher_degree,
    "student": create_data.create_student,
    "teacher": create_data.create_teacher,
    "course": create_data.create_course,
    "course_student": create_data.create_course_student,
    "student_rating": create_data.create_student_rating,
}
final_result = []
connection = database.connect_db.connnect_db(DB_TYPE)

input = input("Enter the function name: ")
if input in create_data_function_mapping.keys():
    final_result.append(create_data_function_mapping[input]())
elif input == "all":
    for func in create_data_function_mapping.values():
        final_result.append(func())
else:
    logger.error(f"Function {input} not found")

if connection is not None:
    # Save data to database
    save_to_db_start = timeit.default_timer()
    database.save_data_to_db(DB_TYPE, connection)
    save_to_db_end = timeit.default_timer()
    save_to_db_total_time = save_to_db_end - save_to_db_start

    # Count total time
    df_final_result = pd.DataFrame(final_result)
    total_time = round(df_final_result["time"].sum() + save_to_db_total_time, 2)
    avg_time = round(df_final_result["time"].mean() + save_to_db_total_time/df_final_result.shape[0],2)
    # logger.info(f"\n{df_final_result}")
    logger.info(f"Total create time (s): {total_time}")
    logger.info(f"Average create time (s): {avg_time}")

    # Disconnect database
    database.disconnect_db(DB_TYPE, connection)

# Clear cache
clear_all_cache()
logger.info(f"Cache cleared: {id(ttl_cache)}")