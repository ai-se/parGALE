from z3 import *
from consts import  METRICS_MAXIMIZE, METRICS_MINIMIZE

FeatureIndexMap = {}
FeatureVariable = []
FeatureIndexMap['eShop'] = 0
eShop = Bool('eShop')
FeatureVariable.append(eShop) 
FeatureIndexMap['eShop'] = 1
eShop = Bool('eShop')
FeatureVariable.append(eShop) 
FeatureIndexMap['store_front'] = 2
store_front = Bool('store_front')
FeatureVariable.append(store_front) 
FeatureIndexMap['homepage'] = 3
homepage = Bool('homepage')
FeatureVariable.append(homepage) 
FeatureIndexMap['_id_1'] = 4
_id_1 = Bool('_id_1')
FeatureVariable.append(_id_1) 
FeatureIndexMap['_id_2'] = 5
_id_2 = Bool('_id_2')
FeatureVariable.append(_id_2) 
FeatureIndexMap['_id_3'] = 6
_id_3 = Bool('_id_3')
FeatureVariable.append(_id_3) 
FeatureIndexMap['_id_5'] = 7
_id_5 = Bool('_id_5')
FeatureVariable.append(_id_5) 
FeatureIndexMap['special_offers'] = 8
special_offers = Bool('special_offers')
FeatureVariable.append(special_offers) 
FeatureIndexMap['_id_6'] = 9
_id_6 = Bool('_id_6')
FeatureVariable.append(_id_6) 
FeatureIndexMap['_id_8'] = 10
_id_8 = Bool('_id_8')
FeatureVariable.append(_id_8) 
FeatureIndexMap['_id_9'] = 11
_id_9 = Bool('_id_9')
FeatureVariable.append(_id_9) 
FeatureIndexMap['registration'] = 12
registration = Bool('registration')
FeatureVariable.append(registration) 
FeatureIndexMap['registration_enforcement'] = 13
registration_enforcement = Bool('registration_enforcement')
FeatureVariable.append(registration_enforcement) 
FeatureIndexMap['_id_11'] = 14
_id_11 = Bool('_id_11')
FeatureVariable.append(_id_11) 
FeatureIndexMap['register_to_buy'] = 15
register_to_buy = Bool('register_to_buy')
FeatureVariable.append(register_to_buy) 
FeatureIndexMap['_id_12'] = 16
_id_12 = Bool('_id_12')
FeatureVariable.append(_id_12) 
FeatureIndexMap['_id_13'] = 17
_id_13 = Bool('_id_13')
FeatureVariable.append(_id_13) 
FeatureIndexMap['_id_14'] = 18
_id_14 = Bool('_id_14')
FeatureVariable.append(_id_14) 
FeatureIndexMap['shipping_address'] = 19
shipping_address = Bool('shipping_address')
FeatureVariable.append(shipping_address) 
FeatureIndexMap['_id_15'] = 20
_id_15 = Bool('_id_15')
FeatureVariable.append(_id_15) 
FeatureIndexMap['_id_16'] = 21
_id_16 = Bool('_id_16')
FeatureVariable.append(_id_16) 
FeatureIndexMap['_id_17'] = 22
_id_17 = Bool('_id_17')
FeatureVariable.append(_id_17) 
FeatureIndexMap['_id_18'] = 23
_id_18 = Bool('_id_18')
FeatureVariable.append(_id_18) 
FeatureIndexMap['_id_19'] = 24
_id_19 = Bool('_id_19')
FeatureVariable.append(_id_19) 
FeatureIndexMap['_id_20'] = 25
_id_20 = Bool('_id_20')
FeatureVariable.append(_id_20) 
FeatureIndexMap['_id_21'] = 26
_id_21 = Bool('_id_21')
FeatureVariable.append(_id_21) 
FeatureIndexMap['_id_22'] = 27
_id_22 = Bool('_id_22')
FeatureVariable.append(_id_22) 
FeatureIndexMap['_id_23'] = 28
_id_23 = Bool('_id_23')
FeatureVariable.append(_id_23) 
FeatureIndexMap['_id_25'] = 29
_id_25 = Bool('_id_25')
FeatureVariable.append(_id_25) 
FeatureIndexMap['_id_26'] = 30
_id_26 = Bool('_id_26')
FeatureVariable.append(_id_26) 
FeatureIndexMap['_id_27'] = 31
_id_27 = Bool('_id_27')
FeatureVariable.append(_id_27) 
FeatureIndexMap['_id_28'] = 32
_id_28 = Bool('_id_28')
FeatureVariable.append(_id_28) 
FeatureIndexMap['_id_29'] = 33
_id_29 = Bool('_id_29')
FeatureVariable.append(_id_29) 
FeatureIndexMap['preferences'] = 34
preferences = Bool('preferences')
FeatureVariable.append(preferences) 
FeatureIndexMap['_id_31'] = 35
_id_31 = Bool('_id_31')
FeatureVariable.append(_id_31) 
FeatureIndexMap['_id_32'] = 36
_id_32 = Bool('_id_32')
FeatureVariable.append(_id_32) 
FeatureIndexMap['_id_33'] = 37
_id_33 = Bool('_id_33')
FeatureVariable.append(_id_33) 
FeatureIndexMap['_id_34'] = 38
_id_34 = Bool('_id_34')
FeatureVariable.append(_id_34) 
FeatureIndexMap['quick_checkout_profile'] = 39
quick_checkout_profile = Bool('quick_checkout_profile')
FeatureVariable.append(quick_checkout_profile) 
FeatureIndexMap['_id_35'] = 40
_id_35 = Bool('_id_35')
FeatureVariable.append(_id_35) 
FeatureIndexMap['user_behaviour_tracking_info'] = 41
user_behaviour_tracking_info = Bool('user_behaviour_tracking_info')
FeatureVariable.append(user_behaviour_tracking_info) 
FeatureIndexMap['catalog'] = 42
catalog = Bool('catalog')
FeatureVariable.append(catalog) 
FeatureIndexMap['product_information'] = 43
product_information = Bool('product_information')
FeatureVariable.append(product_information) 
FeatureIndexMap['product_type'] = 44
product_type = Bool('product_type')
FeatureVariable.append(product_type) 
FeatureIndexMap['eletronic_goods'] = 45
eletronic_goods = Bool('eletronic_goods')
FeatureVariable.append(eletronic_goods) 
FeatureIndexMap['physical_goods'] = 46
physical_goods = Bool('physical_goods')
FeatureVariable.append(physical_goods) 
FeatureIndexMap['services'] = 47
services = Bool('services')
FeatureVariable.append(services) 
FeatureIndexMap['basic_information'] = 48
basic_information = Bool('basic_information')
FeatureVariable.append(basic_information) 
FeatureIndexMap['detailed_information'] = 49
detailed_information = Bool('detailed_information')
FeatureVariable.append(detailed_information) 
FeatureIndexMap['warranty_information'] = 50
warranty_information = Bool('warranty_information')
FeatureVariable.append(warranty_information) 
FeatureIndexMap['customer_reviews'] = 51
customer_reviews = Bool('customer_reviews')
FeatureVariable.append(customer_reviews) 
FeatureIndexMap['associated_assets'] = 52
associated_assets = Bool('associated_assets')
FeatureVariable.append(associated_assets) 
FeatureIndexMap['_id_38'] = 53
_id_38 = Bool('_id_38')
FeatureVariable.append(_id_38) 
FeatureIndexMap['_id_39'] = 54
_id_39 = Bool('_id_39')
FeatureVariable.append(_id_39) 
FeatureIndexMap['_id_41'] = 55
_id_41 = Bool('_id_41')
FeatureVariable.append(_id_41) 
FeatureIndexMap['_id_43'] = 56
_id_43 = Bool('_id_43')
FeatureVariable.append(_id_43) 
FeatureIndexMap['_id_44'] = 57
_id_44 = Bool('_id_44')
FeatureVariable.append(_id_44) 
FeatureIndexMap['_id_45'] = 58
_id_45 = Bool('_id_45')
FeatureVariable.append(_id_45) 
FeatureIndexMap['_id_46'] = 59
_id_46 = Bool('_id_46')
FeatureVariable.append(_id_46) 
FeatureIndexMap['_id_47'] = 60
_id_47 = Bool('_id_47')
FeatureVariable.append(_id_47) 
FeatureIndexMap['_id_48'] = 61
_id_48 = Bool('_id_48')
FeatureVariable.append(_id_48) 
FeatureIndexMap['_id_49'] = 62
_id_49 = Bool('_id_49')
FeatureVariable.append(_id_49) 
FeatureIndexMap['_id_50'] = 63
_id_50 = Bool('_id_50')
FeatureVariable.append(_id_50) 
FeatureIndexMap['product_variants'] = 64
product_variants = Bool('product_variants')
FeatureVariable.append(product_variants) 
FeatureIndexMap['_id_51'] = 65
_id_51 = Bool('_id_51')
FeatureVariable.append(_id_51) 
FeatureIndexMap['size'] = 66
size = Bool('size')
FeatureVariable.append(size) 
FeatureIndexMap['weight'] = 67
weight = Bool('weight')
FeatureVariable.append(weight) 
FeatureIndexMap['availability'] = 68
availability = Bool('availability')
FeatureVariable.append(availability) 
FeatureIndexMap['custom_fields'] = 69
custom_fields = Bool('custom_fields')
FeatureVariable.append(custom_fields) 
FeatureIndexMap['categories'] = 70
categories = Bool('categories')
FeatureVariable.append(categories) 
FeatureIndexMap['categories_catalog'] = 71
categories_catalog = Bool('categories_catalog')
FeatureVariable.append(categories_catalog) 
FeatureIndexMap['_id_52'] = 72
_id_52 = Bool('_id_52')
FeatureVariable.append(_id_52) 
FeatureIndexMap['_id_53'] = 73
_id_53 = Bool('_id_53')
FeatureVariable.append(_id_53) 
FeatureIndexMap['_id_54'] = 74
_id_54 = Bool('_id_54')
FeatureVariable.append(_id_54) 
FeatureIndexMap['_id_55'] = 75
_id_55 = Bool('_id_55')
FeatureVariable.append(_id_55) 
FeatureIndexMap['_id_56'] = 76
_id_56 = Bool('_id_56')
FeatureVariable.append(_id_56) 
FeatureIndexMap['_id_58'] = 77
_id_58 = Bool('_id_58')
FeatureVariable.append(_id_58) 
FeatureIndexMap['_id_59'] = 78
_id_59 = Bool('_id_59')
FeatureVariable.append(_id_59) 
FeatureIndexMap['_id_60'] = 79
_id_60 = Bool('_id_60')
FeatureVariable.append(_id_60) 
FeatureIndexMap['_id_61'] = 80
_id_61 = Bool('_id_61')
FeatureVariable.append(_id_61) 
FeatureIndexMap['category_page'] = 81
category_page = Bool('category_page')
FeatureVariable.append(category_page) 
FeatureIndexMap['_id_62'] = 82
_id_62 = Bool('_id_62')
FeatureVariable.append(_id_62) 
FeatureIndexMap['_id_63'] = 83
_id_63 = Bool('_id_63')
FeatureVariable.append(_id_63) 
FeatureIndexMap['_id_65'] = 84
_id_65 = Bool('_id_65')
FeatureVariable.append(_id_65) 
FeatureIndexMap['_id_66'] = 85
_id_66 = Bool('_id_66')
FeatureVariable.append(_id_66) 
FeatureIndexMap['_id_67'] = 86
_id_67 = Bool('_id_67')
FeatureVariable.append(_id_67) 
FeatureIndexMap['_id_68'] = 87
_id_68 = Bool('_id_68')
FeatureVariable.append(_id_68) 
FeatureIndexMap['_id_69'] = 88
_id_69 = Bool('_id_69')
FeatureVariable.append(_id_69) 
FeatureIndexMap['_id_70'] = 89
_id_70 = Bool('_id_70')
FeatureVariable.append(_id_70) 
FeatureIndexMap['_id_71'] = 90
_id_71 = Bool('_id_71')
FeatureVariable.append(_id_71) 
FeatureIndexMap['_id_72'] = 91
_id_72 = Bool('_id_72')
FeatureVariable.append(_id_72) 
FeatureIndexMap['wish_list'] = 92
wish_list = Bool('wish_list')
FeatureVariable.append(wish_list) 
FeatureIndexMap['wish_list_saved_after_session'] = 93
wish_list_saved_after_session = Bool('wish_list_saved_after_session')
FeatureVariable.append(wish_list_saved_after_session) 
FeatureIndexMap['email_wish_list'] = 94
email_wish_list = Bool('email_wish_list')
FeatureVariable.append(email_wish_list) 
FeatureIndexMap['_id_73'] = 95
_id_73 = Bool('_id_73')
FeatureVariable.append(_id_73) 
FeatureIndexMap['permissions'] = 96
permissions = Bool('permissions')
FeatureVariable.append(permissions) 
FeatureIndexMap['_id_75'] = 97
_id_75 = Bool('_id_75')
FeatureVariable.append(_id_75) 
FeatureIndexMap['_id_76'] = 98
_id_76 = Bool('_id_76')
FeatureVariable.append(_id_76) 
FeatureIndexMap['_id_77'] = 99
_id_77 = Bool('_id_77')
FeatureVariable.append(_id_77) 
FeatureIndexMap['buy_paths'] = 100
buy_paths = Bool('buy_paths')
FeatureVariable.append(buy_paths) 
FeatureIndexMap['_id_78'] = 101
_id_78 = Bool('_id_78')
FeatureVariable.append(_id_78) 
FeatureIndexMap['_id_79'] = 102
_id_79 = Bool('_id_79')
FeatureVariable.append(_id_79) 
FeatureIndexMap['_id_80'] = 103
_id_80 = Bool('_id_80')
FeatureVariable.append(_id_80) 
FeatureIndexMap['_id_81'] = 104
_id_81 = Bool('_id_81')
FeatureVariable.append(_id_81) 
FeatureIndexMap['_id_82'] = 105
_id_82 = Bool('_id_82')
FeatureVariable.append(_id_82) 
FeatureIndexMap['_id_83'] = 106
_id_83 = Bool('_id_83')
FeatureVariable.append(_id_83) 
FeatureIndexMap['_id_84'] = 107
_id_84 = Bool('_id_84')
FeatureVariable.append(_id_84) 
FeatureIndexMap['registered_checkout'] = 108
registered_checkout = Bool('registered_checkout')
FeatureVariable.append(registered_checkout) 
FeatureIndexMap['quick_checkout'] = 109
quick_checkout = Bool('quick_checkout')
FeatureVariable.append(quick_checkout) 
FeatureIndexMap['_id_86'] = 110
_id_86 = Bool('_id_86')
FeatureVariable.append(_id_86) 
FeatureIndexMap['_id_87'] = 111
_id_87 = Bool('_id_87')
FeatureVariable.append(_id_87) 
FeatureIndexMap['shipping_options'] = 112
shipping_options = Bool('shipping_options')
FeatureVariable.append(shipping_options) 
FeatureIndexMap['_id_88'] = 113
_id_88 = Bool('_id_88')
FeatureVariable.append(_id_88) 
FeatureIndexMap['_id_89'] = 114
_id_89 = Bool('_id_89')
FeatureVariable.append(_id_89) 
FeatureIndexMap['_id_90'] = 115
_id_90 = Bool('_id_90')
FeatureVariable.append(_id_90) 
FeatureIndexMap['_id_91'] = 116
_id_91 = Bool('_id_91')
FeatureVariable.append(_id_91) 
FeatureIndexMap['_id_92'] = 117
_id_92 = Bool('_id_92')
FeatureVariable.append(_id_92) 
FeatureIndexMap['_id_93'] = 118
_id_93 = Bool('_id_93')
FeatureVariable.append(_id_93) 
FeatureIndexMap['_id_95'] = 119
_id_95 = Bool('_id_95')
FeatureVariable.append(_id_95) 
FeatureIndexMap['_id_96'] = 120
_id_96 = Bool('_id_96')
FeatureVariable.append(_id_96) 
FeatureIndexMap['_id_98'] = 121
_id_98 = Bool('_id_98')
FeatureVariable.append(_id_98) 
FeatureIndexMap['_id_99'] = 122
_id_99 = Bool('_id_99')
FeatureVariable.append(_id_99) 
FeatureIndexMap['_id_100'] = 123
_id_100 = Bool('_id_100')
FeatureVariable.append(_id_100) 
FeatureIndexMap['_id_101'] = 124
_id_101 = Bool('_id_101')
FeatureVariable.append(_id_101) 
FeatureIndexMap['shipping_2'] = 125
shipping_2 = Bool('shipping_2')
FeatureVariable.append(shipping_2) 
FeatureIndexMap['_id_102'] = 126
_id_102 = Bool('_id_102')
FeatureVariable.append(_id_102) 
FeatureIndexMap['_id_103'] = 127
_id_103 = Bool('_id_103')
FeatureVariable.append(_id_103) 
FeatureIndexMap['_id_105'] = 128
_id_105 = Bool('_id_105')
FeatureVariable.append(_id_105) 
FeatureIndexMap['_id_106'] = 129
_id_106 = Bool('_id_106')
FeatureVariable.append(_id_106) 
FeatureIndexMap['_id_107'] = 130
_id_107 = Bool('_id_107')
FeatureVariable.append(_id_107) 
FeatureIndexMap['_id_108'] = 131
_id_108 = Bool('_id_108')
FeatureVariable.append(_id_108) 
FeatureIndexMap['_id_110'] = 132
_id_110 = Bool('_id_110')
FeatureVariable.append(_id_110) 
FeatureIndexMap['_id_111'] = 133
_id_111 = Bool('_id_111')
FeatureVariable.append(_id_111) 
FeatureIndexMap['_id_112'] = 134
_id_112 = Bool('_id_112')
FeatureVariable.append(_id_112) 
FeatureIndexMap['_id_114'] = 135
_id_114 = Bool('_id_114')
FeatureVariable.append(_id_114) 
FeatureIndexMap['_id_115'] = 136
_id_115 = Bool('_id_115')
FeatureVariable.append(_id_115) 
FeatureIndexMap['_id_116'] = 137
_id_116 = Bool('_id_116')
FeatureVariable.append(_id_116) 
FeatureIndexMap['_id_117'] = 138
_id_117 = Bool('_id_117')
FeatureVariable.append(_id_117) 
FeatureIndexMap['_id_118'] = 139
_id_118 = Bool('_id_118')
FeatureVariable.append(_id_118) 
FeatureIndexMap['_id_120'] = 140
_id_120 = Bool('_id_120')
FeatureVariable.append(_id_120) 
FeatureIndexMap['_id_121'] = 141
_id_121 = Bool('_id_121')
FeatureVariable.append(_id_121) 
FeatureIndexMap['_id_122'] = 142
_id_122 = Bool('_id_122')
FeatureVariable.append(_id_122) 
FeatureIndexMap['_id_123'] = 143
_id_123 = Bool('_id_123')
FeatureVariable.append(_id_123) 
FeatureIndexMap['_id_124'] = 144
_id_124 = Bool('_id_124')
FeatureVariable.append(_id_124) 
FeatureIndexMap['_id_125'] = 145
_id_125 = Bool('_id_125')
FeatureVariable.append(_id_125) 
FeatureIndexMap['_id_126'] = 146
_id_126 = Bool('_id_126')
FeatureVariable.append(_id_126) 
FeatureIndexMap['_id_127'] = 147
_id_127 = Bool('_id_127')
FeatureVariable.append(_id_127) 
FeatureIndexMap['_id_128'] = 148
_id_128 = Bool('_id_128')
FeatureVariable.append(_id_128) 
FeatureIndexMap['_id_129'] = 149
_id_129 = Bool('_id_129')
FeatureVariable.append(_id_129) 
FeatureIndexMap['_id_130'] = 150
_id_130 = Bool('_id_130')
FeatureVariable.append(_id_130) 
FeatureIndexMap['_id_132'] = 151
_id_132 = Bool('_id_132')
FeatureVariable.append(_id_132) 
FeatureIndexMap['_id_133'] = 152
_id_133 = Bool('_id_133')
FeatureVariable.append(_id_133) 
FeatureIndexMap['_id_134'] = 153
_id_134 = Bool('_id_134')
FeatureVariable.append(_id_134) 
FeatureIndexMap['_id_135'] = 154
_id_135 = Bool('_id_135')
FeatureVariable.append(_id_135) 
FeatureIndexMap['_id_136'] = 155
_id_136 = Bool('_id_136')
FeatureVariable.append(_id_136) 
FeatureIndexMap['_id_137'] = 156
_id_137 = Bool('_id_137')
FeatureVariable.append(_id_137) 
FeatureIndexMap['_id_138'] = 157
_id_138 = Bool('_id_138')
FeatureVariable.append(_id_138) 
FeatureIndexMap['_id_139'] = 158
_id_139 = Bool('_id_139')
FeatureVariable.append(_id_139) 
FeatureIndexMap['_id_141'] = 159
_id_141 = Bool('_id_141')
FeatureVariable.append(_id_141) 
FeatureIndexMap['_id_142'] = 160
_id_142 = Bool('_id_142')
FeatureVariable.append(_id_142) 
FeatureIndexMap['_id_143'] = 161
_id_143 = Bool('_id_143')
FeatureVariable.append(_id_143) 
FeatureIndexMap['_id_144'] = 162
_id_144 = Bool('_id_144')
FeatureVariable.append(_id_144) 
FeatureIndexMap['buy_paths_288_289'] = 163
buy_paths_288_289 = Bool('buy_paths_288_289')
FeatureVariable.append(buy_paths_288_289) 
FeatureIndexMap['buy_paths_288_289_290'] = 164
buy_paths_288_289_290 = Bool('buy_paths_288_289_290')
FeatureVariable.append(buy_paths_288_289_290) 
FeatureIndexMap['buy_paths_288_289_291'] = 165
buy_paths_288_289_291 = Bool('buy_paths_288_289_291')
FeatureVariable.append(buy_paths_288_289_291) 
FeatureIndexMap['customer_service'] = 166
customer_service = Bool('customer_service')
FeatureVariable.append(customer_service) 
FeatureIndexMap['_id_146'] = 167
_id_146 = Bool('_id_146')
FeatureVariable.append(_id_146) 
FeatureIndexMap['_id_147'] = 168
_id_147 = Bool('_id_147')
FeatureVariable.append(_id_147) 
FeatureIndexMap['_id_148'] = 169
_id_148 = Bool('_id_148')
FeatureVariable.append(_id_148) 
FeatureIndexMap['_id_149'] = 170
_id_149 = Bool('_id_149')
FeatureVariable.append(_id_149) 
FeatureIndexMap['_id_150'] = 171
_id_150 = Bool('_id_150')
FeatureVariable.append(_id_150) 
FeatureIndexMap['_id_152'] = 172
_id_152 = Bool('_id_152')
FeatureVariable.append(_id_152) 
FeatureIndexMap['_id_153'] = 173
_id_153 = Bool('_id_153')
FeatureVariable.append(_id_153) 
FeatureIndexMap['_id_154'] = 174
_id_154 = Bool('_id_154')
FeatureVariable.append(_id_154) 
FeatureIndexMap['_id_155'] = 175
_id_155 = Bool('_id_155')
FeatureVariable.append(_id_155) 
FeatureIndexMap['_id_156'] = 176
_id_156 = Bool('_id_156')
FeatureVariable.append(_id_156) 
FeatureIndexMap['_id_158'] = 177
_id_158 = Bool('_id_158')
FeatureVariable.append(_id_158) 
FeatureIndexMap['_id_159'] = 178
_id_159 = Bool('_id_159')
FeatureVariable.append(_id_159) 
FeatureIndexMap['user_behaviour_tracking'] = 179
user_behaviour_tracking = Bool('user_behaviour_tracking')
FeatureVariable.append(user_behaviour_tracking) 
FeatureIndexMap['_id_160'] = 180
_id_160 = Bool('_id_160')
FeatureVariable.append(_id_160) 
FeatureIndexMap['locally_visited_pages'] = 181
locally_visited_pages = Bool('locally_visited_pages')
FeatureVariable.append(locally_visited_pages) 
FeatureIndexMap['external_referring_pages'] = 182
external_referring_pages = Bool('external_referring_pages')
FeatureVariable.append(external_referring_pages) 
FeatureIndexMap['behaviour_tracked_previous_purchases'] = 183
behaviour_tracked_previous_purchases = Bool('behaviour_tracked_previous_purchases')
FeatureVariable.append(behaviour_tracked_previous_purchases) 
FeatureIndexMap['business_management'] = 184
business_management = Bool('business_management')
FeatureVariable.append(business_management) 
FeatureIndexMap['_id_162'] = 185
_id_162 = Bool('_id_162')
FeatureVariable.append(_id_162) 
FeatureIndexMap['_id_163'] = 186
_id_163 = Bool('_id_163')
FeatureVariable.append(_id_163) 
FeatureIndexMap['physical_goods_fulfillment'] = 187
physical_goods_fulfillment = Bool('physical_goods_fulfillment')
FeatureVariable.append(physical_goods_fulfillment) 
FeatureIndexMap['warehouse_management'] = 188
warehouse_management = Bool('warehouse_management')
FeatureVariable.append(warehouse_management) 
FeatureIndexMap['shipping'] = 189
shipping = Bool('shipping')
FeatureVariable.append(shipping) 
FeatureIndexMap['_id_166'] = 190
_id_166 = Bool('_id_166')
FeatureVariable.append(_id_166) 
FeatureIndexMap['_id_167'] = 191
_id_167 = Bool('_id_167')
FeatureVariable.append(_id_167) 
FeatureIndexMap['_id_168'] = 192
_id_168 = Bool('_id_168')
FeatureVariable.append(_id_168) 
FeatureIndexMap['_id_169'] = 193
_id_169 = Bool('_id_169')
FeatureVariable.append(_id_169) 
FeatureIndexMap['_id_171'] = 194
_id_171 = Bool('_id_171')
FeatureVariable.append(_id_171) 
FeatureIndexMap['_id_172'] = 195
_id_172 = Bool('_id_172')
FeatureVariable.append(_id_172) 
FeatureIndexMap['_id_173'] = 196
_id_173 = Bool('_id_173')
FeatureVariable.append(_id_173) 
FeatureIndexMap['_id_174'] = 197
_id_174 = Bool('_id_174')
FeatureVariable.append(_id_174) 
FeatureIndexMap['_id_175'] = 198
_id_175 = Bool('_id_175')
FeatureVariable.append(_id_175) 
FeatureIndexMap['_id_177'] = 199
_id_177 = Bool('_id_177')
FeatureVariable.append(_id_177) 
FeatureIndexMap['_id_178'] = 200
_id_178 = Bool('_id_178')
FeatureVariable.append(_id_178) 
FeatureIndexMap['_id_179'] = 201
_id_179 = Bool('_id_179')
FeatureVariable.append(_id_179) 
FeatureIndexMap['_id_180'] = 202
_id_180 = Bool('_id_180')
FeatureVariable.append(_id_180) 
FeatureIndexMap['_id_181'] = 203
_id_181 = Bool('_id_181')
FeatureVariable.append(_id_181) 
FeatureIndexMap['eletronic_goods_fulfillment'] = 204
eletronic_goods_fulfillment = Bool('eletronic_goods_fulfillment')
FeatureVariable.append(eletronic_goods_fulfillment) 
FeatureIndexMap['_id_182'] = 205
_id_182 = Bool('_id_182')
FeatureVariable.append(_id_182) 
FeatureIndexMap['_id_183'] = 206
_id_183 = Bool('_id_183')
FeatureVariable.append(_id_183) 
FeatureIndexMap['services_fulfillment'] = 207
services_fulfillment = Bool('services_fulfillment')
FeatureVariable.append(services_fulfillment) 
FeatureIndexMap['_id_184'] = 208
_id_184 = Bool('_id_184')
FeatureVariable.append(_id_184) 
FeatureIndexMap['_id_185'] = 209
_id_185 = Bool('_id_185')
FeatureVariable.append(_id_185) 
FeatureIndexMap['_id_186'] = 210
_id_186 = Bool('_id_186')
FeatureVariable.append(_id_186) 
FeatureIndexMap['_id_187'] = 211
_id_187 = Bool('_id_187')
FeatureVariable.append(_id_187) 
FeatureIndexMap['customer_preferences'] = 212
customer_preferences = Bool('customer_preferences')
FeatureVariable.append(customer_preferences) 
FeatureIndexMap['_id_189'] = 213
_id_189 = Bool('_id_189')
FeatureVariable.append(_id_189) 
FeatureIndexMap['_id_190'] = 214
_id_190 = Bool('_id_190')
FeatureVariable.append(_id_190) 
FeatureIndexMap['targeting_criteria_previous_purchases'] = 215
targeting_criteria_previous_purchases = Bool('targeting_criteria_previous_purchases')
FeatureVariable.append(targeting_criteria_previous_purchases) 
FeatureIndexMap['_id_191'] = 216
_id_191 = Bool('_id_191')
FeatureVariable.append(_id_191) 
FeatureIndexMap['wish_list_content'] = 217
wish_list_content = Bool('wish_list_content')
FeatureVariable.append(wish_list_content) 
FeatureIndexMap['previously_visited_pages'] = 218
previously_visited_pages = Bool('previously_visited_pages')
FeatureVariable.append(previously_visited_pages) 
FeatureIndexMap['_id_192'] = 219
_id_192 = Bool('_id_192')
FeatureVariable.append(_id_192) 
FeatureIndexMap['_id_193'] = 220
_id_193 = Bool('_id_193')
FeatureVariable.append(_id_193) 
FeatureIndexMap['_id_194'] = 221
_id_194 = Bool('_id_194')
FeatureVariable.append(_id_194) 
FeatureIndexMap['_id_196'] = 222
_id_196 = Bool('_id_196')
FeatureVariable.append(_id_196) 
FeatureIndexMap['_id_197'] = 223
_id_197 = Bool('_id_197')
FeatureVariable.append(_id_197) 
FeatureIndexMap['_id_199'] = 224
_id_199 = Bool('_id_199')
FeatureVariable.append(_id_199) 
FeatureIndexMap['_id_200'] = 225
_id_200 = Bool('_id_200')
FeatureVariable.append(_id_200) 
FeatureIndexMap['_id_201'] = 226
_id_201 = Bool('_id_201')
FeatureVariable.append(_id_201) 
FeatureIndexMap['_id_203'] = 227
_id_203 = Bool('_id_203')
FeatureVariable.append(_id_203) 
FeatureIndexMap['_id_204'] = 228
_id_204 = Bool('_id_204')
FeatureVariable.append(_id_204) 
FeatureIndexMap['_id_205'] = 229
_id_205 = Bool('_id_205')
FeatureVariable.append(_id_205) 
FeatureIndexMap['_id_206'] = 230
_id_206 = Bool('_id_206')
FeatureVariable.append(_id_206) 
FeatureIndexMap['_id_207'] = 231
_id_207 = Bool('_id_207')
FeatureVariable.append(_id_207) 
FeatureIndexMap['discounts'] = 232
discounts = Bool('discounts')
FeatureVariable.append(discounts) 
FeatureIndexMap['_id_208'] = 233
_id_208 = Bool('_id_208')
FeatureVariable.append(_id_208) 
FeatureIndexMap['_id_209'] = 234
_id_209 = Bool('_id_209')
FeatureVariable.append(_id_209) 
FeatureIndexMap['_id_210'] = 235
_id_210 = Bool('_id_210')
FeatureVariable.append(_id_210) 
FeatureIndexMap['_id_211'] = 236
_id_211 = Bool('_id_211')
FeatureVariable.append(_id_211) 
FeatureIndexMap['_id_212'] = 237
_id_212 = Bool('_id_212')
FeatureVariable.append(_id_212) 
FeatureIndexMap['_id_214'] = 238
_id_214 = Bool('_id_214')
FeatureVariable.append(_id_214) 
FeatureIndexMap['_id_215'] = 239
_id_215 = Bool('_id_215')
FeatureVariable.append(_id_215) 
FeatureIndexMap['_id_216'] = 240
_id_216 = Bool('_id_216')
FeatureVariable.append(_id_216) 
FeatureIndexMap['_id_217'] = 241
_id_217 = Bool('_id_217')
FeatureVariable.append(_id_217) 
FeatureIndexMap['_id_218'] = 242
_id_218 = Bool('_id_218')
FeatureVariable.append(_id_218) 
FeatureIndexMap['_id_219'] = 243
_id_219 = Bool('_id_219')
FeatureVariable.append(_id_219) 
FeatureIndexMap['_id_220'] = 244
_id_220 = Bool('_id_220')
FeatureVariable.append(_id_220) 
FeatureIndexMap['_id_222'] = 245
_id_222 = Bool('_id_222')
FeatureVariable.append(_id_222) 
FeatureIndexMap['_id_223'] = 246
_id_223 = Bool('_id_223')
FeatureVariable.append(_id_223) 
FeatureIndexMap['_id_224'] = 247
_id_224 = Bool('_id_224')
FeatureVariable.append(_id_224) 
FeatureIndexMap['_id_225'] = 248
_id_225 = Bool('_id_225')
FeatureVariable.append(_id_225) 
FeatureIndexMap['_id_226'] = 249
_id_226 = Bool('_id_226')
FeatureVariable.append(_id_226) 
FeatureIndexMap['_id_228'] = 250
_id_228 = Bool('_id_228')
FeatureVariable.append(_id_228) 
FeatureIndexMap['_id_229'] = 251
_id_229 = Bool('_id_229')
FeatureVariable.append(_id_229) 
FeatureIndexMap['_id_230'] = 252
_id_230 = Bool('_id_230')
FeatureVariable.append(_id_230) 
FeatureIndexMap['_id_231'] = 253
_id_231 = Bool('_id_231')
FeatureVariable.append(_id_231) 
FeatureIndexMap['_id_232'] = 254
_id_232 = Bool('_id_232')
FeatureVariable.append(_id_232) 
FeatureIndexMap['_id_233'] = 255
_id_233 = Bool('_id_233')
FeatureVariable.append(_id_233) 
FeatureIndexMap['_id_235'] = 256
_id_235 = Bool('_id_235')
FeatureVariable.append(_id_235) 
FeatureIndexMap['_id_236'] = 257
_id_236 = Bool('_id_236')
FeatureVariable.append(_id_236) 
FeatureIndexMap['_id_237'] = 258
_id_237 = Bool('_id_237')
FeatureVariable.append(_id_237) 
FeatureIndexMap['personalized_emails'] = 259
personalized_emails = Bool('personalized_emails')
FeatureVariable.append(personalized_emails) 
FeatureIndexMap['_id_238'] = 260
_id_238 = Bool('_id_238')
FeatureVariable.append(_id_238) 
FeatureIndexMap['_id_239'] = 261
_id_239 = Bool('_id_239')
FeatureVariable.append(_id_239) 
FeatureIndexMap['_id_240'] = 262
_id_240 = Bool('_id_240')
FeatureVariable.append(_id_240) 
FeatureIndexMap['_id_241'] = 263
_id_241 = Bool('_id_241')
FeatureVariable.append(_id_241) 
FeatureIndexMap['_id_242'] = 264
_id_242 = Bool('_id_242')
FeatureVariable.append(_id_242) 
FeatureIndexMap['inventory_tracking'] = 265
inventory_tracking = Bool('inventory_tracking')
FeatureVariable.append(inventory_tracking) 
FeatureIndexMap['_id_243'] = 266
_id_243 = Bool('_id_243')
FeatureVariable.append(_id_243) 
FeatureIndexMap['procurement'] = 267
procurement = Bool('procurement')
FeatureVariable.append(procurement) 
FeatureIndexMap['_id_244'] = 268
_id_244 = Bool('_id_244')
FeatureVariable.append(_id_244) 
FeatureIndexMap['_id_245'] = 269
_id_245 = Bool('_id_245')
FeatureVariable.append(_id_245) 
FeatureIndexMap['automatic'] = 270
automatic = Bool('automatic')
FeatureVariable.append(automatic) 
FeatureIndexMap['_id_246'] = 271
_id_246 = Bool('_id_246')
FeatureVariable.append(_id_246) 
FeatureIndexMap['reporting_and_analysis'] = 272
reporting_and_analysis = Bool('reporting_and_analysis')
FeatureVariable.append(reporting_and_analysis) 
FeatureIndexMap['_id_247'] = 273
_id_247 = Bool('_id_247')
FeatureVariable.append(_id_247) 
FeatureIndexMap['_id_248'] = 274
_id_248 = Bool('_id_248')
FeatureVariable.append(_id_248) 
FeatureIndexMap['_id_249'] = 275
_id_249 = Bool('_id_249')
FeatureVariable.append(_id_249) 
FeatureIndexMap['_id_250'] = 276
_id_250 = Bool('_id_250')
FeatureVariable.append(_id_250) 
FeatureIndexMap['fulfillment_system'] = 277
fulfillment_system = Bool('fulfillment_system')
FeatureVariable.append(fulfillment_system) 
FeatureIndexMap['_id_252'] = 278
_id_252 = Bool('_id_252')
FeatureVariable.append(_id_252) 
FeatureIndexMap['procurement_system'] = 279
procurement_system = Bool('procurement_system')
FeatureVariable.append(procurement_system) 
FeatureIndexMap['_id_253'] = 280
_id_253 = Bool('_id_253')
FeatureVariable.append(_id_253) 
FeatureIndexMap['_id_254'] = 281
_id_254 = Bool('_id_254')
FeatureVariable.append(_id_254) 
FeatureIndexMap['_id_255'] = 282
_id_255 = Bool('_id_255')
FeatureVariable.append(_id_255) 
FeatureIndexMap['_id_256'] = 283
_id_256 = Bool('_id_256')
FeatureVariable.append(_id_256) 
FeatureIndexMap['_id_257'] = 284
_id_257 = Bool('_id_257')
FeatureVariable.append(_id_257) 
FeatureIndexMap['_id_258'] = 285
_id_258 = Bool('_id_258')
FeatureVariable.append(_id_258) 
FeatureIndexMap['_id_259'] = 286
_id_259 = Bool('_id_259')
FeatureVariable.append(_id_259) 
FeatureIndexMap['_id_260'] = 287
_id_260 = Bool('_id_260')
FeatureVariable.append(_id_260) 
FeatureIndexMap['_id_261'] = 288
_id_261 = Bool('_id_261')
FeatureVariable.append(_id_261) 
FeatureIndexMap['_id_262'] = 289
_id_262 = Bool('_id_262')
FeatureVariable.append(_id_262) 
FeatureIndexMap['_id_263'] = 290
_id_263 = Bool('_id_263')
FeatureVariable.append(_id_263) 
s = Solver()


