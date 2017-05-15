# -*- coding: utf-8 -*-



from cbbweb.core.utils import str2array
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName

from cbbweb.service import get_object
from cbbweb.service import list_objs
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import car_series_utils
from cbbweb.service.cms_utils import car_type_utils
from cbbweb.service.cms_utils import dealer_utils



def sorted_offer_price_list(offer_price_list=None,
                            orderby_price=None, descending=None):
    """
        根据条件排序
    """
    if offer_price_list:
        if orderby_price:
            if descending:
                return sorted(
                    offer_price_list,
                    key=lambda tmp_dealer: (
                        -tmp_dealer['offer_price']['public_offer_price'],
                        -tmp_dealer['offer_price']['guide_price'],
                        -tmp_dealer['offer_price']['discount']
                    )
                )
            else:
                return sorted(
                    offer_price_list,
                    key=lambda tmp_dealer: (
                        tmp_dealer['offer_price']['public_offer_price'],
                        tmp_dealer['offer_price']['guide_price'],
                        -tmp_dealer['offer_price']['discount']
                    )
                )
        else:
            if descending:
                return sorted(
                    offer_price_list,
                    key=lambda tmp_dealer: (
                        -tmp_dealer['offer_price']['discount'],
                        tmp_dealer['offer_price']['public_offer_price'],
                        tmp_dealer['offer_price']['guide_price'],
                    )
                )
            else:
                return sorted(
                    offer_price_list,
                    key=lambda tmp_dealer: (
                        tmp_dealer['offer_price']['discount'],
                        tmp_dealer['offer_price']['public_offer_price'],
                        tmp_dealer['offer_price']['guide_price'],
                    )
                )
    return offer_price_list

@redis_func()
def get_offerprice_none():
    offer_price_dict = {
        'public_offer_price': 0,
        'discount': 0,
        'price': 0,
        'guide_price': 0,
    }
    return offer_price_dict

@redis_func()
def get_offerprice_none_series(car_series_id=None):
    car_series = car_series_utils.get_carseries_by_id(
        car_series_id=car_series_id
    )
    if car_series:
        offer_price_dict = {
            'public_offer_price': car_series['start_guideprice'],
            'discount': 0,
            'price': car_series['start_guideprice'],
            'guide_price': car_series['start_guideprice'],
        }
        return offer_price_dict
    return get_offerprice_none()

@redis_func()
def get_offerprice_none_type(car_type_id=None):
    car_type = car_type_utils.get_cartype_by_id(
        car_type_id=car_type_id
    )
    if car_type:
        offer_price_dict = {
            'public_offer_price': car_type['guide_price'],
            'discount': 0,
            'price': car_type['guide_price'],
            'guide_price': car_type['guide_price'],
        }
        return offer_price_dict
    return get_offerprice_none()

@redis_func()
def get_offerprice_by_id(offer_price_id=None):
    offer_price_id = common_utils.to_int(offer_price_id)
    offer_price = get_object(model=ModelName.T_BASE_OFFER_PRICE,
                             is_enable=1,
                             id=offer_price_id)
    if not offer_price:
        return None
    if not offer_price.dealer_id:
        return None
    discount = common_utils.to_positive(offer_price.discount)
    offer_price_dict = {
        'id': offer_price.id,
        'dealer_id': offer_price.dealer_id,
        # 'dealer_name': offer_price.dealer_name,
        'car_type_id': offer_price.car_type_id,
        'car_series_id': offer_price.car_series_id,
        'car_brand_id': offer_price.car_brand_id,
        'public_offer_price': offer_price.public_offer_price,
        'purchase_tax': offer_price.purchase_tax,
        'comercial_insurance': offer_price.comercial_insurance,
        'compulsory_insurance': offer_price.compulsory_insurance,
        'insurance_off': offer_price.insurance_off,
        'travel_tax': offer_price.travel_tax,
        'lisence_cost': offer_price.lisence_cost,
        'other_cost': offer_price.other_cost,
        'province_id': common_utils.to_int(offer_price.province_id),
        'city_id': common_utils.to_int(offer_price.city_id),
        'county_id': common_utils.to_int(offer_price.county_id),
        'discount': discount,
        'price': offer_price.public_offer_price,
        'guide_price': (offer_price.public_offer_price + discount),
    }
    if offer_price.car_type_id:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=offer_price.car_type_id
        )
        if tmp_car_type:
            offer_price_dict['guide_price'] = tmp_car_type['guide_price']
    return offer_price_dict

# @redis_func()
def get_offerprice_by_model(offer_price=None):
    discount = common_utils.to_positive(offer_price.discount)
    offer_price_dict = {
        'id': offer_price.id,
        'dealer_id': offer_price.dealer_id,
        'car_type_id': offer_price.car_type_id,
        'car_series_id': offer_price.car_series_id,
        'car_brand_id': offer_price.car_brand_id,
        'public_offer_price': offer_price.public_offer_price,
        'purchase_tax': offer_price.purchase_tax,
        'comercial_insurance': offer_price.comercial_insurance,
        'compulsory_insurance': offer_price.compulsory_insurance,
        'insurance_off': offer_price.insurance_off,
        'travel_tax': offer_price.travel_tax,
        'lisence_cost': offer_price.lisence_cost,
        'other_cost': offer_price.other_cost,
        'province_id': common_utils.to_int(offer_price.province_id),
        'city_id': common_utils.to_int(offer_price.city_id),
        'county_id': common_utils.to_int(offer_price.county_id),
        'discount': discount,
        'price': offer_price.public_offer_price,
        'guide_price': (offer_price.public_offer_price + discount),
    }
    if offer_price.car_type_id:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=offer_price.car_type_id
        )
        if tmp_car_type:
            offer_price_dict['guide_price'] = tmp_car_type['guide_price']
    return offer_price_dict

