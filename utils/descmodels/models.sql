


consignee_address
CREATE TABLE `consignee_address` (
  `ORDERID` varchar(32) NOT NULL COMMENT '订单号',
  `NAME` varchar(64) DEFAULT '' COMMENT '收货人姓名',
  `SEX` varchar(8) DEFAULT '0' COMMENT '0表示女，1表示男',
  `ZIPCODE` varchar(8) DEFAULT '' COMMENT '邮编',
  `ADDRESS` varchar(256) DEFAULT '' COMMENT '地址',
  `TELEPHONE` varchar(32) DEFAULT '' COMMENT '电话',
  `MOBILETELEPHONE` varchar(32) DEFAULT '' COMMENT '手机号',
  `EMAILADDRESS` varchar(128) DEFAULT NULL COMMENT '邮件地址',
  `COUNTRY` varchar(32) DEFAULT '' COMMENT '国家',
  `PROVINCE` varchar(32) DEFAULT '' COMMENT '省份',
  `CITY` varchar(32) DEFAULT '' COMMENT '城市',
  `AREANO` varchar(32) DEFAULT '' COMMENT '地区号',
  `REGION` varchar(32) DEFAULT '' COMMENT '区号',
  `ORGID` varchar(32) DEFAULT NULL COMMENT '组织机构ID',
  `ID_CARD` varchar(32) DEFAULT '',
  PRIMARY KEY (`ORDERID`),
  KEY `idx_mobiletelephone` (`MOBILETELEPHONE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单收货地址表，存放订单的收货地址信息包'



omorder
CREATE TABLE `omorder` (
  `ORDERID` varchar(32) NOT NULL COMMENT '订单主键',
  `ORDERDATE` varchar(26) DEFAULT '' COMMENT '订单日期',
  `CREATOR` varchar(64) DEFAULT '' COMMENT '下单人',
  `PAYTYPE` varchar(32) DEFAULT '' COMMENT '货到付款，在线支付，话费支付',
  `NOTE` varchar(256) DEFAULT '' COMMENT '给商家的留言',
  `TOTALCOST` decimal(13,2) DEFAULT '0.00' COMMENT '订单总金额',
  `CUSTOMERID` varchar(32) DEFAULT '' COMMENT '会员ID',
  `REMESSAGE` varchar(256) DEFAULT '' COMMENT '订单处理情况',
  `PRODUCTCOST` decimal(13,2) DEFAULT '0.00' COMMENT '产品金额',
  `AFFIXATION` decimal(13,2) DEFAULT '0.00' COMMENT '附加费用\n            比如邮费，算做附加费用\n            ',
  `AGENCY_ID` varchar(32) DEFAULT '' COMMENT '网盟渠道ID',
  `GATHERING` decimal(13,2) DEFAULT '0.00' COMMENT '应收金额',
  `CONSIGNMENT` decimal(8,0) DEFAULT '0' COMMENT '是否已发货\n            0表示为发货\n            1表示已发货\n            ',
  `INVOICE` decimal(8,0) DEFAULT '0' COMMENT '是否要发票\n            0表示不要发票\n            1表示需要发票\n            ',
  `PAID` decimal(13,2) DEFAULT '0.00' COMMENT '已收款金额',
  `ISNET` char(1) DEFAULT '1' COMMENT '是否网站订单\n            0表示非网站订单\n            1表示网站订单\n            ',
  `STATUS` varchar(8) DEFAULT '0' COMMENT '01待处理订单，02已收款未发货，03缺货订单，04无效订单，05应退款订单，06已发货，07已到货订单，08已退款订单 09表示已确认',
  `UUID` varchar(32) DEFAULT '' COMMENT '主键',
  `SOURCE` varchar(64) DEFAULT '' COMMENT '订单来源\n            0 网站 1 电话 2 其他电子商务平台 3 线下销售',
  `SOURCE_VALUE` varchar(64) DEFAULT '' COMMENT '订单来源说明\n            具体来源说明网站来源 为 空串电话来源为 客服电话号码 其他电子商务平台 为电子商务平台名称 线下销售为销售ID',
  `SITE` varchar(64) DEFAULT '' COMMENT '库房',
  `HZSOURCE` varchar(64) DEFAULT '' COMMENT '合作来源',
  `ISVIP` char(1) DEFAULT '0' COMMENT '是否是VIP订单\n            0表示不是VIP订单，1表示是VIP订单',
  `SHIPTYPENAME` varchar(64) DEFAULT '' COMMENT '配送方式名称',
  `PAYTYPENAME` varchar(64) DEFAULT '' COMMENT '支付方式名称',
  `ISCOMPANY_SHIP` char(1) DEFAULT '0' COMMENT '是否公司配送\n            0表示否，1表示是',
  `INVOICE_TITLE` varchar(64) DEFAULT '' COMMENT '发票抬头',
  `INVOICE_CONTENT` varchar(128) DEFAULT '' COMMENT '发票内容',
  `CREATOR_NAME` varchar(64) DEFAULT '' COMMENT '创建人姓名',
  `FROMURL` varchar(256) DEFAULT '' COMMENT '订单来源URL',
  `MANAGER` varchar(32) DEFAULT '' COMMENT '管理员ID',
  `PROMOTIONSINFO` varchar(256) DEFAULT '' COMMENT '促销信息',
  `OFFER_ID` varchar(32) DEFAULT '' COMMENT '促销方案ID',
  `LOGISTICS_ID` varchar(32) DEFAULT '' COMMENT '物流公司编号',
  `EXPRESS_NO` varchar(64) DEFAULT '' COMMENT '物流单号',
  `CONCESSIONS_AMOUNT` decimal(13,2) DEFAULT '0.00' COMMENT '优惠金额',
  `STORE_ID` varchar(32) DEFAULT '' COMMENT '订单所属店铺ID',
  `PARENT_ID` varchar(32) DEFAULT '' COMMENT '订单的父订单编号',
  `CREATOR_TYPE` varchar(16) DEFAULT '' COMMENT '创建人类型\n            创建人类型如：manager，user，store',
  `SERVICE_STATUS` varchar(8) DEFAULT '' COMMENT '服务状态 如：01用户订单退款申请02申请关闭03申请成功',
  `RECON_FLAG` varchar(8) DEFAULT '0' COMMENT '对账状态\n            1表示订单已对账 0表示未对账',
  `DEAL_REASON` varchar(1024) DEFAULT '' COMMENT '处理原因',
  `DEAL_FLAG` varchar(16) DEFAULT '' COMMENT '处理标志',
  `DEAL_TIME` varchar(26) DEFAULT '' COMMENT '处理时间',
  `TYPE` varchar(8) DEFAULT '' COMMENT '订单类型，\n            实物订单， 虚拟卡订单、非货到付款实物订单、货到付款实物订单',
  `G_AMOUNT` decimal(8,0) DEFAULT '0' COMMENT '代金券金额',
  `GCARD_NO` varchar(32) DEFAULT '' COMMENT '代金券编号',
  `PCARD_AMOUNT` decimal(8,0) DEFAULT '0' COMMENT '礼品卡金额',
  `PCARD_NO` varchar(32) DEFAULT '' COMMENT '礼品卡编号',
  `INTEGRAL` decimal(8,0) DEFAULT '0' COMMENT '可获得积分',
  `FROM_URL` varchar(256) DEFAULT '' COMMENT '订单来源路径',
  `SERVICE_TYPE` varchar(16) DEFAULT '' COMMENT '用户退款, 商户取消,商户过期不处理',
  `SERVICE_REASON` varchar(1024) DEFAULT '' COMMENT '服务原因',
  `VIEW_BACK_APP` char(1) DEFAULT '0' COMMENT '客服是否可见退款申请\n            0为不可见，1为可见默认为0',
  `PAY_DATE_TIME` varchar(26) DEFAULT '' COMMENT '付款时间',
  `PROMOTION_TYPE` varchar(8) DEFAULT '' COMMENT '促销类型',
  `ESALESNO` varchar(128) DEFAULT NULL COMMENT '欧飞编号',
  `CLASSTYPE` varchar(128) DEFAULT NULL COMMENT '欧飞分类类型',
  `ES_REC_FLAG` varchar(8) DEFAULT NULL COMMENT '1表示已对账 0表示未对账',
  `SETTLE_DATE` varchar(26) DEFAULT NULL COMMENT '清算时间\n            用于于支付平台对账统一时间',
  `ORGID` varchar(32) DEFAULT NULL COMMENT '组织机构ID',
  `BACK_TIME` varchar(26) DEFAULT NULL COMMENT '退款时间',
  `BACK_STATUS` varchar(8) DEFAULT NULL COMMENT '退款状态\n            01 退款协议等待卖家确认中\n            02 卖家不同意协议，等待买家修改\n            03 退款协议达成，等待买家退货\n            04 买家已退货，等待卖家确认收货\n            05 退款关闭\n            06 退款成功\n            \n            ',
  `HW_STATUS` varchar(8) DEFAULT NULL COMMENT '货物状态\n            1表示已收到货物 0表示未收到货物',
  `BACK_AMOUNT` decimal(13,2) DEFAULT NULL COMMENT '退款金额',
  `BACK_REASON` varchar(8) DEFAULT NULL COMMENT '退款原因\n            01 与卖家协商一致退款\n            02 商品质量问题\n            03 收到的商品不符\n            04 其他\n            ',
  `BACK_GOOD` char(1) DEFAULT NULL COMMENT '是否退货\n            0表示否，1表示是',
  `RETURNREASON` varchar(256) DEFAULT '' COMMENT '退款说明',
  `CUSTOMER_APP` char(1) DEFAULT NULL COMMENT '买家已评价\n            0表示未评价，1表示已评价',
  `STORE_APP` char(1) DEFAULT NULL COMMENT '卖家已评价\n            0表示未评价，1表示已评价',
  `CONFIRM` char(1) DEFAULT '0' COMMENT '1表示已确认 ,0表示未确认 0为默认',
  `FH_NOTE` varchar(1024) DEFAULT NULL COMMENT '发货说明',
  `TK_FLAG` char(1) DEFAULT '0' COMMENT '退款标志 \n            0为支付平台退款失败，1为支付平台退款成功',
  `RESERVATION_DATE` varchar(26) DEFAULT NULL COMMENT '预约日期',
  `RESERVATION_START_HOUR` varchar(26) DEFAULT NULL COMMENT '预约开始时间',
  `RESERVATION_END_HOUR` varchar(26) DEFAULT NULL COMMENT '预约结束时间',
  `FH_ADDRESS` varchar(256) DEFAULT NULL COMMENT '发货地址',
  `FH_ADDRESS_ID` varchar(32) DEFAULT NULL COMMENT '发货地址ID',
  `QH_ADDRESS` varchar(256) DEFAULT NULL COMMENT '取货地址',
  `QH_ADDRESS_ID` varchar(32) DEFAULT NULL COMMENT '取货地址ID',
  `FH_TYPE` varchar(8) DEFAULT '0' COMMENT '发货类型\n            0表示自联系物流1表示在线下单 0为默认',
  `WL_STATUS` varchar(8) DEFAULT NULL COMMENT '物流状态\n            等待确认 CONFIRM\n            接单 ACCEPT\n            不接单 UNACCEPT\n            揽收成功 GOT\n            揽收失败 NOT_SEND\n            签收成功 SIGNED\n            签收失败 FAILED\n            订单已取消 WITHDRAW\n            ',
  `IS_MERGE_PAY` char(1) DEFAULT '1' COMMENT '是否合并支付\n            默认为是 ''0''代表不是 ''1''代表是',
  `ORDER_SUCCESS_DATE` varchar(26) DEFAULT NULL COMMENT '订单到货日期',
  `PAY_STATUS` varchar(8) DEFAULT '00',
  `PAY_GATE_TYPE` varchar(16) DEFAULT NULL COMMENT '支付接口类型\n            gopay01 ，国付宝(担保支付)\n            gopay02 ，国付宝(银行卡支付)\n            kqpay ，快钱支付\n            ybpay ，易宝支付\n            twpay ，台湾精品馆支付方式 上海银联\n            easypay ，渤海易生支付\n            alipay ，支付宝\n            ',
  `STORE_XX_ISFZ` char(1) DEFAULT '0' COMMENT '商家线下是否分账\n            0表示未分账，1表示已分账',
  `ALIPAY_ACCOUNT` varchar(64) DEFAULT ' ' COMMENT '支付宝收款帐号',
  `BILL_ACCOUNT` varchar(64) DEFAULT ' ' COMMENT '快钱收款帐号',
  `INVOICE_NOTE` varchar(256) DEFAULT NULL COMMENT '发货备注',
  `SHIPTYPEID` varchar(32) DEFAULT NULL,
  `NEEDINTEGRAL` decimal(8,0) DEFAULT NULL,
  `FZ_NOTE` varchar(256) DEFAULT NULL,
  `STORE_INTEGRAL` decimal(13,2) NOT NULL DEFAULT '0.00' COMMENT '店铺获取的积分返还',
  `SEND_STORE_INTEGRAL` char(1) DEFAULT NULL,
  `STORE_INTETRAL_NOTE` varchar(256) DEFAULT NULL,
  `GIFTCARD_RLS` char(1) DEFAULT NULL,
  `GIFTCARD_TYPE` varchar(32) DEFAULT NULL,
  `SEND_INTEGRAL_FLAG` char(1) DEFAULT NULL,
  `BACK_INTEGRAL_FLAG` char(1) DEFAULT NULL,
  `PROMOTION_ROLE` char(1) DEFAULT NULL,
  `PROMOTION_GIFT` varchar(512) DEFAULT NULL,
  `PROMOTION_CART_PRICE` decimal(16,2) DEFAULT NULL,
  `PROMOTION_CART_DISCOUNT` decimal(16,2) DEFAULT NULL,
  `FZ_STATUS` char(1) DEFAULT NULL,
  `SHOP_FZ` decimal(13,2) DEFAULT NULL,
  `STORE_FZ` decimal(13,2) DEFAULT NULL,
  `FZ_DATE` varchar(26) DEFAULT NULL,
  `SPLIT_STATUS` char(1) DEFAULT NULL,
  `REFUND_TIMES` int(11) DEFAULT '0',
  `REFUND_ORDER_STATUS` varchar(8) DEFAULT NULL,
  `CANCEL_NOTE` varchar(256) DEFAULT NULL,
  `SELL_ID` varchar(32) DEFAULT NULL,
  `ASSIGN_STATUS` varchar(8) DEFAULT '0',
  `NOTICE_PAY_STATUS` varchar(8) DEFAULT '0',
  `ORG_STORE_FZ` decimal(13,2) DEFAULT '0.00',
  `SHOW_ORDER_TYPE` char(1) DEFAULT '0',
  `SHOW_ORDER_ID` varchar(32) DEFAULT '',
  `GUIDE_ID` varchar(50) DEFAULT NULL COMMENT '导购员ID',
  `HXCODE` varchar(32) DEFAULT NULL COMMENT '整车订单核销码',
  `kefu_remark` varchar(256) DEFAULT NULL COMMENT '客服备注',
  `SOURCE_PARAM` int(11) DEFAULT NULL COMMENT '来源参数，巡展城市/活动',
  `BALANCE_MONEY` varchar(64) DEFAULT NULL COMMENT '结算金额',
  `BALANCE_STATUS` varchar(64) DEFAULT NULL COMMENT '结算状态',
  `BALANCE_TIME` varchar(64) DEFAULT NULL COMMENT '结算时间',
  `BALANCE_VIN` varchar(64) DEFAULT NULL COMMENT 'VIN码',
  `BALANCE_TICKET_URL` varchar(64) DEFAULT NULL COMMENT '发票URL',
  `BALANCE_TICKET_NAME` varchar(64) DEFAULT NULL COMMENT '发票姓名',
  `BANLANCE_CARD_CODE` varchar(64) DEFAULT NULL COMMENT '订单关联卡券ID',
  `RECEIVER_REFUSE_REASON` varchar(256) DEFAULT NULL COMMENT '拒结算原因',
  `SHOW_FLAG` varchar(2) DEFAULT '0' COMMENT '标志订单是否经销商平台显示',
  `PAGEID` varchar(64) DEFAULT NULL COMMENT '页面KEY值',
  `ISBUILDCLUE` varchar(2) DEFAULT '1' COMMENT '是否生成线索 1默认生成线索，0不生成线索',
  PRIMARY KEY (`ORDERID`),
  KEY `idx_order_date` (`ORDERDATE`),
  KEY `idx_parent_id` (`PARENT_ID`),
  KEY `idx_CUSTOMERID` (`CUSTOMERID`),
  KEY `idx_offer_id` (`OFFER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单主表，存放订单总金额，应付金额，已付'



orderdetail
CREATE TABLE `orderdetail` (
  `UUID` varchar(32) NOT NULL COMMENT '主键',
  `ORDERID` varchar(32) DEFAULT '' COMMENT '订单ID',
  `PRODUCTID` varchar(32) DEFAULT '' COMMENT '商品ID',
  `productName` varchar(256) DEFAULT NULL,
  `UNITPRICE` decimal(13,2) DEFAULT '0.00' COMMENT '商品价格',
  `QUANTITY` decimal(8,0) DEFAULT '0' COMMENT '购买数量',
  `ORDER_DATE` datetime NOT NULL DEFAULT '2014-01-01 01:01:01' COMMENT '下单日期',
  `TOTALPRICE` decimal(13,2) DEFAULT '0.00' COMMENT '总价格',
  `NOTE` varchar(256) DEFAULT '' COMMENT '说明',
  `PRODUCT_NO` varchar(32) DEFAULT '' COMMENT '商品编号',
  `CONCESSIONS` decimal(13,2) DEFAULT '0.00' COMMENT '订单抹零金额',
  `USERID` varchar(32) DEFAULT '' COMMENT '用户ID',
  `CUSTOMERID` varchar(32) DEFAULT '' COMMENT '会员ID',
  `VIPPRICE` decimal(13,2) DEFAULT '0.00' COMMENT 'VIP价格',
  `TYPE` varchar(8) DEFAULT '' COMMENT '产品类型\n            捆绑销售子产品类型bundledsub 普通商品为空',
  `ISCHARGE` char(1) DEFAULT '1' COMMENT '是否收款\n            0表示未收款\n            1表示已收款',
  `PARENT_PRODUCT_ID` varchar(32) DEFAULT '' COMMENT '捆绑销售的时候捆绑ID',
  `SPEC_SIZE` varchar(128) DEFAULT '' COMMENT '尺寸',
  `SPEC_COLOR` varchar(128) DEFAULT '' COMMENT '颜色',
  `PRODUCT_INTEGRAL` decimal(13,2) DEFAULT '0.00' COMMENT '商品积分',
  `IS_INTEGRAL` decimal(8,0) DEFAULT '1' COMMENT '是否可获得积分\n            0表示不可以\n            1表示可以',
  `SHIP_TYPE_ID` varchar(32) DEFAULT '' COMMENT '配送方式ID',
  `SHIP_TYPE_NAME` varchar(64) DEFAULT '' COMMENT '配送方式名称',
  `AFFIXATION` decimal(13,2) DEFAULT '0.00' COMMENT '附加费用',
  `BASE_PRICE` decimal(13,2) DEFAULT '0.00' COMMENT '基础价格',
  `BKFLAG` char(1) DEFAULT '0' COMMENT '是否预定',
  `PROMOTIONS_INFO` varchar(256) DEFAULT '' COMMENT '促销信息',
  `PROMOTIONS_ID` varchar(32) DEFAULT '' COMMENT '促销ID',
  `CLASSTYPE` varchar(128) DEFAULT '' COMMENT '殴飞商品分类类型',
  `ESALES_ORDERID` varchar(128) DEFAULT '' COMMENT '殴飞订单ID',
  `ESALES_AMOUNT` decimal(13,2) DEFAULT '0.00' COMMENT '殴飞订单金额',
  `ORGID` varchar(32) DEFAULT NULL COMMENT '组织机构ID',
  `DISCOUNT_RATE` decimal(13,2) DEFAULT '0.00' COMMENT '折扣比率',
  `DISCOUNT_PRICE` decimal(13,2) DEFAULT '0.00' COMMENT '折扣价格',
  `SPECVALUE2` varchar(32) DEFAULT '' COMMENT '规格2',
  `SPECVALUE1` varchar(32) DEFAULT '' COMMENT '规格1',
  `NEEDINTEGRAL` decimal(8,0) NOT NULL DEFAULT '0' COMMENT '积分',
  `MODEL_ID` varchar(32) DEFAULT NULL,
  `RAPID_REPLENISHMENT` char(1) DEFAULT NULL,
  `REPLENISHMENT_ORDERID` varchar(32) DEFAULT NULL,
  `PROMOTION_TYPE` varchar(8) DEFAULT NULL,
  `PROMOTION_PRICE` decimal(13,2) NOT NULL DEFAULT '0.00' COMMENT '活动价',
  `PROMOTION_ROLE` varchar(8) DEFAULT NULL,
  `PROMOTION_GIFT` varchar(512) DEFAULT NULL,
  `PROMOTION_START_DATE` varchar(26) DEFAULT NULL,
  `PROMOTION_END_DATE` varchar(26) DEFAULT NULL,
  `ESALESNO` varchar(100) DEFAULT NULL,
  `SUPPLY_TYPE` varchar(8) DEFAULT '',
  `CAR_TYPE` varchar(32) DEFAULT '',
  `CAR_BRAND` varchar(32) DEFAULT '',
  `CAR_SERIES` varchar(32) DEFAULT '',
  `SELL_NAME` varchar(64) DEFAULT NULL COMMENT '跟进销售名称',
  `SELL_PHONE` varchar(64) DEFAULT NULL COMMENT '跟进销售电话',
  `INNER_COLOR` varchar(64) DEFAULT NULL COMMENT '内饰颜色',
  PRIMARY KEY (`UUID`,`ORDER_DATE`),
  KEY `idx_orderdetail_orderid` (`ORDERID`),
  KEY `idx_orderdetail_data` (`ORDER_DATE`),
  KEY `idx_orderdetail_pid` (`PRODUCTID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='存放订单里商品的信息'



ordertracer
CREATE TABLE `ordertracer` (
  `UUID` varchar(32) NOT NULL COMMENT '主键',
  `ORDERID` varchar(32) NOT NULL COMMENT '订单ID',
  `OPERDATE` varchar(26) NOT NULL COMMENT '操作时间',
  `STATUS` varchar(8) NOT NULL COMMENT '状态\n            这里的状态和订单的状态是一样的。',
  `OPERATOR` varchar(50) NOT NULL COMMENT '操作人',
  `PCNAME` varchar(64) DEFAULT '' COMMENT '计算机名',
  `MAXNAME` varchar(64) DEFAULT '' COMMENT '网卡地址',
  `IPNAME` varchar(64) DEFAULT '' COMMENT 'IP地址',
  `NOTE` varchar(1024) DEFAULT '' COMMENT '操作说明',
  `SERVICE_REASON` varchar(32) DEFAULT '' COMMENT '服务原因',
  `SERVICE_TYPE` varchar(8) DEFAULT '' COMMENT '服务类型',
  `SERVICE_STATUS` varchar(8) DEFAULT '' COMMENT '服务状态\n            01申请中，02申请关闭，03申请成功',
  `OPERATOR_TYPE` varchar(8) DEFAULT '' COMMENT '操作员类型\n            可能是会员，商户，客服',
  `ORGID` varchar(32) DEFAULT NULL COMMENT '组织机构ID',
  PRIMARY KEY (`UUID`),
  KEY `idx_orderId` (`ORDERID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单的操作日志，订单所有的操作都将生成一'



t_base_ad_content
CREATE TABLE `t_base_ad_content` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `AD_CONTENT` text COMMENT '广告内容',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告内容'



t_base_ad_position_type
CREATE TABLE `t_base_ad_position_type` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `POSITION_NAME` varchar(128) NOT NULL COMMENT '位置名称',
  `POSITION_CODE` varchar(32) NOT NULL COMMENT '位置代码',
  `IMAGE_URL` varchar(255) DEFAULT NULL COMMENT '图片url',
  `HEIGHT` int(11) DEFAULT NULL COMMENT '高度',
  `WIDTH` int(11) DEFAULT NULL COMMENT '宽度',
  `POSITION_TYPE` smallint(6) DEFAULT NULL COMMENT '位置类型N            1=主页N            2=商品目录',
  `DISPLAY_TYPE` smallint(6) DEFAULT NULL COMMENT '显示类型N            1=全部N            2=随机',
  `STATUS` smallint(6) DEFAULT NULL COMMENT '状态',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告位置'



t_base_advertisement
CREATE TABLE `t_base_advertisement` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ADPOSITIONTYPE_ID` int(11) unsigned DEFAULT NULL COMMENT '广告位置外键',
  `ADVERTISEMENT_NAME` varchar(128) NOT NULL COMMENT '广告名称',
  `CONTENT_TYPE` smallint(6) NOT NULL COMMENT '广告内容的类型N            1=图片N            2=FLASH',
  `ADVERTISEMENT_DETAIL` varchar(512) DEFAULT NULL COMMENT '描述，用于IMAGE的TITLE',
  `SOURCE` varchar(255) DEFAULT NULL COMMENT '来源',
  `URL` varchar(255) NOT NULL COMMENT '链接',
  `REDIRECT_URL` varchar(255) DEFAULT NULL COMMENT '要链接的URL',
  `WIDTH` decimal(12,2) DEFAULT NULL COMMENT '宽度',
  `HEIGHT` decimal(12,2) DEFAULT NULL COMMENT '高度',
  `START_PUBLISH_TIME` datetime DEFAULT NULL COMMENT '广告开始时间',
  `END_PUBLISH_TIME` datetime DEFAULT NULL COMMENT '广告结束时间',
  `ORDER_NO` int(10) NOT NULL DEFAULT '0' COMMENT '排列顺序',
  `IS_SHOW` smallint(6) DEFAULT NULL COMMENT '是否发布',
  `STATUS` smallint(6) DEFAULT NULL COMMENT '状态       ',
  `VERSION` int(11) NOT NULL DEFAULT '0' COMMENT '版本',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_ADVERTISEMENT_2_AD_POSITION_TYPE` (`ADPOSITIONTYPE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='广告'



t_base_bigarea
CREATE TABLE `t_base_bigarea` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `BIG_AREA_ID` varchar(36) NOT NULL COMMENT '大区ID',
  `BIG_AREA_NAME` varchar(100) DEFAULT NULL COMMENT '大区名称',
  `BRAND_CODE` varchar(32) DEFAULT NULL COMMENT '品牌',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改日期',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=20014 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的大区信息。'



t_base_brand
CREATE TABLE `t_base_brand` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
  `CATEGORY_ID` int(10) unsigned DEFAULT NULL,
  `BRAND_NAME_CN` varchar(255) DEFAULT NULL COMMENT '品牌中文名',
  `BRAND_NAME_EN` varchar(255) DEFAULT NULL COMMENT '品牌英文名',
  `BRAND_CODE` varchar(255) DEFAULT NULL COMMENT '品牌编码',
  `BRAND_LOGO` varchar(255) DEFAULT NULL COMMENT '品牌logo',
  `SORT_ORDER` int(11) DEFAULT NULL COMMENT '排序',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime DEFAULT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=183 DEFAULT CHARSET=utf8 COMMENT='品牌主表'



t_base_car_brand
CREATE TABLE `t_base_car_brand` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '品牌ID',
  `CAR_BRAND_EN` varchar(50) NOT NULL COMMENT '品牌英文名称',
  `CAR_BRAND_CN` varchar(50) NOT NULL COMMENT '品牌中文名称',
  `CAR_BRAND_ALIAS` varchar(50) DEFAULT NULL COMMENT '品牌别名',
  `LOGO_IMG` varchar(256) DEFAULT NULL COMMENT '品牌LOGO',
  `MDM_CAR_BRAND_CODE` varchar(50) DEFAULT NULL COMMENT 'MDM品牌编码（T_BASE_CAR_BRAND_MDM.CAR_BRAND_CODE）',
  `MDM_CAR_BRAND_EN` varchar(50) NOT NULL COMMENT 'MDM品牌英文名称',
  `MDM_CAR_BRAND_CN` varchar(50) NOT NULL COMMENT 'MDM品牌中文名称',
  `PRODUCT_BRAND_ID` int(11) DEFAULT NULL COMMENT '商品品牌ID（T_BASE_BRAND.ID）',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX1_T_E4S_DB_CAR_BRAND` (`CAR_BRAND_EN`),
  KEY `IDX2_T_E4S_DB_CAR_BRAND` (`CAR_BRAND_CN`),
  KEY `idx_ORDER_NO` (`ORDER_NO`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='基础信息，品牌信息。'



t_base_car_brand_mdm
CREATE TABLE `t_base_car_brand_mdm` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `CAR_BRAND_CODE` varchar(50) NOT NULL COMMENT '车辆品牌编码',
  `CAR_BRAND_EN` varchar(50) DEFAULT NULL COMMENT '品牌英文名',
  `CAR_BRAND_CN` varchar(50) DEFAULT NULL COMMENT '品牌中文名',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='基础信息，与MDM系统对接的品牌信息。'



t_base_car_color
CREATE TABLE `t_base_car_color` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `COLOR_TYPE` int(11) NOT NULL COMMENT '颜色类型（1-外观，2-内饰）',
  `COLOR_NAME` varchar(50) NOT NULL COMMENT '颜色名称',
  `MDM_COLOR_ID` varchar(36) DEFAULT NULL COMMENT '对应的MDM颜色ID（外观：T_BASE_COLOR_MDM.CAR_COLOR_ID；内饰：T_BASE_CAR_INCOLOR_MAM.CAR_INCOLOR_ID）',
  `RGB_VALUE` varchar(32) DEFAULT NULL COMMENT '颜色RGB值',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改日期',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8 COMMENT='基础数据，外观(color_type=1)、内饰(color_type=2)颜色信息表。'



t_base_car_color_mdm
CREATE TABLE `t_base_car_color_mdm` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `CAR_COLOR_ID` varchar(36) NOT NULL COMMENT '车身颜色ID',
  `CAR_COLOR_CODE` varchar(50) NOT NULL COMMENT '车身颜色编码',
  `CAR_COLOR_NAME` varchar(100) NOT NULL COMMENT '车身颜色名称',
  `SUPPLY_STATUS` varchar(2) NOT NULL COMMENT '供应状态',
  `CAR_BRAND_CODE` varchar(50) NOT NULL COMMENT '车辆品牌编码',
  `COLOR_BOLID` varchar(32) DEFAULT NULL COMMENT 'RGB颜色代码',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX1_T_E4S_DB_CAR_COLOR` (`CAR_COLOR_CODE`),
  KEY `IDX2_T_E4S_DB_CAR_COLOR` (`CAR_BRAND_CODE`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的车身颜色信息。'



t_base_car_incolor_mdm
CREATE TABLE `t_base_car_incolor_mdm` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `CAR_INCOLOR_ID` varchar(36) NOT NULL COMMENT '内饰颜色ID',
  `CAR_INCOLOR_CODE` varchar(50) NOT NULL COMMENT '内饰颜色编码',
  `CAR_INCOLOR_NAME` varchar(100) NOT NULL COMMENT '内饰颜色名称',
  `CAR_BRAND_CODE` varchar(50) NOT NULL COMMENT '车辆品牌编码',
  `COLOR_BOLID` varchar(32) DEFAULT NULL COMMENT 'RGB颜色代码',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX1_T_E4S_DB_CAR_INCOLOR` (`CAR_INCOLOR_CODE`),
  KEY `IDX2_T_E4S_DB_CAR_INCOLOR` (`CAR_BRAND_CODE`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的内饰颜色信息。'



t_base_car_owner
CREATE TABLE `t_base_car_owner` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `MEMBER_ID` int(11) unsigned NOT NULL COMMENT '会员编号',
  `CAR_MODEL_ID` int(10) unsigned DEFAULT NULL COMMENT '车型ID',
  `CAR_SERIES_CODE` varchar(50) DEFAULT NULL,
  `EXTERIOR_COLOR` varchar(255) DEFAULT NULL COMMENT '外观颜色',
  `INTERIOR_COLOR` varchar(255) DEFAULT NULL COMMENT '内饰颜色',
  `DEALER_ID` int(10) unsigned DEFAULT NULL COMMENT '经销商ID',
  `IC_CARD_NO` varchar(17) DEFAULT NULL COMMENT '会员卡号',
  `VIN` varchar(20) DEFAULT NULL COMMENT 'VIN码',
  `CAR_NO` varchar(255) DEFAULT NULL COMMENT '车牌号',
  `ENGINE_NO` varchar(50) DEFAULT NULL COMMENT '发动机号',
  `POINTS` varchar(128) DEFAULT NULL COMMENT '会员积分',
  `CARD_DEGREE_NAME` varchar(50) DEFAULT NULL COMMENT '会员级别',
  `PURCHASING_DATE` date DEFAULT NULL COMMENT '购买时间',
  `CUST_NO` varchar(32) DEFAULT NULL COMMENT '客户一元化编号',
  `IS_PARTER` tinyint(4) DEFAULT NULL COMMENT '是否合伙人，0否1是',
  `REG_PARTER_TIME` datetime DEFAULT NULL COMMENT '注册合伙人时间',
  `CA` varchar(255) DEFAULT NULL,
  `SA` varchar(255) DEFAULT NULL,
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_BASE_MEMBER_CONTACT_T_BASE_MEMBER_1` (`MEMBER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='车主信息'



t_base_car_series
CREATE TABLE `t_base_car_series` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `MDM_CAR_SERIES_ID` varchar(36) NOT NULL COMMENT 'MDM车系ID',
  `MDM_CAR_SERIES_CODE` varchar(50) NOT NULL COMMENT 'MDM车系编码',
  `CAR_BRAND_ID` int(10) NOT NULL COMMENT '品牌ID（T_BASE_CAR_BRAND.ID）',
  `CAR_SERIES_CN` varchar(50) NOT NULL COMMENT '车系中文名称',
  `CAR_SERIES_EN` varchar(50) DEFAULT NULL COMMENT '车系英文名称',
  `CAR_LEVEL` int(10) DEFAULT NULL COMMENT '车系级别（MPV，SUV，中型车，小型车）',
  `OFFICIAL_CAR_LEVEL` int(10) DEFAULT NULL COMMENT '官网车系级别',
  `CAR_SERIES_ALIAS` varchar(100) DEFAULT NULL COMMENT '车系别名',
  `CAR_PROPERTY` varchar(50) DEFAULT NULL COMMENT '车系属性（热销，推荐，钜惠，新车，购置税减半）',
  `PC_THUMBNAIL` varchar(255) DEFAULT NULL COMMENT 'PC端缩略图',
  `WAP_THUMBNAIL` varchar(255) DEFAULT NULL COMMENT 'wap端缩略图',
  `BRIEF_INTRODUTION` varchar(1024) DEFAULT NULL COMMENT '车系简介',
  `ENERGY_CATEGORY` int(10) DEFAULT NULL COMMENT '能源类目（燃油车，纯电动）',
  `START_GUIDEPRICE` int(11) DEFAULT NULL COMMENT '最低指导价',
  `END_GUIDEPRICE` int(11) DEFAULT NULL COMMENT '最高指导价',
  `IS_TESTDRIVE` char(1) DEFAULT NULL COMMENT '是否接受试驾',
  `STRUCTURE` varchar(2) DEFAULT NULL COMMENT '车身结构',
  `SALES` int(11) DEFAULT NULL COMMENT '销量',
  `QCZJ_GRADE` varchar(32) DEFAULT NULL COMMENT '汽车之家口碑',
  `YCW_GRADE` varchar(32) DEFAULT NULL COMMENT '易车网口碑',
  `TPYQC_GRADE` varchar(32) DEFAULT NULL COMMENT '太平洋汽车口碑',
  `AKQC_GRADE` varchar(32) DEFAULT NULL COMMENT '爱卡汽车口碑',
  `ORDER_NO` decimal(10,0) DEFAULT '0' COMMENT '排序',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX2_T_E4S_DB_VE_CAR_SERIES` (`CAR_SERIES_CN`)
) ENGINE=InnoDB AUTO_INCREMENT=492924 DEFAULT CHARSET=utf8 COMMENT='基础数据，车系信息。'



t_base_car_series_mapping
CREATE TABLE `t_base_car_series_mapping` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `CAR_SERIES_ID` int(10) DEFAULT NULL COMMENT '车系ID',
  `MEDIA_CAR_SERIES_ID` varchar(64) DEFAULT NULL COMMENT '媒体数据ID',
  `MEDIA_CAR_SERIES_NAME` varchar(64) DEFAULT NULL COMMENT '媒体数据名称',
  `MEDIA_FROM` varchar(64) DEFAULT NULL COMMENT '媒体数据来源（1-汽车之家，2-天猫）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8 COMMENT='基础数据，从外部媒体抓取的车系与本平台车系的映射关系信息。'



t_base_car_series_mdm
CREATE TABLE `t_base_car_series_mdm` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `CAR_SERIES_ID` varchar(36) NOT NULL COMMENT '车系ID',
  `CAR_SERIES_CODE` varchar(50) NOT NULL COMMENT '车系编码',
  `CAR_BRAND_CODE` varchar(50) NOT NULL COMMENT '品牌编码',
  `CAR_SERIES_CN` varchar(50) NOT NULL COMMENT '车系中文名称',
  `CAR_SERIES_EN` varchar(50) DEFAULT NULL COMMENT '车系英文名称',
  `GDSNAME` varchar(50) DEFAULT NULL COMMENT 'GDS车系名称',
  `BEGIN_DATE` datetime DEFAULT NULL COMMENT '投产日期',
  `END_DATE` datetime DEFAULT NULL COMMENT '停产日期',
  `PART_SERIES_CODE` varchar(50) DEFAULT NULL COMMENT '备件车系编码',
  `ANSWER_CAR_SERIES_ID` varchar(20) DEFAULT NULL COMMENT 'ANSWER车系',
  `OLD_CARSERIES_ID` decimal(20,0) DEFAULT NULL COMMENT '旧车系ID',
  `SAP_CARSERIES_CODE` varchar(50) DEFAULT NULL COMMENT '车系SAP编码',
  `ORDER_NO` int(11) DEFAULT '999' COMMENT '排列顺序',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=132 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的车系信息。'



t_base_car_type
CREATE TABLE `t_base_car_type` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `MDM_CAR_TYPE_CODE` varchar(50) DEFAULT NULL COMMENT '对应的MDM车型编码',
  `CAR_BRAND_ID` int(10) DEFAULT NULL COMMENT '品牌ID',
  `CAR_SERIES_ID` int(10) DEFAULT NULL COMMENT '车系ID',
  `MODEL_YEAR` varchar(10) DEFAULT NULL COMMENT '年款（2015,2016...）',
  `CAR_TYPE_NAME` varchar(100) DEFAULT NULL COMMENT '车型名称',
  `CAR_LEVEL` int(10) DEFAULT NULL COMMENT '车型级别（MPV,SUV,中型车，小型车，根据关联的车系对应级别继承而来。）',
  `GUIDE_PRICE` int(11) DEFAULT NULL COMMENT '官方指导价',
  `OFFER_PRICE_SECTION` varchar(50) DEFAULT NULL COMMENT '安全报价区间',
  `CAR_TYPE_STATUS` int(10) DEFAULT NULL COMMENT '厂商车型状况（待售，在售，停售）',
  `COLOR_CODE` varchar(500) DEFAULT NULL COMMENT '外观颜色编码',
  `INCOLOR_CODE` varchar(500) DEFAULT NULL COMMENT '内饰颜色编码',
  `QUALITY_ASSURANCE` int(10) DEFAULT NULL COMMENT '整车质保',
  `CHARACTERISTIC_ACTIVITY` varchar(50) DEFAULT NULL COMMENT '特色活动',
  `PRODUCT_SPOT` varchar(500) DEFAULT NULL COMMENT '产品亮点',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=448 DEFAULT CHARSET=utf8 COMMENT='基础数据，车型信息表。'



t_base_car_type_mapping
CREATE TABLE `t_base_car_type_mapping` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `CAR_TYPE_ID` int(10) DEFAULT NULL COMMENT '车型ID（T_BASE_CAR_TYPE.ID）',
  `MEDIA_CAR_TYPE_ID` varchar(64) DEFAULT NULL COMMENT '媒体数据ID',
  `MEDIA_CAR_TYPE_NAME` varchar(64) DEFAULT NULL COMMENT '媒体数据名称',
  `MEDIA_FROM` varchar(64) DEFAULT NULL COMMENT '媒体数据来源（1-汽车之家，2-天猫）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=445 DEFAULT CHARSET=utf8 COMMENT='基础数据，从外部媒体抓取的车型与本平台车型的映射关系信息。'



t_base_car_type_property
CREATE TABLE `t_base_car_type_property` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `CAR_TYPE_ID` int(10) NOT NULL COMMENT '车型ID',
  `PROPERTY_ID` int(10) NOT NULL COMMENT '属性ID',
  `PROPERTY_VALUE` varchar(500) DEFAULT NULL,
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATE_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=30705 DEFAULT CHARSET=utf8 COMMENT='基础数据，车型信息表。'



t_base_car_type_property_template
CREATE TABLE `t_base_car_type_property_template` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `PROPERTY_KEY` varchar(50) NOT NULL COMMENT '属性KEY值',
  `NAME` varchar(32) NOT NULL COMMENT '属性名',
  `PARENT_ID` int(10) NOT NULL DEFAULT '0' COMMENT '父属性ID',
  `REMARK` varchar(128) DEFAULT NULL COMMENT '备注',
  `IS_EDITABLE` char(1) NOT NULL DEFAULT '1' COMMENT '是否可编辑',
  `DEFUALT_VALUE` varchar(256) DEFAULT NULL COMMENT '默认值',
  `EDIT_TYPE` char(2) DEFAULT NULL COMMENT '输入类型',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATE_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=351 DEFAULT CHARSET=utf8 COMMENT='基础数据，车型属性模板表。'



t_base_category
CREATE TABLE `t_base_category` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `CATEGORY_NAME` varchar(255) DEFAULT NULL COMMENT '分类名称',
  `PARENT_ID` int(11) unsigned DEFAULT NULL COMMENT '父类编号',
  `CATEGORY_TYPE` int(11) DEFAULT NULL COMMENT '产品分类, 1实物商品 2虚拟商品 3其他',
  `CATEGORY_LEVEL` int(11) DEFAULT NULL COMMENT '分类级别',
  `CATEGORY_DESC` varchar(255) DEFAULT NULL COMMENT '描述',
  `SORT_ORDER` int(11) DEFAULT NULL COMMENT '排序',
  `ICON` varchar(255) DEFAULT NULL COMMENT 'icon url地址',
  `USED_BY_DLR` varchar(2) DEFAULT NULL COMMENT '经销商是否可选',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `TREE_PATH` varchar(32) DEFAULT NULL COMMENT '所有父节点的路径',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8 COMMENT='商品的基础分类'



t_base_city
CREATE TABLE `t_base_city` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `CITY_ID` varchar(36) NOT NULL DEFAULT '0' COMMENT '城市ID',
  `PROVINCE_ID` varchar(36) NOT NULL COMMENT '省份ID',
  `CITY_CODE` varchar(50) NOT NULL,
  `CITY_NAME` varchar(100) NOT NULL COMMENT '城市名称',
  `CITY_ALIAS` varchar(100) DEFAULT NULL COMMENT '城市别名',
  `IS_LIMITED` char(2) DEFAULT NULL COMMENT '是否限购城市',
  `IS_CAPITAL` char(2) NOT NULL DEFAULT '0' COMMENT '是否省会城市',
  `IS_POPULAR` char(2) DEFAULT NULL COMMENT '是否热门城市（0-否，1-是）',
  `IS_MUNICIPALITY` char(2) DEFAULT NULL COMMENT '是否直辖市（0-否，1-是）',
  `REGIONALISM_CODE` varchar(36) DEFAULT NULL COMMENT '国家统计局行政区划代码',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(32) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
  `MODIFIER` varchar(32) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改日期',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=20442 DEFAULT CHARSET=utf8 COMMENT='基础信息，城市信息表。'



t_base_common_praise
CREATE TABLE `t_base_common_praise` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '口碑编号',
  `COMMON_PRAISE_TYPE` tinyint(255) DEFAULT NULL COMMENT '评价类型，1产品，2SKU，3order_item',
  `TARGET_ID` int(11) unsigned DEFAULT NULL COMMENT '产品ID/商品ID/订单商品ID，根据TYPE来确定',
  `MEMBER_ID` int(11) unsigned DEFAULT NULL COMMENT '会员编号',
  `OWNER_ID` int(11) unsigned DEFAULT NULL COMMENT '经销商ID/金融品牌商ID',
  `TITLE` varchar(255) DEFAULT NULL COMMENT '口碑标题',
  `PUB_DATE` varchar(255) DEFAULT NULL COMMENT '发布日期',
  `PICTURES` varchar(255) DEFAULT NULL COMMENT '图片',
  `CONTENT` varchar(255) DEFAULT NULL COMMENT '内容',
  `VISIT` int(11) DEFAULT NULL COMMENT '浏览数',
  `SOURCE` varchar(255) DEFAULT NULL COMMENT '来源',
  `STATUS` varchar(255) DEFAULT NULL COMMENT '状态',
  `SCORES` longtext COMMENT '评价',
  `IP_ADDRESS` varchar(64) DEFAULT NULL COMMENT '评论者的IP',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_通用口碑记录_产品_1` (`TARGET_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COMMENT='会员对商品/产品的咨询/评价'



t_base_common_praise_reply
CREATE TABLE `t_base_common_praise_reply` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
  `COMMON_PRAISE_ID` int(11) unsigned DEFAULT NULL COMMENT '会员评价ID',
  `REF_ID` int(10) unsigned DEFAULT NULL COMMENT '引用id',
  `MEMBER_ID` int(11) unsigned DEFAULT NULL COMMENT '会员编号',
  `COMMON_PRAISE_TYPE` tinyint(255) DEFAULT NULL COMMENT '评论回复类型',
  `TITLE` varchar(255) DEFAULT NULL COMMENT '标题',
  `PUB_DATE` varchar(255) DEFAULT NULL COMMENT '发布日期',
  `PICTURES` varchar(255) DEFAULT NULL COMMENT '图片',
  `CONTENT` varchar(5000) DEFAULT NULL COMMENT '内容',
  `VISIT` int(11) DEFAULT NULL COMMENT '浏览数',
  `STATUS` varchar(255) DEFAULT NULL COMMENT '状态',
  `IP_ADDRESS` varchar(64) DEFAULT NULL COMMENT '评论者的IP',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_通用口碑记录_产品_1` (`COMMON_PRAISE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='评论回复'



t_base_county
CREATE TABLE `t_base_county` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `COUNTY_ID` varchar(36) NOT NULL DEFAULT '0' COMMENT '区县ID',
  `CITY_ID` varchar(36) NOT NULL COMMENT '城市ID',
  `COUNTY_CODE` varchar(50) NOT NULL,
  `COUNTY_NAME` varchar(100) NOT NULL COMMENT '区县名称',
  `REGIONALISM_CODE` varchar(36) DEFAULT NULL COMMENT '国家统计局行政区划代码',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(32) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
  `MODIFIER` varchar(32) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改日期',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5452 DEFAULT CHARSET=utf8 COMMENT='基础信息，区县信息表。'



t_base_data_dict
CREATE TABLE `t_base_data_dict` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `DICTGROUP_ID` int(11) unsigned DEFAULT NULL COMMENT '分组id, 比如友情链接，基础数据等等',
  `DICT_KEY` varchar(255) DEFAULT NULL COMMENT '名',
  `DICT_VALUE` varchar(255) DEFAULT NULL COMMENT '值',
  `DICT_EXT_VALUES` varchar(1000) DEFAULT NULL COMMENT '扩展值，json:\r\n{\r\n    "attribute1": "value1", \r\n    "attribute2": "value2", \r\n    "attribute3": "value3", \r\n    "attribute4": "value4",\r\n......\r\n}',
  `SORT_ORDER` int(11) DEFAULT '0' COMMENT '排序',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_DATA_DICT_DATA_DICT_GROUP_1` (`DICTGROUP_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2607 DEFAULT CHARSET=utf8 COMMENT='字典值'



t_base_data_dict_group
CREATE TABLE `t_base_data_dict_group` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `DICTGROUP_NAME` varchar(255) DEFAULT NULL COMMENT '分组名，比如友情链接，基础数据等等',
  `REMARK` varchar(1000) DEFAULT NULL COMMENT '备注',
  `SORT_ORDER` int(11) DEFAULT '0' COMMENT '排序',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=utf8 COMMENT='字典组'



t_base_dealer
CREATE TABLE `t_base_dealer` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '经销店ID',
  `DLR_CODE` varchar(10) NOT NULL COMMENT '经销店编号',
  `DLR_SHORT_NAME` varchar(50) NOT NULL COMMENT '经销商简称',
  `DLR_FULL_NAME` varchar(200) NOT NULL COMMENT '经销商全称',
  `DLR_PROP` varchar(36) DEFAULT NULL COMMENT '经销商性质（一网店，二网店，三网店，四网店）',
  `PARENT_DLR_ID` varchar(36) DEFAULT NULL COMMENT '上级网点ID',
  `DLR_STATUS` varchar(10) DEFAULT NULL COMMENT '专营店状态（营业店，在建店，取消店，退出店，停业店，虚拟店）',
  `DLR_LEVEL` varchar(10) DEFAULT NULL COMMENT '经销商级别（A,B,C,D,E,F1,F2）',
  `CAR_SERIES_IDS` varchar(1000) DEFAULT NULL COMMENT '所售车系ID集合',
  `SALE_CITY_IDS` varchar(5000) DEFAULT NULL COMMENT '所售区域（售全国：“1”；售本省：“2，省份id”；售本市：“3，城市id”；售多地：“4，城市id，城市id，城市id...”）',
  `GROUP_ID` varchar(36) DEFAULT NULL COMMENT '集团ID',
  `EMAIL` varchar(200) DEFAULT NULL COMMENT '邮箱',
  `SALE_TEL` varchar(200) DEFAULT NULL COMMENT '销售热线电话',
  `SERVICE_TEL` varchar(200) DEFAULT NULL COMMENT '服务热线电话（400电话）',
  `SERVICE_TEL_SUB` varchar(200) DEFAULT NULL COMMENT '400绑定号码',
  `INSURANCE_TEL` varchar(200) DEFAULT NULL COMMENT '保险热线',
  `URG_SOS_TEL` varchar(200) DEFAULT NULL COMMENT '紧急救援热线',
  `MDM_CAR_BRAND_CODE` varchar(50) NOT NULL COMMENT '从MDM同步过来的经营品牌',
  `CBB_CAR_BRAND_CODE` varchar(50) DEFAULT NULL COMMENT '车巴巴经营品牌',
  `BUSINESS_DOMAIN` varchar(50) DEFAULT NULL COMMENT '业务范畴（全部，售前，售后）',
  `SUBDIVISION_BUSINESS` varchar(50) DEFAULT NULL COMMENT '细分业务（进口授权etc）',
  `IS_VIP` tinyint(1) DEFAULT NULL COMMENT '是否堡垒店（是否VIP）',
  `SERVICE_AUTH` varchar(500) DEFAULT NULL COMMENT '服务认证情况（共网服务，易租车，绿色认证等）',
  `PRE_SALES_SCORE` decimal(8,2) DEFAULT NULL COMMENT '售前评分',
  `AFTER_SALES_SCORE` decimal(8,2) DEFAULT NULL COMMENT '售后评分',
  `PRE_SALES_SCORE_PROP` decimal(8,2) DEFAULT NULL COMMENT '售前评分比例',
  `AFTER_SALES_SCORE_PROP` decimal(8,2) DEFAULT NULL COMMENT '售后评分比例',
  `CLUE_HANDLE_EFFICIENCY` varchar(50) DEFAULT NULL COMMENT '线索处理及时率',
  `DLR_LIVENESS` varchar(50) DEFAULT NULL COMMENT '经销商活跃度',
  `IS_FROZEN` tinyint(1) DEFAULT NULL COMMENT '是否冻结',
  `FREEZE_REASON` varchar(500) DEFAULT NULL COMMENT '冻结原因',
  `DLR_IMAGE_URL` varchar(255) DEFAULT NULL COMMENT '门店图片URL',
  `BIG_AREA_ID` varchar(36) DEFAULT NULL COMMENT '大区ID',
  `SMALL_AREA_ID` varchar(36) DEFAULT NULL COMMENT '小区ID',
  `PROVINCE_ID` varchar(36) NOT NULL COMMENT '省份ID',
  `CITY_ID` varchar(36) NOT NULL COMMENT '城市ID',
  `COUNTY_ID` varchar(36) DEFAULT NULL COMMENT '区域',
  `CONT_ADDRESS` varchar(255) DEFAULT NULL COMMENT '通讯详细地址',
  `ZIP_CODE` varchar(64) DEFAULT NULL COMMENT '邮编',
  `LONGITUDE` decimal(10,6) DEFAULT NULL COMMENT '经度(百度地图)，10，6',
  `LATITUDE` decimal(10,6) DEFAULT NULL COMMENT '纬度(百度地图)，10，6',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序字段',
  `ALIPAY_NO` varchar(255) DEFAULT NULL COMMENT '支付宝账号',
  `ALIPAY_NAME` varchar(255) DEFAULT NULL COMMENT '支付宝账户名',
  `ALIPAY_KEY` varchar(255) DEFAULT NULL COMMENT '支付宝密钥',
  `WECHAT_NO` varchar(255) DEFAULT NULL COMMENT '微信账户',
  `WECHAT_APP_ID` varchar(255) DEFAULT NULL COMMENT '微信APP ID',
  `WECHAT_APP_SECRET` varchar(255) DEFAULT NULL COMMENT '微信APP密钥',
  `ACCOUNT_NAME` varchar(64) DEFAULT NULL COMMENT '开户名称',
  `OPENING_BANK` varchar(255) DEFAULT NULL COMMENT '开户银行',
  `OPENING_ACCOUNT` varchar(255) DEFAULT NULL COMMENT '开户账号',
  `WECHAT_DLR_NUM` varchar(50) DEFAULT NULL COMMENT '微信商户号',
  `IS_SYNC_WECHAT` tinyint(1) DEFAULT NULL COMMENT '是否同步到微信门店（0-否，1-是）',
  `IS_SYNC_MDM` tinyint(1) DEFAULT NULL COMMENT '是否同步MDM的专营店信息（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3105 DEFAULT CHARSET=utf8 COMMENT='基础数据，专营店信息。'



t_base_dealer_mapping
CREATE TABLE `t_base_dealer_mapping` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `DEALER_ID` int(10) DEFAULT NULL COMMENT '专营店ID（T_BASE_DEALER.ID）',
  `MEDIA_DEALER_ID` varchar(64) DEFAULT NULL COMMENT '媒体数据ID',
  `MEDIA_DEALER_NAME` varchar(64) DEFAULT NULL COMMENT '媒体数据名称',
  `MEDIA_FROM` varchar(64) DEFAULT NULL COMMENT '媒体数据来源（1-汽车之家，2-天猫）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=216 DEFAULT CHARSET=utf8 COMMENT='基础数据，从外部媒体抓取的专营店与本平台专营店的映射关系信息。'



t_base_dealer_mdm
CREATE TABLE `t_base_dealer_mdm` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `MDM_DLR_ID` varchar(36) NOT NULL DEFAULT '' COMMENT '专营店ID',
  `DLR_CODE` varchar(10) NOT NULL COMMENT '专营店编码',
  `DLR_SHORT_NAME` varchar(100) NOT NULL COMMENT '专营店简称',
  `DLR_FULL_NAME` varchar(200) NOT NULL COMMENT '专营店全称',
  `DLR_EN_NAME` varchar(200) DEFAULT NULL COMMENT '专营店英文名',
  `DLR_NAME_OLD` varchar(200) DEFAULT NULL COMMENT '专营店曾用名',
  `COMPANY_NAME_OLD` varchar(200) DEFAULT NULL COMMENT '公司曾用名',
  `COMP_SPELL` varchar(200) DEFAULT NULL COMMENT '公司拼音',
  `COMP_TYPE` varchar(10) DEFAULT NULL COMMENT '公司类型',
  `PARENT_DLR_ID` varchar(36) DEFAULT NULL COMMENT '上级网点ID',
  `DLR_ANSWER_CODE` varchar(4) DEFAULT NULL COMMENT '专营店ANSWER编码',
  `SAP_DLR_ID` varchar(10) DEFAULT NULL COMMENT 'SAP专营店ID',
  `DLR_SYMBOL` varchar(50) DEFAULT NULL COMMENT '名称缩写代码',
  `GUNO` varchar(50) DEFAULT NULL COMMENT '组织机构代号',
  `REGISTER_MONEY` decimal(18,6) DEFAULT NULL COMMENT '注册资金',
  `S_REGISTER_MONEY` decimal(18,6) DEFAULT NULL COMMENT '拟组建公司注册资金',
  `DLR_HARDWARE_CLASS` varchar(20) DEFAULT NULL COMMENT '专营店硬体级别',
  `SHOW_ACREAGE` varchar(200) DEFAULT NULL COMMENT '展厅面积',
  `FACTORY_ACREAGE` varchar(200) DEFAULT NULL COMMENT '车间面积',
  `COVER_ACREAGE` varchar(200) DEFAULT NULL COMMENT '占地面积',
  `TATOL_ACREAGE` varchar(200) DEFAULT NULL COMMENT '总建筑面积',
  `FARE_RANGE` varchar(500) DEFAULT NULL COMMENT '经营范围',
  `DLR_BUSS_DATE` datetime DEFAULT NULL COMMENT '专营店营业时间',
  `DLR_LEVEL` varchar(10) DEFAULT NULL COMMENT '专营店级别',
  `DLR_DEBUT_TIME` datetime DEFAULT NULL COMMENT '开业验收时间',
  `LINK_ADDR` varchar(250) DEFAULT NULL COMMENT '联络地址',
  `SMALL_AREA_ID` varchar(36) DEFAULT NULL COMMENT '小区ID',
  `BIG_AREA_ID` varchar(36) DEFAULT NULL COMMENT '大区ID',
  `PROVINCE_ID` varchar(36) DEFAULT NULL COMMENT '省份ID',
  `CITY_ID` varchar(36) DEFAULT NULL COMMENT '城市ID',
  `COUNTY_ID` varchar(36) DEFAULT NULL COMMENT '区县ID',
  `FAX` varchar(200) DEFAULT NULL COMMENT '传真',
  `PHONE` varchar(200) DEFAULT NULL COMMENT '电话号码',
  `MOBILE` varchar(200) DEFAULT NULL COMMENT '手机号码',
  `ZIP` varchar(100) DEFAULT NULL COMMENT '邮编',
  `EMAIL` varchar(200) DEFAULT NULL COMMENT '邮箱',
  `URG_SOS_TEL` varchar(200) DEFAULT NULL COMMENT '紧急救援电话',
  `TEL_SALE` varchar(200) DEFAULT NULL COMMENT '销售热线电话',
  `SALE_FAX` varchar(200) DEFAULT NULL COMMENT '售前传真',
  `SALE_EMAIL` varchar(200) DEFAULT NULL COMMENT '销售邮箱',
  `SERVICE_TEL_FIX` varchar(200) DEFAULT NULL COMMENT '服务热线电话',
  `SERVICE_FAX` varchar(200) DEFAULT NULL COMMENT '服务传真',
  `SERVICE_EMAIL` varchar(200) DEFAULT NULL COMMENT '售后邮箱',
  `LEGAL_PERSON` varchar(100) DEFAULT NULL COMMENT '法人',
  `MASTER_CARD` varchar(20) DEFAULT NULL COMMENT '法人代表证件编码',
  `MASTER_CARD_TYPE` varchar(50) DEFAULT NULL COMMENT '法人代表证件类型',
  `S_MASTER` varchar(100) DEFAULT NULL COMMENT '签约公司法人代表',
  `S_MASTER_CONN` varchar(200) DEFAULT NULL COMMENT '法人代表联系方式',
  `S_ADDR` varchar(400) DEFAULT NULL COMMENT '通讯地址及邮编',
  `MANAGER_NAME` varchar(100) DEFAULT NULL COMMENT '店长姓名',
  `MANAGER_TEL` varchar(200) DEFAULT NULL COMMENT '店长电话',
  `BALANCE_CERTIFICATE` varchar(200) DEFAULT NULL COMMENT '结算资格',
  `BALANCE_DATE` datetime DEFAULT NULL COMMENT '结算日期',
  `MAINTAIN_CERTIFICATE` varchar(200) DEFAULT NULL COMMENT '汽车维修资格',
  `MAINTAIN_CERT_DATE` datetime DEFAULT NULL COMMENT '汽车维修资格获取日期',
  `INIT_DATE` datetime DEFAULT NULL COMMENT 'DMS店上线日期',
  `GROUP_ID` varchar(36) DEFAULT NULL COMMENT '集团ID',
  `CEO` varchar(100) DEFAULT NULL COMMENT '建店联系人',
  `CEO_CONN` varchar(50) DEFAULT NULL COMMENT '建店联系人手机号码',
  `ORG_MODEL_CODE` varchar(100) DEFAULT NULL COMMENT '组织机构模型编号',
  `INIT_FLAG` varchar(26) DEFAULT NULL COMMENT '上线初始化标志',
  `CERTIFICATE_FLAG` varchar(10) DEFAULT NULL COMMENT '认证标志',
  `DLR_STATUS` varchar(10) DEFAULT NULL COMMENT '专营店状态',
  `DLR_RELEATION` varchar(4) DEFAULT NULL COMMENT '专营店关联关系',
  `DLR_TYPE` varchar(5) DEFAULT NULL COMMENT '专营店类型',
  `RELEATION_STATUS` varchar(10) DEFAULT NULL COMMENT '关联关系维护状态',
  `ORDER_NO` varchar(26) DEFAULT NULL COMMENT '排序',
  `REMARK` varchar(500) DEFAULT NULL COMMENT '线索备注',
  `CAR_BRAND_CODE` varchar(50) DEFAULT NULL COMMENT '车辆品牌编码',
  `DOQD_FLAG` varchar(10) DEFAULT NULL COMMENT 'DOQD标记',
  `DLR_SORT` varchar(10) DEFAULT NULL COMMENT '专营店分类',
  `DP_ORG_ID` varchar(36) DEFAULT NULL COMMENT 'DP组织ID',
  `MDS_BIG_AREA_ID` varchar(36) DEFAULT NULL COMMENT 'MDS大区ID',
  `PV_COMP_CODE` varchar(5) DEFAULT NULL COMMENT '所属PV公司代码',
  `IS_SYNCHRONOUS` varchar(10) DEFAULT NULL COMMENT '是否同步信息',
  `AREA` varchar(36) DEFAULT NULL COMMENT '区域',
  `ORG_TYPE` varchar(36) DEFAULT NULL COMMENT '专营店类别',
  `LINK_DLR_ID` varchar(36) DEFAULT NULL COMMENT '连体店',
  `ONLINE_FLAG` varchar(10) DEFAULT NULL COMMENT '新E3S上线标记(上线1，未上0)',
  `ONLINE_TIME` datetime DEFAULT NULL COMMENT '新E3S上线时间',
  `IS_USED_MDS` varchar(2) DEFAULT '0' COMMENT '是否已切换MDS 0未切换MDS;1已切换MDS',
  `IS_USED_COC` varchar(2) DEFAULT '0' COMMENT '是否已切换COC 0未切换COC;1已切换COC',
  `longitude` varchar(50) DEFAULT NULL COMMENT '经度',
  `latitude` varchar(50) DEFAULT NULL COMMENT '纬度',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX2_T_E4S_ORG_DLR` (`DLR_SHORT_NAME`)
) ENGINE=InnoDB AUTO_INCREMENT=7647 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的专营店信息表。'



t_base_employee
CREATE TABLE `t_base_employee` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `EMP_ID` varchar(36) NOT NULL COMMENT '职员ID',
  `DLR_CODE` varchar(10) NOT NULL COMMENT '专营店编码',
  `EMP_CODE` varchar(10) NOT NULL COMMENT '职员编码',
  `EMP_NAME` varchar(100) NOT NULL COMMENT '职员姓名',
  `EMP_STATUS` varchar(2) DEFAULT NULL COMMENT '员工状态',
  `EMP_TYPE` varchar(36) DEFAULT NULL COMMENT '员工类型',
  `SALES_CAR_BRAND_ID` int(10) DEFAULT NULL COMMENT '所售品牌（T_BASE_CAR_BRAND.ID）',
  `ICON` varchar(255) DEFAULT NULL COMMENT '头像',
  `WECHAT_QRCODE` varchar(255) DEFAULT NULL COMMENT '微信二维码图片',
  `PROVINCE_ID` varchar(36) DEFAULT NULL COMMENT '省份ID',
  `CITY_ID` varchar(36) DEFAULT NULL COMMENT '城市ID',
  `COUNTY_ID` varchar(36) DEFAULT NULL COMMENT '区县ID',
  `JOB` varchar(50) DEFAULT NULL COMMENT '职位描述',
  `SERVICE_AREA` varchar(50) DEFAULT NULL COMMENT '服务范围（预约试驾，客户跟进，客户分析，金融协助，客户统计，业务管理）',
  `BIRTH_DATE` datetime DEFAULT NULL COMMENT '出生日期',
  `WORK_TEL` varchar(50) DEFAULT NULL COMMENT '工作电话',
  `MOBILE` varchar(200) DEFAULT NULL COMMENT '手机号码',
  `GENDER_CODE` varchar(10) DEFAULT NULL COMMENT '性别编码',
  `DEGREE_CODE` varchar(10) DEFAULT NULL COMMENT '学历编码',
  `PERSON_ADDR` varchar(250) DEFAULT NULL COMMENT '个人通信地址',
  `ZIP` varchar(100) DEFAULT NULL COMMENT '邮编',
  `EMAIL` varchar(100) DEFAULT NULL COMMENT '邮箱',
  `FAX` varchar(20) DEFAULT NULL COMMENT '传真号',
  `NATIONALITY_CODE` varchar(10) DEFAULT NULL COMMENT '国籍编码',
  `MARRIAGED_CODE` varchar(10) DEFAULT NULL COMMENT '婚姻状况编码',
  `NATIVE_PLACE` varchar(50) DEFAULT NULL COMMENT '籍贯',
  `SCHOOL` varchar(100) DEFAULT NULL COMMENT '毕业院校',
  `DEGREEPRO` varchar(100) DEFAULT NULL COMMENT '专业',
  `SKILL_SPECIAL` varchar(1000) DEFAULT NULL COMMENT '技能特长',
  `FAMILY_PHONE` varchar(20) DEFAULT NULL COMMENT '家庭电话',
  `SECOND_MAN` varchar(100) DEFAULT NULL COMMENT '紧急联络人',
  `SECOND_MAN_TEL` varchar(50) DEFAULT NULL COMMENT '紧急联络人电话',
  `DRIVER_DATE` datetime DEFAULT NULL COMMENT '领取驾照日期',
  `NATION_CODE` varchar(10) DEFAULT NULL COMMENT '民族编码',
  `BUSINESS_DATE` datetime DEFAULT NULL COMMENT '汽车行业从业时间',
  `EMPLOY_DATE` datetime DEFAULT NULL COMMENT '入职日期',
  `IS_DRIVER` varchar(2) DEFAULT NULL COMMENT '是否有驾照',
  `EMPLOY_TYPE` varchar(100) DEFAULT NULL COMMENT '招聘方式',
  `POLITICS_CODE` varchar(10) DEFAULT NULL COMMENT '政治面貌编码',
  `CRED_TYPE_CODE` varchar(10) DEFAULT NULL COMMENT '证件类型编码',
  `CRED_NO` varchar(50) DEFAULT NULL COMMENT '证件号',
  `EMP_CLASS` varchar(100) DEFAULT NULL COMMENT '职称',
  `EMP_PIC` varchar(200) DEFAULT NULL COMMENT '职员照片',
  `SELF_ESTIMATE` varchar(1000) DEFAULT NULL COMMENT '自我评价',
  `DLR_ID` varchar(36) NOT NULL COMMENT '专营店ID',
  `STATION_ID` varchar(36) DEFAULT NULL COMMENT '第一岗位',
  `HEAD_MANAGER` varchar(36) DEFAULT NULL COMMENT '直属上司ID',
  `SEC_DLR_ID` varchar(36) DEFAULT NULL COMMENT '二级网点ID 如属于一级店则为空',
  `SEC_DLR_CODE` varchar(10) DEFAULT NULL COMMENT '二级网点编码 如属于一级店则为空',
  `DEPT_ID` varchar(36) DEFAULT NULL COMMENT '部门ID',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX1_T_E4S_DB_ORG_EMPLOYEE` (`DLR_CODE`),
  KEY `IDX2_T_E4S_DB_ORG_EMPLOYEE` (`EMP_CODE`),
  KEY `IDX3_T_E4S_DB_ORG_EMPLOYEE` (`EMP_NAME`)
) ENGINE=InnoDB AUTO_INCREMENT=279336 DEFAULT CHARSET=utf8 COMMENT='基础数据，员工信息。'



t_base_financial_condition_rel
CREATE TABLE `t_base_financial_condition_rel` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `CONDITION_NAME` varchar(128) DEFAULT NULL COMMENT '申请条件名称',
  `CONDITION_ID` int(10) NOT NULL COMMENT '申请条件id(关联值列表中的申请条件)',
  `FINACIAL_PRODUCT_ID` int(10) NOT NULL COMMENT '金融产品ID',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=273 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品关联的申请条件信息。'



t_base_financial_corp
CREATE TABLE `t_base_financial_corp` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `CORP_NAME` varchar(36) DEFAULT NULL COMMENT '金融机构名称',
  `LOAN_HOUR` int(11) DEFAULT NULL COMMENT '放款时间（小时）',
  `IS_ONLINE_AUDIT` varchar(2) DEFAULT NULL COMMENT '在线审贷',
  `CORP_LOGO` varchar(200) DEFAULT NULL COMMENT '金融机构logo图',
  `SUCCESS_NUM` int(11) DEFAULT NULL COMMENT '申请成功人数',
  `ONLINE_AUDIT_LINK` varchar(200) DEFAULT NULL COMMENT '在线审贷URL',
  `ORDER_NO` int(11) DEFAULT '0' COMMENT '排序',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=258 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融组织机构信息。'



t_base_financial_dlr_rel
CREATE TABLE `t_base_financial_dlr_rel` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `FINANCIAL_PRODUCT_ID` int(10) NOT NULL COMMENT '金融产品ID',
  `DLR_CODE` varchar(36) DEFAULT NULL COMMENT '经销商编码',
  `TYPE_ID` bigint(10) NOT NULL COMMENT '类型',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3474 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品关联的经销商信息。'



t_base_financial_feature_rel
CREATE TABLE `t_base_financial_feature_rel` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `FEATURE_NAME` varchar(128) DEFAULT NULL COMMENT '产品特点',
  `FEATURE_ID` int(10) NOT NULL COMMENT '产品特点id(关联值列表中的产品特点)',
  `FINACIAL_PRODUCT_ID` int(10) NOT NULL COMMENT '金融产品ID',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=222 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品关联的特点信息。'



t_base_financial_first_pay_percent_rel
CREATE TABLE `t_base_financial_first_pay_percent_rel` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `FIRST_PAY_PERCENT` varchar(50) DEFAULT NULL COMMENT '首付比例',
  `FINACIAL_PRODUCT_ID` int(10) NOT NULL COMMENT '金融产品ID',
  `IS_ENABLE` varchar(2) CHARACTER SET gbk NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=348 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品关联的还款方式信息。'



t_base_financial_material_rel
CREATE TABLE `t_base_financial_material_rel` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `MATERIAL_NAME` varchar(128) DEFAULT NULL COMMENT '申请材料',
  `MATERIAL_ID` int(10) NOT NULL COMMENT '申请材料ID(关联值列表的申请材料)',
  `FINACIAL_PRODUCT_ID` int(10) NOT NULL COMMENT '金融产品ID',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=237 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品关联的申请材料信息。'



t_base_financial_pro_sku
CREATE TABLE `t_base_financial_pro_sku` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `SKU_NAME` varchar(50) DEFAULT NULL COMMENT 'SKU名称',
  `SKU_ITEM` int(10) DEFAULT NULL COMMENT 'SKU期数',
  `SKU_RATE` varchar(36) DEFAULT NULL COMMENT 'SKU年利率',
  `FINACIAL_PRODUCT_ID` int(10) NOT NULL COMMENT '金融产品ID',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=231 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品关联的期数信息。'



t_base_financial_product
CREATE TABLE `t_base_financial_product` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `FINANCIAL_PRODUCT_NAME` varchar(50) DEFAULT NULL COMMENT '金融产品名称',
  `FINANCIAL_CORP_ID` int(10) DEFAULT NULL COMMENT '金融机构ID',
  `PASS_PERCENT` int(11) DEFAULT NULL COMMENT '通过率',
  `EFFECT_START_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '上架开始时间',
  `EFFECT_END_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '上架结束时间',
  `REPAYMENT_TYPE` varchar(36) DEFAULT NULL COMMENT '还款方式',
  `COMPUTING_FORMULA` varchar(200) DEFAULT NULL COMMENT '计算公式描述',
  `IS_FINAL_PAYMENT` tinyint(1) DEFAULT NULL COMMENT '是否尾款产品',
  `FINAL_PAYMENT_SCALE` varchar(10) DEFAULT NULL COMMENT '尾款分期比例',
  `CONTAINS_INTEREST` tinyint(1) DEFAULT NULL COMMENT '月供是否包含利息',
  `BRAND_IDS` varchar(255) DEFAULT NULL COMMENT '金融产品关联的品牌ID集合，逗号分隔（T_BASE_CAR_BRAND.ID）',
  `REGION_IDS` varchar(1000) DEFAULT NULL COMMENT '金融产品关联的区域ID集合，逗号分隔（T_BASE_REGION.ID）',
  `PROVINCE_IDS` varchar(1000) DEFAULT NULL COMMENT '金融产品关联的省份ID集合，逗号分隔（T_BASE_PROVINCE.PROVINCE_ID）',
  `DEALER_TYPE` varchar(50) DEFAULT NULL COMMENT '金融产品关联的专营店类型（1-所有专营店，2-堡垒店）。此字段只标识专营店类型，金融产品具体关联的专营店记录在T_BASE_FINANCIAL_DLR_REL',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品信息。'



t_base_financial_series_rel
CREATE TABLE `t_base_financial_series_rel` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `FINANCIAL_PRODUCT_ID` int(10) NOT NULL COMMENT '金融产品ID',
  `CAR_SERIES_ID` varchar(36) NOT NULL COMMENT '车系ID',
  `TYPE_ID` bigint(10) NOT NULL COMMENT '类型',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=852 DEFAULT CHARSET=utf8 COMMENT='基础数据，金融产品关联的车系信息'



t_base_large_car_type
CREATE TABLE `t_base_large_car_type` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `LARGE_CAR_TYPE_ID` varchar(36) NOT NULL COMMENT '车型ID',
  `BASE_SERIES_ID` varchar(36) DEFAULT NULL COMMENT '基准车系ID  T_MDM_VE_BASE_SERIES BASE_SERIES_ID',
  `LARGE_CAR_TYPE_CODE` varchar(50) NOT NULL COMMENT '车型大类编码',
  `LARGE_CAR_TYPE_CN` varchar(100) DEFAULT NULL COMMENT '车型大类中文名称',
  `LARGE_CAR_TYPE_EN` varchar(100) DEFAULT NULL COMMENT '车型大类英文名称',
  `CAR_SERIES_CODE` varchar(50) DEFAULT NULL COMMENT '车系编码',
  `CAR_BRAND_CODE` varchar(50) NOT NULL COMMENT '车辆品牌编码',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX1_T_E4S_DB_LARGE_CAR_TYPE` (`BASE_SERIES_ID`),
  KEY `IDX2_T_E4S_DB_LARGE_CAR_TYPE` (`LARGE_CAR_TYPE_CODE`),
  KEY `IDX3_T_E4S_DB_LARGE_CAR_TYPE` (`CAR_SERIES_CODE`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的车型大类信息。'



t_base_media_activity
CREATE TABLE `t_base_media_activity` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `ACTIVITY_TITLE` varchar(255) NOT NULL COMMENT '活动标题',
  `PAGE_URL` varchar(255) DEFAULT NULL COMMENT '活动页面链接',
  `ACTIVITY_CONTENT` varchar(5000) DEFAULT NULL COMMENT '活动内容、活动描述',
  `ACTIVITY_BEGIN_DATE` datetime DEFAULT NULL COMMENT '活动开始时间',
  `ACTIVITY_END_DATE` datetime DEFAULT NULL COMMENT '活动结束时间',
  `ACTIVITY_TYPE` varchar(255) DEFAULT NULL COMMENT '活动类型（取值参考字典表，dictGroupName=activityType）',
  `DEALER_ID` int(10) NOT NULL COMMENT '专营店ID（T_BASE_DEALER.ID）',
  `CAR_TYPE_ID` int(10) DEFAULT NULL COMMENT '车型编码（T_BASE_CAR_TYPE.ID）',
  `CAR_SERIES_ID` int(10) DEFAULT NULL COMMENT '车系ID（T_BASE_CAR_SERIES.ID）',
  `CAR_BRAND_ID` int(10) DEFAULT NULL COMMENT '品牌ID（T_BASE_CAR_BRAND.ID）',
  `BIG_AREA_ID` varchar(36) DEFAULT NULL COMMENT '大区ID（T_BASE_BIGAREA.BIG_AREA_ID）',
  `SMALL_AREA_ID` varchar(36) DEFAULT NULL COMMENT '小区ID（T_BASE_SMALLAREA.SMALL_AREA_ID）',
  `PROVINCE_ID` varchar(36) DEFAULT NULL COMMENT '省份ID（T_BASE_PROVINCE.PROVINCE_ID）',
  `CITY_ID` varchar(36) DEFAULT NULL COMMENT '城市ID（T_BASE_CITY.CITY_ID）',
  `COUNTY_ID` varchar(36) DEFAULT NULL COMMENT '区县ID（T_BASE_COUNTY.COUNTY_ID）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `MODIFIER` varchar(50) NOT NULL COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `idx_t_e4s_bu_offer_price1` (`DEALER_ID`,`CAR_SERIES_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COMMENT='基础数据，从外部媒体（汽车之家、天猫）抓取的活动信息。'



t_base_media_activity_type
CREATE TABLE `t_base_media_activity_type` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT ' 物理主键',
  `ACTIVITY_TYPE` varchar(50) DEFAULT NULL COMMENT '活动类型值',
  `REMARK` varchar(255) DEFAULT NULL COMMENT '活动类型备注',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(255) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(255) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='基础数据，活动类型信息表。'



t_base_member
CREATE TABLE `t_base_member` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '会员编号',
  `ACCOUNT_ID` int(10) unsigned DEFAULT NULL COMMENT '账号ID，关联权限表',
  `MEMBER_CATEGORY` tinyint(4) DEFAULT NULL COMMENT '会员类型，普通会员/车主会员',
  `MEMBER_CODE` varchar(128) DEFAULT NULL COMMENT '会员唯一编号',
  `USERNAME` varchar(255) DEFAULT NULL COMMENT '登陆用户名',
  `PASSWORD` varchar(255) DEFAULT NULL COMMENT '登陆密码',
  `REAL_NAME` varchar(128) DEFAULT NULL COMMENT '真实姓名',
  `NICK_NAME` varchar(128) DEFAULT NULL COMMENT '昵称',
  `GENDER` tinyint(4) DEFAULT NULL COMMENT '性别',
  `AGE` int(11) DEFAULT NULL COMMENT '年龄',
  `BIRTHDAY` date DEFAULT NULL COMMENT '生日',
  `ID_CARD` varchar(64) DEFAULT NULL COMMENT '身份证',
  `MOBILE` varchar(32) DEFAULT NULL COMMENT '手机号',
  `EMAIL` varchar(255) DEFAULT NULL COMMENT 'email',
  `SOURCE` varchar(255) DEFAULT NULL COMMENT '来源',
  `TAG` varchar(255) DEFAULT NULL,
  `REG_DATE` datetime DEFAULT NULL COMMENT '注册时间',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `INDEX_MEMBER_CODE` (`MEMBER_CODE`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8 COMMENT='会员'



t_base_member_contact
CREATE TABLE `t_base_member_contact` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `MEMBER_ID` int(11) unsigned NOT NULL COMMENT '会员编号',
  `SHOWNAME` varchar(255) DEFAULT NULL COMMENT '姓名',
  `TELEPHONE` varchar(255) DEFAULT NULL COMMENT '电话号码',
  `MOBILE` varchar(128) DEFAULT NULL COMMENT '手机',
  `EMAIL` varchar(128) DEFAULT NULL COMMENT '电邮',
  `ADDRESS` varchar(255) DEFAULT NULL COMMENT '地址',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_BASE_MEMBER_CONTACT_T_BASE_MEMBER_1` (`MEMBER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='会员联系信息'



t_base_member_ext
CREATE TABLE `t_base_member_ext` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `MEMBER_ID` int(11) unsigned NOT NULL COMMENT '会员编号',
  `CUSTOMER_APPLY_STATUS` tinyint(4) DEFAULT NULL COMMENT '线索状态，是否下发，0未下发，1已下发',
  `APPLY_STATIC` int(11) DEFAULT NULL COMMENT '留资次数，由后台定时统计',
  `COMPANY` varchar(255) DEFAULT NULL COMMENT '所在企业',
  `TITLE` varchar(255) DEFAULT NULL COMMENT '职位',
  `EARN` varchar(255) DEFAULT NULL COMMENT '月收入',
  `CREDIT` varchar(255) DEFAULT NULL COMMENT '信用',
  `SOCIAL_INSURANCE` varchar(255) DEFAULT NULL COMMENT '社保',
  `CPF` varchar(255) DEFAULT NULL COMMENT '公积金',
  `LIVING_STATUS` varchar(255) DEFAULT NULL COMMENT '住房情况',
  `COUNTY_ID` int(10) unsigned DEFAULT NULL COMMENT '居住区县',
  `CITY_ID` int(10) unsigned DEFAULT NULL COMMENT '居住城市',
  `PROVINCE_ID` int(10) unsigned DEFAULT NULL COMMENT '居住省份',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_BASE_MEMBER_CONTACT_T_BASE_MEMBER_1` (`MEMBER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8 COMMENT='会员信息扩展'



t_base_member_favorite
CREATE TABLE `t_base_member_favorite` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '会员编号',
  `MEMBER_ID` int(10) unsigned DEFAULT NULL COMMENT '会员ID，关联会员表',
  `CAR_SERIES_ID` int(10) unsigned DEFAULT NULL COMMENT '车系ID，关联车系表',
  `CAR_MODEL_ID` int(10) unsigned DEFAULT NULL COMMENT '车型ID，关联车型表',
  `DEALER_ID` int(10) unsigned DEFAULT NULL COMMENT '经销商ID，关联经销商表',
  `DEALER_CODE` varchar(64) DEFAULT NULL COMMENT '经销商编码',
  `PRODUCT_ID` int(10) unsigned DEFAULT NULL COMMENT '产品ID，关联产品表',
  `COMMODITY_ID` int(10) unsigned DEFAULT NULL COMMENT 'SKU ID,关联sku表',
  `PAYMENT_ID` int(10) unsigned DEFAULT NULL COMMENT '支付方式id，关联数据字典表',
  `BUY_PERIOD` int(11) DEFAULT NULL COMMENT '计划购买时间ID，关联数据字典表',
  `NEED_EXPERIENCE` tinyint(4) DEFAULT NULL COMMENT '是否需要体验，0否，1是，比如试乘试驾',
  `PSYCHOLOGICAL_PRICE` int(11) DEFAULT NULL COMMENT '心理价位，单位分',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='会员关注的产品，包括商品和车型车系'



t_base_member_status
CREATE TABLE `t_base_member_status` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `MEMBER_ID` int(10) unsigned DEFAULT NULL COMMENT '会员ID，外键关联会员表',
  `MEMBER_STATUS` tinyint(4) DEFAULT NULL COMMENT '会员状态,0冻结，1激活',
  `ACTIVE_BEGIN_DATE` datetime DEFAULT NULL COMMENT '开始激活时间，为空时，代表永久有效',
  `ACTIVE_END_DATE` datetime DEFAULT NULL COMMENT '激活结束时间,为空时，代表永久有效',
  `REMARK` varchar(500) DEFAULT NULL COMMENT '备注',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8 COMMENT='会员状态表'



t_base_middle_car_type
CREATE TABLE `t_base_middle_car_type` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `STD_CAR_ID` varchar(36) NOT NULL COMMENT '车型中类ID',
  `LARGE_CAR_TYPE_ID` varchar(36) NOT NULL COMMENT '车型大类ID  T_MDM_LARGE_CAR_TYPE LARGE_CAR_TYPE_ID',
  `STD_CAR_CODE` varchar(50) NOT NULL COMMENT '车型中类编码',
  `STD_CAR_CN` varchar(100) DEFAULT NULL COMMENT '车型中类英文名称',
  `STD_CAR_EN` varchar(100) NOT NULL COMMENT '车型中类中文名称',
  `STD_CAR_TYPE_DESC` varchar(200) DEFAULT NULL COMMENT '车型中类描述',
  `SPECIAL_FLAG` varchar(50) DEFAULT NULL COMMENT '排放标准',
  `OLD_CARTYPE_ID` decimal(20,0) DEFAULT NULL COMMENT '旧车型ID （E3SV车型ID）',
  `CAR_BRAND_CODE` varchar(50) NOT NULL COMMENT '车辆品牌编码',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX1_T_E4S_DB_MIDDLE_CAR_TY` (`LARGE_CAR_TYPE_ID`),
  KEY `IDX2_T_E4S_DB_MIDDLE_CAR_TYPE` (`STD_CAR_CODE`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的车型中类信息。'



t_base_offer_price
CREATE TABLE `t_base_offer_price` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `DEALER_ID` int(10) DEFAULT NULL COMMENT '专营店ID（T_BASE_DEALER.ID）',
  `CAR_TYPE_ID` int(10) DEFAULT NULL COMMENT '车型编码（T_BASE_CAR_TYPE.ID）',
  `CAR_SERIES_ID` int(10) DEFAULT NULL COMMENT '车系ID（T_BASE_CAR_SERIES.ID）',
  `CAR_BRAND_ID` int(10) DEFAULT NULL COMMENT '品牌ID（T_BASE_CAR_BRAND.ID）',
  `PUBLIC_OFFER_PRICE` int(11) DEFAULT NULL COMMENT '公开报价',
  `PURCHASE_TAX` varchar(32) DEFAULT NULL COMMENT '购置税',
  `COMERCIAL_INSURANCE` varchar(32) DEFAULT NULL COMMENT '商业险',
  `COMPULSORY_INSURANCE` varchar(32) DEFAULT NULL COMMENT '交强险',
  `INSURANCE_OFF` varchar(32) DEFAULT NULL COMMENT '保险优惠',
  `TRAVEL_TAX` varchar(32) DEFAULT NULL COMMENT '车船税',
  `LISENCE_COST` varchar(32) DEFAULT NULL COMMENT '上牌费',
  `OTHER_COST` varchar(32) DEFAULT NULL COMMENT '其他费用',
  `BIG_AREA_ID` varchar(36) DEFAULT NULL COMMENT '大区ID（T_BASE_BIGAREA.BIG_AREA_ID）',
  `SMALL_AREA_ID` varchar(36) DEFAULT NULL COMMENT '小区ID（T_BASE_SMALLAREA.SMALL_AREA_ID）',
  `PROVINCE_ID` varchar(36) DEFAULT NULL COMMENT '省份ID（T_BASE_PROVINCE.PROVINCE_ID）',
  `CITY_ID` varchar(36) DEFAULT NULL COMMENT '城市ID（T_BASE_CITY.CITY_ID）',
  `COUNTY_ID` varchar(36) DEFAULT NULL COMMENT '区县ID（T_BASE_COUNTY.COUNTY_ID）',
  `DISCOUNT` int(11) DEFAULT NULL COMMENT '优惠（指导价-报价）（T_BASE_CAR_TYPE.GUIDE_PRICE-T_BASE_OFFER_PRICE.PUBLIC_OFFER_PRICE）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `E4S_CAR_TYPE_ID` varchar(36) DEFAULT NULL,
  `E4S_DLR_CODE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `idx_t_e4s_bu_offer_price1` (`DEALER_ID`,`CAR_SERIES_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=259197 DEFAULT CHARSET=utf8 COMMENT='基础数据，车型报价信息。'



t_base_praise_score
CREATE TABLE `t_base_praise_score` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '属性编号',
  `PRAISE_ID` int(11) unsigned NOT NULL COMMENT '评价ID',
  `SCORE_KEY` varchar(255) DEFAULT NULL COMMENT '属性键',
  `SCORE_VALUE` varchar(255) DEFAULT NULL COMMENT '属性值',
  `SCORE_TYPE` int(11) DEFAULT NULL COMMENT '评分类型',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_评分项_通用口碑记录_1` (`PRAISE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='关键属性评分'



t_base_product
CREATE TABLE `t_base_product` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '产品编号',
  `BRAND_ID` int(11) unsigned DEFAULT NULL COMMENT '品牌编号',
  `CATEGORY_ID` int(11) unsigned DEFAULT NULL COMMENT '类别编号',
  `PRODUCT_STAT_ID` int(11) DEFAULT NULL COMMENT '商品的统计信息，如访问人次，购买人次等等，暂时没有这个表.只是保留数据结构.',
  `DEFAULT_PRODUCT_SKU_ID` int(11) DEFAULT NULL COMMENT '默认的skuID',
  `DEALER_ID` int(11) DEFAULT NULL COMMENT '经销商id，经销商发布的商品',
  `DEALER_CODE` varchar(128) DEFAULT NULL COMMENT '经销商编码',
  `CAR_MODEL_ID` int(11) DEFAULT NULL COMMENT '关联的车型实体ID',
  `PRODUCT_NAME` varchar(255) DEFAULT NULL COMMENT '品名',
  `PRODUCT_CODE` varchar(32) NOT NULL COMMENT '商品编码',
  `PRICE` decimal(12,2) DEFAULT NULL COMMENT '价格或者特价，冗余值，用于价格查询',
  `MIN_ORDER_QUANTITY` int(11) DEFAULT NULL COMMENT '最少定购量 ',
  `MAX_ORDER_QUANTITY` int(11) DEFAULT NULL COMMENT '最大订购量',
  `IMAGE_URL` varchar(255) DEFAULT NULL COMMENT '主图路径',
  `META_TITLE` varchar(128) DEFAULT NULL COMMENT 'meta标题',
  `META_KEYWORD` varchar(256) DEFAULT NULL COMMENT 'meta关键词',
  `META_DESCRIPTION` varchar(256) DEFAULT NULL COMMENT 'meta描述',
  `TEMPLATE_PATH` varchar(128) DEFAULT NULL COMMENT '模板路径',
  `SHELVE_TIME` datetime DEFAULT NULL COMMENT '上架时间，如果商品是上架的，则上架时间为非空，否则上架时间为空',
  `OFF_SHELVE_TIME` datetime DEFAULT NULL COMMENT '下架时间，如果商品是下架的，则下架时间为非空，否则下架时间为空',
  `REDIRECT_URL` varchar(255) DEFAULT NULL COMMENT '跳转url',
  `NEED_SHIPMENT` tinyint(4) DEFAULT NULL COMMENT '是否需要物流，0否，1是',
  `TAGS` varchar(2000) DEFAULT NULL COMMENT '标签，对应数据字典',
  `PROMOTION_TAGS` varchar(1000) DEFAULT NULL COMMENT '促销标签，对应数据字典',
  `DESCRIPTION` varchar(255) DEFAULT NULL COMMENT '描述',
  `SORT_ORDER` int(11) DEFAULT NULL COMMENT '排序',
  `SKU_OPTIONS` varchar(500) DEFAULT NULL COMMENT 'sku可选项，冗余值，用于显示商品详情页的sku选项。格式为 [PROPERTYID1]:[PROPERTYVALUEID1,PROPERTYVALUEID2,PROPERTYVALUEID3,......];[PROPERTYID2]:[PROPERTYVALUEID1,PROPERTYVALUEID2,PROPERTYVALUEID3,......];  例如 1:2,3,4;2:4,5,6;',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_产品_分类表_1` (`CATEGORY_ID`),
  KEY `FK_产品_品牌_1` (`BRAND_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=168 DEFAULT CHARSET=utf8 COMMENT='基础产品/商品'



t_base_product_ext
CREATE TABLE `t_base_product_ext` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '商品编号',
  `PRODUCT_ID` int(10) unsigned DEFAULT NULL COMMENT '产品ID',
  `DESCRIPTION` longtext COMMENT 'PC端描述',
  `M_DESCRIPTION` longtext COMMENT '移动端描述',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='产品扩展'



t_base_product_image
CREATE TABLE `t_base_product_image` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '图片编号',
  `PRODUCT_ID` int(11) unsigned DEFAULT NULL COMMENT '对应产品编号',
  `PIC_TYPE` tinyint(4) DEFAULT NULL COMMENT '产品图片类型，1商品主图',
  `CAR_SERIES_ID` int(10) unsigned DEFAULT NULL COMMENT '车系ID',
  `CAR_MODEL_ID` int(11) unsigned DEFAULT NULL COMMENT '车型ID',
  `CAR_COLOR_ID` int(10) unsigned DEFAULT NULL COMMENT '颜色ID',
  `PIC_SIZE` varchar(32) DEFAULT NULL COMMENT '图片大小编码',
  `POSITION` int(11) DEFAULT NULL COMMENT '汽车什么具体部位',
  `LOCALFILEPATH` varchar(255) DEFAULT NULL COMMENT '文件路径，多个',
  `CDNPATH` varchar(255) DEFAULT NULL COMMENT 'CDN路径',
  `TITLE` varchar(255) DEFAULT NULL COMMENT '图片标题',
  `KEYWORDS` varchar(255) DEFAULT NULL COMMENT '关键字',
  `DESCRIPTION` varchar(255) DEFAULT NULL COMMENT '描述',
  `VISIT` int(11) DEFAULT NULL COMMENT '浏览数',
  `IMAGE_ORDER` int(11) DEFAULT NULL COMMENT '顺序',
  `SHOW_TARGET` varchar(255) DEFAULT NULL COMMENT '需要显示的平台ID/CODE，参考数据字典表',
  `PUB_DATE` varchar(255) DEFAULT NULL COMMENT '正式发布时间',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_图库_产品_1` (`PRODUCT_ID`),
  KEY `fk_t_base_product_image_t_base_carmodel_1` (`CAR_MODEL_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=678 DEFAULT CHARSET=utf8 COMMENT='产品/商品图库'



t_base_product_property
CREATE TABLE `t_base_product_property` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '属性编号',
  `PROPERTY_GROUP_ID` int(11) unsigned DEFAULT NULL COMMENT '组id',
  `PROPERTY_NAME` varchar(255) DEFAULT NULL COMMENT '属性键',
  `PROPERTY_CODE` varchar(255) DEFAULT NULL COMMENT '属性code',
  `PROPERTY_DEFAULT_VALUE` varchar(255) DEFAULT NULL COMMENT '属性默认值',
  `PROPERTY_TYPE` smallint(11) DEFAULT NULL COMMENT '表单类型: 1文本框；2日期；3是/否；4复选；5下拉框；',
  `PROPERTY_DATA_TYPE` smallint(6) DEFAULT NULL COMMENT '表单数据类型： 字符型；浮点型；整型；布尔型；',
  `PROPERTY_BUSINESS_TYPE` tinyint(4) DEFAULT NULL COMMENT '业务类型，比如车型颜色类，车型排量类等等',
  `PROPERTY_OPTIONS` varchar(1000) DEFAULT NULL COMMENT '表单选项，JSON',
  `PROPERTY_EVENT` varchar(1000) DEFAULT NULL COMMENT '属性触发的事件',
  `PROPERTY_EXT_VALUE` varchar(1000) DEFAULT NULL COMMENT '扩展值，json:\r\n{\r\n    "attribute1": "value1", \r\n    "attribute2": "value2", \r\n    "attribute3": "value3", \r\n    "attribute4": "value4",\r\n......\r\n}',
  `IS_MANDATORY` tinyint(4) DEFAULT NULL COMMENT '是否必填',
  `IS_SKU` tinyint(4) DEFAULT NULL COMMENT '是否sku属性',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `SORT_ORDER` int(11) DEFAULT NULL COMMENT '排序',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_BASE_PRODUCT_PROPERTY_T_BASE_PRODUCT_PROPERTY_GROUP_1` (`PROPERTY_GROUP_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=216 DEFAULT CHARSET=utf8 COMMENT='产品/商品属性'



t_base_product_property_group
CREATE TABLE `t_base_product_property_group` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `GROUP_NAME` varchar(255) DEFAULT NULL COMMENT '组名',
  `BUSINESS_TYPE` tinyint(4) DEFAULT NULL COMMENT '业务类型，比如车型颜色类，车型排量类等等',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `SORT_ORDER` int(11) DEFAULT NULL COMMENT '排序',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8 COMMENT='产品/商品属性组'



t_base_product_video
CREATE TABLE `t_base_product_video` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '视频编号',
  `PRODUCT_ID` int(11) unsigned DEFAULT NULL COMMENT '产品编号',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `TITLE` varchar(255) DEFAULT NULL COMMENT '标题',
  `KEYWORDS` varchar(255) DEFAULT NULL COMMENT '关键字',
  `DESCRIPTION` varchar(255) DEFAULT NULL COMMENT '描述',
  `VIDEOS` varchar(255) DEFAULT NULL COMMENT '视频文件路径，本地或线上，支持多个',
  `SOURCE` varchar(255) DEFAULT NULL COMMENT '来源',
  `THUMB` varchar(255) DEFAULT NULL COMMENT '视频缩略图',
  `CONTENT` varchar(255) DEFAULT NULL COMMENT '描述内容',
  `PUB_DATE` datetime DEFAULT NULL COMMENT '发布日期',
  `VIDEO_COUNT` int(11) DEFAULT NULL COMMENT '浏览数',
  `CATEGORY_ID` int(11) unsigned DEFAULT NULL,
  `EDIT_TIME` datetime DEFAULT NULL COMMENT '修改时间',
  `SORT_ORDER` int(11) DEFAULT '0' COMMENT '排序',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_视频_产品_1` (`PRODUCT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='产品/商品视频'



t_base_property_group_item
CREATE TABLE `t_base_property_group_item` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `PROPERTY_GROUP_ID` int(11) unsigned DEFAULT NULL COMMENT '分组ID',
  `PROPERTY_ID` int(11) unsigned DEFAULT NULL COMMENT '属性ID',
  `PRODUCT_ID` int(11) unsigned DEFAULT NULL COMMENT '产品id',
  `CAR_MODEL_ID` int(11) unsigned DEFAULT NULL COMMENT '车型ID',
  `CATEGORY_ID` int(11) unsigned DEFAULT NULL COMMENT '商品分类ID',
  `ITEM_TYPE` tinyint(4) DEFAULT NULL COMMENT '属性类型，0其他属性，1可被筛选的基础属性',
  `SORT_ORDER` int(11) DEFAULT NULL COMMENT '排序',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_PRODUCT_PROPERTY_T_COMMODITY_1` (`CATEGORY_ID`),
  KEY `FK_T_PERPERTY_GROUP_ID` (`PROPERTY_GROUP_ID`),
  KEY `FK_T_PROPERTY` (`PROPERTY_ID`),
  KEY `FK_T_PRODUCT_ID` (`PRODUCT_ID`),
  KEY `fk_t_base_property_group_item_t_base_carmodel_1` (`CAR_MODEL_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=687 DEFAULT CHARSET=utf8 COMMENT='商品SKU，产品属性'



t_base_property_value
CREATE TABLE `t_base_property_value` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `PRODUCT_ID` int(10) unsigned DEFAULT NULL COMMENT '产品ID',
  `PROPERTY_ID` int(11) unsigned DEFAULT NULL COMMENT '属性ID',
  `PROPERTY_GROUP_ITEM_ID` int(11) unsigned DEFAULT NULL COMMENT '所属表单',
  `SHORT_TEXT` varchar(255) DEFAULT NULL COMMENT '短文本',
  `LONG_TEXT` text COMMENT '长文本',
  `INT_VALUE` int(11) DEFAULT NULL COMMENT '整型',
  `DECIMAL_VALUE` decimal(12,2) DEFAULT NULL COMMENT '浮点型',
  `BOOLEAN_VALUE` smallint(6) DEFAULT NULL COMMENT '布尔型',
  `DATE_VALUE` datetime DEFAULT NULL COMMENT '日期型',
  `URL_VALUE` varchar(255) DEFAULT NULL COMMENT 'URL',
  `ICON_VALUE` varchar(255) DEFAULT NULL COMMENT 'ICON',
  `COLOR_VALUE` varchar(255) DEFAULT NULL COMMENT '颜色值，如#000000',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `fk_t_base_property_value_t_base_product_property_1` (`PROPERTY_ID`),
  KEY `fk_t_base_property_value_t_base_property_group_item_1` (`PROPERTY_GROUP_ITEM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='产品/商品属性值'



t_base_province
CREATE TABLE `t_base_province` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `PROVINCE_ID` varchar(36) NOT NULL DEFAULT '0' COMMENT '省份ID',
  `PROVINCE_CODE` varchar(50) NOT NULL COMMENT '省份编码',
  `PROVINCE_NAME` varchar(100) NOT NULL COMMENT '省份名称',
  `PROVINCE_ALIAS` varchar(100) DEFAULT NULL COMMENT '省份别名',
  `PROVINCE_INITIAL` varchar(10) DEFAULT NULL COMMENT '省份首字母',
  `REGION_ID` int(10) DEFAULT NULL COMMENT '区域ID(本平台定义的行政区域T_BASE_REGION)',
  `REGIONALISM_CODE` varchar(36) DEFAULT NULL COMMENT '国家统计局行政区划代码',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(32) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
  `MODIFIER` varchar(32) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改日期',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10002 DEFAULT CHARSET=utf8 COMMENT='基础信息，省份信息表。'



t_base_region
CREATE TABLE `t_base_region` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '区域ID',
  `REGION_NAME` varchar(100) NOT NULL COMMENT '区域名称',
  `REGION_ALIAS` varchar(100) DEFAULT NULL COMMENT '区域别名',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序字段',
  `IS_SHOW` varchar(2) DEFAULT '1' COMMENT '是否显示（0-否，1-是）',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(255) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(255) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8 COMMENT='基础数据，行政区域信息。（本平台划分的行政区域，与外部系统同步过来的销售区域不是同一套）'



t_base_small_car_type
CREATE TABLE `t_base_small_car_type` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `SMALL_CAR_TYPE_ID` varchar(36) NOT NULL COMMENT '车型小类ID',
  `STD_CAR_ID` varchar(36) NOT NULL COMMENT '车型中类ID  T_MDM_MIDDLE_CAR_TYPE STD_CAR_ID',
  `SMALL_CAR_TYPE_CODE` varchar(50) NOT NULL COMMENT '车型小类编码',
  `SMALL_CAR_TYPE_CN` varchar(100) DEFAULT NULL COMMENT '车型小类中文名称',
  `SMALL_CAR_TYPE_EN` varchar(100) DEFAULT NULL COMMENT '车型小类英文名称',
  `CAR_BRAND_CODE` varchar(50) DEFAULT NULL COMMENT '车辆品牌编码',
  `IS_ENABLE` varchar(2) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '最后更新人员',
  `UPDATED_DATE` datetime NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  KEY `IDX1_T_E4S_DB_SMALL_CAR_TY` (`STD_CAR_ID`),
  KEY `IDX2_T_E4S_DB_SMALL_CAR_TY` (`SMALL_CAR_TYPE_CODE`),
  KEY `IDX3_T_E4S_DB_SMALL_CAR_TYPE` (`SMALL_CAR_TYPE_CN`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的车型小类信息。'



t_base_smallarea
CREATE TABLE `t_base_smallarea` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `SMALL_AREA_ID` varchar(36) NOT NULL DEFAULT '0' COMMENT '小区ID',
  `BIG_AREA_ID` varchar(36) DEFAULT NULL COMMENT '大区ID',
  `SMALL_AREA_NAME` varchar(100) DEFAULT NULL COMMENT '小区名称',
  `ORDER_NO` int(11) DEFAULT NULL COMMENT '排序',
  `IS_ENABLE` varchar(2) NOT NULL COMMENT '是否可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL COMMENT '修改日期',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2062 DEFAULT CHARSET=utf8 COMMENT='基础数据，与MDM系统对接的小区信息。'



t_base_system_info
CREATE TABLE `t_base_system_info` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `CORP_NAME` varchar(255) DEFAULT NULL COMMENT '公司名',
  `CORP_LOGO` varchar(255) DEFAULT NULL COMMENT '公司logo',
  `CORP_EMAIL` varchar(255) DEFAULT NULL COMMENT '公司电邮',
  `CORP_PHONE` varchar(255) DEFAULT NULL COMMENT '公司电话',
  `CORP_FAX` varchar(255) DEFAULT NULL COMMENT '公司传真',
  `CORP_QQ` varchar(255) DEFAULT NULL COMMENT '企业QQ',
  `CORP_HOTLINE` varchar(255) DEFAULT NULL COMMENT '公司热线',
  `CORP_ADDRESS` varchar(255) DEFAULT NULL COMMENT '公司地址',
  `CORP_ZIP` varchar(255) DEFAULT NULL COMMENT '公司邮编',
  `INDEXMETA_KEYWORD` varchar(255) DEFAULT NULL COMMENT 'SEO关键字',
  `INDEXMETA_DESCRIPTION` varchar(255) DEFAULT NULL COMMENT 'SEO描述',
  `INDEXMETA_TITLE` varchar(255) DEFAULT NULL COMMENT '首页标题',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `SYS_ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8



t_base_system_pub_info
CREATE TABLE `t_base_system_pub_info` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `SYS_ID` int(11) unsigned DEFAULT NULL COMMENT '系统id',
  `TYPE` smallint(6) DEFAULT NULL COMMENT '内容类型 FOOTER/HEADER/SITEMAP/OTHERS',
  `CONTENT` text COMMENT '内容',
  `PUB_INFO_URL` varchar(255) DEFAULT NULL COMMENT '外链地址',
  `ICON` varchar(255) DEFAULT NULL COMMENT 'icon',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `T_BASE_SYSTEM_INFO_SYSTEM_ID` (`SYS_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='系统公共信息'



t_base_tmall_member
CREATE TABLE `t_base_tmall_member` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `MEMBER_ID` int(11) unsigned NOT NULL COMMENT '会员编号',
  `ALIPAY_ID` varchar(17) DEFAULT NULL COMMENT '支付宝id',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_BASE_MEMBER_CONTACT_T_BASE_MEMBER_1` (`MEMBER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='天猫会员信息'



t_base_wechat_member
CREATE TABLE `t_base_wechat_member` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `MEMBER_ID` int(11) unsigned NOT NULL COMMENT '会员编号',
  `UNION_ID` varchar(50) DEFAULT NULL COMMENT '微信唯一ID',
  `HEADIMGURL` varchar(2000) DEFAULT NULL COMMENT '用户头像',
  `WX_AREA` varchar(64) DEFAULT NULL COMMENT '微信地区',
  `REMARK` varchar(5000) DEFAULT NULL COMMENT '备注',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_BASE_MEMBER_CONTACT_T_BASE_MEMBER_1` (`MEMBER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COMMENT='微信会员信息'



t_cms_article
CREATE TABLE `t_cms_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `title` varchar(255) NOT NULL COMMENT '文章标题',
  `keywords` varchar(255) NOT NULL COMMENT '关键字，多个使用逗号分隔',
  `front_img_path` varchar(500) NOT NULL COMMENT '封面路径',
  `source` varchar(255) NOT NULL COMMENT '文章来源',
  `description` text NOT NULL COMMENT '资讯摘要',
  `content` text NOT NULL COMMENT '文章正文',
  `add_link` char(255) NOT NULL COMMENT '是否添加内链词，1_是，0_否',
  `status` varchar(10) NOT NULL COMMENT '文章状态，草稿_DRAFT，发布_PUBLISH，作废_INVALID',
  `creator` varchar(255) NOT NULL COMMENT '创建人',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建人',
  `modifier` varchar(255) NOT NULL COMMENT '修改人',
  `update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `sort_order` int(11) NOT NULL DEFAULT '178' COMMENT '排序',
  `section_id` int(11) NOT NULL COMMENT '栏目标识',
  `trans_content` text COMMENT '转化后的文章正文（譬如增加内链词链接）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8 COMMENT='资讯文章表'



t_cms_article_rela
CREATE TABLE `t_cms_article_rela` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '唯一标识，主键',
  `article_id` int(11) NOT NULL COMMENT '文章标识',
  `type` varchar(20) NOT NULL COMMENT '文章关联类型，车系: CAR_SERIES',
  `object_id` int(11) NOT NULL COMMENT '文章关联对象标识，根据文章关联类型区分',
  `object_name` varchar(255) NOT NULL COMMENT '文章关联对象名称',
  `creator` varchar(255) NOT NULL COMMENT '创建人',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `modifier` varchar(255) NOT NULL COMMENT '修改人',
  `update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=183 DEFAULT CHARSET=utf8 COMMENT='文章关联数据'



t_cms_cata_attrs
CREATE TABLE `t_cms_cata_attrs` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '属性ID',
  `CATA_ID` int(11) NOT NULL DEFAULT '0' COMMENT '频道类型',
  `ENNAME` varchar(255) NOT NULL DEFAULT '' COMMENT '属性键',
  `CNNAME` varchar(255) NOT NULL DEFAULT '' COMMENT '属性中文名',
  `DATATYPE` int(11) NOT NULL DEFAULT '0' COMMENT '数据类型',
  `VALUE` varchar(255) NOT NULL DEFAULT '' COMMENT '属性值',
  `LENGTH` float NOT NULL DEFAULT '0' COMMENT '字段长度',
  `ISNULL` int(11) NOT NULL DEFAULT '0' COMMENT '是否可空',
  `MIN` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '最小值',
  `MAX` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '最大值',
  `BOXMODE` int(11) NOT NULL DEFAULT '0' COMMENT '控件类型',
  `SERIALIDS` varchar(500) NOT NULL DEFAULT '' COMMENT 'ID序列',
  `SERIALVALUES` varchar(500) NOT NULL DEFAULT '' COMMENT '值序列',
  `REMARK` varchar(255) NOT NULL DEFAULT '' COMMENT '注释',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8 COMMENT='频道属性表'



t_cms_catalogs
CREATE TABLE `t_cms_catalogs` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '频道ID',
  `cata_name` varchar(255) NOT NULL DEFAULT '' COMMENT '频道名称',
  `level` varchar(255) NOT NULL DEFAULT '' COMMENT '层级',
  `parent_id` varchar(255) NOT NULL DEFAULT '' COMMENT '父频道ID',
  `pc_display` int(11) NOT NULL DEFAULT '1' COMMENT 'PC是否显示',
  `mobile_display` int(11) NOT NULL DEFAULT '1' COMMENT '移动是否显示',
  `vieworder` int(11) NOT NULL DEFAULT '0' COMMENT '显示顺序',
  `model_id` int(11) NOT NULL DEFAULT '0' COMMENT '关联模型ID',
  `model_table` varchar(255) NOT NULL DEFAULT '' COMMENT '关联模型表名,冗余字段 t_cms_models.model_table',
  `model_instanceid` int(11) NOT NULL DEFAULT '0' COMMENT '关联模型实例id',
  `cata_attr_type` int(11) NOT NULL DEFAULT '1' COMMENT '平台内容属性。1：封面；2：列表；3：链接',
  `cata_type_id` int(255) NOT NULL DEFAULT '0' COMMENT '栏目类型',
  `cata_alias` varchar(255) NOT NULL DEFAULT '' COMMENT '栏目别名',
  `title` varchar(255) NOT NULL DEFAULT '' COMMENT '标题',
  `futitle` varchar(255) NOT NULL DEFAULT '' COMMENT '副标题',
  `keywords` varchar(255) NOT NULL DEFAULT '' COMMENT '关键字',
  `description` varchar(255) NOT NULL DEFAULT '' COMMENT '描述',
  `url_pattern` varchar(255) NOT NULL DEFAULT '' COMMENT '栏目url',
  `pc_template` varchar(255) NOT NULL DEFAULT '' COMMENT 'PC模板',
  `mobile_template` varchar(255) NOT NULL DEFAULT '' COMMENT '移动模板',
  `pc_content_template` varchar(255) NOT NULL DEFAULT '' COMMENT 'pc叶子节点内容模板',
  `mobile_content_template` varchar(255) NOT NULL DEFAULT '' COMMENT '移动叶子节点内容模板',
  `is_enable` int(11) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `creator` varchar(255) NOT NULL DEFAULT '',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modifier` varchar(255) NOT NULL DEFAULT '',
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cata_full_alias` varchar(255) DEFAULT '' COMMENT '栏目全别名，包含父节点，一直追溯到根，用"/"相连。如：/father/son',
  `as_search_result` int(1) DEFAULT NULL COMMENT '是否加入搜索结果，用于搜索功能，1_是，0_否',
  `cata_full_alias_path` varchar(500) DEFAULT NULL COMMENT '栏目全别名路径，包含所有父节点，使用分号分割，如"/hui;/hui/lania"',
  `cata_name_path` varchar(500) DEFAULT NULL COMMENT '栏目名称路径，包含所有父节点，使用分号分割，如"惠挑车;蓝鸟"',
  `rela_table` varchar(255) DEFAULT NULL COMMENT '关联依赖模型表名,冗余字段 t_cms_models.rela_table',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=309 DEFAULT CHARSET=utf8 COMMENT='频道信息表'



t_cms_catatype
CREATE TABLE `t_cms_catatype` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '频道类型ID',
  `TYPE_NAME` varchar(255) NOT NULL DEFAULT '' COMMENT '频道类型名称',
  `REMARK` varchar(255) NOT NULL DEFAULT '' COMMENT '频道类型说明',
  `IS_ENABLE` int(11) DEFAULT '1' COMMENT '是否可用',
  `CREATOR` varchar(255) DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(255) DEFAULT '' COMMENT '修改人',
  `UPDATED_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=918 DEFAULT CHARSET=utf8 COMMENT='频道类型表'



t_cms_catatype_attrs
CREATE TABLE `t_cms_catatype_attrs` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '属性ID',
  `CATA_TYPE_ID` int(11) NOT NULL DEFAULT '0' COMMENT '频道类型',
  `ENNAME` varchar(255) NOT NULL DEFAULT '' COMMENT '属性键',
  `CNNAME` varchar(255) NOT NULL DEFAULT '' COMMENT '属性中文名',
  `DATATYPE` int(11) NOT NULL DEFAULT '0' COMMENT '数据类型',
  `LENGTH` float NOT NULL DEFAULT '0' COMMENT '字段长度',
  `ISNULL` int(11) NOT NULL DEFAULT '0' COMMENT '是否可空',
  `MIN` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '最小值',
  `MAX` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '最大值',
  `BOXMODE` varchar(255) NOT NULL DEFAULT '' COMMENT '控件类型',
  `SERIALIDS` varchar(500) NOT NULL DEFAULT '' COMMENT 'ID序列',
  `SERIALVALUES` varchar(500) NOT NULL DEFAULT '' COMMENT '值序列',
  `REMARK` varchar(255) NOT NULL DEFAULT '' COMMENT '注释',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=501 DEFAULT CHARSET=utf8 COMMENT='频道类型自定义属性表'



t_cms_linkword
CREATE TABLE `t_cms_linkword` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `word` varchar(50) NOT NULL COMMENT '词语',
  `link` varchar(50) NOT NULL COMMENT '链接',
  `status` varchar(10) NOT NULL COMMENT '状态，启用_WORK，停用_STOP，删除_DEL',
  `creator` varchar(255) NOT NULL COMMENT '创建人',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `modifier` varchar(255) NOT NULL COMMENT '修改人',
  `update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8 COMMENT='内链词'



t_cms_models
CREATE TABLE `t_cms_models` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '模型ID',
  `MODEL_NAME` varchar(255) NOT NULL DEFAULT '' COMMENT '模型名称',
  `MODEL_TABLE` varchar(255) NOT NULL DEFAULT '' COMMENT '模型对应表名',
  `ID_FIELD` varchar(255) NOT NULL DEFAULT '' COMMENT '模型ID字段',
  `NAME_FILED` varchar(255) NOT NULL DEFAULT '' COMMENT '模型名称字段',
  `REMARK` varchar(255) NOT NULL DEFAULT '' COMMENT '模型注释',
  `IS_ENABLE` int(11) NOT NULL DEFAULT '1' COMMENT '是否可用',
  `rela_table` varchar(255) DEFAULT NULL COMMENT '关联库表（目前针对频道类型）',
  `rela_id_field` varchar(255) DEFAULT NULL COMMENT '关联表主键字段',
  `rela_name_field` varchar(255) DEFAULT NULL COMMENT '关联表名称字段',
  `rela_extra_field` varchar(255) DEFAULT NULL COMMENT '关联表额外字段，多个使用逗号分割，如：age,sex,createtime ',
  `rela_foreign_field` varchar(255) DEFAULT NULL COMMENT '关联表外键字段，关联本表字段id_field',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COMMENT='系统业务模型表'



t_cms_section
CREATE TABLE `t_cms_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '唯一标识，主键',
  `parent_id` int(11) DEFAULT NULL COMMENT '父标识，关联 t_cms_section.id',
  `name` varchar(100) DEFAULT NULL COMMENT '栏目名称',
  `cata_id` int(11) DEFAULT NULL COMMENT '关联频道，关联t_cms_catalogs.id',
  `pc_template_id` int(11) DEFAULT NULL COMMENT 'PC端模板标识，关联t_cms_template.id',
  `description` text COMMENT '栏目简介（描述）',
  `status` varchar(10) DEFAULT NULL COMMENT '栏目状态，启用_WORK，停用_STOP，删除_DEL',
  `creator` varchar(255) DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `modifier` varchar(255) DEFAULT NULL,
  `update_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `sort_order` int(11) DEFAULT NULL COMMENT '排序（暂无用）',
  `id_path` varchar(500) DEFAULT NULL COMMENT 'id(t_cms_section.id)的路径，用半角英文分号作为分割，如：1;12;78',
  `name_path` varchar(500) DEFAULT NULL COMMENT 'name(t_cms_section.name)的路径，用半角英文分号作为分割，如：新闻中心;进口新车;评测',
  `mobile_template_id` int(11) DEFAULT NULL COMMENT '移动端模板标识，关联t_cms_template.id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8 COMMENT='资讯栏目'



t_cms_template
CREATE TABLE `t_cms_template` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '唯一标识，主键',
  `template_name` varchar(100) DEFAULT NULL COMMENT '模板名称',
  `template_path` varchar(255) DEFAULT NULL COMMENT '模板路径',
  `creator` varchar(255) DEFAULT NULL COMMENT '创建人',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `modifier` varchar(255) DEFAULT NULL COMMENT '修改人',
  `update_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `template_type` varchar(30) DEFAULT 'ARTICLE' COMMENT '模板类型，频道_CATALOGS，资讯_ARTICLE',
  `template_teriminal` varchar(255) DEFAULT 'PC' COMMENT '模板终端，PC端_PC，移动端_WAP',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='模板配置'



t_e4s_db_customer_account
CREATE TABLE `t_e4s_db_customer_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `CUSTOMER_ID` varchar(32) NOT NULL COMMENT '会员编号，是会员的唯一标识',
  `CUSTOMER_NAME` varchar(64) DEFAULT ' ',
  `TYPE` varchar(8) DEFAULT NULL COMMENT '会员类型包括1个人会员，2企业会员，3商铺会员，4大买家，5中间商，还可能是这几种的集合',
  `ACTIVATION_STATUS` char(1) DEFAULT NULL COMMENT '需要激活的时候，记录会员是否已经激活过。0未激活，1激活。',
  `STATUS` char(1) DEFAULT NULL COMMENT '0冻结, 1正常',
  `PASSWORD` varchar(64) DEFAULT NULL COMMENT '密码',
  `QUESTION` varchar(128) DEFAULT NULL COMMENT '密码提问问题',
  `ANSWER` varchar(128) DEFAULT NULL COMMENT '密码问题答案',
  `EMAIL` varchar(128) DEFAULT NULL COMMENT '注册电子邮箱，注册时填写的电子邮箱，可以用来登录。',
  `mobile` varchar(32) DEFAULT ' ',
  `nick_name` varchar(64) DEFAULT ' ',
  `ORGID` varchar(32) DEFAULT NULL COMMENT '组织机构ID',
  `ACTIVATING_KEY` varchar(32) DEFAULT NULL COMMENT '激活码',
  `SOURCE` varchar(32) DEFAULT NULL COMMENT '0:总站注册；1:区域平台注册；2:管理员录入；3:抓取导入',
  `SEARCHPWD_KEY` varchar(32) DEFAULT NULL COMMENT '找回密码验证码。找回密码时向，邮箱发送的验证码。同时用于信息的验证。',
  `RESET_EMAIL` varchar(128) DEFAULT NULL COMMENT '重设邮箱',
  `RESET_MOBILE` varchar(32) DEFAULT NULL COMMENT '重设手机',
  `PWD_SAFE_FACTOR` varchar(8) DEFAULT '1' COMMENT '''1''弱，''2''表示中，''3''表强',
  `BINDING_EMAIL` varchar(128) DEFAULT NULL COMMENT '绑定邮箱。会员的真实邮箱，同时为会员提供服务时，用的邮箱 。',
  `RESET_BINDING_EMAIL` varchar(128) DEFAULT NULL COMMENT '重置绑定邮箱。重置绑定邮箱时，存放会员要重置成为的邮箱。',
  `GUIDE_STEP` varchar(8) DEFAULT NULL COMMENT '店铺设置主导航步骤',
  `SUB_GUIDE_STEP` varchar(8) DEFAULT NULL COMMENT '店铺设置二级导航步骤',
  `OPEN_GUIDE_STEP` varchar(8) DEFAULT NULL COMMENT '开店主导航步骤',
  `LEVEL_UP_STEP` varchar(8) DEFAULT NULL COMMENT '会员升级导航步骤',
  `INFORMATION_SOURCE` varchar(32) DEFAULT NULL COMMENT '信息来源',
  `APPLICATION_STATUS` varchar(8) DEFAULT NULL COMMENT '会员解冻申请状态',
  `DOMAIN` varchar(256) DEFAULT NULL COMMENT '注册来源域名',
  `APPLICATION_ID` varchar(32) DEFAULT NULL COMMENT '申请ID',
  `BLACKLIST` int(11) DEFAULT '0',
  `internal_account` varchar(64) DEFAULT '',
  `TRADE_PASSWORD` varchar(60) DEFAULT NULL,
  `USER_TYPE` varchar(1) DEFAULT ' ',
  `PAY_PWD` varchar(64) DEFAULT '',
  `PAYPWD_SAFE_FACTOR` char(1) DEFAULT '1',
  `GUIDE_ID` varchar(50) DEFAULT NULL COMMENT '导购员ID',
  `CRM_USER_ID` varchar(50) DEFAULT NULL COMMENT 'CRM USERID',
  `USER_VERSION` varchar(10) DEFAULT NULL COMMENT '用户信息版本',
  `STORE_ID` varchar(32) DEFAULT NULL COMMENT '经销商账户ID',
  `EMP_PIC` varchar(500) DEFAULT NULL,
  `GENDER_CODE` varchar(10) DEFAULT NULL COMMENT '性别编码',
  `REAL_NAME` varchar(100) DEFAULT NULL COMMENT '职员姓名',
  `EMP_CODE` varchar(10) DEFAULT NULL COMMENT '职员编码',
  `CUSTOMER_CONTRACT_STATUS` char(2) DEFAULT '0' COMMENT '用户协议状态',
  `WECHAT_OPENID` varchar(50) DEFAULT NULL COMMENT '微信OPENID',
  `ZFB_OPENID` varchar(50) DEFAULT NULL COMMENT '支付宝OPENID',
  `LAST_UPDATE_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'LAST_UPDATE_DATE 最后更新时间',
  `CREATE_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'CREATE_DATE 创建时间',
  `USER_ID` int(11) DEFAULT '0' COMMENT '基础用户ID',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_CUSTOMER_ID` (`CUSTOMER_ID`),
  KEY `idx_CUSTOMER_NAME` (`CUSTOMER_NAME`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=62208 DEFAULT CHARSET=utf8 COMMENT='存放会员的账户信息'



t_e4s_db_dictionary_data
CREATE TABLE `t_e4s_db_dictionary_data` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `DICT_TYPE_ID` int(10) NOT NULL,
  `DICT_DATA_CODE` varchar(32) NOT NULL,
  `DICT_DATA_NAME` varchar(64) NOT NULL,
  `ORDERING` int(2) NOT NULL,
  `STATE` varchar(32) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8



t_e4s_db_dictionary_type
CREATE TABLE `t_e4s_db_dictionary_type` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `DICT_TYPE_CODE` varchar(32) NOT NULL COMMENT '字典类型代码',
  `DICT_TYPE_NAME` varchar(32) NOT NULL COMMENT '字典类型名称',
  `STATE` varchar(32) NOT NULL COMMENT '状态',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='字典类型表'



t_e4s_db_function
CREATE TABLE `t_e4s_db_function` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `PARENT_ID` int(10) DEFAULT NULL COMMENT '父功能编号',
  `FUNCTION_CODE` varchar(64) DEFAULT NULL COMMENT '功能代码',
  `FUNCTION_NAME` varchar(64) DEFAULT NULL COMMENT '功能名称',
  `FUNCTION_TYPE` varchar(32) DEFAULT NULL COMMENT '功能类型',
  `PAGE_LINK` varchar(128) DEFAULT NULL COMMENT '页面链接',
  `ICON_CLASS` char(20) DEFAULT NULL COMMENT '菜单样式',
  `ORDERING` int(2) DEFAULT NULL COMMENT '排序',
  `LAYER` int(2) DEFAULT NULL COMMENT '菜单层级',
  `STATE` varchar(32) DEFAULT NULL COMMENT '状态',
  `AUTHC_LINK` varchar(128) DEFAULT NULL COMMENT '权限表达式',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2694 DEFAULT CHARSET=utf8 COMMENT='功能表'



t_e4s_db_log_message
CREATE TABLE `t_e4s_db_log_message` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
  `USER_ID` int(10) unsigned DEFAULT NULL COMMENT '用户编号',
  `USER_NAME` varchar(64) DEFAULT NULL COMMENT '用户名',
  `CLASS_NAME` varchar(128) DEFAULT NULL COMMENT '类名',
  `METHOD_NAME` varchar(64) DEFAULT NULL COMMENT '方法名',
  `METHOD_PARAMS` text COMMENT '方法参数',
  `LOG_DATE` datetime DEFAULT NULL COMMENT '日志时间',
  `LOG_MESSAGE` text COMMENT '日志信息',
  `OPERATION_TYPE` varchar(32) DEFAULT NULL COMMENT '操作类型',
  `REMARK` text COMMENT '备注',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=39243 DEFAULT CHARSET=utf8 COMMENT='日志信息表'



t_e4s_db_log_register
CREATE TABLE `t_e4s_db_log_register` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
  `FUNCTION_ID` int(10) unsigned DEFAULT NULL COMMENT '功能编号',
  `OPERATION_TYPE` varchar(32) DEFAULT NULL COMMENT '操作类型',
  `CLASS_NAME` varchar(64) DEFAULT NULL COMMENT '类名',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='日志注册表'



t_e4s_db_password_history
CREATE TABLE `t_e4s_db_password_history` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `USER_ID` varchar(32) NOT NULL COMMENT '用户编号',
  `PASSWORD` varchar(64) NOT NULL COMMENT '密码',
  `CREATE_DATE` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`ID`),
  KEY `idx_CUSTOMER_ID` (`USER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户密码历史表'



t_e4s_db_role
CREATE TABLE `t_e4s_db_role` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `ROLE_CODE` varchar(32) DEFAULT NULL COMMENT '角色代码',
  `ROLE_NAME` varchar(64) DEFAULT NULL COMMENT '角色名称',
  `STATE` varchar(32) DEFAULT NULL COMMENT '状态',
  `STORE_ID` varchar(32) DEFAULT NULL COMMENT '经销商ID',
  `ROLE_TYPE` int(11) DEFAULT NULL COMMENT '角色类型',
  `USER_ID` int(10) DEFAULT NULL COMMENT '用户编号',
  `CREATED_DATE` datetime DEFAULT NULL COMMENT '创建时间',
  `CREATOR` varchar(50) DEFAULT NULL COMMENT '创建人',
  `UPDATED_DATE` datetime DEFAULT NULL COMMENT '最近更新时间',
  `MODIFIER` varchar(50) DEFAULT NULL COMMENT '最新更新人',
  `IS_ENABLE` tinyint(4) DEFAULT NULL COMMENT '是否可用',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8 COMMENT='角色表'



t_e4s_db_role_function
CREATE TABLE `t_e4s_db_role_function` (
  `ID` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `ROLE_ID` int(10) NOT NULL,
  `FUNCTION_ID` int(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10806 DEFAULT CHARSET=utf8



t_e4s_db_user
CREATE TABLE `t_e4s_db_user` (
  `ID` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `LOGIN_NAME` varchar(32) DEFAULT NULL COMMENT '登陆名',
  `USER_NAME` varchar(64) DEFAULT NULL COMMENT '用户名',
  `PASSWORD` varchar(128) DEFAULT NULL COMMENT '密码',
  `SALT` varchar(64) DEFAULT NULL COMMENT 'SALT',
  `EMAIL` varchar(32) DEFAULT NULL COMMENT '邮箱',
  `MOBILE_PHONE` varchar(32) DEFAULT NULL COMMENT '手机号码',
  `USER_TYPE` varchar(32) DEFAULT NULL COMMENT '用户类型',
  `DLR_CODE` varchar(32) DEFAULT NULL COMMENT '专营店编码',
  `USER_STATE` varchar(32) DEFAULT 'OFFLINE',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=98481 DEFAULT CHARSET=utf8 COMMENT='基础用户表'



t_e4s_db_user_info
CREATE TABLE `t_e4s_db_user_info` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '编号',
  `USER_ID` int(10) DEFAULT NULL COMMENT '用户编号',
  `LOGIN_NAME` varchar(32) NOT NULL COMMENT '登录名',
  `USER_NAME` varchar(64) DEFAULT NULL COMMENT '用户名',
  `PASSWORD` varchar(128) NOT NULL COMMENT '登录密码',
  `SALT` varchar(64) DEFAULT NULL COMMENT 'Salt值',
  `EMAIL` varchar(32) DEFAULT NULL COMMENT '邮件',
  `MOBILE_PHONE` varchar(32) DEFAULT NULL COMMENT '电话',
  `USER_TYPE` varchar(32) DEFAULT NULL COMMENT '用户类型',
  `DLR_CODE` varchar(32) DEFAULT NULL COMMENT '专营店编码',
  `LAST_ROLE_ID` int(11) DEFAULT NULL COMMENT '最近的角色编号',
  `STATUS` tinyint(4) DEFAULT NULL COMMENT '用户状态，1：激活  0：冻结',
  `IS_ENABLE` tinyint(4) DEFAULT '1' COMMENT '是否可用',
  `REMARK` varchar(256) DEFAULT NULL COMMENT '备注',
  `CREATED_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `CREATOR` varchar(50) DEFAULT NULL COMMENT '创建人',
  `UPDATED_DATE` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `MODIFIER` varchar(50) DEFAULT NULL COMMENT '最后更新人员',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8 COMMENT='用户详细表'



t_e4s_db_user_role
CREATE TABLE `t_e4s_db_user_role` (
  `ID` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `CUSTOMER_ID` varchar(32) NOT NULL DEFAULT '' COMMENT '用户编号',
  `ROLE_ID` int(10) NOT NULL DEFAULT '0' COMMENT '角色编号',
  `MANAGER_ID` varchar(32) DEFAULT NULL COMMENT '经销商操作员编号',
  `USER_ID` int(10) NOT NULL COMMENT '基础用户ID',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3252 DEFAULT CHARSET=utf8 COMMENT='用户角色表'



t_ecommerce_card_payment
CREATE TABLE `t_ecommerce_card_payment` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ORDERPAYMENT_ID` int(11) unsigned DEFAULT NULL COMMENT '订单支付ID',
  `CARD_ID` int(11) unsigned DEFAULT NULL COMMENT '优惠券ID',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_ECOMMERCE_CARD_PAYMENT_T_ECOMMERCE_COUPON_CARD_1` (`CARD_ID`),
  KEY `FK_T_ECOMMERCE_CARD_PAYMENT_T_ECOMMERCE_ORDER_PAYMENT_1` (`ORDERPAYMENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='优惠券使用记录'



t_ecommerce_comment
CREATE TABLE `t_ecommerce_comment` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '点评编号',
  `ORDERSKU_ID` int(11) unsigned DEFAULT NULL COMMENT '订单编号',
  `COM_DATE` varchar(255) DEFAULT NULL COMMENT '点评日期',
  `CONTENT` varchar(255) DEFAULT NULL COMMENT '点评内容',
  `COMMENT_NEXT` int(11) DEFAULT NULL COMMENT '下一条评论编号',
  `MEMBER_ID` int(11) unsigned DEFAULT NULL COMMENT '会员编号',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime DEFAULT NULL COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_点评表_会员表_1` (`MEMBER_ID`),
  KEY `FK_T_COMMENT_ORDER_SKU_1` (`ORDERSKU_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='订单商品评价'



t_ecommerce_commodity
CREATE TABLE `t_ecommerce_commodity` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '商品编号',
  `DEALER_ID` int(11) unsigned DEFAULT NULL COMMENT '经销商ID',
  `PRODUCT_ID` int(11) unsigned DEFAULT NULL COMMENT '产品ID',
  `INVENTORY_ID` int(11) unsigned DEFAULT NULL COMMENT '库存ID',
  `STATUS` varchar(255) DEFAULT NULL COMMENT '1在售、0下架、-1删除',
  `DATE_FROM` datetime DEFAULT NULL COMMENT '开始时间',
  `DATE_TO` datetime DEFAULT NULL COMMENT '结束时间',
  `PERIOD` tinyint(4) DEFAULT NULL COMMENT '有效周期，比如一天，两条，一周，一个月。',
  `ORG_PRICE` int(11) DEFAULT NULL COMMENT '原始价格',
  `OFF_PRICE` int(11) DEFAULT NULL COMMENT '商品价格',
  `SALE_PRICE` int(11) DEFAULT NULL COMMENT '特价',
  `ORDER_PRICE` int(11) DEFAULT NULL COMMENT '定金',
  `SALES_TOTAL` int(11) DEFAULT NULL COMMENT '手工维护的销量',
  `RESTRICTION_TOTAL` int(11) DEFAULT NULL COMMENT '限制购买的数量',
  `TAG` varchar(255) DEFAULT NULL COMMENT '商品标记',
  `PROPERTYVALUEINFOS` text COMMENT '规格值信息，冗余值，用于规格搜索。格式为 [PROPERTYID1]:[PROPERTYVALUEID1];[PROPERTYID2]:[PROPERTYVALUEID2];  例如 1:2;2:4;',
  `METAKEYWORD` varchar(255) DEFAULT NULL COMMENT 'SEO关键字',
  `METADESCRIPTION` varchar(255) DEFAULT NULL COMMENT 'SEO描述',
  `GEN_CLUE` tinyint(4) DEFAULT NULL COMMENT '是否生成线索',
  `REDIRECT_URL` varchar(255) DEFAULT NULL COMMENT '跳转url',
  `VERSION` int(11) DEFAULT '0' COMMENT '版本',
  `SORT_ORDER` int(11) DEFAULT '0' COMMENT '排序',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_ECOMMERCE_COMMODITY_T_ECOMMERCE_COMMODITY_INVENTORY_1` (`INVENTORY_ID`),
  KEY `fk_t_ecommerce_commodity_t_base_product_1` (`PRODUCT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8 COMMENT='商品SKU'



t_ecommerce_commodity_car_ext
CREATE TABLE `t_ecommerce_commodity_car_ext` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `COMMODITY_ID` int(11) unsigned DEFAULT NULL COMMENT '商品id',
  `CAR_SERIES_ID` int(11) unsigned DEFAULT NULL COMMENT '车系ID',
  `CAR_MODEL_ID` int(128) unsigned DEFAULT NULL COMMENT '车型ID',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `fk_t_eCommerce_commodity_dealer_t_ecommerce_commodity_1` (`COMMODITY_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8 COMMENT='商品适用的车系'



t_ecommerce_commodity_dealer
CREATE TABLE `t_ecommerce_commodity_dealer` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `COMMODITY_ID` int(11) unsigned DEFAULT NULL COMMENT '商品id',
  `DEALER_ID` int(11) unsigned DEFAULT NULL COMMENT '经销商ID',
  `DEALER_CODE` varchar(128) DEFAULT NULL COMMENT '经销商编码',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `fk_t_eCommerce_commodity_dealer_t_ecommerce_commodity_1` (`COMMODITY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='经销商商品'



t_ecommerce_commodity_ext
CREATE TABLE `t_ecommerce_commodity_ext` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '商品编号',
  `COMMODITY_ID` int(11) DEFAULT NULL COMMENT '商品ID',
  `TITLE` varchar(255) DEFAULT NULL,
  `TITLE_MINI` varchar(255) DEFAULT NULL,
  `PIC` varchar(255) DEFAULT NULL,
  `PIC_MINI` varchar(255) DEFAULT NULL,
  `DESCRIPTION` longtext,
  `M_DESCRIPTION` longtext COMMENT '移动端描述',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商品SKU扩展'



t_ecommerce_commodity_inventory
CREATE TABLE `t_ecommerce_commodity_inventory` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `COMMODITY_ID` int(11) unsigned DEFAULT NULL COMMENT '商品外键',
  `QUANTITY_ONHAND` int(11) DEFAULT NULL COMMENT '现有库存',
  `ALLOCATED_QUANTITY` int(11) DEFAULT NULL COMMENT '已分配数量',
  `REORDER_MINIMNM` int(11) DEFAULT NULL COMMENT '最少库存，当少于这值时提示低库存',
  `VERSION` int(11) NOT NULL DEFAULT '1' COMMENT ' 版本',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8 COMMENT='商品SKU库存'



t_ecommerce_commodity_sku
CREATE TABLE `t_ecommerce_commodity_sku` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `PRODUCT_ID` int(11) unsigned DEFAULT NULL COMMENT '产品id',
  `COMMODITY_ID` int(11) unsigned DEFAULT NULL COMMENT '商品ID',
  `CAR_COLOR_ID` int(11) unsigned DEFAULT NULL COMMENT '外键关联车颜色表',
  `PROPERTY_ID` int(11) unsigned DEFAULT NULL COMMENT '属性ID',
  `PROPERTY_VALUE_ID` int(11) unsigned DEFAULT NULL COMMENT '属性值ID',
  `SKU_NAME` varchar(255) DEFAULT NULL COMMENT '属性值名，冗余，可与原表的值不一样，方便页面展示',
  `SKU_VALUE` varchar(255) DEFAULT NULL COMMENT '属性值，冗余',
  `SKU_ICON` varchar(255) DEFAULT NULL COMMENT 'icon',
  `SKU_REDIRECT_URL` varchar(255) DEFAULT NULL COMMENT 'URL',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `fk_t_ecommerce_commodity_sku_t_ecommerce_commodity_1` (`COMMODITY_ID`),
  KEY `fk_t_ecommerce_commodity_sku_t_base_property_value_1` (`PROPERTY_VALUE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8



t_ecommerce_commodity_verify_ext
CREATE TABLE `t_ecommerce_commodity_verify_ext` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `LOGO_URL` varchar(255) DEFAULT NULL COMMENT '微信优惠劵中显示的logo.\r\n卡券的商户logo，建议像素为300*300。 ',
  `CODE_TYPE` varchar(255) DEFAULT NULL COMMENT 'Code展示类型，"CODE_TYPE_TEXT"，文本；"CODE_TYPE_BARCODE"，一维码 ；"CODE_TYPE_QRCODE"，二维码；"CODE_TYPE_ONLY_QRCODE",二维码无code显示；"CODE_TYPE_ONLY_BARCODE",一维码无code显示；CODE_TYPE_NONE，不显示code和条形码类型，须开发者传入"立即使用"自定义cell完成线上券核销。',
  `COLOR` varchar(64) DEFAULT NULL COMMENT '"Color010":"#63b359",\r\n券颜色。按色彩规范标注填写Color010-Color100。\r\n"Color020":"#2c9f67",\r\n"Color030":"#509fc9",\r\n"Color040":"#5885cf",\r\n"Color050":"#9062c0",\r\n"Color060":"#d09a45",\r\n"Color070":"#e4b138",\r\n"Color080":"#ee903c",\r\n"Color081":"#f08500",\r\n"Color082":"#a9d92d",\r\n"Color090":"#dd6549",\r\n"Color100":"#cc463d",\r\n"Color101":"#cf3e36",\r\n"Color102":"#5E6671"',
  `TITLE` varchar(27) DEFAULT NULL COMMENT '卡券名，字数上限为9个汉字。(建议涵盖卡券属性、服务及金额)。',
  `SUB_TITLE` varchar(54) DEFAULT NULL COMMENT '券名，字数上限为18个汉字。',
  `DESCRIPTION` varchar(255) DEFAULT NULL COMMENT '使用提示',
  `NEED_VERIFIED` tinyint(4) DEFAULT NULL COMMENT '是否需要核销',
  `VERIFIED` varchar(255) DEFAULT NULL COMMENT '核销类型，json',
  `VERIFIED_FROM` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '核销开始日期',
  `VERIFIED_TO` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '核销结束日期',
  `FIXED_TERM` int(15) DEFAULT NULL COMMENT '表示自领取后多少天内有效，不支持填写0',
  `FIXED_BEGIN_TERM` int(15) DEFAULT NULL COMMENT '表示自领取后多少天开始生效，领取后当天生效填写0。（单位为天）',
  `RECONCILIATION_CLEARING` varchar(2000) DEFAULT NULL COMMENT '对账结算，json',
  `IS_ENABLE` int(11) DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL COMMENT '修改人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8



t_ecommerce_coupon
CREATE TABLE `t_ecommerce_coupon` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '优惠券编号',
  `COUPON_GROUP_ID` int(10) unsigned DEFAULT NULL COMMENT '优惠劵分组ID',
  `SHOW_NAME` varchar(255) DEFAULT NULL COMMENT '优惠券名',
  `COUPON_TYPE` tinyint(255) DEFAULT '1' COMMENT '1自有、0外部',
  `DEALER_ID` int(11) unsigned DEFAULT NULL COMMENT '经销商编号',
  `VALID_PERIOD` tinyint(4) DEFAULT NULL COMMENT '有效期类型',
  `SOURCE` varchar(255) DEFAULT NULL COMMENT '优惠券来源依据，可用作分组',
  `REPEAT` tinyint(255) DEFAULT '0' COMMENT '是否允许重复使用',
  `DOUBLE_DISCOUNTING` tinyint(255) DEFAULT '0' COMMENT '是否允许折上折',
  `CONDITION` varchar(255) DEFAULT NULL COMMENT '约束条件，可以是SQL',
  `DESCRIPTION` varchar(255) DEFAULT NULL COMMENT '描述',
  `STATUS` varchar(255) DEFAULT NULL COMMENT '0:未使用；1已使用',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8 COMMENT='优惠券'



t_ecommerce_coupon_card
CREATE TABLE `t_ecommerce_coupon_card` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '卡密编号',
  `COUPON_ID` int(11) unsigned DEFAULT NULL COMMENT '优惠券ID',
  `MEMBER_ID` int(11) unsigned DEFAULT NULL COMMENT '会员ID',
  `GIFT_CERTIFICATENO` varchar(255) DEFAULT NULL COMMENT '卡号',
  `SECRET` varchar(255) DEFAULT NULL COMMENT '卡密',
  `EXPIRE` datetime DEFAULT NULL COMMENT '过期时间',
  `GEN_DATE` datetime DEFAULT NULL COMMENT '生成日期',
  `USE_DATE` datetime DEFAULT NULL COMMENT '使用日期',
  `STATUS` varchar(255) DEFAULT NULL COMMENT '状态',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_卡密表_优惠券_1` (`COUPON_ID`),
  KEY `FK_T_ECOMMERCE_COUPON_CARD_T_BASE_MEMBER_1` (`MEMBER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8 COMMENT='会员优惠券'



t_ecommerce_coupon_group
CREATE TABLE `t_ecommerce_coupon_group` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '优惠券编号',
  `COUPON_GROUP_NAME` varchar(255) DEFAULT NULL COMMENT '优惠劵组名',
  `TOTAL` int(11) DEFAULT NULL COMMENT '发券的总数',
  `DICOUNT_TOTAL` int(11) DEFAULT NULL COMMENT '可抵消金额，如90，代表可抵消订单金额90元',
  `DISCOUNT_PERCENTAGE` int(11) DEFAULT NULL COMMENT '百分比，百分之九十，则填90',
  `CONDITION` varchar(255) DEFAULT NULL COMMENT '使用条件，可以是sql，用来指明适用于那些商品',
  `SOURCE` varchar(255) DEFAULT NULL COMMENT '来源依据，可用作分组',
  `ACTIVE_DATE` datetime DEFAULT NULL COMMENT '激活时间',
  `EXPIRE_DATE` datetime DEFAULT NULL COMMENT '过期时间',
  `DESCRIPTION` varchar(255) DEFAULT NULL COMMENT '描述',
  `STATUS` varchar(255) DEFAULT NULL COMMENT '0:未使用；1已使用',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8 COMMENT='优惠组'



t_ecommerce_finacial_order
CREATE TABLE `t_ecommerce_finacial_order` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '金融编号',
  `ITEM_ID` int(11) unsigned DEFAULT NULL COMMENT '商品编号',
  `LICENSE_TYPE` int(11) DEFAULT NULL COMMENT '证件类型',
  `LICENSE_NO` varchar(255) DEFAULT NULL COMMENT '证件号码',
  `JOB` varchar(255) DEFAULT NULL COMMENT '职业',
  `INCOME` varchar(255) DEFAULT NULL COMMENT '收入范围',
  `INSURANCE` varchar(255) DEFAULT NULL COMMENT '社保',
  `RESERVEFUND` varchar(255) DEFAULT NULL COMMENT '公积金',
  `SELF_CREDIT` varchar(255) DEFAULT NULL COMMENT '自评信用记录',
  `HOUSE` varchar(255) DEFAULT NULL COMMENT '住房状态',
  `CREDIT_STATUS` varchar(255) DEFAULT NULL,
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='金融订单'



t_ecommerce_order
CREATE TABLE `t_ecommerce_order` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '订单编号',
  `DEALER_ID` int(11) unsigned DEFAULT NULL COMMENT '商家编号',
  `MEMBER_ID` int(11) unsigned DEFAULT NULL COMMENT '会员编号',
  `OPEN_ID` varchar(64) DEFAULT NULL COMMENT '微信OPEN_ID',
  `ORDERADDRESSID` int(11) DEFAULT NULL,
  `ORDER_TYPE` int(11) DEFAULT NULL COMMENT '订单类型',
  `ORDER_NO` varchar(255) DEFAULT NULL COMMENT '交易编号',
  `PRICE` int(11) DEFAULT NULL COMMENT '订单金额，单位：分',
  `SOURCE` int(10) unsigned DEFAULT NULL COMMENT '订单来源，比如车巴巴-移动端，车巴巴-PC端,\r\n参考数据字典',
  `CONTACT_ID` varchar(255) DEFAULT NULL COMMENT '联系人ID',
  `EXTRA_INFO` varchar(255) DEFAULT NULL COMMENT '订单扩展字段：如活动ID记录',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_订单索引_会员表_1` (`MEMBER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=282 DEFAULT CHARSET=utf8 COMMENT='订单'



t_ecommerce_order_address
CREATE TABLE `t_ecommerce_order_address` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `REGION_ID` int(11) unsigned DEFAULT NULL COMMENT '地区ID',
  `REGION_FULLNAME` varchar(128) DEFAULT NULL COMMENT '地区全名,如“中国,广东,广州,越秀区”,冗余字段',
  `FIRST_NAME` varchar(32) DEFAULT NULL COMMENT '名',
  `LAST_NAME` varchar(32) DEFAULT NULL COMMENT '姓',
  `PHONE_NUMBER` varchar(32) DEFAULT NULL COMMENT '电话号码',
  `EMAIL` varchar(64) DEFAULT NULL COMMENT '电子邮件',
  `FAX_NUMBER` varchar(32) DEFAULT NULL COMMENT '传真号码',
  `POSTAL_CODE` varchar(20) DEFAULT NULL COMMENT '邮政编码',
  `ADDRESS1` varchar(128) DEFAULT NULL COMMENT '地址',
  `ADDRESS2` varchar(128) DEFAULT NULL COMMENT '地址2',
  `CONTACT_FULL_NAME` varchar(128) DEFAULT NULL COMMENT '联系人全名',
  `CONTACT_MOBILE` varchar(128) DEFAULT NULL COMMENT '联系人手机',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=273 DEFAULT CHARSET=utf8 COMMENT='订单地址'



t_ecommerce_order_flowstatus
CREATE TABLE `t_ecommerce_order_flowstatus` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `STATUS` int(11) DEFAULT NULL COMMENT '订单状态,-1取消，0收到订单、1处理中、2已发货，3完成',
  `PAY_STATUS` int(11) DEFAULT NULL COMMENT '支付状态：0未付款、1已付款、2已退款',
  `INFO` varchar(255) DEFAULT NULL COMMENT '备注',
  `VERSION` int(11) NOT NULL DEFAULT '0',
  `ORDER_ID` int(11) unsigned DEFAULT NULL,
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_ORDERID` (`ORDER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=651 DEFAULT CHARSET=utf8 COMMENT='订单状态'



t_ecommerce_order_payment
CREATE TABLE `t_ecommerce_order_payment` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ORDER_ID` int(11) unsigned NOT NULL COMMENT '订单ID',
  `DOCUMENT_NO` varchar(32) NOT NULL COMMENT '收/退款单号',
  `DOCUMENT_TYPE` smallint(6) NOT NULL COMMENT '单据类型N            1=收款单            0=退款单',
  `PAYMENT_AMOUNT` decimal(12,2) NOT NULL COMMENT '收/退款金额',
  `COMMISSION` decimal(12,2) DEFAULT NULL COMMENT '手续费',
  `PAYMENTGATEWAY_NAME` text COMMENT '支付网关名称',
  `PAYMENTGATEWAY_ID` int(11) unsigned DEFAULT NULL COMMENT '支付方式ID，用于前台支付跳转',
  `PAYMENT_TYPE` smallint(6) DEFAULT NULL COMMENT '支付方式类型(货到付款、自提)N            1=现金N            2=POS刷卡N            3=支票',
  `PAYMENTTYPE_DESC` text COMMENT '支付方式的描述，例如N            货到付款 现金支付N            货到付款 POS刷卡支付N            在线支付N            银行卡转账N            邮局汇款N            自提 支票支付',
  `HAS_INVOICE` smallint(6) NOT NULL COMMENT '是否需要发票',
  `INVOICE_TITLE` varchar(128) DEFAULT NULL COMMENT '发票抬头',
  `IP_ADDRESS` varchar(64) DEFAULT NULL COMMENT 'IP地址',
  `GIFT_CERTIFICATENO` varchar(32) DEFAULT NULL COMMENT '支付礼券号码',
  `USED_SHOPPOINT` int(11) DEFAULT NULL COMMENT '支付所使用的积分数量',
  `ACCOUNT_INFO` text COMMENT '收/退款账号信息：N            例如N            开户行：中国农业银行广州黄花岗支行N            银行户名：广州信息科技有限公司N            银行帐号：1111 2222 3333 4444 5555N            N            或N            商户客户账号：1234567890N            收款客户：广州信息科技有限公司N            ',
  `RETURN_REASON` text COMMENT '退款原因',
  `MEMO` text COMMENT '备注',
  `PAYER` varchar(32) DEFAULT NULL COMMENT '付款人姓名',
  `PAYEE` varchar(32) DEFAULT NULL COMMENT '收款人姓名',
  `PAY_TIME` varchar(255) DEFAULT NULL COMMENT '收/退款时间',
  `VERSION` int(11) NOT NULL DEFAULT '0',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `AK_DOCUMENT_NO` (`DOCUMENT_NO`),
  KEY `FK_ORDER_PAYMENT_2_SALES_ORDER` (`ORDER_ID`),
  KEY `FK_T_ECOMMERCE_ORDER_PAYMENT_T_ECOMMERCE_PAYMENTGATEWAY_1` (`PAYMENTGATEWAY_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8 COMMENT='订单支付信息'



t_ecommerce_order_shipment
CREATE TABLE `t_ecommerce_order_shipment` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ORDER_ID` int(11) unsigned NOT NULL COMMENT '销售订单外键',
  `DOCUMENT_TYPE` smallint(6) NOT NULL COMMENT '单据类型           1=发货单            0=退货单',
  `SHIPPINGADDRESS_ID` int(11) unsigned DEFAULT NULL COMMENT '发/退货地址外键',
  `DOCUMENT_NO` varchar(32) NOT NULL COMMENT '发/退货单号',
  `TRACKING_NO` varchar(128) DEFAULT NULL COMMENT '物流跟踪号',
  `WRAP_COST` int(11) DEFAULT NULL COMMENT '包装费,单位（分）',
  `WRAP_ID` int(11) unsigned DEFAULT NULL COMMENT '包装外键，不使用包装即为NULL',
  `WRAP_NAME` varchar(64) DEFAULT NULL COMMENT '包装名称',
  `CARRIER_CODE` varchar(128) DEFAULT NULL COMMENT '运输公司编码',
  `CARRIER_NAME` varchar(128) DEFAULT NULL COMMENT '运输公司名称',
  `SHIPPING_COST` int(11) DEFAULT NULL COMMENT '运输费用,单位（分）',
  `SHIPPINGMETHOD_ID` int(11) unsigned DEFAULT NULL COMMENT '运输方式ID,暂无数据表，先作为数据结构',
  `SHIPPINGRATE_ID` int(11) unsigned DEFAULT NULL COMMENT '运输费率ID',
  `DELIVERY_TIME` varchar(32) DEFAULT NULL COMMENT '送货时间',
  `NEEDCONFRIM_B4DELIVERY` smallint(6) DEFAULT NULL COMMENT '是否送货前电话确认',
  `SELFCOLLECTIONCENTRE_ID` int(11) unsigned DEFAULT NULL COMMENT '客户取货中心ID',
  `SELFCOLLECTIONCENTRE_NAME` varchar(64) DEFAULT NULL COMMENT '客户取货中心名称',
  `EXCEPTEDSELFCOLLECT_DATE` varchar(255) DEFAULT NULL COMMENT '要求提货日期',
  `ACTUALSELFCOLLECT_DATE` varchar(255) DEFAULT NULL COMMENT '实际提货日期',
  `NEED_INTERFACE` tinyint(4) DEFAULT NULL COMMENT '是否通过接口获取物流信息。 0 否 1 是',
  `STATUS` smallint(6) DEFAULT NULL COMMENT '单据状态',
  `VERSION` int(11) NOT NULL DEFAULT '0',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `AK_DOCUMENT_NO` (`DOCUMENT_NO`),
  KEY `FK_ORDER_SHIPMENT_2_ORDER_ADDRESS` (`SHIPPINGADDRESS_ID`),
  KEY `FK_ORDER_SHIPMENT_2_SALES_ORDER` (`ORDER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8 COMMENT='订单物流'



t_ecommerce_order_shipment_ext
CREATE TABLE `t_ecommerce_order_shipment_ext` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `SHIPMENT_ID` int(11) unsigned NOT NULL COMMENT '销售订单外键',
  `WRAP_NOTE` text COMMENT '包装祝福语',
  `DELIVERYTYPE_DESC` text COMMENT '配送方式描述，例如“货到付款 邮政EMS”，“款到发货 圆通快递”，“自提 中国,广东,广州,先烈中路自提点”等',
  `RETURN_REASON` text COMMENT '退货原因',
  `SHIPMENT_MESSAGE` text COMMENT '快递信息 （冗余）,JSON,json，记录纳期/物流信息。\r\n{\r\n    "shipmentInfos": {\r\n        "info": [\r\n            {\r\n                "create_date": "2016-01-17 10:57:12", \r\n                "info": "实际下线"\r\n            }, \r\n            {\r\n                "create_date": "2016-01-17 10:57:12", \r\n                "info": "实际出库"\r\n            }, \r\n            {\r\n                "create_date": "2016-01-18 10:57:12", \r\n                "info": "实际到店"\r\n            }\r\n        ]\r\n    }\r\n}',
  `MEMO` text COMMENT '备注',
  `STATUS` smallint(6) DEFAULT NULL COMMENT '单据状态',
  `VERSION` int(11) NOT NULL DEFAULT '0',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_ORDER_SHIPMENT_2_SALES_ORDER` (`SHIPMENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单物流扩展'



t_ecommerce_order_shipment_item
CREATE TABLE `t_ecommerce_order_shipment_item` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ORDERSHIPMENT_ID` int(11) unsigned NOT NULL COMMENT '发货单外键',
  `ORDERSKU_ID` int(11) unsigned NOT NULL COMMENT '销售项外键',
  `DELIVERY_QUANTITY` int(11) NOT NULL COMMENT '发货数量',
  `INCOMING_QUANTITY` int(11) DEFAULT NULL COMMENT '退货后入库数量',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_ORDER_SHIPMENT_ITEM_2_ORDER_SHIPMENT` (`ORDERSHIPMENT_ID`),
  KEY `FK_ORDER_SHIPMENT_ITEM_2_ORDER_SKU` (`ORDERSKU_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8 COMMENT='订单物流包裹'



t_ecommerce_order_shipment_message
CREATE TABLE `t_ecommerce_order_shipment_message` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `SHIPMENT_ID` int(11) unsigned NOT NULL COMMENT '销售订单外键',
  `SHIPMENT_TYPE` int(11) DEFAULT NULL COMMENT '纳期类型，0下线 1到库 2到店',
  `SHIPMENT_MESSAGE` text COMMENT '快递信息 （冗余）,JSON,json，记录纳期/物流信息。\r\n{\r\n    "shipmentInfos": {\r\n        "info": [\r\n            {\r\n                "create_date": "2016-01-17 10:57:12", \r\n                "info": "实际下线"\r\n            }, \r\n            {\r\n                "create_date": "2016-01-17 10:57:12", \r\n                "info": "实际出库"\r\n            }, \r\n            {\r\n                "create_date": "2016-01-18 10:57:12", \r\n                "info": "实际到店"\r\n            }\r\n        ]\r\n    }\r\n}',
  `SHIPMENT_TIME` datetime DEFAULT NULL COMMENT '物流时间',
  `STATE` smallint(10) DEFAULT NULL COMMENT '单据当前状态 \r\n0：在途，即货物处于运输过程中；\r\n1：揽件，货物已由快递公司揽收并且产生了第一条跟踪信息；\r\n2：疑难，货物寄送过程出了问题；\r\n3：签收，收件人已签收；\r\n4：退签，即货物由于用户拒签、超区等原因退回，而且发件人已经签收；\r\n5：派件，即快递正在进行同城派件；\r\n6：退回，货物正处于退回发件人的途中；',
  `STATUS` smallint(10) DEFAULT NULL COMMENT '查询结果状态：\r\n0：物流单暂无结果，\r\n1：查询成功，\r\n2：接口出现异常，',
  `VERSION` int(11) NOT NULL DEFAULT '0',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='物流/纳期信息'



t_ecommerce_order_sku
CREATE TABLE `t_ecommerce_order_sku` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ITEM_TYPE` smallint(6) NOT NULL COMMENT '销售项的类型           1=汽车            2=核销券            3=其他商品            ',
  `ORDER_ID` int(11) unsigned NOT NULL COMMENT '销售订单外键',
  `COMMODITY_ID` int(11) unsigned DEFAULT NULL COMMENT '商品ID',
  `PRODUCT_NAME` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `PRODUCTSKU_CODE` varchar(32) DEFAULT NULL COMMENT '货品编号',
  `DISPLAYSKU_OPTIONS` varchar(255) DEFAULT NULL COMMENT '规格字符串 用于显示SKUOPTION;            格式OPTIONNAME1:OPTIONVALUE1;OPTIONNAME2:OPTIONVALUE2            例如:COLOR:RED;SIZE:XL',
  `QUANTITY` int(11) NOT NULL COMMENT '数量',
  `PRICE` int(11) NOT NULL COMMENT '售出价格（单件）,单位：分',
  `IS_ONSALE` smallint(6) DEFAULT '0' COMMENT '是否特价产品',
  `IS_WHOLESALE` smallint(6) DEFAULT '0' COMMENT '是否批发产品',
  `TAX` int(11) DEFAULT NULL COMMENT '税费,单位：分',
  `TAX_NAME` text COMMENT '税名称',
  `SUBTOTAL` decimal(12,2) DEFAULT NULL COMMENT '销售项小计 = 单件价格X数量-单项折扣+税费            SUBTOTAL = PRICE * QUANTITY - DISCOUNT+TAX ',
  `DISCOUNT` int(11) DEFAULT NULL COMMENT '单项折扣,单位：分',
  `WEIGHT` decimal(12,2) DEFAULT NULL COMMENT '重量',
  `ALLOCATED_QUANTITY` int(11) DEFAULT NULL COMMENT '已分配数量',
  `DELIVERY_QUANTITY` int(11) DEFAULT NULL COMMENT '已发货数量',
  `GROSS_WEIGHT` decimal(12,0) DEFAULT NULL,
  `VERSION` int(11) NOT NULL DEFAULT '0',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_ORDER_SKU_2_SALES_ORDER` (`ORDER_ID`),
  KEY `FK_T_ECOMMERCE_ORDER_SKU_T_ECOMMERCE_COMMODITY_1` (`COMMODITY_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=156 DEFAULT CHARSET=utf8 COMMENT='订单商品'



t_ecommerce_paymentgateway
CREATE TABLE `t_ecommerce_paymentgateway` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `PAYMENTGATEWAY_NAME` varchar(256) NOT NULL COMMENT '支付网关名',
  `PAYMENTGATEWAY_DETAIL` varchar(1024) DEFAULT NULL COMMENT '支付网关描述',
  `GATEWAY_ICON` varchar(255) DEFAULT NULL COMMENT '支付网关icon',
  `PAYMENTGATEWAY_CODE` varchar(32) NOT NULL COMMENT '支付网关code',
  `PAYMENTGATEWAY_TYPE` smallint(6) DEFAULT '0' COMMENT '0:PC支付，1:MOBILE支付',
  `VERSION` int(11) NOT NULL DEFAULT '0' COMMENT '版本',
  `SORT_ORDER` int(11) DEFAULT '0' COMMENT '排序',
  `IS_SHOW` tinyint(4) DEFAULT NULL COMMENT '是否显示',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `AK_PAYMENTGATEWAYCODE` (`PAYMENTGATEWAY_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='支付网关'



t_ecommerce_paymentgateway_property
CREATE TABLE `t_ecommerce_paymentgateway_property` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `PAYMENTGATEWAY_ID` int(11) unsigned DEFAULT NULL COMMENT '支付网关ID',
  `PROPERTY_KEY` varchar(255) DEFAULT NULL COMMENT '支付网关属性key',
  `PROPERTY_VALUE` varchar(255) DEFAULT NULL COMMENT '支付网关属性值',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_T_PAYMENT_ID` (`PAYMENTGATEWAY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='支付网关属性'



t_ecommerce_verified
CREATE TABLE `t_ecommerce_verified` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '核销编号',
  `ORDERSKU_ID` int(11) unsigned DEFAULT NULL COMMENT '订单编号',
  `DEALER_ID` int(11) unsigned DEFAULT NULL COMMENT '经销商编号',
  `VERI_CODE` varchar(128) DEFAULT NULL COMMENT '核销劵号',
  `VERI_DATE` datetime DEFAULT NULL COMMENT '核销日期',
  `VERI_NUMBER` varchar(255) DEFAULT NULL COMMENT '核销码',
  `VERI_LOGS` varchar(5000) DEFAULT NULL COMMENT '核销日志表，json格式，时间：备注',
  `IS_ENABLE` int(2) NOT NULL DEFAULT '1' COMMENT '是否可用。0，不可用 ; 1，可用',
  `CREATOR` varchar(50) NOT NULL DEFAULT '' COMMENT '创建人',
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `MODIFIER` varchar(50) NOT NULL DEFAULT '' COMMENT '更新人',
  `UPDATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`ID`),
  KEY `FK_核销记录_ORDER_SKU_1` (`ORDERSKU_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='订单核销'



