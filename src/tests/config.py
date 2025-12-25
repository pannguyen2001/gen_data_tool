from string import Template

not_in_result_error: str = Template("""${value} not in result.""")

error_messages: dict = {
    "not_in_result": not_in_result_error
}