@redis_func()
def get_offerprice_by_series(car_series_id=None):
    car_series_id = common_utils.to_int(car_series_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_series_id=car_series_id)[0]
    except IndexError:
        return get_offerprice_none_series(car_series_id=car_series_id)
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice_by_series_dealer(car_series_id=None, dealer_id=None):
    car_series_id = common_utils.to_int(car_series_id)
    dealer_id = common_utils.to_int(dealer_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_series_id=car_series_id,
                                dealer_id=dealer_id)[0]
    except IndexError:
        return get_offerprice_none_series(car_series_id=car_series_id)
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice_by_series_dealer_list(car_series_id=None, dealer_id_list=None):
    car_series_id = common_utils.to_int(car_series_id)
    dealer_id_list = str2array(dealer_id_list)
    if not dealer_id_list:
        return get_offerprice_none_series(car_series_id=car_series_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_series_id=car_series_id,
                                dealer_id__in=dealer_id_list)[0]
    except IndexError:
        return get_offerprice_none_series(car_series_id=car_series_id)
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice_by_series_city(car_series_id=None, city_id=None):
    car_series_id = common_utils.to_int(car_series_id)
    city_id = common_utils.to_int(city_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_series_id=car_series_id,
                                city_id=city_id)[0]
    except IndexError:
        dealer_id_list = dealer_utils.get_dealer_id_list(
            city_id=city_id,
            car_series_id=car_series_id
        )
        if not dealer_id_list:
            return get_offerprice_none_series(car_series_id=car_series_id)
        return get_offerprice_by_series_dealer_list(
            car_series_id=car_series_id,
            dealer_id_list=dealer_id_list
        )
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice_by_type(car_type_id=None):
    car_type_id = common_utils.to_int(car_type_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_type_id=car_type_id)[0]
    except IndexError:
        return get_offerprice_none_type(car_type_id=car_type_id)
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice_by_type_dealer(car_type_id=None, dealer_id=None):
    car_type_id = common_utils.to_int(car_type_id)
    dealer_id = common_utils.to_int(dealer_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_type_id=car_type_id,
                                dealer_id=dealer_id)[0]
    except IndexError:
        return get_offerprice_none_type(car_type_id=car_type_id)
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice_by_type_dealer_list(car_type_id=None, dealer_id_list=None):
    car_type_id = common_utils.to_int(car_type_id)
    dealer_id_list = str2array(dealer_id_list)
    if not dealer_id_list:
        return get_offerprice_none_type(car_type_id=car_type_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_type_id=car_type_id,
                                dealer_id__in=dealer_id_list)[0]
    except IndexError:
        return get_offerprice_none_type(car_type_id=car_type_id)
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice_by_type_city(car_type_id=None, city_id=None):
    car_type_id = common_utils.to_int(car_type_id)
    city_id = common_utils.to_int(city_id)
    try:
        offer_price = list_objs(model=ModelName.T_BASE_OFFER_PRICE,
                                orderby=['public_offer_price', '-created_date'],
                                is_enable=1,
                                car_type_id=car_type_id,
                                city_id=city_id)[0]
    except IndexError:
        car_type = car_type_utils.get_cartype_by_id(
            car_type_id=car_type_id
        )
        if not car_type:
            return get_offerprice_none()
        dealer_id_list = dealer_utils.get_dealer_id_list(
            city_id=city_id,
            car_series_id=car_type['car_series_id']
        )
        if not dealer_id_list:
            return get_offerprice_none_type(car_type_id=car_type_id)
        return get_offerprice_by_type_dealer_list(
            car_type_id=car_type_id,
            dealer_id_list=dealer_id_list
        )
    offer_price_dict = get_offerprice_by_model(offer_price=offer_price)
    return offer_price_dict

@redis_func()
def get_offerprice(city_id=None, dealer_id=None, dealer_id_list=None,
                   car_series_id=None, car_type_id=None):
    """
        根据城市ID或者经销商ID或者车系ID或者车型ID返回最低报价，
        车系ID和车型ID必选一个

        参数
        ----
        city_id : int, 可选
            城市ID
        dealer_id : int, 可选
            经销商ID
        dealer_id_list : list, 可选
            经销商ID数组
        car_series_id : int, 可选
            车系ID
        car_type_id : int, 可选
            车型ID

        返回值
        ------
        result_dict : dict
            返回最低报价
    """
    city_id = common_utils.to_int(city_id)
    dealer_id = common_utils.to_int(dealer_id)
    dealer_id_list = str2array(dealer_id_list)
    car_series_id = common_utils.to_int(car_series_id)
    car_type_id = common_utils.to_int(car_type_id)
    if car_type_id:
        if dealer_id:
            return get_offerprice_by_type_dealer(
                car_type_id=car_type_id,
                dealer_id=dealer_id
            )
        elif dealer_id_list:
            return get_offerprice_by_type_dealer_list(
                car_type_id=car_type_id,
                dealer_id_list=dealer_id_list
            )
        elif city_id:
            return get_offerprice_by_type_city(
                car_type_id=car_type_id,
                city_id=city_id
            )
        else:
            return get_offerprice_by_type(car_type_id=car_type_id)
    elif car_series_id:
        if dealer_id:
            return get_offerprice_by_series_dealer(
                car_series_id=car_series_id,
                dealer_id=dealer_id
            )
        elif dealer_id_list:
            return get_offerprice_by_series_dealer_list(
                car_series_id=car_series_id,
                dealer_id_list=dealer_id_list
            )
        elif city_id:
            return get_offerprice_by_series_city(
                car_series_id=car_series_id,
                city_id=city_id
            )
        else:
            return get_offerprice_by_series(car_series_id=car_series_id)

    else:
        return get_offerprice_none()


