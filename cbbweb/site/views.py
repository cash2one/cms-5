# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from cbbweb.core.utils import (is_mobile, to_dict, db)
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.constants import API
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.service import (get_object)
from cbbweb.service.cms_utils import (common_utils,
                                      car_brand_utils, car_series_utils,
                                      car_type_utils, offer_price_utils,
                                      activity_utils, dealer_utils)
from cbbweb.core.utils.views import (init_context, CbbTemplateView)
from django.conf import settings

logger = logging.getLogger("cms")


class IndexView(CbbTemplateView):
    pc_template = 'site/index.html'
    wap_template = 'wap/site/index.html'


class CarConfigView(CbbTemplateView):
    pc_template = 'site/carseries-arguments.html'
    wap_template = 'wap/site/car/car_para.html'


class CheckloanView(CbbTemplateView):
    pc_template = 'site/checkloan.html'
    wap_template = 'wap/site/loan/loan_clue.html'


class DealerActivityView(CbbTemplateView):
    pc_template = 'site/dealer-detail.html'
    wap_template = 'wap/site/store/store_onsale_detail.html'

    def get_service_data(self, request, context, **kwargs):
        sql = """
            select * from T_BASE_MEDIA_ACTIVITY
            where date_format(created_date, '%%Y%%m')=%(yyyymm)s
            and id=%(activity_id)s
            and activity_type=%(activity_type)s
        """

        activity = db.fetchone(sql, kwargs)
        if not activity:
            raise Http404

        context['activity'] = activity_utils.get_activity_by_id(
            activity_id=activity['ID']
        )
        return context


class ProductImageView(CbbTemplateView):
    pc_template = 'wap/site/car/car_display.html'
    wap_template = 'wap/site/car/car_display.html'


class FinanceDetailView(CbbTemplateView):
    pc_template = 'site/vclist.html'
    wap_template = 'wap/site/loan/locan_finance.html'


class FinanceApplyView(CbbTemplateView):
    pc_template = 'site/jrsign.html'
    wap_template = 'wap/site/loan/loan-finance-liuzi.html'


class FinanceApplyDone(CbbTemplateView):
    pc_template = 'wap/site/loan/clue_success.html'
    wap_template = 'wap/site/loan/clue_success.html'


class FinanceApplyComplete(CbbTemplateView):
    pc_template = ''
    wap_template = ''


class InfoApplyView(CbbTemplateView):
    '''
        留资页
    '''
    pc_template = 'site/sign.html'
    wap_template = 'wap/site/clue/get_preferential.html'


class InfoCompleteView(CbbTemplateView):
    '''
        完善留资数据
    '''
    pc_template = 'site/questions.html'
    wap_template = 'wap/site/clue/compelete_info.html'

class InfoDoneView(CbbTemplateView):
    '''
        留资成功
    '''
    pc_template = 'site/signsuccess.html'
    wap_template = 'wap/site/clue/get_discount_success.html'


def handle_static_html(request, template_path, *args, **kwargs):
    '''
        所有静态html入口
    '''
    context = init_context()
    if not settings.DEBUG:
        if template_path.startswith('test'):
            template_path = 'test/test'
    return render(request, template_path+".html", context)
