# -*- coding: utf-8 -*-
# This file is part of Shuup REST API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import six
from rest_framework.test import APIClient

from shuup import configuration


def get_client(admin_user):
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client


def set_configuration():
    config = {
        "api_permission_ShopViewSet": 3,
        "api_permission_FrontShopProductViewSet": 3,
        "api_permission_PersonContactViewSet": 4,
        "api_permission_FrontUserViewSet": 2,
        "api_permission_FrontOrderViewSet": 4,
        "api_permission_AttributeViewSet": 5,
        "api_permission_TaxClassViewSet": 5,
        "api_permission_FrontProductViewSet": 3,
        "api_permission_ProductVariationVariableValueViewSet": 5,
        "api_permission_SalesUnitViewSet": 5,
        "api_permission_UserViewSet": 5,
        "api_permission_ShopReviewViewSet": 4,
        "api_permission_BasketViewSet": 2,
        "api_permission_CategoryViewSet": 1,
        "api_permission_ShipmentViewSet": 5,
        "api_permission_CgpPriceViewSet": 5,
        "api_permission_ShopProductViewSet": 3,
        "api_permission_ContactViewSet": 4,
        "api_permission_OrderViewSet": 5,
        "api_permission_ProductViewSet": 5,
        "api_permission_ProductTypeViewSet": 5,
        "api_permission_ProductVariationVariableViewSet": 5,
        "api_permission_SupplierViewSet": 5,
        "api_permission_ManufacturerViewSet": 5,
        "api_permission_ProductMediaViewSet": 5,
        "api_permission_ProductAttributeViewSet": 5,
        "api_permission_MutableAddressViewSet": 5,
        "api_permission_ProductPackageViewSet": 5,
    }
    for field, value in six.iteritems(config):
        configuration.set(None, field, value)
