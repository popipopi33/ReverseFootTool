def main():
    mel.eval("setAttr -k off \"reverseBall_ctrlShape.v\"")
    mel.eval("setAttr \"reverseBall_ctrlShape.ove\" yes")
    mel.eval("setAttr \"reverseBall_ctrlShape.ovc\" 6")
    mel.eval("setAttr \"reverseBall_ctrlShape.cc\" -type \"nurbsCurve\" 1 8 0 no 3 9 0 1 2 3 4 5 6 7 8 9 9.8313054377068383 5.3958844757490398 -4.886548421622571 9.8313054377068383 -2.999707747932812 -4.8865484216225772 -7.3052929107740567 -2.999707747932812 -4.8865484216225772 -7.3052929107740567 -2.9997110480727733 5.1881622467956214 9.8313054377068383 -2.9997110480727778 5.1881622467956214 9.8313054377068383 -2.999707747932812 -4.8865484216225772 9.8313054377068383 -2.9997110480727778 5.1881622467956214 9.8313054377068383 5.3958844757490398 5.1881622467956339 9.8313054377068383 5.3958844757490398 -4.886548421622571 ")
    mel.eval("setAttr -k off \"reverseToe_ctrlShape.v\"")
    mel.eval("setAttr \"reverseToe_ctrlShape.ove\" yes")
    mel.eval("setAttr \"reverseToe_ctrlShape.ovc\" 6")
    mel.eval("setAttr \"reverseToe_ctrlShape.cc\" -type \"nurbsCurve\" 1 8 0 no 3 9 0 1 2 3 4 5 6 7 8 9 7.8109096636136677 8.3993569807678607 -0.026413760579250312 7.8109096636136677 0.0037647570861377112 -0.026413760579250312 7.8109096636136677 0.0037647570861377112 -8.3873594112945256 -7.3011563390136276 0.0037647570861377112 -8.3873594112945256 -7.3011563390136276 0.0037647570861377112 -0.026413760579250312 7.8109096636136677 0.0037647570861377112 -0.026413760579250312 -7.3011563390136276 0.0037647570861377112 -0.026413760579250312 -7.3011563390136276 8.3993569807678607 -0.026413760579250312 7.8109096636136677 8.3993569807678607 -0.026413760579250312 ")
    mel.eval("setAttr -k off \"reverseHeel_ctrlShape.v\"")
    mel.eval("setAttr \"reverseHeel_ctrlShape.ove\" yes")
    mel.eval("setAttr \"reverseHeel_ctrlShape.ovc\" 6")
    mel.eval("setAttr \"reverseHeel_ctrlShape.cc\" -type \"nurbsCurve\" 1 8 0 no 3 9 0 1 2 3 4 5 6 7 8 9 -7.2433229970832276 8.4521673647722491 -0.025604946971164423 -7.2433229970832276 0.056575141090532702 -0.025604946971158459 -7.2433229970832276 0.056575141090532702 8.7499215345074681 7.8687430055440677 0.056575141090532702 8.7499215345074681 7.8687430055440677 0.056575141090532702 -0.025604946971158459 -7.2433229970832276 0.056575141090532702 -0.025604946971158459 7.8687430055440677 0.056575141090532702 -0.025604946971158459 7.8687430055440677 8.4521673647722491 -0.025604946971164423 -7.2433229970832276 8.4521673647722491 -0.025604946971164423 ")
    mel.eval("setAttr -k off \"reverseFoot_ctrlShape.v\"")
    mel.eval("setAttr \"reverseFoot_ctrlShape.ove\" yes")
    mel.eval("setAttr \"reverseFoot_ctrlShape.ovc\" 6")
    mel.eval("setAttr \"reverseFoot_ctrlShape.cc\" -type \"nurbsCurve\" 1 12 0 no 3 13 0 0.51763809020504148 1.035276180410083 1.5529142706151244 2.0705523608201659  2.5881904510252074 3.1058285412302489 3.6234666314352904 4.1411047216403318 4.6587428118453733  5.1763809020504148 5.6940189922554563 6.2116570824604977 13 1.2044190285712675e-09 -10.999716098084241 -10.834248881859066 -6.074591277986265 -10.999716098084241 -8.2965546813752109 -10.52150072956846 -10.999716098084241 -1.3634451915797994 -12.149182557176605 -10.999716098084241 8.107358498699444 -10.521500729568295 -10.999716098084241 17.578162188978702 -6.074591277986265 -10.999716098084237 24.511271678773856 1.2044236322061727e-09 -10.999716098084237 27.048965879257974 6.0745912803947482 -10.999716098084237 24.511271678773856 10.521500731976829 -10.999716098084241 17.578162188978713 12.149182559585382 -10.999716098084241 8.1073584986994867 10.521500731976829 -10.999716098084241 -1.3634451915798225 6.0745912803949551 -10.999716098084241 -8.2965546813750208 1.2044282358410779e-09 -10.999716098084241 -10.834248881859066 ")
    mel.eval("setAttr -k off \"toe_ctrlShape.v\"")
    mel.eval("setAttr \"toe_ctrlShape.ove\" yes")
    mel.eval("setAttr \"toe_ctrlShape.ovc\" 15")
    mel.eval("setAttr \"toe_ctrlShape.cc\" -type \"nurbsCurve\" 1 8 0 no 3 9 0 0.76536686473017945 1.5307337294603589 2.2961005941905386 3.0614674589207183  3.8268343236508975 4.5922011883810772 5.3575680531112564 6.1229349178414356 9 2.249639673992787e-32 6.0000000000000018 -9.2250555205678431e-16 -2.5978681687064801e-16 4.2426406871192865 4.2426406871192848 -3.6739403974420604e-16 1.6996616692943943e-15 6 -2.5978681687064806e-16 -4.2426406871192848 4.2426406871192857 -1.2446872724844474e-31 -6.0000000000000018 1.4776170643693632e-15 2.5978681687064796e-16 -4.2426406871192874 -4.2426406871192857 3.6739403974420604e-16 -3.0319292988445827e-15 -6.0000000000000027 2.5978681687064816e-16 4.2426406871192839 -4.2426406871192892 2.6722998996036831e-31 6.0000000000000018 -4.9193084407073488e-15 ")
    mel.eval("setAttr -k off \"ankle_ctrlShape.v\"")
    mel.eval("setAttr \"ankle_ctrlShape.ove\" yes")
    mel.eval("setAttr \"ankle_ctrlShape.ovc\" 15")
    mel.eval("setAttr \"ankle_ctrlShape.cc\" -type \"nurbsCurve\" 1 8 0 no 3 9 0 0.76536686473017945 1.5307337294603589 2.2961005941905386 3.0614674589207183  3.8268343236508975 4.5922011883810772 5.3575680531112564 6.1229349178414356 9 5.329070518200753e-15 -11.481837684191833 -3.4218516908879343e-07 -7.1054273576010034e-15 -8.1188877993557984 8.1188877993558517 5.329070518200753e-15 -6.8437032751944582e-07 11.48183768419185 -5.329070518200753e-15 8.1188877993558197 8.1188877993558553 -5.329070518200753e-15 11.481837684191833 -3.4218517175332868e-07 -3.5527136788005017e-15 8.1188877993557984 -8.1188877993558481 7.1054273576010034e-15 -6.8437032751944582e-07 -11.48183768419185 5.329070518200753e-15 -8.1188877993558553 -8.1188877993558481 5.329070518200753e-15 -11.481837684191833 -3.421851770823992e-07 ")
main()