#Parent-Children
s.add(Implies(store_front, eShop))
s.add(Implies(business_management, eShop))
s.add(Implies(homepage, store_front))
s.add(Implies(registration, store_front))
s.add(Implies(catalog, store_front))
s.add(Implies(wish_list, store_front))
s.add(Implies(buy_paths, store_front))
s.add(Implies(customer_service, store_front))
s.add(Implies(user_behaviour_tracking, store_front))
s.add(Implies(_id_1, homepage))
s.add(Implies(_id_2, homepage))
s.add(Implies(_id_3, _id_2))
s.add(Implies(_id_6, _id_2))
s.add(Implies(_id_5, _id_3))
s.add(Implies(special_offers, _id_3))
s.add(Implies(_id_8, _id_6))
s.add(Implies(_id_9, _id_6))
s.add(Implies(registration_enforcement, registration))
s.add(Implies(_id_13, registration))
s.add(Implies(user_behaviour_tracking_info, registration))
s.add(Implies(_id_11, registration_enforcement))
s.add(Implies(register_to_buy, registration_enforcement))
s.add(Implies(_id_12, registration_enforcement))
s.add(Implies(_id_14, _id_13))
s.add(Implies(shipping_address, _id_13))
s.add(Implies(_id_16, _id_13))
s.add(Implies(_id_18, _id_13))
s.add(Implies(_id_23, _id_13))
s.add(Implies(_id_29, _id_13))
s.add(Implies(preferences, _id_13))
s.add(Implies(_id_34, _id_13))
s.add(Implies(quick_checkout_profile, _id_13))
s.add(Implies(_id_35, _id_13))
s.add(Implies(_id_15, shipping_address))
s.add(Implies(_id_17, _id_16))
s.add(Implies(_id_19, _id_18))
s.add(Implies(_id_20, _id_18))
s.add(Implies(_id_21, _id_18))
s.add(Implies(_id_22, _id_18))
s.add(Implies(_id_25, _id_23))
s.add(Implies(_id_26, _id_23))
s.add(Implies(_id_27, _id_23))
s.add(Implies(_id_28, _id_23))
s.add(Implies(_id_31, preferences))
s.add(Implies(_id_32, preferences))
s.add(Implies(_id_33, preferences))
s.add(Implies(product_information, catalog))
s.add(Implies(categories, catalog))
s.add(Implies(_id_55, catalog))
s.add(Implies(_id_56, catalog))
s.add(Implies(_id_60, catalog))
s.add(Implies(_id_70, catalog))
s.add(Implies(product_type, product_information))
s.add(Implies(basic_information, product_information))
s.add(Implies(detailed_information, product_information))
s.add(Implies(warranty_information, product_information))
s.add(Implies(customer_reviews, product_information))
s.add(Implies(associated_assets, product_information))
s.add(Implies(product_variants, product_information))
s.add(Implies(size, product_information))
s.add(Implies(weight, product_information))
s.add(Implies(availability, product_information))
s.add(Implies(custom_fields, product_information))
s.add(Implies(eletronic_goods, product_type))
s.add(Implies(physical_goods, product_type))
s.add(Implies(services, product_type))
s.add(Implies(_id_38, associated_assets))
s.add(Implies(_id_39, associated_assets))
s.add(Implies(_id_41, _id_39))
s.add(Implies(_id_49, _id_39))
s.add(Implies(_id_50, _id_39))
s.add(Implies(_id_43, _id_41))
s.add(Implies(_id_44, _id_41))
s.add(Implies(_id_45, _id_41))
s.add(Implies(_id_46, _id_41))
s.add(Implies(_id_47, _id_41))
s.add(Implies(_id_48, _id_41))
s.add(Implies(_id_51, product_variants))
s.add(Implies(categories_catalog, categories))
s.add(Implies(_id_52, categories_catalog))
s.add(Implies(_id_53, _id_52))
s.add(Implies(_id_54, _id_52))
s.add(Implies(_id_58, _id_56))
s.add(Implies(_id_59, _id_56))
s.add(Implies(_id_61, _id_60))
s.add(Implies(category_page, _id_60))
s.add(Implies(_id_62, _id_60))
s.add(Implies(_id_63, _id_62))
s.add(Implies(_id_65, _id_63))
s.add(Implies(_id_66, _id_63))
s.add(Implies(_id_67, _id_63))
s.add(Implies(_id_68, _id_63))
s.add(Implies(_id_69, _id_63))
s.add(Implies(_id_71, _id_70))
s.add(Implies(_id_72, _id_70))
s.add(Implies(wish_list_saved_after_session, wish_list))
s.add(Implies(email_wish_list, wish_list))
s.add(Implies(_id_73, wish_list))
s.add(Implies(permissions, wish_list))
s.add(Implies(_id_75, permissions))
s.add(Implies(_id_76, permissions))
s.add(Implies(_id_77, permissions))
s.add(Implies(_id_78, buy_paths))
s.add(Implies(_id_83, buy_paths))
s.add(Implies(_id_139, buy_paths))
s.add(Implies(buy_paths_288_289, buy_paths))
s.add(Implies(_id_79, _id_78))
s.add(Implies(_id_80, _id_78))
s.add(Implies(_id_81, _id_78))
s.add(Implies(_id_82, _id_78))
s.add(Implies(_id_84, _id_83))
s.add(Implies(shipping_options, _id_83))
s.add(Implies(_id_93, _id_83))
s.add(Implies(_id_117, _id_83))
s.add(Implies(registered_checkout, _id_84))
s.add(Implies(_id_87, _id_84))
s.add(Implies(quick_checkout, registered_checkout))
s.add(Implies(_id_86, quick_checkout))
s.add(Implies(_id_88, shipping_options))
s.add(Implies(_id_89, shipping_options))
s.add(Implies(_id_90, shipping_options))
s.add(Implies(_id_91, shipping_options))
s.add(Implies(_id_92, shipping_options))
s.add(Implies(_id_95, _id_93))
s.add(Implies(_id_112, _id_93))
s.add(Implies(_id_96, _id_95))
s.add(Implies(_id_108, _id_95))
s.add(Implies(_id_98, _id_96))
s.add(Implies(_id_99, _id_96))
s.add(Implies(_id_100, _id_99))
s.add(Implies(_id_101, _id_99))
s.add(Implies(_id_103, _id_99))
s.add(Implies(shipping_2, _id_101))
s.add(Implies(_id_102, _id_101))
s.add(Implies(_id_105, _id_103))
s.add(Implies(_id_106, _id_103))
s.add(Implies(_id_107, _id_103))
s.add(Implies(_id_110, _id_108))
s.add(Implies(_id_111, _id_108))
s.add(Implies(_id_114, _id_112))
s.add(Implies(_id_115, _id_112))
s.add(Implies(_id_116, _id_112))
s.add(Implies(_id_118, _id_117))
s.add(Implies(_id_129, _id_117))
s.add(Implies(_id_130, _id_117))
s.add(Implies(_id_120, _id_118))
s.add(Implies(_id_121, _id_118))
s.add(Implies(_id_122, _id_118))
s.add(Implies(_id_123, _id_118))
s.add(Implies(_id_124, _id_118))
s.add(Implies(_id_125, _id_118))
s.add(Implies(_id_126, _id_118))
s.add(Implies(_id_127, _id_118))
s.add(Implies(_id_128, _id_118))
s.add(Implies(_id_132, _id_130))
s.add(Implies(_id_133, _id_130))
s.add(Implies(_id_134, _id_130))
s.add(Implies(_id_135, _id_130))
s.add(Implies(_id_136, _id_130))
s.add(Implies(_id_137, _id_130))
s.add(Implies(_id_138, _id_130))
s.add(Implies(_id_141, _id_139))
s.add(Implies(_id_142, _id_139))
s.add(Implies(_id_143, _id_139))
s.add(Implies(_id_144, _id_139))
s.add(Implies(buy_paths_288_289_290, buy_paths_288_289))
s.add(Implies(buy_paths_288_289_291, buy_paths_288_289))
s.add(Implies(_id_146, customer_service))
s.add(Implies(_id_148, customer_service))
s.add(Implies(_id_149, customer_service))
s.add(Implies(_id_156, customer_service))
s.add(Implies(_id_147, _id_146))
s.add(Implies(_id_150, _id_149))
s.add(Implies(_id_155, _id_149))
s.add(Implies(_id_152, _id_150))
s.add(Implies(_id_153, _id_150))
s.add(Implies(_id_154, _id_150))
s.add(Implies(_id_158, _id_156))
s.add(Implies(_id_159, _id_156))
s.add(Implies(_id_160, user_behaviour_tracking))
s.add(Implies(locally_visited_pages, _id_160))
s.add(Implies(external_referring_pages, _id_160))
s.add(Implies(behaviour_tracked_previous_purchases, _id_160))
s.add(Implies(_id_162, business_management))
s.add(Implies(_id_186, business_management))
s.add(Implies(_id_240, business_management))
s.add(Implies(inventory_tracking, business_management))
s.add(Implies(procurement, business_management))
s.add(Implies(reporting_and_analysis, business_management))
s.add(Implies(_id_250, business_management))
s.add(Implies(_id_254, business_management))
s.add(Implies(_id_163, _id_162))
s.add(Implies(physical_goods_fulfillment, _id_163))
s.add(Implies(eletronic_goods_fulfillment, _id_163))
s.add(Implies(services_fulfillment, _id_163))
s.add(Implies(warehouse_management, physical_goods_fulfillment))
s.add(Implies(shipping, physical_goods_fulfillment))
s.add(Implies(_id_166, shipping))
s.add(Implies(_id_175, shipping))
s.add(Implies(_id_167, _id_166))
s.add(Implies(_id_168, _id_167))
s.add(Implies(_id_169, _id_167))
s.add(Implies(_id_171, _id_169))
s.add(Implies(_id_172, _id_169))
s.add(Implies(_id_173, _id_169))
s.add(Implies(_id_174, _id_169))
s.add(Implies(_id_177, _id_175))
s.add(Implies(_id_178, _id_175))
s.add(Implies(_id_179, _id_175))
s.add(Implies(_id_180, _id_175))
s.add(Implies(_id_181, _id_175))
s.add(Implies(_id_182, eletronic_goods_fulfillment))
s.add(Implies(_id_183, eletronic_goods_fulfillment))
s.add(Implies(_id_184, services_fulfillment))
s.add(Implies(_id_185, services_fulfillment))
s.add(Implies(_id_187, _id_186))
s.add(Implies(_id_194, _id_186))
s.add(Implies(_id_233, _id_186))
s.add(Implies(_id_239, _id_186))
s.add(Implies(customer_preferences, _id_187))
s.add(Implies(_id_189, _id_187))
s.add(Implies(_id_190, _id_187))
s.add(Implies(targeting_criteria_previous_purchases, _id_187))
s.add(Implies(_id_191, _id_187))
s.add(Implies(wish_list_content, _id_187))
s.add(Implies(previously_visited_pages, _id_187))
s.add(Implies(_id_192, _id_187))
s.add(Implies(_id_193, _id_187))
s.add(Implies(_id_196, _id_194))
s.add(Implies(discounts, _id_194))
s.add(Implies(_id_226, _id_194))
s.add(Implies(_id_197, _id_196))
s.add(Implies(_id_201, _id_196))
s.add(Implies(_id_206, _id_196))
s.add(Implies(_id_207, _id_196))
s.add(Implies(_id_199, _id_197))
s.add(Implies(_id_200, _id_197))
s.add(Implies(_id_203, _id_201))
s.add(Implies(_id_204, _id_201))
s.add(Implies(_id_205, _id_204))
s.add(Implies(_id_208, discounts))
s.add(Implies(_id_212, discounts))
s.add(Implies(_id_217, discounts))
s.add(Implies(_id_220, discounts))
s.add(Implies(_id_224, discounts))
s.add(Implies(_id_225, discounts))
s.add(Implies(_id_209, _id_208))
s.add(Implies(_id_210, _id_208))
s.add(Implies(_id_211, _id_208))
s.add(Implies(_id_214, _id_212))
s.add(Implies(_id_215, _id_212))
s.add(Implies(_id_216, _id_212))
s.add(Implies(_id_218, _id_217))
s.add(Implies(_id_219, _id_217))
s.add(Implies(_id_222, _id_220))
s.add(Implies(_id_223, _id_220))
s.add(Implies(_id_228, _id_226))
s.add(Implies(_id_229, _id_226))
s.add(Implies(_id_231, _id_226))
s.add(Implies(_id_230, _id_229))
s.add(Implies(_id_232, _id_231))
s.add(Implies(_id_235, _id_233))
s.add(Implies(_id_236, _id_233))
s.add(Implies(_id_237, _id_233))
s.add(Implies(personalized_emails, _id_237))
s.add(Implies(_id_238, _id_237))
s.add(Implies(_id_241, _id_240))
s.add(Implies(_id_242, _id_240))
s.add(Implies(_id_243, inventory_tracking))
s.add(Implies(_id_244, procurement))
s.add(Implies(_id_245, _id_244))
s.add(Implies(automatic, _id_244))
s.add(Implies(_id_246, automatic))
s.add(Implies(_id_247, reporting_and_analysis))
s.add(Implies(_id_248, reporting_and_analysis))
s.add(Implies(_id_249, reporting_and_analysis))
s.add(Implies(fulfillment_system, _id_250))
s.add(Implies(_id_252, _id_250))
s.add(Implies(procurement_system, _id_250))
s.add(Implies(_id_253, _id_250))
s.add(Implies(_id_255, _id_254))
s.add(Implies(_id_260, _id_254))
s.add(Implies(_id_256, _id_255))
s.add(Implies(_id_257, _id_255))
s.add(Implies(_id_258, _id_255))
s.add(Implies(_id_259, _id_255))
s.add(Implies(_id_261, _id_260))
s.add(Implies(_id_262, _id_260))
s.add(Implies(_id_263, _id_260))


