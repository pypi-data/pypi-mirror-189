# sts_credentials
get sts credentials tools, use pydantic for autocompletion.

now support
 - Alibaba Cloud OSS 
 - qcloud cos

```python
from sts_credentials.credentials.oss import get_credential_oss
from sts_credentials.credentials.cos import get_credential_cos
from secrets_for_test import (
    aliyun_access_key_id,
    aliyun_access_key_secret,
    aliyun_bucket,
    aliyun_region,
    aliyun_role_arn,
    qcloud_bucket,
    qcloud_region,
    qcloud_secret_id,
    qcloud_secret_key,
)

print(
    get_credential_oss(
        access_key_id=aliyun_access_key_id,
        access_key_secret=aliyun_access_key_secret,
        bucket=aliyun_bucket,
        region=aliyun_region,
        role_arn=aliyun_role_arn,
    )
)
# class OssCredentials(BaseModel):
#     AccessKeyId: str
#     AccessKeySecret: str
#     SecurityToken: str
#     Expiration: str
#     Domain: str
#     Bucket: str
#     Region: str
#     Endpoint: str

print(
    get_credential_cos(
        bucket=qcloud_bucket,
        region=qcloud_region,
        secret_id=qcloud_secret_id,
        secret_key=qcloud_secret_key,
    )
)
# class CosCredentials(BaseModel):
#     sessionToken: str
#     tmpSecretId: str
#     tmpSecretKey: str
#     domain: str
#     bucket: str
#     region: str
#     endpoint: str

# class CosStsModel(BaseModel):
#     expiredTime: int
#     expiration: str
#     credentials: CosCredentials
#     requestId: str
#     startTime: int

import time
from sts_credentials.utils.decorators import ttl_lru_cache


@ttl_lru_cache(ttl=2)
def test_func(i=0):
    return time.time() - i


assert test_func(123) != test_func(456)

f1 = test_func()
time.sleep(1)
f2 = test_func()
time.sleep(3)
f3 = test_func()

assert f1 == f2
assert f2 != f3

```