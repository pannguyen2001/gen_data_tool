import pandas as pd
import numpy as np
from src.helpers.create_data_wrapper import create_data_wrapper
from src.helpers import generate_random_dates, generate_random_number, generate_hash_password, get_parent_module_path, create_prequisite_data
from src.utils.column_setup import AccountConfig, RoleConfig, CommonColumns
from src.utils import EMAIL_DOMAIN, PROVINCE, AVATAR_URL
from loguru import logger

@create_data_wrapper
@logger.catch
def create_account():
    """
    Create test account data.
    Returns:
        df (pd.DataFrame): A dataframe containing the new account data.
    """

    parent_module_path = get_parent_module_path(__name__)
    prequisite = AccountConfig.CREATE_ROLE.value

    df_role = create_prequisite_data(prequisite, f"{parent_module_path}.{prequisite}")

    amount_of_data= sum(list(AccountConfig.AMOUNT.value.values()))
    df = pd.DataFrame(index=range(amount_of_data))

    # role_id
    role_id = []
    for key, value in AccountConfig.AMOUNT.value.items():
        id_list = df_role[df_role[RoleConfig.NAME.value] == RoleConfig.ROLE_VALUES.value[key]][CommonColumns._ID.value].values.tolist() * value
        role_id.extend(id_list)

    df[AccountConfig.ROLE_ID.value] = role_id

    # full_name
    df[AccountConfig.FULL_NAME.value] = [f"test_user_{str(i+1).zfill(2)}" for i in range(df.shape[0])]

    # date_of_birth
    df[AccountConfig.DATE_OF_BIRTH.value] = generate_random_dates(n=df.shape[0])

    # gender
    df[AccountConfig.GENDER.value] = [np.random.choice([*AccountConfig.GENDER_VALUES.value.values()]) for _ in range(df.shape[0])]

    # address
    df[AccountConfig.ADDRESS.value] = np.random.choice(PROVINCE, df.shape[0])

    # email
    df[AccountConfig.EMAIL.value] = df[AccountConfig.FULL_NAME.value] + [np.random.choice(EMAIL_DOMAIN, 1)[0] for _ in range(df.shape[0])]

    # phone_number
    df[AccountConfig.PHONE_NUMBER.value] = [generate_random_number(10) for _ in range(df.shape[0])]

    # password
    df[AccountConfig.PASSWORD.value] = generate_hash_password(data_size=df.shape[0])

    # avata_url
    df[AccountConfig.AVATAR_URL.value] = AVATAR_URL

    # status
    df[AccountConfig.STATUS.value] = AccountConfig.STATUS_VALUES.value["active"]
    df.to_csv("account.csv", index=False)

    return df