#Mandatory-Children
s.add(store_front == eShop)
s.add(business_management == eShop)
s.add(catalog == store_front)
s.add(buy_paths == store_front)
s.add(_id_3 == _id_2)
s.add(_id_6 == _id_2)
s.add(registration_enforcement == registration)
s.add(_id_13 == registration)
s.add(_id_14 == _id_13)
s.add(_id_19 == _id_18)
s.add(_id_20 == _id_18)
s.add(_id_21 == _id_18)
s.add(product_information == catalog)
s.add(product_type == product_information)
s.add(basic_information == product_information)
s.add(categories_catalog == categories)
s.add(_id_61 == _id_60)
s.add(_id_78 == buy_paths)
s.add(_id_83 == buy_paths)
s.add(_id_139 == buy_paths)
s.add(_id_79 == _id_78)
s.add(_id_80 == _id_78)
s.add(_id_84 == _id_83)
s.add(_id_93 == _id_83)
s.add(_id_117 == _id_83)
s.add(_id_92 == shipping_options)
s.add(_id_96 == _id_95)
s.add(_id_108 == _id_95)
s.add(_id_100 == _id_99)
s.add(_id_101 == _id_99)
s.add(shipping_2 == _id_101)
s.add(_id_118 == _id_117)
s.add(buy_paths_288_289_290 == buy_paths_288_289)
s.add(_id_150 == _id_149)
s.add(_id_160 == user_behaviour_tracking)
s.add(_id_162 == business_management)
s.add(_id_254 == business_management)
s.add(_id_163 == _id_162)
s.add(warehouse_management == physical_goods_fulfillment)
s.add(shipping == physical_goods_fulfillment)
s.add(_id_167 == _id_166)
s.add(_id_168 == _id_167)
s.add(_id_182 == eletronic_goods_fulfillment)
s.add(_id_183 == eletronic_goods_fulfillment)
s.add(_id_187 == _id_186)
s.add(_id_194 == _id_186)
s.add(_id_233 == _id_186)
s.add(_id_197 == _id_196)
s.add(_id_201 == _id_196)
s.add(_id_205 == _id_204)
s.add(_id_208 == discounts)
s.add(_id_212 == discounts)
s.add(_id_217 == discounts)
s.add(_id_220 == discounts)
s.add(_id_225 == discounts)
s.add(_id_209 == _id_208)
s.add(_id_210 == _id_208)
s.add(_id_230 == _id_229)
s.add(_id_232 == _id_231)
s.add(_id_241 == _id_240)
s.add(_id_242 == _id_240)
s.add(_id_244 == procurement)
s.add(_id_245 == _id_244)
s.add(_id_246 == automatic)
s.add(_id_247 == reporting_and_analysis)
s.add(_id_248 == reporting_and_analysis)
s.add(_id_249 == reporting_and_analysis)
s.add(_id_255 == _id_254)
s.add(_id_260 == _id_254)
s.add(_id_256 == _id_255)
s.add(_id_257 == _id_255)
s.add(_id_258 == _id_255)
s.add(_id_261 == _id_260)
s.add(_id_262 == _id_260)
s.add(_id_263 == _id_260)


