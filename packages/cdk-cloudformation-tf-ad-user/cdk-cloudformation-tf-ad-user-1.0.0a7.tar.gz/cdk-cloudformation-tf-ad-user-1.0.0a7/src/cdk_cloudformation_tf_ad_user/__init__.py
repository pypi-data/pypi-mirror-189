'''
# tf-ad-user

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::AD::User` v1.0.0.

## Description

CloudFormation equivalent of ad_user

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/ad/TF-AD-User/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::AD::User \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-AD-User \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::AD::User`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-ad-user+v1.0.0).
* Issues related to `TF::AD::User` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/ad/TF-AD-User/docs/README.md).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnUser(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-ad-user.CfnUser",
):
    '''A CloudFormation ``TF::AD::User``.

    :cloudformationResource: TF::AD::User
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        principal_name: builtins.str,
        sam_account_name: builtins.str,
        cannot_change_password: typing.Optional[builtins.bool] = None,
        city: typing.Optional[builtins.str] = None,
        company: typing.Optional[builtins.str] = None,
        container: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        email_address: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        fax: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        home_directory: typing.Optional[builtins.str] = None,
        home_drive: typing.Optional[builtins.str] = None,
        home_page: typing.Optional[builtins.str] = None,
        home_phone: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office: typing.Optional[builtins.str] = None,
        office_phone: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        other_name: typing.Optional[builtins.str] = None,
        password_never_expires: typing.Optional[builtins.bool] = None,
        po_box: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        smart_card_logon_required: typing.Optional[builtins.bool] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        trusted_for_delegation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``TF::AD::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param display_name: 
        :param principal_name: 
        :param sam_account_name: 
        :param cannot_change_password: 
        :param city: 
        :param company: 
        :param container: 
        :param country: 
        :param custom_attributes: 
        :param department: 
        :param description: 
        :param division: 
        :param email_address: 
        :param employee_id: 
        :param employee_number: 
        :param enabled: 
        :param fax: 
        :param given_name: 
        :param home_directory: 
        :param home_drive: 
        :param home_page: 
        :param home_phone: 
        :param initial_password: 
        :param initials: 
        :param mobile_phone: 
        :param office: 
        :param office_phone: 
        :param organization: 
        :param other_name: 
        :param password_never_expires: 
        :param po_box: 
        :param postal_code: 
        :param smart_card_logon_required: 
        :param state: 
        :param street_address: 
        :param surname: 
        :param title: 
        :param trusted_for_delegation: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__559b1430a5b2af9a8265b2f7b1fc4e370616420a3dcb556846a4790bb9fdc5a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            display_name=display_name,
            principal_name=principal_name,
            sam_account_name=sam_account_name,
            cannot_change_password=cannot_change_password,
            city=city,
            company=company,
            container=container,
            country=country,
            custom_attributes=custom_attributes,
            department=department,
            description=description,
            division=division,
            email_address=email_address,
            employee_id=employee_id,
            employee_number=employee_number,
            enabled=enabled,
            fax=fax,
            given_name=given_name,
            home_directory=home_directory,
            home_drive=home_drive,
            home_page=home_page,
            home_phone=home_phone,
            initial_password=initial_password,
            initials=initials,
            mobile_phone=mobile_phone,
            office=office,
            office_phone=office_phone,
            organization=organization,
            other_name=other_name,
            password_never_expires=password_never_expires,
            po_box=po_box,
            postal_code=postal_code,
            smart_card_logon_required=smart_card_logon_required,
            state=state,
            street_address=street_address,
            surname=surname,
            title=title,
            trusted_for_delegation=trusted_for_delegation,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::AD::User.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSid")
    def attr_sid(self) -> builtins.str:
        '''Attribute ``TF::AD::User.Sid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSid"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AD::User.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUserProps":
        '''Resource props.'''
        return typing.cast("CfnUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-ad-user.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "principal_name": "principalName",
        "sam_account_name": "samAccountName",
        "cannot_change_password": "cannotChangePassword",
        "city": "city",
        "company": "company",
        "container": "container",
        "country": "country",
        "custom_attributes": "customAttributes",
        "department": "department",
        "description": "description",
        "division": "division",
        "email_address": "emailAddress",
        "employee_id": "employeeId",
        "employee_number": "employeeNumber",
        "enabled": "enabled",
        "fax": "fax",
        "given_name": "givenName",
        "home_directory": "homeDirectory",
        "home_drive": "homeDrive",
        "home_page": "homePage",
        "home_phone": "homePhone",
        "initial_password": "initialPassword",
        "initials": "initials",
        "mobile_phone": "mobilePhone",
        "office": "office",
        "office_phone": "officePhone",
        "organization": "organization",
        "other_name": "otherName",
        "password_never_expires": "passwordNeverExpires",
        "po_box": "poBox",
        "postal_code": "postalCode",
        "smart_card_logon_required": "smartCardLogonRequired",
        "state": "state",
        "street_address": "streetAddress",
        "surname": "surname",
        "title": "title",
        "trusted_for_delegation": "trustedForDelegation",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        principal_name: builtins.str,
        sam_account_name: builtins.str,
        cannot_change_password: typing.Optional[builtins.bool] = None,
        city: typing.Optional[builtins.str] = None,
        company: typing.Optional[builtins.str] = None,
        container: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        email_address: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        fax: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        home_directory: typing.Optional[builtins.str] = None,
        home_drive: typing.Optional[builtins.str] = None,
        home_page: typing.Optional[builtins.str] = None,
        home_phone: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office: typing.Optional[builtins.str] = None,
        office_phone: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        other_name: typing.Optional[builtins.str] = None,
        password_never_expires: typing.Optional[builtins.bool] = None,
        po_box: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        smart_card_logon_required: typing.Optional[builtins.bool] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        trusted_for_delegation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''CloudFormation equivalent of ad_user.

        :param display_name: 
        :param principal_name: 
        :param sam_account_name: 
        :param cannot_change_password: 
        :param city: 
        :param company: 
        :param container: 
        :param country: 
        :param custom_attributes: 
        :param department: 
        :param description: 
        :param division: 
        :param email_address: 
        :param employee_id: 
        :param employee_number: 
        :param enabled: 
        :param fax: 
        :param given_name: 
        :param home_directory: 
        :param home_drive: 
        :param home_page: 
        :param home_phone: 
        :param initial_password: 
        :param initials: 
        :param mobile_phone: 
        :param office: 
        :param office_phone: 
        :param organization: 
        :param other_name: 
        :param password_never_expires: 
        :param po_box: 
        :param postal_code: 
        :param smart_card_logon_required: 
        :param state: 
        :param street_address: 
        :param surname: 
        :param title: 
        :param trusted_for_delegation: 

        :schema: CfnUserProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14530a23914f041a85ed4bef05a7b1eba1e0deb466be322c6615e478dbca3e40)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument principal_name", value=principal_name, expected_type=type_hints["principal_name"])
            check_type(argname="argument sam_account_name", value=sam_account_name, expected_type=type_hints["sam_account_name"])
            check_type(argname="argument cannot_change_password", value=cannot_change_password, expected_type=type_hints["cannot_change_password"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument company", value=company, expected_type=type_hints["company"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument department", value=department, expected_type=type_hints["department"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument division", value=division, expected_type=type_hints["division"])
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument employee_id", value=employee_id, expected_type=type_hints["employee_id"])
            check_type(argname="argument employee_number", value=employee_number, expected_type=type_hints["employee_number"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument fax", value=fax, expected_type=type_hints["fax"])
            check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
            check_type(argname="argument home_directory", value=home_directory, expected_type=type_hints["home_directory"])
            check_type(argname="argument home_drive", value=home_drive, expected_type=type_hints["home_drive"])
            check_type(argname="argument home_page", value=home_page, expected_type=type_hints["home_page"])
            check_type(argname="argument home_phone", value=home_phone, expected_type=type_hints["home_phone"])
            check_type(argname="argument initial_password", value=initial_password, expected_type=type_hints["initial_password"])
            check_type(argname="argument initials", value=initials, expected_type=type_hints["initials"])
            check_type(argname="argument mobile_phone", value=mobile_phone, expected_type=type_hints["mobile_phone"])
            check_type(argname="argument office", value=office, expected_type=type_hints["office"])
            check_type(argname="argument office_phone", value=office_phone, expected_type=type_hints["office_phone"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument other_name", value=other_name, expected_type=type_hints["other_name"])
            check_type(argname="argument password_never_expires", value=password_never_expires, expected_type=type_hints["password_never_expires"])
            check_type(argname="argument po_box", value=po_box, expected_type=type_hints["po_box"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument smart_card_logon_required", value=smart_card_logon_required, expected_type=type_hints["smart_card_logon_required"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
            check_type(argname="argument surname", value=surname, expected_type=type_hints["surname"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument trusted_for_delegation", value=trusted_for_delegation, expected_type=type_hints["trusted_for_delegation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "principal_name": principal_name,
            "sam_account_name": sam_account_name,
        }
        if cannot_change_password is not None:
            self._values["cannot_change_password"] = cannot_change_password
        if city is not None:
            self._values["city"] = city
        if company is not None:
            self._values["company"] = company
        if container is not None:
            self._values["container"] = container
        if country is not None:
            self._values["country"] = country
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if department is not None:
            self._values["department"] = department
        if description is not None:
            self._values["description"] = description
        if division is not None:
            self._values["division"] = division
        if email_address is not None:
            self._values["email_address"] = email_address
        if employee_id is not None:
            self._values["employee_id"] = employee_id
        if employee_number is not None:
            self._values["employee_number"] = employee_number
        if enabled is not None:
            self._values["enabled"] = enabled
        if fax is not None:
            self._values["fax"] = fax
        if given_name is not None:
            self._values["given_name"] = given_name
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if home_drive is not None:
            self._values["home_drive"] = home_drive
        if home_page is not None:
            self._values["home_page"] = home_page
        if home_phone is not None:
            self._values["home_phone"] = home_phone
        if initial_password is not None:
            self._values["initial_password"] = initial_password
        if initials is not None:
            self._values["initials"] = initials
        if mobile_phone is not None:
            self._values["mobile_phone"] = mobile_phone
        if office is not None:
            self._values["office"] = office
        if office_phone is not None:
            self._values["office_phone"] = office_phone
        if organization is not None:
            self._values["organization"] = organization
        if other_name is not None:
            self._values["other_name"] = other_name
        if password_never_expires is not None:
            self._values["password_never_expires"] = password_never_expires
        if po_box is not None:
            self._values["po_box"] = po_box
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if smart_card_logon_required is not None:
            self._values["smart_card_logon_required"] = smart_card_logon_required
        if state is not None:
            self._values["state"] = state
        if street_address is not None:
            self._values["street_address"] = street_address
        if surname is not None:
            self._values["surname"] = surname
        if title is not None:
            self._values["title"] = title
        if trusted_for_delegation is not None:
            self._values["trusted_for_delegation"] = trusted_for_delegation

    @builtins.property
    def display_name(self) -> builtins.str:
        '''
        :schema: CfnUserProps#DisplayName
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_name(self) -> builtins.str:
        '''
        :schema: CfnUserProps#PrincipalName
        '''
        result = self._values.get("principal_name")
        assert result is not None, "Required property 'principal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sam_account_name(self) -> builtins.str:
        '''
        :schema: CfnUserProps#SamAccountName
        '''
        result = self._values.get("sam_account_name")
        assert result is not None, "Required property 'sam_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cannot_change_password(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#CannotChangePassword
        '''
        result = self._values.get("cannot_change_password")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#City
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def company(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Company
        '''
        result = self._values.get("company")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Container
        '''
        result = self._values.get("container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Country
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_attributes(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#CustomAttributes
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def department(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Department
        '''
        result = self._values.get("department")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def division(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Division
        '''
        result = self._values.get("division")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#EmailAddress
        '''
        result = self._values.get("email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#EmployeeId
        '''
        result = self._values.get("employee_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_number(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#EmployeeNumber
        '''
        result = self._values.get("employee_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fax(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Fax
        '''
        result = self._values.get("fax")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def given_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#GivenName
        '''
        result = self._values.get("given_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomeDirectory
        '''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_drive(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomeDrive
        '''
        result = self._values.get("home_drive")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_page(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomePage
        '''
        result = self._values.get("home_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_phone(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#HomePhone
        '''
        result = self._values.get("home_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_password(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#InitialPassword
        '''
        result = self._values.get("initial_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initials(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Initials
        '''
        result = self._values.get("initials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_phone(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#MobilePhone
        '''
        result = self._values.get("mobile_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Office
        '''
        result = self._values.get("office")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office_phone(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#OfficePhone
        '''
        result = self._values.get("office_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Organization
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def other_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#OtherName
        '''
        result = self._values.get("other_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_never_expires(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#PasswordNeverExpires
        '''
        result = self._values.get("password_never_expires")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def po_box(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#PoBox
        '''
        result = self._values.get("po_box")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#PostalCode
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smart_card_logon_required(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#SmartCardLogonRequired
        '''
        result = self._values.get("smart_card_logon_required")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#State
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#StreetAddress
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def surname(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Surname
        '''
        result = self._values.get("surname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnUserProps#Title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trusted_for_delegation(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnUserProps#TrustedForDelegation
        '''
        result = self._values.get("trusted_for_delegation")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnUser",
    "CfnUserProps",
]

publication.publish()

def _typecheckingstub__559b1430a5b2af9a8265b2f7b1fc4e370616420a3dcb556846a4790bb9fdc5a5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    principal_name: builtins.str,
    sam_account_name: builtins.str,
    cannot_change_password: typing.Optional[builtins.bool] = None,
    city: typing.Optional[builtins.str] = None,
    company: typing.Optional[builtins.str] = None,
    container: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    custom_attributes: typing.Optional[builtins.str] = None,
    department: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    division: typing.Optional[builtins.str] = None,
    email_address: typing.Optional[builtins.str] = None,
    employee_id: typing.Optional[builtins.str] = None,
    employee_number: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    fax: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    home_directory: typing.Optional[builtins.str] = None,
    home_drive: typing.Optional[builtins.str] = None,
    home_page: typing.Optional[builtins.str] = None,
    home_phone: typing.Optional[builtins.str] = None,
    initial_password: typing.Optional[builtins.str] = None,
    initials: typing.Optional[builtins.str] = None,
    mobile_phone: typing.Optional[builtins.str] = None,
    office: typing.Optional[builtins.str] = None,
    office_phone: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    other_name: typing.Optional[builtins.str] = None,
    password_never_expires: typing.Optional[builtins.bool] = None,
    po_box: typing.Optional[builtins.str] = None,
    postal_code: typing.Optional[builtins.str] = None,
    smart_card_logon_required: typing.Optional[builtins.bool] = None,
    state: typing.Optional[builtins.str] = None,
    street_address: typing.Optional[builtins.str] = None,
    surname: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    trusted_for_delegation: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14530a23914f041a85ed4bef05a7b1eba1e0deb466be322c6615e478dbca3e40(
    *,
    display_name: builtins.str,
    principal_name: builtins.str,
    sam_account_name: builtins.str,
    cannot_change_password: typing.Optional[builtins.bool] = None,
    city: typing.Optional[builtins.str] = None,
    company: typing.Optional[builtins.str] = None,
    container: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    custom_attributes: typing.Optional[builtins.str] = None,
    department: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    division: typing.Optional[builtins.str] = None,
    email_address: typing.Optional[builtins.str] = None,
    employee_id: typing.Optional[builtins.str] = None,
    employee_number: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    fax: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    home_directory: typing.Optional[builtins.str] = None,
    home_drive: typing.Optional[builtins.str] = None,
    home_page: typing.Optional[builtins.str] = None,
    home_phone: typing.Optional[builtins.str] = None,
    initial_password: typing.Optional[builtins.str] = None,
    initials: typing.Optional[builtins.str] = None,
    mobile_phone: typing.Optional[builtins.str] = None,
    office: typing.Optional[builtins.str] = None,
    office_phone: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    other_name: typing.Optional[builtins.str] = None,
    password_never_expires: typing.Optional[builtins.bool] = None,
    po_box: typing.Optional[builtins.str] = None,
    postal_code: typing.Optional[builtins.str] = None,
    smart_card_logon_required: typing.Optional[builtins.bool] = None,
    state: typing.Optional[builtins.str] = None,
    street_address: typing.Optional[builtins.str] = None,
    surname: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    trusted_for_delegation: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
