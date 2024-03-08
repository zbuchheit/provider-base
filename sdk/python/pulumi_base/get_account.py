# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

@pulumi.output_type
class GetAccountResult:
    def __init__(__self__, account_id=None, environment=None, name=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if environment and not isinstance(environment, str):
            raise TypeError("Expected argument 'environment' to be a str")
        pulumi.set(__self__, "environment", environment)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        Id of account created
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def environment(self) -> str:
        """
        Environment of account
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of account created
        """
        return pulumi.get(self, "name")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            account_id=self.account_id,
            environment=self.environment,
            name=self.name)


def get_account(account_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    GetOrganization gets the Organization information


    :param str account_name: Name of the Account
    """
    __args__ = dict()
    __args__['AccountName'] = account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('base:index:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        environment=pulumi.get(__ret__, 'environment'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_account)
def get_account_output(account_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountResult]:
    """
    GetOrganization gets the Organization information


    :param str account_name: Name of the Account
    """
    ...