#Exclusive-Or Constraints


#Or Constraints
s.add(homepage==Or(_id_1,_id_2))
s.add(_id_3==Or(_id_5,special_offers))
s.add(_id_6==Or(_id_8,_id_9))
s.add(registration_enforcement==Or(_id_11,register_to_buy,_id_12))
s.add(_id_23==Or(_id_25,_id_26,_id_27,_id_28))
s.add(preferences==Or(_id_31,_id_32,_id_33))
s.add(product_type==Or(eletronic_goods,physical_goods,services))
s.add(associated_assets==Or(_id_38,_id_39))
s.add(_id_39==Or(_id_41,_id_49,_id_50))
s.add(_id_41==Or(_id_43,_id_44,_id_45,_id_46,_id_47,_id_48))
s.add(_id_56==Or(_id_58,_id_59))
s.add(_id_63==Or(_id_65,_id_66,_id_67,_id_68,_id_69))
s.add(permissions==Or(_id_75,_id_76,_id_77))
s.add(_id_84==Or(registered_checkout,_id_87))
s.add(_id_93==Or(_id_95,_id_112))
s.add(_id_96==Or(_id_98,_id_99))
s.add(_id_103==Or(_id_105,_id_106,_id_107))
s.add(_id_108==Or(_id_110,_id_111))
s.add(_id_112==Or(_id_114,_id_115,_id_116))
s.add(_id_118==Or(_id_120,_id_121,_id_122,_id_123,_id_124,_id_125,_id_126,_id_127,_id_128))
s.add(_id_130==Or(_id_132,_id_133,_id_134,_id_135,_id_136,_id_137,_id_138))
s.add(_id_139==Or(_id_141,_id_142,_id_143,_id_144))
s.add(buy_paths==Or(buy_paths_288_289))
s.add(customer_service==Or(_id_146,_id_148,_id_149,_id_156))
s.add(_id_150==Or(_id_152,_id_153,_id_154))
s.add(_id_156==Or(_id_158,_id_159))
s.add(_id_160==Or(locally_visited_pages,external_referring_pages,behaviour_tracked_previous_purchases))
s.add(_id_163==Or(physical_goods_fulfillment,eletronic_goods_fulfillment,services_fulfillment))
s.add(shipping==Or(_id_166,_id_175))
s.add(_id_169==Or(_id_171,_id_172,_id_173,_id_174))
s.add(_id_175==Or(_id_177,_id_178,_id_179,_id_180,_id_181))
s.add(_id_187==Or(customer_preferences,_id_189,_id_190,targeting_criteria_previous_purchases,_id_191,wish_list_content,previously_visited_pages,_id_192,_id_193))
s.add(_id_194==Or(_id_196,discounts,_id_226))
s.add(_id_197==Or(_id_199,_id_200))
s.add(_id_201==Or(_id_203,_id_204))
s.add(_id_212==Or(_id_214,_id_215,_id_216))
s.add(_id_220==Or(_id_222,_id_223))
s.add(_id_226==Or(_id_228,_id_229,_id_231))
s.add(_id_233==Or(_id_235,_id_236,_id_237))
s.add(_id_250==Or(fulfillment_system,_id_252,procurement_system,_id_253))


#Requires Constraints
s.add(Implies(special_offers, discounts))
s.add(Implies(user_behaviour_tracking_info, user_behaviour_tracking))
s.add(Implies(eletronic_goods, size))
s.add(Implies(eletronic_goods, eletronic_goods_fulfillment))
s.add(Implies(physical_goods, size))
s.add(Implies(physical_goods, physical_goods_fulfillment))
s.add(Implies(physical_goods, weight))
s.add(Implies(services, services_fulfillment))
s.add(Implies(availability, inventory_tracking))
s.add(Implies(category_page, categories))
s.add(Implies(wish_list, wish_list_saved_after_session))
s.add(Implies(email_wish_list, registration))
s.add(Implies(permissions, registration))
s.add(Implies(registered_checkout, register_to_buy))
s.add(Implies(registered_checkout, registration_enforcement))
s.add(Implies(quick_checkout, quick_checkout_profile))
s.add(Implies(shipping_options, shipping))
s.add(Implies(customer_preferences, preferences))
s.add(Implies(wish_list_content, wish_list))


#Excludes Constraints


#Attributes
total_Cost = Real('total_Cost')
total_UsedBefore = Int('total_UsedBefore')
total_FeatureCount = Int('total_FeatureCount')
total_Defects = Int('total_Defects')


#Sums for Attributes
s.add(total_Cost== 7.6408989963771194*If(eShop, 1.0, 0.0 ) \
+ 7.5092053767634654*If(store_front, 1.0, 0.0 ) \
+ 14.689398134577047*If(homepage, 1.0, 0.0 ) \
+ 6.166499393904992*If(_id_1, 1.0, 0.0 ) \
+ 10.419039139443939*If(_id_2, 1.0, 0.0 ) \
+ 9.758947026333994*If(_id_3, 1.0, 0.0 ) \
+ 8.148236814831348*If(_id_5, 1.0, 0.0 ) \
+ 13.465111749758071*If(special_offers, 1.0, 0.0 ) \
+ 10.95267855613079*If(_id_6, 1.0, 0.0 ) \
+ 8.863099463028671*If(_id_8, 1.0, 0.0 ) \
+ 7.7496457787452195*If(_id_9, 1.0, 0.0 ) \
+ 6.4745651041969055*If(registration, 1.0, 0.0 ) \
+ 11.397415959703473*If(registration_enforcement, 1.0, 0.0 ) \
+ 7.363245163135134*If(_id_11, 1.0, 0.0 ) \
+ 13.428384485896377*If(register_to_buy, 1.0, 0.0 ) \
+ 5.452286607902222*If(_id_12, 1.0, 0.0 ) \
+ 6.100473520805334*If(_id_13, 1.0, 0.0 ) \
+ 12.322224885205483*If(_id_14, 1.0, 0.0 ) \
+ 5.65369920107192*If(shipping_address, 1.0, 0.0 ) \
+ 10.308317459185346*If(_id_15, 1.0, 0.0 ) \
+ 5.901282664841281*If(_id_16, 1.0, 0.0 ) \
+ 11.54075936960424*If(_id_17, 1.0, 0.0 ) \
+ 13.682644828346174*If(_id_18, 1.0, 0.0 ) \
+ 13.008853827785588*If(_id_19, 1.0, 0.0 ) \
+ 10.048601003623034*If(_id_20, 1.0, 0.0 ) \
+ 9.733988067434892*If(_id_21, 1.0, 0.0 ) \
+ 11.101621731632662*If(_id_22, 1.0, 0.0 ) \
+ 12.247116996854373*If(_id_23, 1.0, 0.0 ) \
+ 8.620782055044714*If(_id_25, 1.0, 0.0 ) \
+ 10.641905327748809*If(_id_26, 1.0, 0.0 ) \
+ 12.952913973746648*If(_id_27, 1.0, 0.0 ) \
+ 12.141681946598066*If(_id_28, 1.0, 0.0 ) \
+ 10.474662762049276*If(_id_29, 1.0, 0.0 ) \
+ 14.054171683911981*If(preferences, 1.0, 0.0 ) \
+ 6.7377605081216725*If(_id_31, 1.0, 0.0 ) \
+ 5.013527622729248*If(_id_32, 1.0, 0.0 ) \
+ 9.556632783363145*If(_id_33, 1.0, 0.0 ) \
+ 5.222981863350846*If(_id_34, 1.0, 0.0 ) \
+ 12.234241931520607*If(quick_checkout_profile, 1.0, 0.0 ) \
+ 13.706631087816838*If(_id_35, 1.0, 0.0 ) \
+ 11.690308919683972*If(user_behaviour_tracking_info, 1.0, 0.0 ) \
+ 9.08978755801254*If(catalog, 1.0, 0.0 ) \
+ 8.283453001056765*If(product_information, 1.0, 0.0 ) \
+ 13.822548843969992*If(product_type, 1.0, 0.0 ) \
+ 13.448408309917696*If(eletronic_goods, 1.0, 0.0 ) \
+ 6.678736375202533*If(physical_goods, 1.0, 0.0 ) \
+ 12.67406591130029*If(services, 1.0, 0.0 ) \
+ 11.457470718191058*If(basic_information, 1.0, 0.0 ) \
+ 12.494044110891522*If(detailed_information, 1.0, 0.0 ) \
+ 14.158574797258682*If(warranty_information, 1.0, 0.0 ) \
+ 13.062453109869914*If(customer_reviews, 1.0, 0.0 ) \
+ 11.701115238621854*If(associated_assets, 1.0, 0.0 ) \
+ 11.547061191916773*If(_id_38, 1.0, 0.0 ) \
+ 9.453300186017023*If(_id_39, 1.0, 0.0 ) \
+ 10.208465594152253*If(_id_41, 1.0, 0.0 ) \
+ 14.774074453130641*If(_id_43, 1.0, 0.0 ) \
+ 10.085590098061834*If(_id_44, 1.0, 0.0 ) \
+ 10.210916141715822*If(_id_45, 1.0, 0.0 ) \
+ 7.543934936803468*If(_id_46, 1.0, 0.0 ) \
+ 11.978877919311298*If(_id_47, 1.0, 0.0 ) \
+ 5.49755040865408*If(_id_48, 1.0, 0.0 ) \
+ 11.208088215279345*If(_id_49, 1.0, 0.0 ) \
+ 12.508123577544836*If(_id_50, 1.0, 0.0 ) \
+ 6.471631630916066*If(product_variants, 1.0, 0.0 ) \
+ 13.969655250593194*If(_id_51, 1.0, 0.0 ) \
+ 7.448026706260711*If(size, 1.0, 0.0 ) \
+ 13.5192772577005*If(weight, 1.0, 0.0 ) \
+ 10.504307809193955*If(availability, 1.0, 0.0 ) \
+ 11.739153744172338*If(custom_fields, 1.0, 0.0 ) \
+ 7.0134361910209275*If(categories, 1.0, 0.0 ) \
+ 8.404022678530714*If(categories_catalog, 1.0, 0.0 ) \
+ 10.626942793292814*If(_id_52, 1.0, 0.0 ) \
+ 11.05043773180602*If(_id_53, 1.0, 0.0 ) \
+ 13.89161796147099*If(_id_54, 1.0, 0.0 ) \
+ 9.591618891844988*If(_id_55, 1.0, 0.0 ) \
+ 12.366684857811785*If(_id_56, 1.0, 0.0 ) \
+ 9.487897640172001*If(_id_58, 1.0, 0.0 ) \
+ 13.702779929045597*If(_id_59, 1.0, 0.0 ) \
+ 5.45850856619111*If(_id_60, 1.0, 0.0 ) \
+ 6.467647715800785*If(_id_61, 1.0, 0.0 ) \
+ 12.48283554461106*If(category_page, 1.0, 0.0 ) \
+ 8.034771161927633*If(_id_62, 1.0, 0.0 ) \
+ 6.991322414222251*If(_id_63, 1.0, 0.0 ) \
+ 11.513321410348365*If(_id_65, 1.0, 0.0 ) \
+ 10.078358185854231*If(_id_66, 1.0, 0.0 ) \
+ 10.859511185037704*If(_id_67, 1.0, 0.0 ) \
+ 14.682982382667115*If(_id_68, 1.0, 0.0 ) \
+ 12.864288224579106*If(_id_69, 1.0, 0.0 ) \
+ 12.96948841967712*If(_id_70, 1.0, 0.0 ) \
+ 11.507125456509785*If(_id_71, 1.0, 0.0 ) \
+ 10.967145387731474*If(_id_72, 1.0, 0.0 ) \
+ 5.550831042269108*If(wish_list, 1.0, 0.0 ) \
+ 7.445684603109893*If(wish_list_saved_after_session, 1.0, 0.0 ) \
+ 11.602951673043904*If(email_wish_list, 1.0, 0.0 ) \
+ 14.060340843740168*If(_id_73, 1.0, 0.0 ) \
+ 8.326253343143712*If(permissions, 1.0, 0.0 ) \
+ 12.45600555886055*If(_id_75, 1.0, 0.0 ) \
+ 8.594488385227859*If(_id_76, 1.0, 0.0 ) \
+ 12.62468951953338*If(_id_77, 1.0, 0.0 ) \
+ 10.164989565538537*If(buy_paths, 1.0, 0.0 ) \
+ 6.529268725752865*If(_id_78, 1.0, 0.0 ) \
+ 8.155732289876509*If(_id_79, 1.0, 0.0 ) \
+ 5.725949717154771*If(_id_80, 1.0, 0.0 ) \
+ 6.926431468819042*If(_id_81, 1.0, 0.0 ) \
+ 12.597600046091099*If(_id_82, 1.0, 0.0 ) \
+ 6.198151931227723*If(_id_83, 1.0, 0.0 ) \
+ 11.746491470890124*If(_id_84, 1.0, 0.0 ) \
+ 5.326602472759153*If(registered_checkout, 1.0, 0.0 ) \
+ 11.026294259831477*If(quick_checkout, 1.0, 0.0 ) \
+ 11.469575240642563*If(_id_86, 1.0, 0.0 ) \
+ 10.442794419354625*If(_id_87, 1.0, 0.0 ) \
+ 14.523692666711222*If(shipping_options, 1.0, 0.0 ) \
+ 7.075733586365502*If(_id_88, 1.0, 0.0 ) \
+ 6.3737725152566815*If(_id_89, 1.0, 0.0 ) \
+ 13.168854518610257*If(_id_90, 1.0, 0.0 ) \
+ 8.952452340103575*If(_id_91, 1.0, 0.0 ) \
+ 9.743824552594432*If(_id_92, 1.0, 0.0 ) \
+ 13.712023626055357*If(_id_93, 1.0, 0.0 ) \
+ 8.050203855345863*If(_id_95, 1.0, 0.0 ) \
+ 5.767914526601341*If(_id_96, 1.0, 0.0 ) \
+ 9.514361895187513*If(_id_98, 1.0, 0.0 ) \
+ 5.497472803122494*If(_id_99, 1.0, 0.0 ) \
+ 11.142072152189773*If(_id_100, 1.0, 0.0 ) \
+ 9.948847677143242*If(_id_101, 1.0, 0.0 ) \
+ 6.082961503828988*If(shipping_2, 1.0, 0.0 ) \
+ 6.527724568792362*If(_id_102, 1.0, 0.0 ) \
+ 11.203206814997543*If(_id_103, 1.0, 0.0 ) \
+ 14.23962411202238*If(_id_105, 1.0, 0.0 ) \
+ 7.605837233697922*If(_id_106, 1.0, 0.0 ) \
+ 14.777380257716834*If(_id_107, 1.0, 0.0 ) \
+ 5.868448477389622*If(_id_108, 1.0, 0.0 ) \
+ 14.065012623995926*If(_id_110, 1.0, 0.0 ) \
+ 13.264524029624305*If(_id_111, 1.0, 0.0 ) \
+ 6.491361097497386*If(_id_112, 1.0, 0.0 ) \
+ 10.097715855216958*If(_id_114, 1.0, 0.0 ) \
+ 7.619948146871513*If(_id_115, 1.0, 0.0 ) \
+ 11.284442404074237*If(_id_116, 1.0, 0.0 ) \
+ 12.803944177000096*If(_id_117, 1.0, 0.0 ) \
+ 11.177131658441173*If(_id_118, 1.0, 0.0 ) \
+ 10.375141881576544*If(_id_120, 1.0, 0.0 ) \
+ 10.203074566109287*If(_id_121, 1.0, 0.0 ) \
+ 9.12948139557153*If(_id_122, 1.0, 0.0 ) \
+ 10.854707452827949*If(_id_123, 1.0, 0.0 ) \
+ 10.087078325962382*If(_id_124, 1.0, 0.0 ) \
+ 14.253526963711174*If(_id_125, 1.0, 0.0 ) \
+ 12.724805651193767*If(_id_126, 1.0, 0.0 ) \
+ 9.390004399171492*If(_id_127, 1.0, 0.0 ) \
+ 10.182288390910879*If(_id_128, 1.0, 0.0 ) \
+ 12.33661467770325*If(_id_129, 1.0, 0.0 ) \
+ 13.533374580882548*If(_id_130, 1.0, 0.0 ) \
+ 9.783003239135972*If(_id_132, 1.0, 0.0 ) \
+ 13.375006279647351*If(_id_133, 1.0, 0.0 ) \
+ 6.257091668571168*If(_id_134, 1.0, 0.0 ) \
+ 14.282875695623588*If(_id_135, 1.0, 0.0 ) \
+ 13.483561473234046*If(_id_136, 1.0, 0.0 ) \
+ 11.616328376817465*If(_id_137, 1.0, 0.0 ) \
+ 10.700664325219154*If(_id_138, 1.0, 0.0 ) \
+ 7.846548015341941*If(_id_139, 1.0, 0.0 ) \
+ 10.50601265095132*If(_id_141, 1.0, 0.0 ) \
+ 14.535242420298093*If(_id_142, 1.0, 0.0 ) \
+ 8.276489830222296*If(_id_143, 1.0, 0.0 ) \
+ 14.490419888736582*If(_id_144, 1.0, 0.0 ) \
+ 5.8749229841071635*If(buy_paths_288_289, 1.0, 0.0 ) \
+ 7.303193781549829*If(buy_paths_288_289_290, 1.0, 0.0 ) \
+ 7.308405930634457*If(buy_paths_288_289_291, 1.0, 0.0 ) \
+ 9.813824236456133*If(customer_service, 1.0, 0.0 ) \
+ 13.6713929781265*If(_id_146, 1.0, 0.0 ) \
+ 9.161126272326035*If(_id_147, 1.0, 0.0 ) \
+ 11.363851001115922*If(_id_148, 1.0, 0.0 ) \
+ 6.180057473327856*If(_id_149, 1.0, 0.0 ) \
+ 5.519473765541136*If(_id_150, 1.0, 0.0 ) \
+ 14.454651974297574*If(_id_152, 1.0, 0.0 ) \
+ 9.000032433277097*If(_id_153, 1.0, 0.0 ) \
+ 9.563743081616527*If(_id_154, 1.0, 0.0 ) \
+ 9.603053341939427*If(_id_155, 1.0, 0.0 ) \
+ 9.603156848605927*If(_id_156, 1.0, 0.0 ) \
+ 6.202492136699816*If(_id_158, 1.0, 0.0 ) \
+ 6.422839261961561*If(_id_159, 1.0, 0.0 ) \
+ 9.003503855902935*If(user_behaviour_tracking, 1.0, 0.0 ) \
+ 10.18170375937266*If(_id_160, 1.0, 0.0 ) \
+ 13.702994660048802*If(locally_visited_pages, 1.0, 0.0 ) \
+ 8.778914100047968*If(external_referring_pages, 1.0, 0.0 ) \
+ 14.803972018798849*If(behaviour_tracked_previous_purchases, 1.0, 0.0 ) \
+ 5.235859854829556*If(business_management, 1.0, 0.0 ) \
+ 10.69523188241153*If(_id_162, 1.0, 0.0 ) \
+ 8.34384661319209*If(_id_163, 1.0, 0.0 ) \
+ 7.379857380503002*If(physical_goods_fulfillment, 1.0, 0.0 ) \
+ 5.212683488537882*If(warehouse_management, 1.0, 0.0 ) \
+ 13.927054474546289*If(shipping, 1.0, 0.0 ) \
+ 14.316931612686966*If(_id_166, 1.0, 0.0 ) \
+ 5.226818865333093*If(_id_167, 1.0, 0.0 ) \
+ 10.741950240698534*If(_id_168, 1.0, 0.0 ) \
+ 14.927689970101804*If(_id_169, 1.0, 0.0 ) \
+ 14.617141103497246*If(_id_171, 1.0, 0.0 ) \
+ 12.277718659183789*If(_id_172, 1.0, 0.0 ) \
+ 7.728433901536269*If(_id_173, 1.0, 0.0 ) \
+ 8.008843469729102*If(_id_174, 1.0, 0.0 ) \
+ 7.470519878765421*If(_id_175, 1.0, 0.0 ) \
+ 14.119752303499357*If(_id_177, 1.0, 0.0 ) \
+ 13.169622237502637*If(_id_178, 1.0, 0.0 ) \
+ 7.4340524051970975*If(_id_179, 1.0, 0.0 ) \
+ 7.660526899028069*If(_id_180, 1.0, 0.0 ) \
+ 6.386028029383401*If(_id_181, 1.0, 0.0 ) \
+ 12.09590450074183*If(eletronic_goods_fulfillment, 1.0, 0.0 ) \
+ 12.860651688435825*If(_id_182, 1.0, 0.0 ) \
+ 7.773943811534883*If(_id_183, 1.0, 0.0 ) \
+ 7.835798717834518*If(services_fulfillment, 1.0, 0.0 ) \
+ 12.54059140084555*If(_id_184, 1.0, 0.0 ) \
+ 5.289227421140858*If(_id_185, 1.0, 0.0 ) \
+ 14.570772998711021*If(_id_186, 1.0, 0.0 ) \
+ 6.367356999419799*If(_id_187, 1.0, 0.0 ) \
+ 9.154310023650796*If(customer_preferences, 1.0, 0.0 ) \
+ 12.751351245477414*If(_id_189, 1.0, 0.0 ) \
+ 8.682538690139769*If(_id_190, 1.0, 0.0 ) \
+ 6.9295468134050076*If(targeting_criteria_previous_purchases, 1.0, 0.0 ) \
+ 9.055213665970443*If(_id_191, 1.0, 0.0 ) \
+ 11.223727442341552*If(wish_list_content, 1.0, 0.0 ) \
+ 7.2905067142925954*If(previously_visited_pages, 1.0, 0.0 ) \
+ 5.79535237955037*If(_id_192, 1.0, 0.0 ) \
+ 9.13571350667006*If(_id_193, 1.0, 0.0 ) \
+ 11.109531126009914*If(_id_194, 1.0, 0.0 ) \
+ 12.466071508305017*If(_id_196, 1.0, 0.0 ) \
+ 13.447243179447357*If(_id_197, 1.0, 0.0 ) \
+ 6.5513313931736885*If(_id_199, 1.0, 0.0 ) \
+ 13.315224257055526*If(_id_200, 1.0, 0.0 ) \
+ 5.924711844857119*If(_id_201, 1.0, 0.0 ) \
+ 5.518117944119156*If(_id_203, 1.0, 0.0 ) \
+ 10.403832496970772*If(_id_204, 1.0, 0.0 ) \
+ 10.576469894933119*If(_id_205, 1.0, 0.0 ) \
+ 5.371376890338358*If(_id_206, 1.0, 0.0 ) \
+ 14.315024849730273*If(_id_207, 1.0, 0.0 ) \
+ 7.830326937440545*If(discounts, 1.0, 0.0 ) \
+ 6.877300315668863*If(_id_208, 1.0, 0.0 ) \
+ 7.118092393983096*If(_id_209, 1.0, 0.0 ) \
+ 12.592573609526692*If(_id_210, 1.0, 0.0 ) \
+ 7.5807140117872756*If(_id_211, 1.0, 0.0 ) \
+ 9.712307599750698*If(_id_212, 1.0, 0.0 ) \
+ 5.792393472961842*If(_id_214, 1.0, 0.0 ) \
+ 14.037104543778335*If(_id_215, 1.0, 0.0 ) \
+ 13.296547190692081*If(_id_216, 1.0, 0.0 ) \
+ 5.631269880070435*If(_id_217, 1.0, 0.0 ) \
+ 11.689508686249935*If(_id_218, 1.0, 0.0 ) \
+ 13.597557988446027*If(_id_219, 1.0, 0.0 ) \
+ 7.6251799609267445*If(_id_220, 1.0, 0.0 ) \
+ 5.68796351990089*If(_id_222, 1.0, 0.0 ) \
+ 7.800091605433927*If(_id_223, 1.0, 0.0 ) \
+ 8.91267372831946*If(_id_224, 1.0, 0.0 ) \
+ 12.141293196584547*If(_id_225, 1.0, 0.0 ) \
+ 10.812845320759738*If(_id_226, 1.0, 0.0 ) \
+ 10.815947814780277*If(_id_228, 1.0, 0.0 ) \
+ 8.428147386597693*If(_id_229, 1.0, 0.0 ) \
+ 14.494740529315258*If(_id_230, 1.0, 0.0 ) \
+ 8.651026317216887*If(_id_231, 1.0, 0.0 ) \
+ 8.755357522161653*If(_id_232, 1.0, 0.0 ) \
+ 11.857993980900236*If(_id_233, 1.0, 0.0 ) \
+ 12.047372721567406*If(_id_235, 1.0, 0.0 ) \
+ 11.15659243752523*If(_id_236, 1.0, 0.0 ) \
+ 9.962261313880632*If(_id_237, 1.0, 0.0 ) \
+ 9.232374201501939*If(personalized_emails, 1.0, 0.0 ) \
+ 13.866371729466655*If(_id_238, 1.0, 0.0 ) \
+ 9.167755016880207*If(_id_239, 1.0, 0.0 ) \
+ 7.98212521969543*If(_id_240, 1.0, 0.0 ) \
+ 10.76244706819834*If(_id_241, 1.0, 0.0 ) \
+ 11.690561848142444*If(_id_242, 1.0, 0.0 ) \
+ 7.640803318082028*If(inventory_tracking, 1.0, 0.0 ) \
+ 8.312398600153221*If(_id_243, 1.0, 0.0 ) \
+ 8.632823657078369*If(procurement, 1.0, 0.0 ) \
+ 10.739013712652836*If(_id_244, 1.0, 0.0 ) \
+ 12.208847540822239*If(_id_245, 1.0, 0.0 ) \
+ 6.248853928287709*If(automatic, 1.0, 0.0 ) \
+ 5.763206411300586*If(_id_246, 1.0, 0.0 ) \
+ 8.942313675400635*If(reporting_and_analysis, 1.0, 0.0 ) \
+ 8.35006013894472*If(_id_247, 1.0, 0.0 ) \
+ 8.118225697062444*If(_id_248, 1.0, 0.0 ) \
+ 13.872371191167929*If(_id_249, 1.0, 0.0 ) \
+ 6.050023565088099*If(_id_250, 1.0, 0.0 ) \
+ 7.124615560222673*If(fulfillment_system, 1.0, 0.0 ) \
+ 7.293364159442385*If(_id_252, 1.0, 0.0 ) \
+ 10.14799509210012*If(procurement_system, 1.0, 0.0 ) \
+ 5.0477787924505355*If(_id_253, 1.0, 0.0 ) \
+ 8.785456640090194*If(_id_254, 1.0, 0.0 ) \
+ 12.1518082270672*If(_id_255, 1.0, 0.0 ) \
+ 10.801568955063226*If(_id_256, 1.0, 0.0 ) \
+ 12.706150661423859*If(_id_257, 1.0, 0.0 ) \
+ 5.910254712808497*If(_id_258, 1.0, 0.0 ) \
+ 7.485389165154594*If(_id_259, 1.0, 0.0 ) \
+ 12.749264361694152*If(_id_260, 1.0, 0.0 ) \
+ 5.109649705338875*If(_id_261, 1.0, 0.0 ) \
+ 13.437739114692404*If(_id_262, 1.0, 0.0 ) \
+ 11.962505615097202*If(_id_263, 1.0, 0.0 ) \
)
s.add(total_UsedBefore== 1*If(eShop, 1, 0 ) \
+ 0*If(store_front, 1, 0 ) \
+ 1*If(homepage, 1, 0 ) \
+ 0*If(_id_1, 1, 0 ) \
+ 0*If(_id_2, 1, 0 ) \
+ 1*If(_id_3, 1, 0 ) \
+ 0*If(_id_5, 1, 0 ) \
+ 1*If(special_offers, 1, 0 ) \
+ 1*If(_id_6, 1, 0 ) \
+ 0*If(_id_8, 1, 0 ) \
+ 1*If(_id_9, 1, 0 ) \
+ 1*If(registration, 1, 0 ) \
+ 0*If(registration_enforcement, 1, 0 ) \
+ 1*If(_id_11, 1, 0 ) \
+ 0*If(register_to_buy, 1, 0 ) \
+ 1*If(_id_12, 1, 0 ) \
+ 0*If(_id_13, 1, 0 ) \
+ 1*If(_id_14, 1, 0 ) \
+ 0*If(shipping_address, 1, 0 ) \
+ 0*If(_id_15, 1, 0 ) \
+ 0*If(_id_16, 1, 0 ) \
+ 0*If(_id_17, 1, 0 ) \
+ 1*If(_id_18, 1, 0 ) \
+ 0*If(_id_19, 1, 0 ) \
+ 1*If(_id_20, 1, 0 ) \
+ 0*If(_id_21, 1, 0 ) \
+ 0*If(_id_22, 1, 0 ) \
+ 1*If(_id_23, 1, 0 ) \
+ 0*If(_id_25, 1, 0 ) \
+ 0*If(_id_26, 1, 0 ) \
+ 1*If(_id_27, 1, 0 ) \
+ 1*If(_id_28, 1, 0 ) \
+ 0*If(_id_29, 1, 0 ) \
+ 1*If(preferences, 1, 0 ) \
+ 0*If(_id_31, 1, 0 ) \
+ 0*If(_id_32, 1, 0 ) \
+ 0*If(_id_33, 1, 0 ) \
+ 1*If(_id_34, 1, 0 ) \
+ 0*If(quick_checkout_profile, 1, 0 ) \
+ 0*If(_id_35, 1, 0 ) \
+ 0*If(user_behaviour_tracking_info, 1, 0 ) \
+ 0*If(catalog, 1, 0 ) \
+ 0*If(product_information, 1, 0 ) \
+ 0*If(product_type, 1, 0 ) \
+ 0*If(eletronic_goods, 1, 0 ) \
+ 1*If(physical_goods, 1, 0 ) \
+ 1*If(services, 1, 0 ) \
+ 0*If(basic_information, 1, 0 ) \
+ 0*If(detailed_information, 1, 0 ) \
+ 0*If(warranty_information, 1, 0 ) \
+ 1*If(customer_reviews, 1, 0 ) \
+ 1*If(associated_assets, 1, 0 ) \
+ 0*If(_id_38, 1, 0 ) \
+ 1*If(_id_39, 1, 0 ) \
+ 0*If(_id_41, 1, 0 ) \
+ 0*If(_id_43, 1, 0 ) \
+ 0*If(_id_44, 1, 0 ) \
+ 1*If(_id_45, 1, 0 ) \
+ 1*If(_id_46, 1, 0 ) \
+ 0*If(_id_47, 1, 0 ) \
+ 1*If(_id_48, 1, 0 ) \
+ 1*If(_id_49, 1, 0 ) \
+ 0*If(_id_50, 1, 0 ) \
+ 0*If(product_variants, 1, 0 ) \
+ 0*If(_id_51, 1, 0 ) \
+ 0*If(size, 1, 0 ) \
+ 1*If(weight, 1, 0 ) \
+ 0*If(availability, 1, 0 ) \
+ 1*If(custom_fields, 1, 0 ) \
+ 1*If(categories, 1, 0 ) \
+ 1*If(categories_catalog, 1, 0 ) \
+ 0*If(_id_52, 1, 0 ) \
+ 1*If(_id_53, 1, 0 ) \
+ 0*If(_id_54, 1, 0 ) \
+ 1*If(_id_55, 1, 0 ) \
+ 0*If(_id_56, 1, 0 ) \
+ 1*If(_id_58, 1, 0 ) \
+ 1*If(_id_59, 1, 0 ) \
+ 1*If(_id_60, 1, 0 ) \
+ 1*If(_id_61, 1, 0 ) \
+ 1*If(category_page, 1, 0 ) \
+ 1*If(_id_62, 1, 0 ) \
+ 0*If(_id_63, 1, 0 ) \
+ 1*If(_id_65, 1, 0 ) \
+ 1*If(_id_66, 1, 0 ) \
+ 1*If(_id_67, 1, 0 ) \
+ 0*If(_id_68, 1, 0 ) \
+ 1*If(_id_69, 1, 0 ) \
+ 0*If(_id_70, 1, 0 ) \
+ 0*If(_id_71, 1, 0 ) \
+ 0*If(_id_72, 1, 0 ) \
+ 0*If(wish_list, 1, 0 ) \
+ 0*If(wish_list_saved_after_session, 1, 0 ) \
+ 1*If(email_wish_list, 1, 0 ) \
+ 0*If(_id_73, 1, 0 ) \
+ 0*If(permissions, 1, 0 ) \
+ 1*If(_id_75, 1, 0 ) \
+ 0*If(_id_76, 1, 0 ) \
+ 0*If(_id_77, 1, 0 ) \
+ 1*If(buy_paths, 1, 0 ) \
+ 0*If(_id_78, 1, 0 ) \
+ 0*If(_id_79, 1, 0 ) \
+ 0*If(_id_80, 1, 0 ) \
+ 1*If(_id_81, 1, 0 ) \
+ 1*If(_id_82, 1, 0 ) \
+ 1*If(_id_83, 1, 0 ) \
+ 0*If(_id_84, 1, 0 ) \
+ 1*If(registered_checkout, 1, 0 ) \
+ 1*If(quick_checkout, 1, 0 ) \
+ 0*If(_id_86, 1, 0 ) \
+ 1*If(_id_87, 1, 0 ) \
+ 1*If(shipping_options, 1, 0 ) \
+ 1*If(_id_88, 1, 0 ) \
+ 1*If(_id_89, 1, 0 ) \
+ 0*If(_id_90, 1, 0 ) \
+ 0*If(_id_91, 1, 0 ) \
+ 0*If(_id_92, 1, 0 ) \
+ 1*If(_id_93, 1, 0 ) \
+ 0*If(_id_95, 1, 0 ) \
+ 1*If(_id_96, 1, 0 ) \
+ 0*If(_id_98, 1, 0 ) \
+ 0*If(_id_99, 1, 0 ) \
+ 0*If(_id_100, 1, 0 ) \
+ 1*If(_id_101, 1, 0 ) \
+ 1*If(shipping_2, 1, 0 ) \
+ 0*If(_id_102, 1, 0 ) \
+ 0*If(_id_103, 1, 0 ) \
+ 0*If(_id_105, 1, 0 ) \
+ 0*If(_id_106, 1, 0 ) \
+ 0*If(_id_107, 1, 0 ) \
+ 1*If(_id_108, 1, 0 ) \
+ 1*If(_id_110, 1, 0 ) \
+ 0*If(_id_111, 1, 0 ) \
+ 0*If(_id_112, 1, 0 ) \
+ 0*If(_id_114, 1, 0 ) \
+ 0*If(_id_115, 1, 0 ) \
+ 1*If(_id_116, 1, 0 ) \
+ 0*If(_id_117, 1, 0 ) \
+ 0*If(_id_118, 1, 0 ) \
+ 0*If(_id_120, 1, 0 ) \
+ 0*If(_id_121, 1, 0 ) \
+ 0*If(_id_122, 1, 0 ) \
+ 0*If(_id_123, 1, 0 ) \
+ 1*If(_id_124, 1, 0 ) \
+ 0*If(_id_125, 1, 0 ) \
+ 1*If(_id_126, 1, 0 ) \
+ 0*If(_id_127, 1, 0 ) \
+ 0*If(_id_128, 1, 0 ) \
+ 1*If(_id_129, 1, 0 ) \
+ 1*If(_id_130, 1, 0 ) \
+ 1*If(_id_132, 1, 0 ) \
+ 0*If(_id_133, 1, 0 ) \
+ 1*If(_id_134, 1, 0 ) \
+ 0*If(_id_135, 1, 0 ) \
+ 0*If(_id_136, 1, 0 ) \
+ 1*If(_id_137, 1, 0 ) \
+ 0*If(_id_138, 1, 0 ) \
+ 1*If(_id_139, 1, 0 ) \
+ 1*If(_id_141, 1, 0 ) \
+ 1*If(_id_142, 1, 0 ) \
+ 0*If(_id_143, 1, 0 ) \
+ 0*If(_id_144, 1, 0 ) \
+ 0*If(buy_paths_288_289, 1, 0 ) \
+ 0*If(buy_paths_288_289_290, 1, 0 ) \
+ 1*If(buy_paths_288_289_291, 1, 0 ) \
+ 1*If(customer_service, 1, 0 ) \
+ 1*If(_id_146, 1, 0 ) \
+ 0*If(_id_147, 1, 0 ) \
+ 1*If(_id_148, 1, 0 ) \
+ 0*If(_id_149, 1, 0 ) \
+ 0*If(_id_150, 1, 0 ) \
+ 1*If(_id_152, 1, 0 ) \
+ 1*If(_id_153, 1, 0 ) \
+ 0*If(_id_154, 1, 0 ) \
+ 0*If(_id_155, 1, 0 ) \
+ 0*If(_id_156, 1, 0 ) \
+ 0*If(_id_158, 1, 0 ) \
+ 1*If(_id_159, 1, 0 ) \
+ 1*If(user_behaviour_tracking, 1, 0 ) \
+ 0*If(_id_160, 1, 0 ) \
+ 1*If(locally_visited_pages, 1, 0 ) \
+ 0*If(external_referring_pages, 1, 0 ) \
+ 1*If(behaviour_tracked_previous_purchases, 1, 0 ) \
+ 0*If(business_management, 1, 0 ) \
+ 1*If(_id_162, 1, 0 ) \
+ 1*If(_id_163, 1, 0 ) \
+ 1*If(physical_goods_fulfillment, 1, 0 ) \
+ 0*If(warehouse_management, 1, 0 ) \
+ 1*If(shipping, 1, 0 ) \
+ 0*If(_id_166, 1, 0 ) \
+ 0*If(_id_167, 1, 0 ) \
+ 0*If(_id_168, 1, 0 ) \
+ 1*If(_id_169, 1, 0 ) \
+ 0*If(_id_171, 1, 0 ) \
+ 0*If(_id_172, 1, 0 ) \
+ 1*If(_id_173, 1, 0 ) \
+ 0*If(_id_174, 1, 0 ) \
+ 1*If(_id_175, 1, 0 ) \
+ 0*If(_id_177, 1, 0 ) \
+ 0*If(_id_178, 1, 0 ) \
+ 1*If(_id_179, 1, 0 ) \
+ 1*If(_id_180, 1, 0 ) \
+ 0*If(_id_181, 1, 0 ) \
+ 0*If(eletronic_goods_fulfillment, 1, 0 ) \
+ 1*If(_id_182, 1, 0 ) \
+ 0*If(_id_183, 1, 0 ) \
+ 0*If(services_fulfillment, 1, 0 ) \
+ 0*If(_id_184, 1, 0 ) \
+ 0*If(_id_185, 1, 0 ) \
+ 1*If(_id_186, 1, 0 ) \
+ 1*If(_id_187, 1, 0 ) \
+ 1*If(customer_preferences, 1, 0 ) \
+ 1*If(_id_189, 1, 0 ) \
+ 0*If(_id_190, 1, 0 ) \
+ 0*If(targeting_criteria_previous_purchases, 1, 0 ) \
+ 1*If(_id_191, 1, 0 ) \
+ 1*If(wish_list_content, 1, 0 ) \
+ 1*If(previously_visited_pages, 1, 0 ) \
+ 0*If(_id_192, 1, 0 ) \
+ 1*If(_id_193, 1, 0 ) \
+ 0*If(_id_194, 1, 0 ) \
+ 1*If(_id_196, 1, 0 ) \
+ 1*If(_id_197, 1, 0 ) \
+ 0*If(_id_199, 1, 0 ) \
+ 1*If(_id_200, 1, 0 ) \
+ 1*If(_id_201, 1, 0 ) \
+ 1*If(_id_203, 1, 0 ) \
+ 1*If(_id_204, 1, 0 ) \
+ 1*If(_id_205, 1, 0 ) \
+ 1*If(_id_206, 1, 0 ) \
+ 1*If(_id_207, 1, 0 ) \
+ 0*If(discounts, 1, 0 ) \
+ 1*If(_id_208, 1, 0 ) \
+ 0*If(_id_209, 1, 0 ) \
+ 0*If(_id_210, 1, 0 ) \
+ 0*If(_id_211, 1, 0 ) \
+ 1*If(_id_212, 1, 0 ) \
+ 1*If(_id_214, 1, 0 ) \
+ 1*If(_id_215, 1, 0 ) \
+ 1*If(_id_216, 1, 0 ) \
+ 0*If(_id_217, 1, 0 ) \
+ 1*If(_id_218, 1, 0 ) \
+ 1*If(_id_219, 1, 0 ) \
+ 0*If(_id_220, 1, 0 ) \
+ 0*If(_id_222, 1, 0 ) \
+ 0*If(_id_223, 1, 0 ) \
+ 1*If(_id_224, 1, 0 ) \
+ 1*If(_id_225, 1, 0 ) \
+ 1*If(_id_226, 1, 0 ) \
+ 0*If(_id_228, 1, 0 ) \
+ 1*If(_id_229, 1, 0 ) \
+ 0*If(_id_230, 1, 0 ) \
+ 0*If(_id_231, 1, 0 ) \
+ 0*If(_id_232, 1, 0 ) \
+ 0*If(_id_233, 1, 0 ) \
+ 0*If(_id_235, 1, 0 ) \
+ 0*If(_id_236, 1, 0 ) \
+ 0*If(_id_237, 1, 0 ) \
+ 1*If(personalized_emails, 1, 0 ) \
+ 0*If(_id_238, 1, 0 ) \
+ 1*If(_id_239, 1, 0 ) \
+ 0*If(_id_240, 1, 0 ) \
+ 1*If(_id_241, 1, 0 ) \
+ 0*If(_id_242, 1, 0 ) \
+ 1*If(inventory_tracking, 1, 0 ) \
+ 1*If(_id_243, 1, 0 ) \
+ 1*If(procurement, 1, 0 ) \
+ 1*If(_id_244, 1, 0 ) \
+ 0*If(_id_245, 1, 0 ) \
+ 1*If(automatic, 1, 0 ) \
+ 1*If(_id_246, 1, 0 ) \
+ 1*If(reporting_and_analysis, 1, 0 ) \
+ 0*If(_id_247, 1, 0 ) \
+ 0*If(_id_248, 1, 0 ) \
+ 1*If(_id_249, 1, 0 ) \
+ 0*If(_id_250, 1, 0 ) \
+ 1*If(fulfillment_system, 1, 0 ) \
+ 0*If(_id_252, 1, 0 ) \
+ 1*If(procurement_system, 1, 0 ) \
+ 1*If(_id_253, 1, 0 ) \
+ 0*If(_id_254, 1, 0 ) \
+ 0*If(_id_255, 1, 0 ) \
+ 0*If(_id_256, 1, 0 ) \
+ 1*If(_id_257, 1, 0 ) \
+ 1*If(_id_258, 1, 0 ) \
+ 1*If(_id_259, 1, 0 ) \
+ 1*If(_id_260, 1, 0 ) \
+ 0*If(_id_261, 1, 0 ) \
+ 0*If(_id_262, 1, 0 ) \
+ 0*If(_id_263, 1, 0 ) \
)
s.add(total_FeatureCount== 1*If(eShop, 1, 0 ) \
+ 1*If(store_front, 1, 0 ) \
+ 1*If(homepage, 1, 0 ) \
+ 1*If(_id_1, 1, 0 ) \
+ 1*If(_id_2, 1, 0 ) \
+ 1*If(_id_3, 1, 0 ) \
+ 1*If(_id_5, 1, 0 ) \
+ 1*If(special_offers, 1, 0 ) \
+ 1*If(_id_6, 1, 0 ) \
+ 1*If(_id_8, 1, 0 ) \
+ 1*If(_id_9, 1, 0 ) \
+ 1*If(registration, 1, 0 ) \
+ 1*If(registration_enforcement, 1, 0 ) \
+ 1*If(_id_11, 1, 0 ) \
+ 1*If(register_to_buy, 1, 0 ) \
+ 1*If(_id_12, 1, 0 ) \
+ 1*If(_id_13, 1, 0 ) \
+ 1*If(_id_14, 1, 0 ) \
+ 1*If(shipping_address, 1, 0 ) \
+ 1*If(_id_15, 1, 0 ) \
+ 1*If(_id_16, 1, 0 ) \
+ 1*If(_id_17, 1, 0 ) \
+ 1*If(_id_18, 1, 0 ) \
+ 1*If(_id_19, 1, 0 ) \
+ 1*If(_id_20, 1, 0 ) \
+ 1*If(_id_21, 1, 0 ) \
+ 1*If(_id_22, 1, 0 ) \
+ 1*If(_id_23, 1, 0 ) \
+ 1*If(_id_25, 1, 0 ) \
+ 1*If(_id_26, 1, 0 ) \
+ 1*If(_id_27, 1, 0 ) \
+ 1*If(_id_28, 1, 0 ) \
+ 1*If(_id_29, 1, 0 ) \
+ 1*If(preferences, 1, 0 ) \
+ 1*If(_id_31, 1, 0 ) \
+ 1*If(_id_32, 1, 0 ) \
+ 1*If(_id_33, 1, 0 ) \
+ 1*If(_id_34, 1, 0 ) \
+ 1*If(quick_checkout_profile, 1, 0 ) \
+ 1*If(_id_35, 1, 0 ) \
+ 1*If(user_behaviour_tracking_info, 1, 0 ) \
+ 1*If(catalog, 1, 0 ) \
+ 1*If(product_information, 1, 0 ) \
+ 1*If(product_type, 1, 0 ) \
+ 1*If(eletronic_goods, 1, 0 ) \
+ 1*If(physical_goods, 1, 0 ) \
+ 1*If(services, 1, 0 ) \
+ 1*If(basic_information, 1, 0 ) \
+ 1*If(detailed_information, 1, 0 ) \
+ 1*If(warranty_information, 1, 0 ) \
+ 1*If(customer_reviews, 1, 0 ) \
+ 1*If(associated_assets, 1, 0 ) \
+ 1*If(_id_38, 1, 0 ) \
+ 1*If(_id_39, 1, 0 ) \
+ 1*If(_id_41, 1, 0 ) \
+ 1*If(_id_43, 1, 0 ) \
+ 1*If(_id_44, 1, 0 ) \
+ 1*If(_id_45, 1, 0 ) \
+ 1*If(_id_46, 1, 0 ) \
+ 1*If(_id_47, 1, 0 ) \
+ 1*If(_id_48, 1, 0 ) \
+ 1*If(_id_49, 1, 0 ) \
+ 1*If(_id_50, 1, 0 ) \
+ 1*If(product_variants, 1, 0 ) \
+ 1*If(_id_51, 1, 0 ) \
+ 1*If(size, 1, 0 ) \
+ 1*If(weight, 1, 0 ) \
+ 1*If(availability, 1, 0 ) \
+ 1*If(custom_fields, 1, 0 ) \
+ 1*If(categories, 1, 0 ) \
+ 1*If(categories_catalog, 1, 0 ) \
+ 1*If(_id_52, 1, 0 ) \
+ 1*If(_id_53, 1, 0 ) \
+ 1*If(_id_54, 1, 0 ) \
+ 1*If(_id_55, 1, 0 ) \
+ 1*If(_id_56, 1, 0 ) \
+ 1*If(_id_58, 1, 0 ) \
+ 1*If(_id_59, 1, 0 ) \
+ 1*If(_id_60, 1, 0 ) \
+ 1*If(_id_61, 1, 0 ) \
+ 1*If(category_page, 1, 0 ) \
+ 1*If(_id_62, 1, 0 ) \
+ 1*If(_id_63, 1, 0 ) \
+ 1*If(_id_65, 1, 0 ) \
+ 1*If(_id_66, 1, 0 ) \
+ 1*If(_id_67, 1, 0 ) \
+ 1*If(_id_68, 1, 0 ) \
+ 1*If(_id_69, 1, 0 ) \
+ 1*If(_id_70, 1, 0 ) \
+ 1*If(_id_71, 1, 0 ) \
+ 1*If(_id_72, 1, 0 ) \
+ 1*If(wish_list, 1, 0 ) \
+ 1*If(wish_list_saved_after_session, 1, 0 ) \
+ 1*If(email_wish_list, 1, 0 ) \
+ 1*If(_id_73, 1, 0 ) \
+ 1*If(permissions, 1, 0 ) \
+ 1*If(_id_75, 1, 0 ) \
+ 1*If(_id_76, 1, 0 ) \
+ 1*If(_id_77, 1, 0 ) \
+ 1*If(buy_paths, 1, 0 ) \
+ 1*If(_id_78, 1, 0 ) \
+ 1*If(_id_79, 1, 0 ) \
+ 1*If(_id_80, 1, 0 ) \
+ 1*If(_id_81, 1, 0 ) \
+ 1*If(_id_82, 1, 0 ) \
+ 1*If(_id_83, 1, 0 ) \
+ 1*If(_id_84, 1, 0 ) \
+ 1*If(registered_checkout, 1, 0 ) \
+ 1*If(quick_checkout, 1, 0 ) \
+ 1*If(_id_86, 1, 0 ) \
+ 1*If(_id_87, 1, 0 ) \
+ 1*If(shipping_options, 1, 0 ) \
+ 1*If(_id_88, 1, 0 ) \
+ 1*If(_id_89, 1, 0 ) \
+ 1*If(_id_90, 1, 0 ) \
+ 1*If(_id_91, 1, 0 ) \
+ 1*If(_id_92, 1, 0 ) \
+ 1*If(_id_93, 1, 0 ) \
+ 1*If(_id_95, 1, 0 ) \
+ 1*If(_id_96, 1, 0 ) \
+ 1*If(_id_98, 1, 0 ) \
+ 1*If(_id_99, 1, 0 ) \
+ 1*If(_id_100, 1, 0 ) \
+ 1*If(_id_101, 1, 0 ) \
+ 1*If(shipping_2, 1, 0 ) \
+ 1*If(_id_102, 1, 0 ) \
+ 1*If(_id_103, 1, 0 ) \
+ 1*If(_id_105, 1, 0 ) \
+ 1*If(_id_106, 1, 0 ) \
+ 1*If(_id_107, 1, 0 ) \
+ 1*If(_id_108, 1, 0 ) \
+ 1*If(_id_110, 1, 0 ) \
+ 1*If(_id_111, 1, 0 ) \
+ 1*If(_id_112, 1, 0 ) \
+ 1*If(_id_114, 1, 0 ) \
+ 1*If(_id_115, 1, 0 ) \
+ 1*If(_id_116, 1, 0 ) \
+ 1*If(_id_117, 1, 0 ) \
+ 1*If(_id_118, 1, 0 ) \
+ 1*If(_id_120, 1, 0 ) \
+ 1*If(_id_121, 1, 0 ) \
+ 1*If(_id_122, 1, 0 ) \
+ 1*If(_id_123, 1, 0 ) \
+ 1*If(_id_124, 1, 0 ) \
+ 1*If(_id_125, 1, 0 ) \
+ 1*If(_id_126, 1, 0 ) \
+ 1*If(_id_127, 1, 0 ) \
+ 1*If(_id_128, 1, 0 ) \
+ 1*If(_id_129, 1, 0 ) \
+ 1*If(_id_130, 1, 0 ) \
+ 1*If(_id_132, 1, 0 ) \
+ 1*If(_id_133, 1, 0 ) \
+ 1*If(_id_134, 1, 0 ) \
+ 1*If(_id_135, 1, 0 ) \
+ 1*If(_id_136, 1, 0 ) \
+ 1*If(_id_137, 1, 0 ) \
+ 1*If(_id_138, 1, 0 ) \
+ 1*If(_id_139, 1, 0 ) \
+ 1*If(_id_141, 1, 0 ) \
+ 1*If(_id_142, 1, 0 ) \
+ 1*If(_id_143, 1, 0 ) \
+ 1*If(_id_144, 1, 0 ) \
+ 1*If(buy_paths_288_289, 1, 0 ) \
+ 1*If(buy_paths_288_289_290, 1, 0 ) \
+ 1*If(buy_paths_288_289_291, 1, 0 ) \
+ 1*If(customer_service, 1, 0 ) \
+ 1*If(_id_146, 1, 0 ) \
+ 1*If(_id_147, 1, 0 ) \
+ 1*If(_id_148, 1, 0 ) \
+ 1*If(_id_149, 1, 0 ) \
+ 1*If(_id_150, 1, 0 ) \
+ 1*If(_id_152, 1, 0 ) \
+ 1*If(_id_153, 1, 0 ) \
+ 1*If(_id_154, 1, 0 ) \
+ 1*If(_id_155, 1, 0 ) \
+ 1*If(_id_156, 1, 0 ) \
+ 1*If(_id_158, 1, 0 ) \
+ 1*If(_id_159, 1, 0 ) \
+ 1*If(user_behaviour_tracking, 1, 0 ) \
+ 1*If(_id_160, 1, 0 ) \
+ 1*If(locally_visited_pages, 1, 0 ) \
+ 1*If(external_referring_pages, 1, 0 ) \
+ 1*If(behaviour_tracked_previous_purchases, 1, 0 ) \
+ 1*If(business_management, 1, 0 ) \
+ 1*If(_id_162, 1, 0 ) \
+ 1*If(_id_163, 1, 0 ) \
+ 1*If(physical_goods_fulfillment, 1, 0 ) \
+ 1*If(warehouse_management, 1, 0 ) \
+ 1*If(shipping, 1, 0 ) \
+ 1*If(_id_166, 1, 0 ) \
+ 1*If(_id_167, 1, 0 ) \
+ 1*If(_id_168, 1, 0 ) \
+ 1*If(_id_169, 1, 0 ) \
+ 1*If(_id_171, 1, 0 ) \
+ 1*If(_id_172, 1, 0 ) \
+ 1*If(_id_173, 1, 0 ) \
+ 1*If(_id_174, 1, 0 ) \
+ 1*If(_id_175, 1, 0 ) \
+ 1*If(_id_177, 1, 0 ) \
+ 1*If(_id_178, 1, 0 ) \
+ 1*If(_id_179, 1, 0 ) \
+ 1*If(_id_180, 1, 0 ) \
+ 1*If(_id_181, 1, 0 ) \
+ 1*If(eletronic_goods_fulfillment, 1, 0 ) \
+ 1*If(_id_182, 1, 0 ) \
+ 1*If(_id_183, 1, 0 ) \
+ 1*If(services_fulfillment, 1, 0 ) \
+ 1*If(_id_184, 1, 0 ) \
+ 1*If(_id_185, 1, 0 ) \
+ 1*If(_id_186, 1, 0 ) \
+ 1*If(_id_187, 1, 0 ) \
+ 1*If(customer_preferences, 1, 0 ) \
+ 1*If(_id_189, 1, 0 ) \
+ 1*If(_id_190, 1, 0 ) \
+ 1*If(targeting_criteria_previous_purchases, 1, 0 ) \
+ 1*If(_id_191, 1, 0 ) \
+ 1*If(wish_list_content, 1, 0 ) \
+ 1*If(previously_visited_pages, 1, 0 ) \
+ 1*If(_id_192, 1, 0 ) \
+ 1*If(_id_193, 1, 0 ) \
+ 1*If(_id_194, 1, 0 ) \
+ 1*If(_id_196, 1, 0 ) \
+ 1*If(_id_197, 1, 0 ) \
+ 1*If(_id_199, 1, 0 ) \
+ 1*If(_id_200, 1, 0 ) \
+ 1*If(_id_201, 1, 0 ) \
+ 1*If(_id_203, 1, 0 ) \
+ 1*If(_id_204, 1, 0 ) \
+ 1*If(_id_205, 1, 0 ) \
+ 1*If(_id_206, 1, 0 ) \
+ 1*If(_id_207, 1, 0 ) \
+ 1*If(discounts, 1, 0 ) \
+ 1*If(_id_208, 1, 0 ) \
+ 1*If(_id_209, 1, 0 ) \
+ 1*If(_id_210, 1, 0 ) \
+ 1*If(_id_211, 1, 0 ) \
+ 1*If(_id_212, 1, 0 ) \
+ 1*If(_id_214, 1, 0 ) \
+ 1*If(_id_215, 1, 0 ) \
+ 1*If(_id_216, 1, 0 ) \
+ 1*If(_id_217, 1, 0 ) \
+ 1*If(_id_218, 1, 0 ) \
+ 1*If(_id_219, 1, 0 ) \
+ 1*If(_id_220, 1, 0 ) \
+ 1*If(_id_222, 1, 0 ) \
+ 1*If(_id_223, 1, 0 ) \
+ 1*If(_id_224, 1, 0 ) \
+ 1*If(_id_225, 1, 0 ) \
+ 1*If(_id_226, 1, 0 ) \
+ 1*If(_id_228, 1, 0 ) \
+ 1*If(_id_229, 1, 0 ) \
+ 1*If(_id_230, 1, 0 ) \
+ 1*If(_id_231, 1, 0 ) \
+ 1*If(_id_232, 1, 0 ) \
+ 1*If(_id_233, 1, 0 ) \
+ 1*If(_id_235, 1, 0 ) \
+ 1*If(_id_236, 1, 0 ) \
+ 1*If(_id_237, 1, 0 ) \
+ 1*If(personalized_emails, 1, 0 ) \
+ 1*If(_id_238, 1, 0 ) \
+ 1*If(_id_239, 1, 0 ) \
+ 1*If(_id_240, 1, 0 ) \
+ 1*If(_id_241, 1, 0 ) \
+ 1*If(_id_242, 1, 0 ) \
+ 1*If(inventory_tracking, 1, 0 ) \
+ 1*If(_id_243, 1, 0 ) \
+ 1*If(procurement, 1, 0 ) \
+ 1*If(_id_244, 1, 0 ) \
+ 1*If(_id_245, 1, 0 ) \
+ 1*If(automatic, 1, 0 ) \
+ 1*If(_id_246, 1, 0 ) \
+ 1*If(reporting_and_analysis, 1, 0 ) \
+ 1*If(_id_247, 1, 0 ) \
+ 1*If(_id_248, 1, 0 ) \
+ 1*If(_id_249, 1, 0 ) \
+ 1*If(_id_250, 1, 0 ) \
+ 1*If(fulfillment_system, 1, 0 ) \
+ 1*If(_id_252, 1, 0 ) \
+ 1*If(procurement_system, 1, 0 ) \
+ 1*If(_id_253, 1, 0 ) \
+ 1*If(_id_254, 1, 0 ) \
+ 1*If(_id_255, 1, 0 ) \
+ 1*If(_id_256, 1, 0 ) \
+ 1*If(_id_257, 1, 0 ) \
+ 1*If(_id_258, 1, 0 ) \
+ 1*If(_id_259, 1, 0 ) \
+ 1*If(_id_260, 1, 0 ) \
+ 1*If(_id_261, 1, 0 ) \
+ 1*If(_id_262, 1, 0 ) \
+ 1*If(_id_263, 1, 0 ) \
)
s.add(total_Defects== 3*If(eShop, 1, 0 ) \
+ 0*If(store_front, 1, 0 ) \
+ 5*If(homepage, 1, 0 ) \
+ 0*If(_id_1, 1, 0 ) \
+ 0*If(_id_2, 1, 0 ) \
+ 3*If(_id_3, 1, 0 ) \
+ 0*If(_id_5, 1, 0 ) \
+ 5*If(special_offers, 1, 0 ) \
+ 5*If(_id_6, 1, 0 ) \
+ 0*If(_id_8, 1, 0 ) \
+ 6*If(_id_9, 1, 0 ) \
+ 8*If(registration, 1, 0 ) \
+ 0*If(registration_enforcement, 1, 0 ) \
+ 6*If(_id_11, 1, 0 ) \
+ 0*If(register_to_buy, 1, 0 ) \
+ 5*If(_id_12, 1, 0 ) \
+ 0*If(_id_13, 1, 0 ) \
+ 6*If(_id_14, 1, 0 ) \
+ 0*If(shipping_address, 1, 0 ) \
+ 0*If(_id_15, 1, 0 ) \
+ 0*If(_id_16, 1, 0 ) \
+ 0*If(_id_17, 1, 0 ) \
+ 6*If(_id_18, 1, 0 ) \
+ 0*If(_id_19, 1, 0 ) \
+ 5*If(_id_20, 1, 0 ) \
+ 0*If(_id_21, 1, 0 ) \
+ 0*If(_id_22, 1, 0 ) \
+ 7*If(_id_23, 1, 0 ) \
+ 0*If(_id_25, 1, 0 ) \
+ 0*If(_id_26, 1, 0 ) \
+ 4*If(_id_27, 1, 0 ) \
+ 7*If(_id_28, 1, 0 ) \
+ 0*If(_id_29, 1, 0 ) \
+ 6*If(preferences, 1, 0 ) \
+ 0*If(_id_31, 1, 0 ) \
+ 0*If(_id_32, 1, 0 ) \
+ 0*If(_id_33, 1, 0 ) \
+ 5*If(_id_34, 1, 0 ) \
+ 0*If(quick_checkout_profile, 1, 0 ) \
+ 0*If(_id_35, 1, 0 ) \
+ 0*If(user_behaviour_tracking_info, 1, 0 ) \
+ 0*If(catalog, 1, 0 ) \
+ 0*If(product_information, 1, 0 ) \
+ 0*If(product_type, 1, 0 ) \
+ 0*If(eletronic_goods, 1, 0 ) \
+ 6*If(physical_goods, 1, 0 ) \
+ 5*If(services, 1, 0 ) \
+ 0*If(basic_information, 1, 0 ) \
+ 0*If(detailed_information, 1, 0 ) \
+ 0*If(warranty_information, 1, 0 ) \
+ 7*If(customer_reviews, 1, 0 ) \
+ 6*If(associated_assets, 1, 0 ) \
+ 0*If(_id_38, 1, 0 ) \
+ 7*If(_id_39, 1, 0 ) \
+ 0*If(_id_41, 1, 0 ) \
+ 0*If(_id_43, 1, 0 ) \
+ 0*If(_id_44, 1, 0 ) \
+ 3*If(_id_45, 1, 0 ) \
+ 4*If(_id_46, 1, 0 ) \
+ 0*If(_id_47, 1, 0 ) \
+ 8*If(_id_48, 1, 0 ) \
+ 5*If(_id_49, 1, 0 ) \
+ 0*If(_id_50, 1, 0 ) \
+ 0*If(product_variants, 1, 0 ) \
+ 0*If(_id_51, 1, 0 ) \
+ 0*If(size, 1, 0 ) \
+ 5*If(weight, 1, 0 ) \
+ 0*If(availability, 1, 0 ) \
+ 4*If(custom_fields, 1, 0 ) \
+ 5*If(categories, 1, 0 ) \
+ 5*If(categories_catalog, 1, 0 ) \
+ 0*If(_id_52, 1, 0 ) \
+ 5*If(_id_53, 1, 0 ) \
+ 0*If(_id_54, 1, 0 ) \
+ 2*If(_id_55, 1, 0 ) \
+ 0*If(_id_56, 1, 0 ) \
+ 4*If(_id_58, 1, 0 ) \
+ 5*If(_id_59, 1, 0 ) \
+ 7*If(_id_60, 1, 0 ) \
+ 4*If(_id_61, 1, 0 ) \
+ 3*If(category_page, 1, 0 ) \
+ 4*If(_id_62, 1, 0 ) \
+ 0*If(_id_63, 1, 0 ) \
+ 6*If(_id_65, 1, 0 ) \
+ 8*If(_id_66, 1, 0 ) \
+ 5*If(_id_67, 1, 0 ) \
+ 0*If(_id_68, 1, 0 ) \
+ 6*If(_id_69, 1, 0 ) \
+ 0*If(_id_70, 1, 0 ) \
+ 0*If(_id_71, 1, 0 ) \
+ 0*If(_id_72, 1, 0 ) \
+ 0*If(wish_list, 1, 0 ) \
+ 0*If(wish_list_saved_after_session, 1, 0 ) \
+ 3*If(email_wish_list, 1, 0 ) \
+ 0*If(_id_73, 1, 0 ) \
+ 0*If(permissions, 1, 0 ) \
+ 5*If(_id_75, 1, 0 ) \
+ 0*If(_id_76, 1, 0 ) \
+ 0*If(_id_77, 1, 0 ) \
+ 6*If(buy_paths, 1, 0 ) \
+ 0*If(_id_78, 1, 0 ) \
+ 0*If(_id_79, 1, 0 ) \
+ 0*If(_id_80, 1, 0 ) \
+ 5*If(_id_81, 1, 0 ) \
+ 5*If(_id_82, 1, 0 ) \
+ 3*If(_id_83, 1, 0 ) \
+ 0*If(_id_84, 1, 0 ) \
+ 4*If(registered_checkout, 1, 0 ) \
+ 4*If(quick_checkout, 1, 0 ) \
+ 0*If(_id_86, 1, 0 ) \
+ 4*If(_id_87, 1, 0 ) \
+ 4*If(shipping_options, 1, 0 ) \
+ 5*If(_id_88, 1, 0 ) \
+ 7*If(_id_89, 1, 0 ) \
+ 0*If(_id_90, 1, 0 ) \
+ 0*If(_id_91, 1, 0 ) \
+ 0*If(_id_92, 1, 0 ) \
+ 6*If(_id_93, 1, 0 ) \
+ 0*If(_id_95, 1, 0 ) \
+ 6*If(_id_96, 1, 0 ) \
+ 0*If(_id_98, 1, 0 ) \
+ 0*If(_id_99, 1, 0 ) \
+ 0*If(_id_100, 1, 0 ) \
+ 5*If(_id_101, 1, 0 ) \
+ 5*If(shipping_2, 1, 0 ) \
+ 0*If(_id_102, 1, 0 ) \
+ 0*If(_id_103, 1, 0 ) \
+ 0*If(_id_105, 1, 0 ) \
+ 0*If(_id_106, 1, 0 ) \
+ 0*If(_id_107, 1, 0 ) \
+ 5*If(_id_108, 1, 0 ) \
+ 4*If(_id_110, 1, 0 ) \
+ 0*If(_id_111, 1, 0 ) \
+ 0*If(_id_112, 1, 0 ) \
+ 0*If(_id_114, 1, 0 ) \
+ 0*If(_id_115, 1, 0 ) \
+ 4*If(_id_116, 1, 0 ) \
+ 0*If(_id_117, 1, 0 ) \
+ 0*If(_id_118, 1, 0 ) \
+ 0*If(_id_120, 1, 0 ) \
+ 0*If(_id_121, 1, 0 ) \
+ 0*If(_id_122, 1, 0 ) \
+ 0*If(_id_123, 1, 0 ) \
+ 6*If(_id_124, 1, 0 ) \
+ 0*If(_id_125, 1, 0 ) \
+ 6*If(_id_126, 1, 0 ) \
+ 0*If(_id_127, 1, 0 ) \
+ 0*If(_id_128, 1, 0 ) \
+ 6*If(_id_129, 1, 0 ) \
+ 4*If(_id_130, 1, 0 ) \
+ 8*If(_id_132, 1, 0 ) \
+ 0*If(_id_133, 1, 0 ) \
+ 4*If(_id_134, 1, 0 ) \
+ 0*If(_id_135, 1, 0 ) \
+ 0*If(_id_136, 1, 0 ) \
+ 4*If(_id_137, 1, 0 ) \
+ 0*If(_id_138, 1, 0 ) \
+ 6*If(_id_139, 1, 0 ) \
+ 5*If(_id_141, 1, 0 ) \
+ 5*If(_id_142, 1, 0 ) \
+ 0*If(_id_143, 1, 0 ) \
+ 0*If(_id_144, 1, 0 ) \
+ 0*If(buy_paths_288_289, 1, 0 ) \
+ 0*If(buy_paths_288_289_290, 1, 0 ) \
+ 7*If(buy_paths_288_289_291, 1, 0 ) \
+ 5*If(customer_service, 1, 0 ) \
+ 5*If(_id_146, 1, 0 ) \
+ 0*If(_id_147, 1, 0 ) \
+ 5*If(_id_148, 1, 0 ) \
+ 0*If(_id_149, 1, 0 ) \
+ 0*If(_id_150, 1, 0 ) \
+ 3*If(_id_152, 1, 0 ) \
+ 6*If(_id_153, 1, 0 ) \
+ 0*If(_id_154, 1, 0 ) \
+ 0*If(_id_155, 1, 0 ) \
+ 0*If(_id_156, 1, 0 ) \
+ 0*If(_id_158, 1, 0 ) \
+ 2*If(_id_159, 1, 0 ) \
+ 3*If(user_behaviour_tracking, 1, 0 ) \
+ 0*If(_id_160, 1, 0 ) \
+ 4*If(locally_visited_pages, 1, 0 ) \
+ 0*If(external_referring_pages, 1, 0 ) \
+ 6*If(behaviour_tracked_previous_purchases, 1, 0 ) \
+ 0*If(business_management, 1, 0 ) \
+ 5*If(_id_162, 1, 0 ) \
+ 5*If(_id_163, 1, 0 ) \
+ 8*If(physical_goods_fulfillment, 1, 0 ) \
+ 0*If(warehouse_management, 1, 0 ) \
+ 4*If(shipping, 1, 0 ) \
+ 0*If(_id_166, 1, 0 ) \
+ 0*If(_id_167, 1, 0 ) \
+ 0*If(_id_168, 1, 0 ) \
+ 5*If(_id_169, 1, 0 ) \
+ 0*If(_id_171, 1, 0 ) \
+ 0*If(_id_172, 1, 0 ) \
+ 5*If(_id_173, 1, 0 ) \
+ 0*If(_id_174, 1, 0 ) \
+ 4*If(_id_175, 1, 0 ) \
+ 0*If(_id_177, 1, 0 ) \
+ 0*If(_id_178, 1, 0 ) \
+ 8*If(_id_179, 1, 0 ) \
+ 5*If(_id_180, 1, 0 ) \
+ 0*If(_id_181, 1, 0 ) \
+ 0*If(eletronic_goods_fulfillment, 1, 0 ) \
+ 4*If(_id_182, 1, 0 ) \
+ 0*If(_id_183, 1, 0 ) \
+ 0*If(services_fulfillment, 1, 0 ) \
+ 0*If(_id_184, 1, 0 ) \
+ 0*If(_id_185, 1, 0 ) \
+ 5*If(_id_186, 1, 0 ) \
+ 3*If(_id_187, 1, 0 ) \
+ 6*If(customer_preferences, 1, 0 ) \
+ 4*If(_id_189, 1, 0 ) \
+ 0*If(_id_190, 1, 0 ) \
+ 0*If(targeting_criteria_previous_purchases, 1, 0 ) \
+ 5*If(_id_191, 1, 0 ) \
+ 7*If(wish_list_content, 1, 0 ) \
+ 5*If(previously_visited_pages, 1, 0 ) \
+ 0*If(_id_192, 1, 0 ) \
+ 4*If(_id_193, 1, 0 ) \
+ 0*If(_id_194, 1, 0 ) \
+ 7*If(_id_196, 1, 0 ) \
+ 5*If(_id_197, 1, 0 ) \
+ 0*If(_id_199, 1, 0 ) \
+ 8*If(_id_200, 1, 0 ) \
+ 2*If(_id_201, 1, 0 ) \
+ 6*If(_id_203, 1, 0 ) \
+ 7*If(_id_204, 1, 0 ) \
+ 7*If(_id_205, 1, 0 ) \
+ 6*If(_id_206, 1, 0 ) \
+ 4*If(_id_207, 1, 0 ) \
+ 0*If(discounts, 1, 0 ) \
+ 6*If(_id_208, 1, 0 ) \
+ 0*If(_id_209, 1, 0 ) \
+ 0*If(_id_210, 1, 0 ) \
+ 0*If(_id_211, 1, 0 ) \
+ 3*If(_id_212, 1, 0 ) \
+ 5*If(_id_214, 1, 0 ) \
+ 6*If(_id_215, 1, 0 ) \
+ 8*If(_id_216, 1, 0 ) \
+ 0*If(_id_217, 1, 0 ) \
+ 6*If(_id_218, 1, 0 ) \
+ 6*If(_id_219, 1, 0 ) \
+ 0*If(_id_220, 1, 0 ) \
+ 0*If(_id_222, 1, 0 ) \
+ 0*If(_id_223, 1, 0 ) \
+ 6*If(_id_224, 1, 0 ) \
+ 5*If(_id_225, 1, 0 ) \
+ 6*If(_id_226, 1, 0 ) \
+ 0*If(_id_228, 1, 0 ) \
+ 1*If(_id_229, 1, 0 ) \
+ 0*If(_id_230, 1, 0 ) \
+ 0*If(_id_231, 1, 0 ) \
+ 0*If(_id_232, 1, 0 ) \
+ 0*If(_id_233, 1, 0 ) \
+ 0*If(_id_235, 1, 0 ) \
+ 0*If(_id_236, 1, 0 ) \
+ 0*If(_id_237, 1, 0 ) \
+ 5*If(personalized_emails, 1, 0 ) \
+ 0*If(_id_238, 1, 0 ) \
+ 6*If(_id_239, 1, 0 ) \
+ 0*If(_id_240, 1, 0 ) \
+ 6*If(_id_241, 1, 0 ) \
+ 0*If(_id_242, 1, 0 ) \
+ 3*If(inventory_tracking, 1, 0 ) \
+ 8*If(_id_243, 1, 0 ) \
+ 3*If(procurement, 1, 0 ) \
+ 2*If(_id_244, 1, 0 ) \
+ 0*If(_id_245, 1, 0 ) \
+ 4*If(automatic, 1, 0 ) \
+ 5*If(_id_246, 1, 0 ) \
+ 5*If(reporting_and_analysis, 1, 0 ) \
+ 0*If(_id_247, 1, 0 ) \
+ 0*If(_id_248, 1, 0 ) \
+ 7*If(_id_249, 1, 0 ) \
+ 0*If(_id_250, 1, 0 ) \
+ 7*If(fulfillment_system, 1, 0 ) \
+ 0*If(_id_252, 1, 0 ) \
+ 8*If(procurement_system, 1, 0 ) \
+ 6*If(_id_253, 1, 0 ) \
+ 0*If(_id_254, 1, 0 ) \
+ 0*If(_id_255, 1, 0 ) \
+ 0*If(_id_256, 1, 0 ) \
+ 7*If(_id_257, 1, 0 ) \
+ 3*If(_id_258, 1, 0 ) \
+ 5*If(_id_259, 1, 0 ) \
+ 5*If(_id_260, 1, 0 ) \
+ 0*If(_id_261, 1, 0 ) \
+ 0*If(_id_262, 1, 0 ) \
+ 0*If(_id_263, 1, 0 ) \
)
s.add(eShop==True)


metrics_variables = [total_Cost,total_Defects,total_FeatureCount,\
        total_UsedBefore]
metrics_objective_direction = [METRICS_MINIMIZE, METRICS_MINIMIZE, \
        METRICS_MAXIMIZE, METRICS_MAXIMIZE]
    
##    parser = argparse.ArgumentParser(description="Computes Pareto Front")
##    parser.add_argument('--logfile',   dest='logfile', metavar='logfile',\
##         default="EshopICSE2013.json", type=str,
##          help='File where to store detailed call logs')
##    parser.add_argument('--timefile',   dest='timefile', metavar='timefile',\
##         default="timefile.csv", type=str,
##          help='File where to store a total time count')
##    parser.add_argument('--randomseedfile',   dest='randomseedfile', metavar='randomseedfile',\
##         default="randomseed.csv", type=str,
##          help='File where to store random seed used')
##    
##    args = parser.parse_args()
##    
##    
##    GIAOptions = GuidedImprovementAlgorithmOptions(verbosity=0, \
##        incrementallyWriteLog=True, writeLogFilename=args.logfile, \
##        writeTotalTimeFilename=args.timefile, writeRandomSeedsFilename=args.randomseedfile)    
##    GIAAlgorithm = GuidedImprovementAlgorithm(s, metrics_variables, metrics_objective_direction, FeatureVariable,  options=GIAOptions)
##    GIAAlgorithm.ExecuteGuidedImprovementAlgorithm()
##    
##if __name__ == '__main__':
##    execute_main()
